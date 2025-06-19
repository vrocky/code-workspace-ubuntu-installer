# AGENTS instructions for code-workspace-ubuntu-installer

This repository contains a bootstrap shell script and a Python package that installs development tools on Ubuntu.

## Guidelines

- Keep the `install.sh` script idempotent and easy to run in a single command.
- When modifying the script or documentation, run `bash -n install.sh` to check syntax.
- Ensure Python files compile by running `python -m py_compile $(git ls-files '*.py')`.
- Update the README whenever new tools or commands are added.

## Programmatic checks

Run the following commands before committing to ensure scripts have valid syntax:

```bash
bash -n install.sh
python -m py_compile $(git ls-files '*.py')
```
