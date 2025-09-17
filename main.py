import sys
import os
import shutil
import pandas as pd

from config import REPORTS_PATH, RESULTS_PATH

def main():
    verbose = "--verbose" in sys.argv
    if not sys.argv[1:]:
        print("Octpopus LTE Signal Meter Report Analyzer")
        print('\nAnalyzes any reports in the reports/ directory')
        print('Usage: python main.py [--verbose]')
        print('[--verbose] prints results to the console')
        print('Results are stored in the results/ directory\n')
        
    df = pd.read_excel('reports/Hampton Inn 1.xls')

    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH)


    for report in get_report_names():
        if report not in os.listdir(RESULTS_PATH): # avoids overwritting any preexisting results with that name
            print(f"copying file {report} to {RESULTS_PATH} dir")
            
            open(f"{RESULTS_PATH}/{report}", 'w') # create file with name
                
            shutil.copy(
                f"{REPORTS_PATH}/{report}",
                f"{RESULTS_PATH}/{report}"
            ) # copy file to results folder

        # open copied file for reading    
            # perform analysis on report
                # open the file
                # apply formula to each row
                # add intermediary results in new columns
                # add final results to end
        # save file
        # lock file
        else:
            print(f"already found file {report} in {RESULTS_PATH} dir, skipping...")
        pass





def get_report_names():
    report_names = []
    # returns a list of reports names in reports dir
    for item in os.listdir(REPORTS_PATH):
        if item.endswith(".xls"): # only gets excel files
            report_names.append(item)
    return report_names
    
    


if __name__ == "__main__":
    main()


