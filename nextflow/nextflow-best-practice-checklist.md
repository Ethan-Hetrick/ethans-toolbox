# Nextflow Best Practices Checklist
`made by ethan hetrick`

A checklist to ensure adherence to best practices when working with Nextflow pipelines.

---

## Table of Contents
1. [Configuration](#configuration)
2. [Execution](#execution)
3. [Debugging](#debugging)
4. [Code Quality](#code-quality)

---

## Configuration
- [ ] **Executor profiles**: Use separate profiles for each executor. All execution-specific configs should be constrained to the profile scope. E.g `sge`, `slurm`
- [ ] **Container profiles**: Use separate profiles for each container software. E.g. `docker`, `singularity`
- [ ] **Process labels**: Every process should be given a label that resources can default to. E.g. `process_single`, `process_high`. These labels should be configured flexibly and a label should exist for each "level" of resources a process can use (`base.config` in the nf-core pipeline structure)
- [ ] **Process-specific configurations**: If single processes need their own configuration, this should be confined to the `withName` scope (`modules.config` in the nf-core pipeline structure)
- [ ] **Naming profiles**: Don't name two profiles the same thing to avoid profile collisions. Try to avoid using the same name as nf-core institutional config profiles (see https://nf-co.re/configs)
- [ ] **Flexible error resolution**: It should be configured where if a process errors out that the process is re-submitted with more resources for appropriate error messages. See `retry` scope in Nextflow docs
- [ ] **Resource allocation**: Allocate an appropriate amount of resources for every process. Remember, flexible label definitions will resolve one-offs from erroring out. General rules:
    - Only request the amount of cores/threads/processors as the process actually uses
    - Request 10-20% more memory/RAM than the process needs, no more
    - Request 10-20% more time than the process will need to run, no more
    - Submit jobs to the appropriate queue if using HPC environments. E.g. `short.q`, `long.q`
    - Use the tracing function in Nextflow to generate a resource usage table and adjust resource allocation as needed. Use `-with-trace` at runtime
    - Use a sparing amount of resources for the head Nextflow job that runs the JVM. Usually `16-32G` and 1-4 CPUs is plenty, and make sure to give it enough time to run all the way through (this will vary depending on use-case)

Link to Nextflow docs: https://www.nextflow.io/docs/latest/config.html

---

## Execution
- [ ] **Execution configs**: Utilize config files and profiles specific to your execution platform at runtime. `-c` and `-profile` on CLI
- [ ] **Resuming runs**: Use `-resume` at runtime to utilized cached results. This is very helpful when actively developing a pipeline or when pipelines fail half-way
- [ ] **Configuring the head job**: Use a sparing amount of resources for the head Nextflow job that runs the JVM. Usually `16-32G` and 1-4 CPUs is plenty, and make sure to give it enough time to run all the way through (this will vary depending on use-case)

---

## Debugging
- [ ] **Runtime options for debugging**: There are `nextflow run` options that help with debugging:
    - `-with-trace` generates a trace report. Good in case a process runs out of resources you can see how much it used
    - `-dump-channels` prints information about the channels
    - `-dump-hashes` prints the hash keys for each process
- [ ] **.nextflow.log**: Nextflow generates a log file for each run. `.nextflow.log` will have the most recent run. Main things to note:
    - Which parameters the pipeline used to run, usually located at the top
    - The main error code and error message
    - The task hashes which correspond to the process scripts and files located in the work directory
- [ ] **Check Nextflow install**: Run `nextflow info -d`, does everything look as expected?
- [ ] **The work directory**: The work directory contains all scripts and files that a process needs to run. There are a few things to note here:
    1. Navigate to your work directory and run `ls -la`, are all the expected files there?
    2. Check `.command.sh`, did the script render properly?
    3. Check the top of `.command.run`, did Nextflow execute the job correctly?
    4. Check `.command.log`, are there any more detail about your error message?
    5. Check all inputs/outputs for the process, do they look correct?
---

## Code Quality

---

## Notes

---
