# Nextflow Developer’s Heuristic Checklist

Written by Ethan Hetrick

## Description

This document contains heuristic checklists designed to assist with common tasks that Nextflow developers encounter regularly.

---

## Table of Contents
1. [Configuration](#configuration)
2. [Execution](#execution)
3. [Debugging](#debugging)
4. [Code Quality](#code-quality)
5. [Nf-core pipelines](#nf-core-pipelines)

---

## Configuration
- [ ] **Decouple configs and pipeline logic**: Your pipeline code base (e.g. workflows, subworkflows, modules, scripts) should not hard-code **any** execution configurations, rather these should all be confined to config files (`projectDir/conf` or `projectDir/nextflow.config` in the nf-core pipeline structure). This is an intentional feature of Nextflow to allow pipelines to be executed on various platforms on-the-fly. General rule of thumb: If I need to modify your code base in order to execute your pipeline on my machine, then it's wrong.
- [ ] **Executor profiles**: Use separate profiles for each executor. All execution-specific configs should be constrained to the profile scope. E.g `sge`, `slurm`
- [ ] **Container profiles**: Use separate profiles for each container software. E.g. `docker`, `singularity`
- [ ] **Process labels**: Every process should be given a label that resources can default to. E.g. `process_single`, `process_high`. These labels should be configured flexibly and a label should exist for each "level" of resources a process can use (`base.config` in the nf-core pipeline structure)
- [ ] **Process-specific configurations**: If single processes need their own configuration, this should be confined to the `withName` scope (`modules.config` in the nf-core pipeline structure)
- [ ] **Naming profiles**: Don't name two profiles the same thing to avoid profile collisions. Try to avoid using the same name as nf-core institutional config profiles (see https://nf-co.re/configs)
- [ ] **Flexible error resolution**: It should be configured where if a process errors out that the process is re-submitted with more resources for appropriate error messages. See `retry` scope in Nextflow docs
- [ ] **Resource allocation**: Allocate an appropriate amount of resources for every process. Remember, flexible label definitions will resolve one-offs from erroring out. General advice:
    - Only request the amount of cores/threads/processors as the process actually uses
    - Request 10-20% more memory/RAM than the process needs, no more
    - Request 10-20% more time than the process will need to run, no more
    - Submit jobs to the appropriate queue if using HPC environments. E.g. `short.q`, `long.q`
    - Use the tracing function in Nextflow to generate a resource usage table and adjust resource allocation as needed. Use `-with-trace` at runtime
    - Use a sparing amount of resources for the head Nextflow job that runs the JVM. Usually `16-32G` and 1-4 CPUs is plenty, and make sure to give it enough time to run all the way through (this will vary depending on use-case)

Nextflow configuration docs: https://www.nextflow.io/docs/latest/config.html

---

## Execution
- [ ] **Execution configs**: Utilize config files and profiles specific to your execution platform at runtime. `-c` and `-profile` on CLI
- [ ] **Resuming runs**: Use `-resume` at runtime to utilize cached results. This is very helpful when actively developing a pipeline or when pipelines fail half-way
- [ ] **Configuring the head job**: Use a sparing amount of resources for the head Nextflow job that runs the JVM. Usually `16-32G` and 1-4 CPUs is plenty, and make sure to give it enough time to run all the way through (this will vary depending on use-case)

Nextflow execution docs: https://www.nextflow.io/docs/latest/executor.html

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
    5. Check all inputs/outputs for the process, are they correctly formatted? Do they have adequate permissions?
- [ ] **Clearing caches**: If nothing else is working, try deleting your Nextflow and/or nf-core caches and work directories. Potential locations:
    - `~/.nextflow` or `$NXF_HOME` - Nextflow packages, plugins, etc. e.g. `rm -rf ~/.nextflow/*`
    - `~/.cache/nfcore` - Nf-core packages, pipelines, etc. e.g. `rm -rf ~/.cache/nfcore`
    - `$NXF_WORK` or `./work` - Cached pipeline results. e.g. `nextflow clean -f` or `rm -rf ./work`
    - `$NXF_TEMP` or `$TMP` or `$TMPDIR` or `-Djava.io.tmpdir` - Clear out general temporary files. e.g. `rm -rf ${NXF_TEMP}/*`

### Where else to go to if you're stuck
- Nextflow docs: https://www.nextflow.io/docs/latest/index.html
- nf-core docs: https://nf-co.re/docs/
- Groovy docs: https://groovy-lang.org/documentation.html
- Nextflow troubleshooting workshop: https://training.nextflow.io/troubleshoot/
- nf-core troubleshooting guide: https://nf-co.re/docs/usage/troubleshooting/basics
- Nextflow GitHub: https://github.com/nextflow-io/nextflow
- Nf-core GitHub: https://github.com/nf-core
- Nf-core Slack and other community channels: https://nf-co.re/join
- Stackoverflow (good luck): https://stackoverflow.com/
- Your institution's system administrators

---

## Code Quality
- [ ] **Syntax**: Adhere to up-to-date Nextflow DSL2 syntax: https://www.nextflow.io/docs/latest/reference/syntax.html#syntax-page
- [ ] **Modularization**: Each process should be contained in it's own module file (`projectDir/modules` in nf-core pipeline structure). Workflows and subworkflows should be staged to reduce redundancy and enhance readability of the code base -- this task is less straight-forward
- [ ] **Flexibility**: Processes and workflows should be designed with flexibility in mind (i.e. the least hard-coded solution). For example, you want to design a process to only use the most basic command-line options, while allowing the user to customize the parameters at runtime. Multiple pipeline tracks can be designed to work with a variety of input data and desired outputs
- [ ] **Dataflow programming model**: Appropriately use channels in order to control the I/O of data for processes. Use queue channels when a series of values (e.g. samples) are needed and a value channel for static values (e.g. a reference genome). A process should never directly read/write to the output directory. All I/O should be controlled with channels which reads and write to the **work** directory. This will also ensure proper functionality of the `-resume` function
- [ ] **Containerization**: Each process should have it's own container. e.g. Docker, Singularity. For basic Bash scripts, consider using generic containers such as Ubuntu:22.04. Program versions that are currently supported/maintained are your best options. I generally advise to avoid using Conda if possible as it is the least consistent and most difficult to debug in my experience
- [ ] **General programming best-practices**: Make sure in general you follow programming best practices, here are a few examples:
    - Define variables using distinct and clear names
    - Avoid globally defining variables
    - Use functions to reduce code redundancy
    - Annotate code using docstrings and comment lines
    - Avoid hard-coding
    - Utilize version control
    - Validate inputs
    - Use consistent, easy-to-read formatting. The `prettier` application is good at automating this task

---

## Nf-core pipelines
- [ ] **Linting**: Use `nf-core lint` (might now be `nf-core pipelines lint` after updates) to perform quality checks on your pipeline. `nf-core schema lint` can be used to just validate your schema
- [ ] **To-do's**: Check the "TO-DO" lines in the nf-core pipeline template for suggested best-practices

---

## Disclaimer

The items on the list are derived solely from my personal experience as a Nextflow developer and do not reflect the standards set by Nextflow, nf-core, or any of my personal affiliations. 

---
