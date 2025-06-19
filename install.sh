#!/bin/bash
set -e

# Install system prerequisites
sudo apt-get update
sudo apt-get install -y git curl build-essential

# Install pyenv if missing
if [ ! -d "$HOME/.pyenv" ]; then
  curl https://pyenv.run | bash
fi

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

PYTHON_VERSION=3.11.9
pyenv install -s "$PYTHON_VERSION"
pyenv global "$PYTHON_VERSION"

# Install pipx and ensure PATH
pip install --user pipx
python3 -m pipx ensurepath
export PATH="$HOME/.local/bin:$PATH"

# Install the installer via pipx from GitHub
pipx install --force git+https://github.com/vrocky/code-workspace-ubuntu-installer.git

# Launch the CLI
code-workspace-ubuntu-installer install
