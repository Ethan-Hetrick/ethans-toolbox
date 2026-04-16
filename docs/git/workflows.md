# Git Workflows

Common Git commands I reach for when setting up branches, cleaning up tracked files, or checking repository state.

## GitLab

### Clone a remote repository and switch to a development branch

```bash
git clone <URL>.git
cd <repo>

git fetch --all
git branch --all --verbose
git checkout -b <branch> origin/<branch>
git status
```

### Create a new branch from an existing development branch

```bash
git clone <URL>.git
cd <repo>

git fetch --all
git checkout -b <new-branch> origin/<dev-branch>
git push -u origin <new-branch>
```

## Create a branch from a previous commit

```bash
git branch <branch> <commit_hash>
git checkout <branch>
git push --set-upstream origin <branch>
```

## Remove a file or directory from Git without deleting it locally

```bash
echo "<path>" >> .gitignore
git rm -r --cached <path>
```

## Reset to a different commit

!!! warning
    `git reset --hard` is destructive. Make sure you really want to discard local changes before using it.

```bash
git reset --hard <commit_hash>
```

## Debugging

```bash
git branch -v
git status -v
git remote -v
git branch --all --verbose
git config --list
```
