# code-workspace-ubuntu-installer

This project bootstraps a fresh Ubuntu system with essential developer tools using a Python-based CLI installed via `pipx`.

## Quick Start

Run the following command on a new Ubuntu system:

```bash
curl -sSL https://raw.githubusercontent.com/vrocky/code-workspace-ubuntu-installer/main/install.sh | bash
```

The bootstrap script installs Python from Ubuntu packages, installs `pipx`, installs this package from GitHub, and then launches the installer CLI.

## CLI Usage

Once installed you can invoke the tool directly:

```bash
code-workspace-ubuntu-installer install --profile full
code-workspace-ubuntu-installer status
```

The installer tracks progress in `~/.installer-state/install_status.json` so you can resume or retry steps as needed.

## Tools Installed by Python Orchestrator

### Programming Languages & Version Managers

| Tool | Installer | Purpose |
|------|-----------|---------|
| Python | apt | Base language + orchestration |
| pipx | `pip install --user pipx` | For isolated Python CLI apps |
| Node.js | nvm | Frontend, tooling, CLI utilities |
| Go | gvm | Backend, concurrency-based systems |
| Rust | rustup | CLI tools, performance apps |
| Java | sdkman | JVM apps, Spring, build tools |
| .NET SDK | Microsoft install script | C#, F#, cross-platform development |
| Git | `apt install git` | Version control |
| Git LFS | `git lfs install` | Large file support in Git |
| GitHub CLI | gh | GitHub automation from terminal |

### Developer Tools

| Tool | Install Method | Purpose |
|------|---------------|---------|
| Visual Studio Code | `.deb` package | Code editor |
| VS Code Extensions | `code --install-extension` | Language and dev tooling |
| &nbsp;&nbsp;├─ GitHub Copilot | | AI-assisted coding |
| &nbsp;&nbsp;├─ Python | | Python dev |
| &nbsp;&nbsp;├─ Pylance | | Python language server |
| &nbsp;&nbsp;├─ Prettier | | Code formatting |
| &nbsp;&nbsp;└─ ESLint | | JS/TS linting |
| Code Server | `.tar.gz` or `.deb` | Browser-accessible VS Code |

### DevOps & Infrastructure

| Tool | Install Method | Purpose |
|------|---------------|---------|
| Docker Engine | Official script | Containerization |
| Docker Compose Plugin | Docker CLI plugin | Multi-container setups |
| kubectl | Binary download | Kubernetes CLI |
| Helm (optional) | Script | Kubernetes package manager |
| Minikube (optional) | Binary download | Local Kubernetes cluster |

### System Utilities & Shell

| Tool | Purpose |
|------|---------|
| curl, wget | Download files and APIs |
| zip, unzip, tar | Archive and compression tools |
| zsh + Oh My Zsh | Better shell and prompt |
| tree, htop, fd, ripgrep | Dev-friendly CLI tools |

### Optional System Enhancements

| Tool | Purpose |
|------|---------|
| bat | Better `cat` with syntax highlighting |
| fzf | Fuzzy file finder |
| jq | JSON CLI parser |
| exa | Modern replacement for `ls` |

## Project Structure

- `install.sh` – bootstrap script to install Python and the CLI
- `installer/` – Python package containing the CLI and installation steps
- `pyproject.toml` – project metadata for packaging

## License

MIT
