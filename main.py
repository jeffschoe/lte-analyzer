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

from config import (
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

    create_results_dir()

    print_start_message()

    cmd_registry = {
        "exit": (exit_program, "Exits the analyzer"),
        "help": (show_help, "Prints list of possible commands"),
        "run": (run_analyzer, "Runs the analyzer"),
        "clear": (clear_results_dir, "Clears (deletes) all contents of the results directory"),
        "showthresh" : (show_thresholds, "Displays the current theshold valaues"),
        "adjthresh" : (adjust_thresholds, "Allows user to adjust the threshold values"),
        "rstthresh" : (reset_thresholds, "Resets threshold values to defaults"),
    }

    verbose = "--verbose" in sys.argv

    #repl state
    repl = True

    while (repl):
        print('')
        arg = input('Enter command > ').strip().lower() # get user command
        cmd = cmd_registry.get(arg) # return tuples of (funcs, descps)
        
        if cmd: # got a command
            cmd_func, _ = cmd # tuple unpacking, have func, ignore description
            if cmd_func == cmd_registry['help'][0]: # help cmd, needs registry passed
                cmd_func(cmd_registry) # calls `show_help(cmd_registry)`
            elif cmd_func == cmd_registry['run'][0]: # help cmd, needs registry passed
                cmd_func(verbose) # calls `run_analyzer(verbose)`
            else: cmd_func() # doesn't need adtl args, just execute it
        
        else:
            unknown_command(arg)
         

def run_analyzer(verbose):
    # get report names
        for report in get_report_names(verbose):

            # assigns result file name, removes ".xls" suffix with new suffix
            file_name = report.replace(".xls", f"{RESULT_FILE_NAME_SUFFIX}")
            
            # create data frame
            df = pd.read_excel(f'{REPORTS_PATH}/{report}')

            # perform analysis on dataframe
            rssi_dbm_series = df['RSSI (dBm)'] # get the data from the original report column (series)
            rsrp_dbm_series = df['RSRP (dBm)']
            rsrq_db_series = df['RSRQ (dB)']
            rssi_dbm_series_evaled = rssi_dbm_series.map(eval_rssi) # example 'GOOD', 'POOR'
            rsrp_dbm_series_evaled = rsrp_dbm_series.map(eval_rsrp)
            rsrq_db_series_evaled = rsrq_db_series.map(eval_rsrq)
        
            # add results columns
            df['RSSI (dBm) Result'] = rssi_dbm_series_evaled # example 'GOOD', 'POOR'
            df['RSRP (dBm) Result'] = rsrp_dbm_series_evaled
            df['RSRQ (dB) Result'] = rsrq_db_series_evaled

            # saves dataframe to .xlsx in results dir
            df.to_excel(f'{RESULTS_PATH}/{file_name}.xlsx')

            # view results in the CLI
            if verbose:
                print(f'Results for file {file_name}\n{df}')
                print('')

        print('')
        print(f'✅ Success, your results are now available at {RESULTS_PATH}')


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


def create_results_dir():
    if not os.path.exists(RESULTS_PATH): # if results dir does not exist, create it
        os.makedirs(RESULTS_PATH)


def clear_results_dir():
    for filename in os.listdir(RESULTS_PATH):
        file_path = os.path.join(RESULTS_PATH, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    print("Results folder cleared.")


def print_start_message():
    print("🐙Octpopus LTE Signal Meter Report Analyzer")
    print('Analyzes any Octopus cellular reports in the reports/ directory')
    print('')
    print('Usage: python main.py [--verbose]')
    print('[--verbose] prints additional information to the console')
    print('')
    print('Once program has, use command <help> for list of additional commands')
    print('')
    print(f'Results are stored as .xlsx in the results/ directory with the same file name + " {RESULT_FILE_NAME_SUFFIX}" appended')
    print('Existing files in results/ dir with the same file name will be overwritten')


def exit_program():
    print('')
    print('exiting...')
    sys.exit(1)


def show_help(cmd_registry):
    print('')
    print('Possible commands:')
    for cmd, (_, desc) in cmd_registry.items():
        print(f'    {cmd} : {desc}')


def unknown_command(cmd):
        print('')
        print(f'unknown command <{cmd}>')


def show_thresholds():
    print('')
    print(f'RSSI_POOR_UNUSBL_BOUND = {RSSI_EXCLNT_GOOD_BOUND} dBm')
    print(f'RSSI_GOOD_FAIR_BOUND   = {RSSI_GOOD_FAIR_BOUND} dBm')
    print(f'RSSI_FAIR_POOR_BOUND   = {RSSI_FAIR_POOR_BOUND} dBm')
    print(f'RSSI_POOR_UNUSBL_BOUND = {RSSI_POOR_UNUSBL_BOUND} dBm')
    print('')
    print(f'RSRP_EXCLNT_GOOD_BOUND = {RSRP_EXCLNT_GOOD_BOUND} dBm')
    print(f'RSRP_GOOD_FAIR_BOUND   = {RSRP_GOOD_FAIR_BOUND} dBm')
    print(f'RSRP_FAIR_POOR_BOUND   = {RSRP_FAIR_POOR_BOUND} dBm')
    print(f'RSRP_POOR_UNUSBL_BOUND = {RSRP_POOR_UNUSBL_BOUND} dBm')
    print('')
    print(f'RSRQ_EXCLNT_GOOD_BOUND = {RSRQ_EXCLNT_GOOD_BOUND} dB')
    print(f'RSRQ_GOOD_FAIR_BOUND   = {RSRQ_GOOD_FAIR_BOUND} dB')
    print(f'RSRQ_FAIR_POOR_BOUND   = {RSRQ_FAIR_POOR_BOUND} dB')
    print(f'RSRQ_POOR_UNUSBL_BOUND = {RSRQ_POOR_UNUSBL_BOUND} dB')
    # NOTE: may consider storing bounds as dictionary for easier access to vars and names, allows for more customization

def adjust_thresholds():
    # Allows user to adjust the threshold values"
    pass
    

def reset_thresholds():
    # Resets threshold values to defaults
    pass


if __name__ == "__main__":
    main()


