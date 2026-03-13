# File Creation
REPORTS_PATH = "./reports"
RESULTS_PATH = "./results"
RESULT_FILE_NAME_SUFFIX = "_RESULT"

# signal types
rssi_type = 'RSSI'
rsrp_type = 'RSRP'
rsrq_type = 'RSRQ'

# unit lables
RSSI_UNIT = 'dBm'
RSRP_UNIT = 'dBm'
RSRQ_UNIT = 'dB'

# result descriptions
EXCELLENT_RESULT = 'Excellent'
GOOD_RESULT = 'Good'
FAIR_RESULT = 'Fair'
POOR_RESULT = 'Poor'
UNUSABLE_RESULT = 'Unusable'

# Thresholds for report evaluation
rssi_max_bound = float('inf')
rssi_excellent_good_bound = -59
rssi_good_fair_bound = -69
rssi_fair_poor_bound = -74
rssi_poor_unusable_bound = -79
rssi_min_bound = float('-inf')

rsrp_max_bound = float('inf')
rsrp_excellent_good_bound = -79
rsrp_good_fair_bound = -89
rsrp_fair_poor_bound = -109
rsrp_poor_unusable_bound = -119
rsrp_min_bound = float('-inf')

rsrq_max_bound = float('inf')
rsrq_excellent_good_bound = -5
rsrq_good_fair_bound = -8
rsrq_fair_poor_bound = -10
rsrq_poor_unusable_bound = -19
rsrq_min_bound = float('-inf')

signal_ranges = {
    #range name/key: (signal type, upper bound, lower bound, unit, ranking, result description)
    "rssi_excellent_range": (rssi_type, rssi_max_bound, rssi_excellent_good_bound, RSSI_UNIT, 0, EXCELLENT_RESULT),
    "rssi_good_range" : (rssi_type, rssi_excellent_good_bound, rssi_good_fair_bound, RSSI_UNIT, 1, GOOD_RESULT),
    "rssi_fair_range" : (rssi_type, rssi_good_fair_bound, rssi_fair_poor_bound, RSSI_UNIT, 2, FAIR_RESULT),
    "rssi_poor_range" : (rssi_type, rssi_fair_poor_bound, rssi_poor_unusable_bound, RSSI_UNIT, 3, POOR_RESULT),
    "rssi_unusable_range" : (rssi_type, rssi_poor_unusable_bound, rssi_min_bound, RSSI_UNIT, 4, UNUSABLE_RESULT),

    "rsrp_excellent_range": (rsrp_type, rsrp_max_bound, rsrp_excellent_good_bound, RSRP_UNIT, 0, EXCELLENT_RESULT),
    "rsrp_good_range" : (rsrp_type, rsrp_excellent_good_bound, rsrp_good_fair_bound, RSRP_UNIT, 1, GOOD_RESULT),
    "rsrp_fair_range" : (rsrp_type, rsrp_good_fair_bound, rsrp_fair_poor_bound, RSRP_UNIT, 2, FAIR_RESULT),
    "rsrp_poor_range" : (rsrp_type, rsrp_fair_poor_bound, rsrp_poor_unusable_bound, RSRP_UNIT, 3, POOR_RESULT),
    "rsrp_unusable_range" : (rsrp_type, rsrp_poor_unusable_bound, rsrp_min_bound, RSRP_UNIT, 4, UNUSABLE_RESULT),

    "rsrq_excellent_range": (rsrq_type, rsrq_max_bound, rsrq_excellent_good_bound, RSRP_UNIT, 0, EXCELLENT_RESULT),
    "rsrq_good_range" : (rsrq_type, rsrq_excellent_good_bound, rsrq_good_fair_bound, RSRP_UNIT, 1, GOOD_RESULT),
    "rsrq_fair_range" : (rsrq_type, rsrq_good_fair_bound, rsrq_fair_poor_bound, RSRP_UNIT, 2, FAIR_RESULT),
    "rsrq_poor_range" : (rsrq_type, rsrq_fair_poor_bound, rsrq_poor_unusable_bound, RSRP_UNIT, 3, POOR_RESULT),
    "rsrq_unusable_range" : (rsrq_type, rsrq_poor_unusable_bound, rsrq_min_bound, RSRP_UNIT, 4, UNUSABLE_RESULT),
}


