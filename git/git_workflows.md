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
git push --set-upstream origin dev/ethan
```

## GitHub
