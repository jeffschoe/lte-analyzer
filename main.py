import sys
import os
import shutil
import pandas as pd

from config import (REPORTS_PATH, 
                    RESULTS_PATH, 
                    RESULT_FILE_NAME_SUFFIX,
                    RSSI_EXCLNT_GOOD_BOUND,
                    RSSI_GOOD_FAIR_BOUND,
                    RSSI_FAIR_POOR_BOUND,
                    RSSI_POOR_UNUSBL_BOUND,
                    RSRP_EXCLNT_GOOD_BOUND,
                    RSRP_GOOD_FAIR_BOUND,
                    RSRP_FAIR_POOR_BOUND,
                    RSRP_POOR_UNUSBL_BOUND,
                    RSRQ_EXCLNT_GOOD_BOUND,
                    RSRQ_GOOD_FAIR_BOUND,
                    RSRQ_FAIR_POOR_BOUND,
                    RSRQ_POOR_UNUSBL_BOUND,
)


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

        # assigns result file name, removes ".xls" suffix with new suffix
        file_name = report.replace(".xls", f" {RESULT_FILE_NAME_SUFFIX}")
        
        # create data frame
        df = pd.read_excel(f'{REPORTS_PATH}/{report}')

        # TODO
        # perform analysis on dataframe

        # get column titles "RSSI (dBm)"
        print(df['RSSI (dBm)'], '\n')


        # get column titles "RSRP (dBm)"
        print(df['RSRP (dBm)'], '\n')

        # get column titles "RSRQ (dB)"
        print(df['RSRQ (dB)'], '\n')

            # apply formula to each row
            # add intermediary results in new columns
            # add final results to end




        # saves dataframe to .xlsx in results dir
        df.to_excel(f'{RESULTS_PATH}/{file_name}.xlsx')

            
        


def eval_rssi(rssi):
    if float('inf') > rssi >= RSSI_EXCLNT_GOOD_BOUND:
        return "Excellent"
    elif RSSI_EXCLNT_GOOD_BOUND > rssi >= RSSI_GOOD_FAIR_BOUND:
        return "Good"
    elif RSSI_GOOD_FAIR_BOUND > rssi >= RSSI_FAIR_POOR_BOUND:
        return "Fair"
    elif RSSI_FAIR_POOR_BOUND > rssi >= RSSI_POOR_UNUSBL_BOUND:
        return "Poor"
    else: 
        return "Unusable"

    
def eval_rsrp(rsrp):
    if float('inf') > rsrp >= RSRP_EXCLNT_GOOD_BOUND:
        return "Excellent"
    elif RSRP_EXCLNT_GOOD_BOUND > rsrp >= RSRP_GOOD_FAIR_BOUND:
        return "Good"
    elif RSRP_GOOD_FAIR_BOUND > rsrp >= RSRP_FAIR_POOR_BOUND:
        return "Fair"
    elif RSRP_FAIR_POOR_BOUND > rsrp >= RSRP_POOR_UNUSBL_BOUND:
        return "Poor"
    else: 
        return "Unusable"

def eval_rsrq(rsrq):
    if float('inf') > rsrq >= RSRQ_EXCLNT_GOOD_BOUND:
        return "Excellent"
    elif RSRQ_EXCLNT_GOOD_BOUND > rsrq >= RSRQ_GOOD_FAIR_BOUND:
        return "Good"
    elif RSRQ_GOOD_FAIR_BOUND > rsrq >= RSRQ_FAIR_POOR_BOUND:
        return "Fair"
    elif RSRQ_FAIR_POOR_BOUND > rsrq >= RSRQ_POOR_UNUSBL_BOUND:
        return "Poor"
    else: 
        return "Unusable"


def get_report_names():
    report_names = []
    # returns a list of reports names in reports dir
    for item in os.listdir(REPORTS_PATH):
        if item.endswith(".xls"): # only gets excel files
            report_names.append(item)
    return report_names
    
    


if __name__ == "__main__":
    main()


