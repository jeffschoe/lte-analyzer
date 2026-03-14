import sys
import os
import shutil
import pandas as pd

from config import (
    REPORTS_PATH, 
    RESULTS_PATH, 
    RESULT_FILE_NAME_SUFFIX,
)

from calcs import (
    eval_rssi, 
    eval_rsrp, 
    eval_rsrq, 
    get_rank, 
    get_recommendation
)

from config import signal_ranges


def main():

    create_results_dir()

    print_start_message()

    cmd_registry = {
        "exit": (exit_program, "Exits the analyzer"),
        "help": (show_help, "Prints list of possible commands"),
        "run": (run_analyzer, "Runs the analyzer"),
        "run --verbose": (run_analyzer, "Runs the analyzer and outputs adtl info and results to the console"),
        "clear": (clear_results_dir, "Clears (deletes) all contents of the results directory"),
        "bnd" : (show_bounds, "Displays the current signal boundary valaues"),
        "bnd -a" : (adjust_bounds, "⚠️  CMD NOT AVAILABLE YET - Allows user to adjust the signal boundar values"),
        "bnd -r" : (reset_bounds, "⚠️  CMD NOT AVAILABLE YET - Resets signal boundary values to defaults"),
        "info" : (show_info, "Displays some additional information and resources on the subject of cellular signal analysis")
    }

    while (True):
        print('')
        arg = input('Enter command > ').strip().lower() # get user command        
        verbose = "--verbose" in arg
        cmd = cmd_registry.get(arg) # return tuples of (funcs, descps)
        
        if cmd: # got a command
            cmd_func, _ = cmd # tuple unpacking, have func, ignore description
            if cmd_func == cmd_registry['help'][0]: # help cmd, needs registry passed
                cmd_func(cmd_registry) # calls `show_help(cmd_registry)`
            elif cmd_func == cmd_registry['run'][0]: # run cmd, needs registry passed
                cmd_func(verbose) # calls `run_analyzer(verbose)`
            else: cmd_func() # doesn't need adtl args, just execute it
        
        else:
            unknown_command(arg)
         

def run_analyzer(verbose):
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

        #rssi_evaled_rank_series = rssi_dbm_series_evaled.map(get_rank) this is not needed for current implementation
        rsrp_evaled_rank_series = rsrp_dbm_series_evaled.map(get_rank)
        rsrq_evaled_rank_series = rsrq_db_series_evaled.map(get_rank)
        final_result_series = rsrp_evaled_rank_series.combine(rsrq_evaled_rank_series, get_recommendation) # `.combine` allows pairwise operations on two series

        # add results columns
        df['RSSI (dBm) Result'] = rssi_dbm_series_evaled # example 'GOOD', 'POOR'
        df['RSRP (dBm) Result'] = rsrp_dbm_series_evaled
        df['RSRQ (dB) Result'] = rsrq_db_series_evaled
        df['FINAL RESULT'] = final_result_series

        # saves dataframe to .xlsx in results dir
        df.to_excel(f'{RESULTS_PATH}/{file_name}.xlsx')

        # view results in the CLI
        if verbose:
            print('')
            print(f'Results for file {file_name}\n{df}')

    print('')
    print(f'✅ Success, your results are now available at {RESULTS_PATH}')


def get_report_names(verbose):
    report_names = []
    print('')
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
    print('')
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
    print('Commands:')
    for cmd, (_, desc) in cmd_registry.items(): # unpacking, ignores function in tuple
        print(f'    {cmd} : {desc}')


def unknown_command(cmd):
        print('')
        print(f'unknown command <{cmd}>')


#range name/key: (signal type, upper bound, lower bound, unit, ranking, result description)
# "rssi_excellent_range": (rssi_type, rssi_max_bound, rssi_excellent_good_bound, RSSI_UNIT, 0, EXCELLENT_RESULT),
def show_bounds():
    print('')
    for _, (signal_type, upper_bound, lower_bound, unit, _, result_desc) in signal_ranges.items(): # `_` ignores arg/param in unpacking
        print(f'{signal_type} {result_desc}: {upper_bound} {unit} to {lower_bound} {unit}')


def adjust_bounds():
    print('')
    print('⚠️  Function under construction')
    

def reset_bounds():
    print('')
    print('⚠️  Function under construction')


def show_info():
    print('')
    print('- RSSI: Received Signal Strength Indicator - Measures overall signal strength, including noise and interference. Higher values indicate stronger reception. This metric alone if not a great indicator of LTE quality.')
    print('- RSRP: Reference Signal Received Power - Measures the strength of the LTE reference signal from the tower. Higher values are better. This, in conjuction with RSRQ, are a good indicator of LTE quality.')
    print('- RSRQ: Reference Signal Received Quality - Measures LTE signal quality and network congestion. Higher values are better. This, in conjuction with RSRP, are a good indicator of LTE quality.')
    print('- To learn more about cellular signal analysis, see sources such as: https://help.ui.com/hc/en-us/articles/31173907212567-Understanding-Cellular-Signal-Strength-and-Quality')


if __name__ == "__main__":
    main()


