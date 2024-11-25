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

## 1. Configuration
- [ ] **Organized Profiles**: Use separate profiles for dev, test, and production environments.
- [ ] **Parameter Defaults**: Define default parameters clearly in `nextflow.config`.
- [ ] **Containerized Environment**: Specify containers (e.g., Docker or Singularity) in the configuration.
- [ ] **Resource Specification**: Properly define CPU, memory, and time limits for each process.
- [ ] **Secrets Management**: Use `.env` files or secure secrets storage for sensitive information.

---

## 2. Execution
- [ ] **Reproducibility**: Pin software versions and containers to ensure consistent results.
- [ ] **Work Directory Management**: Clean up old work directories to save disk space.
- [ ] **Storage**: Use shared storage (e.g., NFS) for intermediate files when running on HPC.
- [ ] **Error Handling**: Enable retry logic using `maxRetries` for non-deterministic failures.
- [ ] **Checkpointing**: Use `resume` effectively to avoid recomputing completed tasks.

---

## 3. Debugging
- [ ] **Verbose Logging**: Use `-log` or `NXF_DEBUG` for detailed logs during debugging.
- [ ] **Error Messages**: Review `.command.log` and `.command.err` for process-specific errors.
- [ ] **Container Debugging**: Use interactive mode to debug issues in containers.
- [ ] **Test Small Data**: Test with small datasets before scaling up.
- [ ] **Reproduce Errors**: Re-run failed processes individually using `.command.sh`.

---

## 4. Code Quality
- [ ] **Readable Script**: Use clear, concise naming conventions for processes and variables.
- [ ] **Module Reusability**: Use `includeConfig` or modules to maintain DRY (Don't Repeat Yourself) principles.
- [ ] **Channel Management**: Avoid excessive use of `broadcast` or `mix` unless necessary.
- [ ] **Documentation**: Document each process with comments or README files.
- [ ] **Code Reviews**: Conduct peer reviews for new pipelines or changes to existing ones.

---

## Notes
- [ ] Regularly review and update the checklist as Nextflow and your workflows evolve.
- [ ] Share this checklist with team members to ensure consistent pipeline quality.

---
