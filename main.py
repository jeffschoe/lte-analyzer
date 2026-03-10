import sys
import os
import shutil
import pandas as pd

from config import (
    REPORTS_PATH, 
    RESULTS_PATH, 
    RESULT_FILE_NAME_SUFFIX,
)

from calcs import eval_rssi, eval_rsrp, eval_rsrq


def main():
    run_command = "run"
    verbose = "--verbose" in sys.argv
    
    if not sys.argv[1:]: # if not arguments provided
        print("🐙Octpopus LTE Signal Meter Report Analyzer")
        print('Analyzes any Octopus cellular reports in the reports/ directory')
        print('')
        print('Usage: python main.py run [--verbose]')
        print('[--verbose] prints additional information to the console')
        print('')
        print(f'Results are stored as .xlsx in the results/ directory with the same file name + " {RESULT_FILE_NAME_SUFFIX}" appended')
        print('Existing files in results/ dir with the same file name will be overwritten')
        print('')
        print('exiting...')
        print('')
        sys.exit(1)
    if sys.argv[1] != run_command:
        print(f'unknown command <{sys.argv[1]}>')
        print("usage: python main.py run [--verbose]")  
        print('')
        print('exiting...')
        print('')
        sys.exit(1)
    
    # if results dir does not exist, create it
    if not os.path.exists(RESULTS_PATH):
        os.makedirs(RESULTS_PATH)

    # get report names
    for report in get_report_names(verbose):

        # assigns result file name, removes ".xls" suffix with new suffix
        file_name = report.replace(".xls", f" {RESULT_FILE_NAME_SUFFIX}")
        
        # create data frame
        df = pd.read_excel(f'{REPORTS_PATH}/{report}')

        # TODO
        # perform analysis on dataframe
        rssi_dbm_df = df['RSSI (dBm)']
        rsrp_dbm_df = df['RSRP (dBm)']
        rsrq_db_df = df['RSRQ (dB)']

        rssi_dbm_df_evaled = rssi_dbm_df.map(eval_rssi)
        rsrp_dbm_df_evaled = rsrp_dbm_df.map(eval_rssi)
        rsrq_db_df_evaled = rsrq_db_df.map(eval_rssi)

        if verbose:
            print(rssi_dbm_df, '\n')
            print(rsrp_dbm_df, '\n')
            print(rsrq_db_df, '\n')
            print(rssi_dbm_df_evaled, '\n')
            print(rsrp_dbm_df_evaled, '\n')
            print(rsrq_db_df_evaled, '\n')

        # apply formula to each row
        # add intermediary results in new columns
        # add final results to end




        # saves dataframe to .xlsx in results dir
        df.to_excel(f'{RESULTS_PATH}/{file_name}.xlsx')

            



def get_report_names(verbose):
    report_names = []
    # returns a list of reports names in reports dir
    for item in os.listdir(REPORTS_PATH):
        if item.endswith(".xls"): # only gets excel files
            report_names.append(item)
            if verbose:
                print(f"file '{item}' found and queued")
        else: 
            if verbose:
                print(f"file '{item}' skipped, .xls type not detected")
    return report_names
    
    


if __name__ == "__main__":
    main()


