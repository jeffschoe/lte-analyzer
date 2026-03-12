# octopus-lte-signal-meter-report-analyzer
CLI based tool for accepting .xls signal meter reports and giving an analysis/recommendation based on the data.

# Motivation
I'm an engineer who utilizes a device called the [Octopus](https://www.bvsystems.com/product/octopus-4g-lte-signal-meter/) to perform cellular signal scans. These scans produce a basic report of various celluar network characteristics in an .xls format. A manual analysis of these values must be performed, usually consisting of applying formulas in Excel. My aim with this program is to apply my analysis parameters to the reports and have pass/fail result automatically generated for me.  

# Requirements 
- uv
- pandas: uv add pandas
- openpyxl: uv add openpyxl

# usage
- add cellular signal reports in the reports/ directory
- start program (REPL): python main.py [--verbose]
    - once in the REPL, use command <help> to see list of all possible commands
- view analyzed reports in the results/ directory
