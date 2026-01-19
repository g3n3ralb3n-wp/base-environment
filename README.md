# Algorithms for Data Science Base Environment Setup Guide

## Note: If you need further explanations and instructions on how to use this repo for submitting assignments please see [Student Workflow Guide](STUDENT_WORKFLOW.md)

This guide will help you set up a Python development environment for this course using modern Python tools. All of our homework and programming assignments were created and completed using this environment. You may add to the environment if you so choose, we are just providing a base environment to help start you on the right foot. We will update this repository as Python changes but it works as of 1/19/2026. 

Claude Code wrote the instructions on how to do this for Windows as I have never used `pyenv` with Windows so mileage may vary. I would suggest using your [WSL2 Linux environment](https://learn.microsoft.com/en-us/windows/wsl/install) to do your work for this course if you are using a Windows machine. 

## Prerequisites

You'll need to install two tools:
1. **pyenv** - to manage Python versions
2. **uv** - to manage virtual environments and dependencies (faster alternative to pip/venv)

## Step 1: Install pyenv

### On macOS/Linux:

```bash
# Install pyenv
curl https://pyenv.run | bash

# Add to your shell configuration (~/.bashrc, ~/.zshrc, or ~/.bash_profile)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Reload your shell
source ~/.bashrc
```

### On Windows:

Use [pyenv-win](https://github.com/pyenv-win/pyenv-win):

```powershell
# In PowerShell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

Then restart your terminal.

## Step 2: Install Python 3.13 with pyenv

```bash
# Install Python 3.13 (latest version)
pyenv install 3.13

# Set it as your global Python version (optional)
pyenv global 3.13

# Verify installation
python --version
# Should show: Python 3.13.x
```

## Step 3: Install uv

### On macOS/Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### On Windows:

```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Alternative (using pip):

```bash
pip install uv
```

## Step 4: Set Up This Project

1. **Navigate to the project directory:**

```bash
cd path/to/base-environment
```

2. **Create and sync the virtual environment:**

```bash
uv sync
```

This command will:
- Create a `.venv` directory with a virtual environment
- Install all required dependencies listed in `pyproject.toml`
- Create/update a `uv.lock` file to ensure reproducible installs

3. **Activate the virtual environment:**

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

You should see `(base-environment)` appear in your terminal prompt.

## Step 5: Test Your Installation

Run the test script to verify everything is working:

```bash
python main.py
```

If all dependencies are installed correctly, the script will confirm your setup is complete.

## Daily Workflow

When you start working on this project:

1. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\Activate.ps1  # Windows PowerShell
   ```

2. **Work on your code** - all packages will be available

3. **Deactivate when done:**
   ```bash
   deactivate
   ```

## Managing Dependencies

### Adding a new package:

```bash
uv add package-name
```

### Removing a package:

```bash
uv remove package-name
```

### Updating all packages:

```bash
uv sync --upgrade
```

## Installed Packages

This environment includes the following packages for algorithms and machine learning coursework:

- **Data Processing:** numpy, pandas, scipy
- **Visualization:** matplotlib, seaborn, plotly
- **Machine Learning:** scikit-learn, tensorflow, torch (PyTorch), transformers
- **Statistical Analysis:** statsmodels, lifelines
- **Optimization:** cvxopt
- **Probabilistic Models:** pgmpy
- **Datasets:** datasets (Hugging Face)
- **Notebooks:** jupyter, ipykernel

## Troubleshooting

### Python version mismatch
If `uv sync` fails due to Python version, ensure you're using Python 3.13:
```bash
python --version
pyenv local 3.13  # Set Python 3.13 for this directory
```

### uv command not found
Restart your terminal after installing uv, or add it to your PATH manually.

### Virtual environment activation issues (Windows)
If you get a script execution error on Windows, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Why uv?

`uv` is a modern Python package manager written in Rust that is:
- **10-100x faster** than pip
- **More reliable** with better dependency resolution
- **Compatible** with existing Python tools and workflows
- **Simpler** with commands like `uv add` and `uv sync`

## Additional Resources

- [pyenv documentation](https://github.com/pyenv/pyenv)
- [uv documentation](https://docs.astral.sh/uv/)
- [Python 3.13 release notes](https://docs.python.org/3.13/whatsnew/3.13.html)
