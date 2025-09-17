import sys
import os
import shutil
import pandas as pd

from config import REPORTS_PATH, RESULTS_PATH, RESULT_FILE_NAME_SUFFIX

def main():
    verbose = "--verbose" in sys.argv
    if not sys.argv[1:]:
        print("Octpopus LTE Signal Meter Report Analyzer")
        print('\nAnalyzes any reports in the reports/ directory')
        print('Usage: python main.py [--verbose]')
        print('[--verbose] prints results to the console')
        print(f'Results are stored as .xlsx in the results/ directory with the same file name + " {RESULT_FILE_NAME_SUFFIX}" appended')
        print('Existing files in results/ dir with the same file name will be overwritten\n')
        
    
    # if results dir does not exist, create it
    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH)

    # get report names
    for report in get_report_names():
        # create data frame
        df = pd.read_excel('reports/Hampton Inn 1.xls')

        # play code
        #print(df, "\n")
        #for column_name in df:
        #    print(df[column_name], "\n")



        # assigns result file name, removes ".xls" suffix with new suffix
        file_name = report.replace(".xls", f" {RESULT_FILE_NAME_SUFFIX}")
        
        
        
        
        # TODO
        # perform analysis on dataframe
            # apply formula to each row
            # add intermediary results in new columns
            # add final results to end




        # saves dataframe to .xlsx in results dir
        df.to_excel(f'{RESULTS_PATH}/{file_name}.xlsx')

            
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


