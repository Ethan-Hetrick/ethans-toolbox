## GitLab

### Clone a remote repository and switch to development branch

```bash
# Clone repo
git clone <URL>.git

# Print out available remote branches
git branch --all --v

# Make sure you have all updates
git fetch --all

# Create local branch and track a remote branch
git checkout -b <branch> origin/<branch>

# Check to see if it worked
git status
```

### Copy a development branch to a new branch

```bash
# Clone repo
git clone <URL>.git

# Fetch all
git fetch --all

# Create local branch from dev branch
git checkout -b <dev/new branch> <remotes/origin/dev/branch>

# Push new branch
git push -u origin <dev/branch>

# Set upstream for tracking
git branch --set-upstream-to=<origin/dev/branch>
```

## Reset to a different commit

```bash
git reset --hard <commit_hash>
```

## Create a development branch from a previous commit

```bash
# Create a local branch from a commit hash
git branch <branch> <hash>

# Switch to the new branch
git checkout <branch>

# Push branch to remote
git push --set-upstream origin <branch>
```

## Remove a file or directory from commit without deleting it locally

```bash
# Add the file to .gititignore
echo "<path>" >> .gitignore

# Remove it from git index
git rm -r --cached <path>
```

## Debugging

```bash
git branch -v
git status -v
git remote -v
git branch --all --v
git config --list
```

## GitHub
