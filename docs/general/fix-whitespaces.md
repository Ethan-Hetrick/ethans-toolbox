# Pre-commit, Whitespace, and Python Environment Troubleshooting Guide

## 1. Create a clean conda environment

Use a stable Python version such as 3.10 or 3.11:

```
conda create -n dev_env python=3.11
conda activate dev_env
pip install pre-commit gitpython
```

Optional (useful for many projects):

```
pip install prettier nf-core
```

## 2. Reset pre-commit environments

Clear out any old cached environments created with incompatible Python versions:

```
pre-commit clean
rm -rf ~/.cache/pre-commit
```

## 3. Prevent pip from forcing user installs (common on HPC systems)

Some clusters configure pip to always use `--user`, which breaks pre-commit.

Disable this behavior:

```
export PIP_USER=false
export PIP_CONFIG_FILE=/dev/null
```

## 4. Run whitespace and end-of-file fixers

Pre-commit hooks to remove trailing spaces and ensure newline at EOF:

```
pre-commit run trailing-whitespace -a
pre-commit run end-of-file-fixer -a
```

## 5. Run Prettier on files

You can format files manually with Prettier:

Format a single file:

```
prettier --write path/to/file
```

Format all supported files:

```
prettier --write .
```

Check formatting without modifying files:

```
prettier --check .
```

## 6. Fix Prettier or whitespace conflicts during git commit

If a commit fails with a message such as:

* "files were modified by this hook"
* "stashed changes conflicted with hook auto-fixes"

Then:

1. Inspect differences:

   ```
   git diff path/to/file
   ```

2. Accept the auto-formatted version:

   ```
   git checkout -- path/to/file
   git add path/to/file
   git commit -m "apply formatting fixes"
   ```

## 7. Re-run a commit after formatting

After fixing all formatting issues:

```
git add -A
git commit -m "apply formatting and whitespace corrections"
```

## Extra Tips

* Always stage your changes before committing to avoid pre-commit stash conflicts:

  ```
  git add -A
  ```

* Run all pre-commit hooks locally before pushing:

  ```
  pre-commit run -a
  ```

* Enable automatic whitespace handling in VS Code:

  ```
  "files.trimTrailingWhitespace": true,
  "files.insertFinalNewline": true
  ```

* If pre-commit keeps selecting an unwanted Python version, add this to `.pre-commit-config.yaml`:

  ```
  default_language_version:
    python: python3.11
  ```
