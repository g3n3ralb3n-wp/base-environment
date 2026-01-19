"""
Test script to verify that the virtual environment is set up correctly.
Run this after activating your virtual environment with: source .venv/bin/activate
"""

import sys


def test_imports():
    """Test that all required packages can be imported."""
    print("Testing package imports...\n")

    packages = [
        ("numpy", "NumPy"),
        ("pandas", "Pandas"),
        ("matplotlib", "Matplotlib"),
        ("seaborn", "Seaborn"),
        ("plotly", "Plotly"),
        ("scipy", "SciPy"),
        ("sklearn", "Scikit-learn"),
        ("statsmodels", "Statsmodels"),
        ("tensorflow", "TensorFlow"),
        ("torch", "PyTorch"),
        ("transformers", "Transformers"),
        ("cvxopt", "CVXOPT"),
        ("pgmpy", "pgmpy"),
        ("lifelines", "Lifelines"),
        ("datasets", "Datasets"),
        ("jupyter", "Jupyter"),
    ]

    failed = []

    for module_name, display_name in packages:
        try:
            __import__(module_name)
            print(f"✓ {display_name:20} - OK")
        except ImportError as e:
            print(f"✗ {display_name:20} - FAILED")
            failed.append((display_name, str(e)))

    print("\n" + "="*60)

    if not failed:
        print("SUCCESS! All packages are installed correctly.")
        print("\nYour environment is ready to use!")
    else:
        print(f"FAILED! {len(failed)} package(s) could not be imported:\n")
        for name, error in failed:
            print(f"  - {name}: {error}")
        print("\nTry running: uv sync")
        return False

    print("="*60)
    return True


def show_versions():
    """Display Python and key package versions."""
    print("\nPython and Package Versions:")
    print(f"Python: {sys.version}")

    try:
        import numpy as np
        print(f"NumPy: {np.__version__}")
    except:
        pass

    try:
        import pandas as pd
        print(f"Pandas: {pd.__version__}")
    except:
        pass

    try:
        import sklearn
        print(f"Scikit-learn: {sklearn.__version__}")
    except:
        pass

    try:
        import torch
        print(f"PyTorch: {torch.__version__}")
    except:
        pass

    try:
        import tensorflow as tf
        print(f"TensorFlow: {tf.__version__}")
    except:
        pass

    print()


if __name__ == "__main__":
    print("="*60)
    print("Base Environment Setup Verification")
    print("="*60)
    print()

    # Check Python version
    python_version = sys.version_info
    if python_version.major == 3 and python_version.minor >= 13:
        print(f"✓ Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    else:
        print(f"⚠ Warning: Expected Python 3.13+, but found {python_version.major}.{python_version.minor}.{python_version.micro}")

    print()

    # Test all imports
    success = test_imports()

    if success:
        show_versions()
