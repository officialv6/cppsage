import shutil
import sys
import subprocess
from pathlib import Path

def run(cmd: str):
    print(f"→ {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(result.returncode)

# Clean old build artifacts
for folder in ["dist", "cppsage.egg-info", "build"]:
    path = Path(folder)
    if path.exists():
        print(f"Removing {folder}/")
        shutil.rmtree(path)

# Build the package
run("python -m build")

# Upload to PyPI
run("twine upload dist/*")
