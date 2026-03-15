# lte-analyzer
CLI based tool for accepting .xls signal meter reports and giving an analysis/recommendation based on the data.

## Motivation
I'm an engineer who utilizes a device called the [Octopus](https://www.bvsystems.com/product/octopus-4g-lte-signal-meter/) to perform cellular signal scans. These scans produce a basic report of various cellular network characteristics in an .xls format. A manual analysis of these values must be performed, usually consisting of applying formulas in Excel. My aim with this program is to apply my analysis parameters to the reports and have overall signal quality results automatically generated for me.  

## Requirements 
- Python 3.12 or higher

## Installation and running

### Option 1: Using uv (recommended)
Install uv if you don't have it:
https://docs.astral.sh/uv/getting-started/installation/

Sync dependencies and run:
```sh
uv sync 
uv run main.py
```
- `uv sync` reads your pyproject.toml and installs all dependencies automatically into a local .venv.
- `uv run main.py` executes your script inside that environment without needing to manually activate it

### Option 2: Using pip

Create and activate a virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

Install dependencies:
```sh
pip install openpyxl pandas
```

Run the project:
```sh
python main.py
```

## Usage Notes
- Add new cellular signal reports in `reports/` before running. 
- Users without reports can copy sample reports from `reports_sample/`: 
  ```sh 
  cp -r ./reports_sample/* ./reports/
  ```
- Start program as described above, which opens a REPL.
- Use command `run` to start the analyzer.
- Use command `help` to see all available commands.
- View results in `results/`.

## Future Project Extension
- allow user to define custom parameters from the repl
- graphical output of results
- gui


