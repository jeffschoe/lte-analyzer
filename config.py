# File Creation
REPORTS_PATH = "./reports"
RESULTS_PATH = "./results"
RESULT_FILE_NAME_SUFFIX = "RESULT"

# Thresholds for report evaluation
RSSI_EXCLNT = (float('inf'), -59)
RSSI_GOOD = (-59, -69)
RSSI_FAIR = (-69, -74)
RSSI_POOR = (-74, -79)
RSSI_UNUSBL = (-79, float('-inf'))

RSRP_EXCLNT = (float('inf'), -79)
RSRP_GOOD = (-79, -89)
RSRP_FAIR = (-89, -109)
RSRP_POOR = (-109, -119)
RSRP_UNUSBL = (-119, float('-inf'))

RSRQ_EXCLNT = (float('inf'), -5)
RSRQ_GOOD = (-5, -8)
RSRQ_FAIR = (-8, -10)
RSRQ_POOR = (-10, -19)
RSRQ_UNUSBL = (-19, float('-inf'))
