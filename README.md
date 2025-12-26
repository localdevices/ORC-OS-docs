# OpenRiverCam Operating System documentation

This repository contains the documentation for OpenRiverCam OS.

## Setup the environment

First make a virtual environment:

```bash
python3 -m venv orc-os-docs
source orc-os-docs/bin/activate
```

Setup the required packages:

```bash
pip install -r requirements.txt
```

The documentation built requires a browser back-end to render HTML pages automatically. Set this up as follows:

```
playwright install chromium
```

To build the documentation:
```bash
cd docs
make clean  # if you want to rebuild the documentation from scratch
make html
```

For installation instructions of OpenRiverCam OS, see https://github.com/localdevices/ORC-OS/blob/main/README.md
