# 🐙 Octopus LTE Signal Analyzer
A CLI tool for accepting 4G LTE signal meter reports and giving an analysis of the signal quality for each carrier and associated channel based on the data.

---

## 🏋️ Motivation
I'm an engineer who utilizes a device called the  [Octopus](https://www.bvsystems.com/product/octopus-4g-lte-signal-meter/) to perform cellular signal scans. These scans produce a basic report of various cellular network characteristics in an .xls format. A manual analysis of these values must be performed, usually consisting of applying formulas in Excel. My aim with this program is to apply my analysis parameters to the reports and have overall signal quality results automatically generated for me.  

--- 

## ✅ Requirements 
- Python 3.12 or higher

---

## 🚀 Getting Started

### Option 1: Using uv (recommended)
Install uv if you don't have it:
https://docs.astral.sh/uv/getting-started/installation/

#### Sync dependencies:
```sh
uv sync 
```
- This reads your `pyproject.toml` and installs all dependencies automatically into a local `.venv`.

#### Populate reports:
- Add reports to the `reports/` directory.
- Users without reports can copy sample reports from `reports_sample/`: 
  ```sh 
  cp -r ./reports_sample/* ./reports/
  ```
Running the project without populating any reports will not cause any harm. User will be prompted with a warning in such cases.

#### Run the project:
```sh
uv run main.py
```
- This executes your script inside that environment without needing to manually activate it.

### Option 2: Using pip

Create and activate a virtual environment:
```sh
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

#### Install dependencies:
```sh
pip install openpyxl pandas
```

#### Populate reports:
- Add reports to the `reports/` directory.
- Users without reports can copy sample reports from `reports_sample/`: 
  ```sh 
  cp -r ./reports_sample/* ./reports/
  ```
Running the project without populating any reports will not cause any harm. User will be prompted with a warning in such cases.

#### Run the project:
```sh
python main.py
```

---

## ✏️ Usage Notes
- It is recommended to add new cellular signal reports in `reports/` before running. See above 'Populate Reports' sections for more information.
- Run program as described above, which opens a REPL.
- Once inside the REPL
    - Use command `run` to start the analyzer.
    - Use command `help` to see all available commands.
- View results in `results/` directory.

---

## 🌱 Future Project Extensions and Ideas
- Refactor to NOT be REPL (REPL style does not add a lot of value).
- Use the argparse library for better argument integration.
- Allow user to define custom analysis parameters.
- Add Graphical output of results.
- Add a GUI.

---

## 📄 Contributing

This repo is a personal project, so contributions aren’t actively sought — but if you have suggestions or fixes, feel free to open an issue or pull request 👍

---

## 📜 License

MIT License

---

## 👤 Author

[jeffschoe](https://github.com/jeffschoe)

---


