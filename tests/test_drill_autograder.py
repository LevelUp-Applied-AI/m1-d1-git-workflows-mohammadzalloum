import subprocess
import sys
import os


def test_hello_py_has_completion_note():
    with open("hello.py") as f:
        content = f.read()
    assert "# Drill completed by" in content, \
        "hello.py must contain a '# Drill completed by' line"
    assert "# Drill completed by Your Name" not in content, \
        "Replace 'Your Name' with your actual name before submitting"


def test_environment_imports():
    result = subprocess.run(
        [sys.executable, "-c",
         "import pandas; import matplotlib; print('Environment OK')"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, \
        f"Import failed. Check requirements.txt is intact.\n{result.stderr}"
    assert "Environment OK" in result.stdout


def test_branch_name_not_placeholder():
    branch = os.environ.get("GITHUB_HEAD_REF", "")
    assert branch, \
        "GITHUB_HEAD_REF is not set — this test must run in a pull request context"
    assert "<" not in branch and ">" not in branch, \
        (f"Branch name '{branch}' looks like a placeholder. "
         "Use your actual GitHub username (e.g., drill/jsmith).")
