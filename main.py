import sys
import os
import pandas as pd

from config import (
    REPORTS_PATH, 
    RESULTS_PATH, 
    RESULT_FILE_NAME_SUFFIX,
)

from calcs import eval_rssi, eval_rsrp, eval_rsrq

        



def main():

    create_results_dir()

    print_start_message()

    cmd_registry = {
        "exit": (exit_program, "Exits the analyzer"),
        "help": (show_help, "Prints list of possible commands"),
        "run": (run_analyzer, "Runs the analyzer"),
    }

    verbose = "--verbose" in sys.argv

    #repl state
    repl = True

    while (repl):
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
            file_name = report.replace(".xls", f" {RESULT_FILE_NAME_SUFFIX}")
            
            # create data frame
            df = pd.read_excel(f'{REPORTS_PATH}/{report}')

            # perform analysis on dataframe
            rssi_dbm_series = df['RSSI (dBm)']
            rsrp_dbm_series = df['RSRP (dBm)']
            rsrq_db_series = df['RSRQ (dB)']
            rssi_dbm_series_evaled = rssi_dbm_series.map(eval_rssi)
            rsrp_dbm_series_evaled = rsrp_dbm_series.map(eval_rsrp)
            rsrq_db_series_evaled = rsrq_db_series.map(eval_rsrq)
        
            # add results columns
            df['RSSI (dBm) Result'] = rssi_dbm_series_evaled
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
        print('')


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
    print('')


def exit_program():
    print('exiting...')
    sys.exit(1)


def show_help(cmd_registry):
    print('Possible commands:')
    for cmd, (_, desc) in cmd_registry.items():
        print(f'    {cmd} : {desc}')
    print('')


def unknown_command(cmd):
        print(f'unknown command <{cmd}>')


if __name__ == "__main__":
    main()


