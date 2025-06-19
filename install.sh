#!/bin/bash
set -e

# Install system prerequisites
sudo apt-get update
sudo apt-get install -y git curl python3 python3-pip python3-venv build-essential

# Install pipx and ensure PATH
if ! command -v pipx >/dev/null 2>&1; then
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath
fi
export PATH="$HOME/.local/bin:$PATH"

# Install the installer via pipx from GitHub
pipx install --force git+https://github.com/vrocky/code-workspace-ubuntu-installer.git

# Launch the CLI
code-workspace-ubuntu-installer install
