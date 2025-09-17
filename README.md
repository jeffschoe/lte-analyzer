# octopus-lte-signal-meter-report-analyzer
CLI based tool for accepting .xls signal meter reports and giving an analysis/recommendation based on the data.

# Motivation
I'm an engineer who utilizes a device called the [Octopus](https://www.bvsystems.com/product/octopus-4g-lte-signal-meter/) to perform cellular signal scans. These scans produce a basic report of various celluar network characteristics in an .xls format. A manual analsis of these values must be performed, usually consisting of applying formulas in Excel. My aim with this program is to apply my analysis parameters to the reports and have pass/fail result automatically generated for me.  

# Requirements 
- uv
- pandas, pip install pandas

# usage
1. add cellular signal reports in the reports/ directory
2. run program: main.py [--verbose]
3. view analyzed reports in the results/ directory
