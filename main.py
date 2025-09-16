import sys


def main():
    verbose = "--verbose" in sys.argv
    if not sys.argv[1:]:
        print("Octpopus LTE Signal Meter Report Analyzer")
        print('\nAnalyzes any reports in the reports/ directory')
        print('Usage: python main.py [--verbose]')
        print('[--verbose] prints results to the console')
        print('Results are stored in the results/ directory\n')
        sys.exit(1)




if __name__ == "__main__":
    main()


