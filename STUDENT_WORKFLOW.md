# Student Workflow Guide

This guide explains how to use this base environment for your course assignments, from cloning the repository to submitting your work.

## Getting Started

### Option 1: Local Development (Recommended for Learning)

#### 1. Clone the Repository

```bash
# Clone the base environment repository
git clone <repository-url>
cd base-environment

# Or if you forked it
git clone <your-fork-url>
cd base-environment
```

#### 2. Set Up Your Environment

Follow the instructions in [README.md](README.md) to:
- Install pyenv
- Install Python 3.13
- Install uv
- Create and activate your virtual environment

```bash
# Quick recap:
uv sync
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\Activate.ps1  # Windows PowerShell
```

#### 3. Verify Your Setup

```bash
python main.py
```

You should see all packages marked as "OK".

#### 4. Start Jupyter

```bash
jupyter notebook
# or
jupyter lab
```

Your browser will open with the Jupyter interface.

### Option 2: Google Colab (Alternative)

If you prefer to use Google Colab or encounter issues with local setup, that's perfectly acceptable!

1. Go to [Google Colab](https://colab.research.google.com/)
2. Create a new notebook
3. Install any packages you need at the start of your notebook:

```python
# Example: Installing packages in Colab
!pip install package-name
```

**Note:** Most common packages (numpy, pandas, matplotlib, scikit-learn, tensorflow) are pre-installed in Colab.

## Working on Assignments

### Creating Your Assignment Files

1. **Create a new folder for each assignment:**

```bash
mkdir assignment-1
cd assignment-1
```

2. **Create your Jupyter notebook:**

```bash
jupyter notebook assignment-1.ipynb
# or create it directly in the Jupyter interface
```

3. **Structure your notebook with both code and markdown cells**

### Using Markdown Cells (IMPORTANT!)

We expect you to use markdown cells extensively to:
- Explain your thought process
- Describe your approach to solving problems
- Interpret results and findings
- Document assumptions and decisions
- Show mathematical formulas when relevant

**Example notebook structure:**

```
[Markdown Cell]
# Assignment 1: Problem 1
## Understanding the Problem
In this problem, we need to...

[Markdown Cell]
## Approach
I will solve this by:
1. First, ...
2. Then, ...
3. Finally, ...

[Code Cell]
import numpy as np
import pandas as pd
# Your code here

[Markdown Cell]
## Results and Interpretation
The results show that...

[Code Cell]
# Visualization or additional analysis

[Markdown Cell]
## Conclusion
Based on the analysis...
```

**Why markdown cells matter:**
- They demonstrate your understanding of the concepts
- They show your problem-solving process
- They make your work easier to grade
- They give you practice in technical communication
- They help you organize your thoughts

### Best Practices

1. **Always execute all cells** before submitting (Kernel → Restart & Run All)
2. **Clear output and re-run** to ensure reproducibility
3. **Use descriptive variable names**
4. **Comment complex code**
5. **Include visualizations** where appropriate
6. **Explain your results** in markdown cells

## Organizing Your Work

We recommend this folder structure:

```
base-environment/
├── .venv/                  # Virtual environment (don't commit this)
├── assignment-1/
│   ├── assignment-1.ipynb  # Your notebook
│   ├── assignment-1.html   # Exported HTML
│   └── data/               # Any data files (if needed)
├── assignment-2/
│   ├── assignment-2.ipynb
│   └── assignment-2.pdf
├── project/
│   └── ...
├── pyproject.toml
├── README.md
└── main.py
```

## Submission Requirements

For each assignment, you must submit:

### 1. Fully Executed Jupyter Notebook (.ipynb)

- All cells must be executed
- All output must be visible
- Include both code and markdown cells

To ensure your notebook is fully executed:
```
Kernel → Restart & Run All
```

Then save the notebook (Ctrl+S or Cmd+S).

### 2. Exported Version (HTML or PDF)

You must also submit an exported version for easy viewing in Canvas.

#### Option A: Export to HTML (Recommended)

**From Jupyter Notebook/Lab:**
```
File → Download as → HTML (.html)
```

**From command line:**
```bash
jupyter nbconvert --to html assignment-1.ipynb
```

#### Option B: Export to PDF

**From Jupyter (requires additional setup):**
```
File → Download as → PDF via LaTeX (.pdf)
```

**From command line:**
```bash
# First, ensure you have nbconvert and pandoc installed
uv add nbconvert
# Install pandoc: https://pandoc.org/installing.html

jupyter nbconvert --to pdf assignment-1.ipynb
```

**Alternative (HTML → PDF):**
1. Export to HTML first
2. Open the HTML file in your browser
3. Print to PDF (Ctrl+P / Cmd+P → Save as PDF)

### What to Submit to Canvas

Upload both files:
1. `assignment-X.ipynb` (the notebook file)
2. `assignment-X.html` or `assignment-X.pdf` (the exported version)

The exported version ensures we can view your work even if there are compatibility issues with the notebook.

## Using Git for Your Work (Optional but Recommended)

If you want to version control your work:

```bash
# Create your own repository for assignments
git init my-algorithms-assignments
cd my-algorithms-assignments

# Copy the base environment setup
cp -r ../base-environment/.venv .
cp ../base-environment/pyproject.toml .
cp ../base-environment/uv.lock .

# Create .gitignore
echo ".venv/" >> .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".ipynb_checkpoints/" >> .gitignore

# Start tracking your work
git add .
git commit -m "Initial setup"
```

**Important:** Don't commit the `.venv` directory (it's large and can be recreated with `uv sync`).

## Getting Help

### Environment Issues

If you have issues with your local environment:
1. Check the troubleshooting section in [README.md](README.md)
2. Try `uv sync` again
3. Consider using Google Colab as an alternative

### Package Installation

If you need a package that's not in the base environment:

**Local:**
```bash
uv add package-name
```

**Colab:**
```python
!pip install package-name
```

### Jupyter Issues

**Kernel not found:**
```bash
# Make sure you're in the activated environment
source .venv/bin/activate
# Reinstall ipykernel
uv add ipykernel
python -m ipykernel install --user --name=base-environment
```

**Can't start Jupyter:**
```bash
# Ensure jupyter is installed
uv add jupyter
```

## Tips for Success

1. **Start early** - Don't wait until the deadline to set up your environment
2. **Test your setup** - Run `python main.py` to verify everything works
3. **Use markdown liberally** - Explain your thinking, not just your code
4. **Execute all cells** - Before submitting, always "Restart & Run All"
5. **Check your exports** - Open the HTML/PDF to make sure it looks correct
6. **Ask questions** - If you're stuck, reach out early

## Workflow Checklist

Before submitting any assignment:

- [ ] All code cells execute without errors
- [ ] Markdown cells explain your approach and reasoning
- [ ] Visualizations are clear and labeled
- [ ] Results are interpreted and explained
- [ ] Notebook has been run from top to bottom (Restart & Run All)
- [ ] Output is saved in the notebook
- [ ] Exported to HTML or PDF
- [ ] Both .ipynb and .html/.pdf files are ready to submit
- [ ] File names are clear (e.g., `assignment-1.ipynb`, not `Untitled.ipynb`)

## Environment Flexibility

**You are free to:**
- Use Google Colab instead of a local environment
- Add additional packages as needed for your work
- Use any IDE you prefer (VS Code, PyCharm, Jupyter Lab, etc.)
- Work on any operating system

**We require:**
- A fully executed Jupyter notebook (.ipynb)
- An exported version (HTML or PDF)
- Clear explanations in markdown cells
- Reproducible results

## Summary

This base environment is here to help you get started quickly with a consistent setup. Whether you use it locally, modify it, or use Google Colab instead, the goal is the same: to give you hands-on experience with algorithms and data science while developing your technical communication skills through well-documented notebooks.

Good luck with your assignments!
