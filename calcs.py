import pandas as pd
from pandas import Series

from config import (
    signal_ranges, 
    EXCELLENT_RESULT, 
    GOOD_RESULT, 
    FAIR_RESULT, 
    POOR_RESULT, 
    UNUSABLE_RESULT
)
    


#range name/key: (signal type, upper bound, lower bound, unit, ranking, result description)
#"rssi_excellent_range": (rssi_type, rssi_max_bound, rssi_excellent_good_bound, RSSI_UNIT, 0, EXCELLENT_RESULT),
def eval_rssi(rssi): # arg comes from excel table (cell of the series)
    if signal_ranges["rssi_excellent_range"][1] > rssi >= signal_ranges["rssi_excellent_range"][2]:
        return signal_ranges["rssi_excellent_range"][5]
    
    elif signal_ranges["rssi_good_range"][1] > rssi >= signal_ranges["rssi_good_range"][2]:
        return signal_ranges["rssi_good_range"][5]
    
    elif signal_ranges["rssi_fair_range"][1] > rssi >= signal_ranges["rssi_fair_range"][2]:
        return signal_ranges["rssi_fair_range"][5]
    
    elif signal_ranges["rssi_poor_range"][1] > rssi >= signal_ranges["rssi_poor_range"][2]:
        return signal_ranges["rssi_poor_range"][5]
    
    elif signal_ranges["rssi_unusable_range"][1] > rssi >= signal_ranges["rssi_unusable_range"][2]:
        return signal_ranges["rssi_unusable_range"][5]
    else:
        return "ERROR"
    
def eval_rsrp(rsrp): # arg comes from excel table (cell of the series)
    if signal_ranges["rsrp_excellent_range"][1] > rsrp >= signal_ranges["rsrp_excellent_range"][2]:
        return signal_ranges["rsrp_excellent_range"][5]
    
    elif signal_ranges["rsrp_good_range"][1] > rsrp >= signal_ranges["rsrp_good_range"][2]:
        return signal_ranges["rsrp_good_range"][5]
    
    elif signal_ranges["rsrp_fair_range"][1] > rsrp >= signal_ranges["rsrp_fair_range"][2]:
        return signal_ranges["rsrp_fair_range"][5]
    
    elif signal_ranges["rsrp_poor_range"][1] > rsrp >= signal_ranges["rsrp_poor_range"][2]:
        return signal_ranges["rsrp_poor_range"][5]
    
    elif signal_ranges["rsrp_unusable_range"][1] > rsrp >= signal_ranges["rsrp_unusable_range"][2]:
        return signal_ranges["rsrp_unusable_range"][5]
    else:
        return "ERROR"
    
def eval_rsrq(rsrq): # arg comes from excel table (cell of the series)
    if signal_ranges["rsrq_excellent_range"][1] > rsrq >= signal_ranges["rsrq_excellent_range"][2]:
        return signal_ranges["rsrq_excellent_range"][5]
    
    elif signal_ranges["rsrq_good_range"][1] > rsrq >= signal_ranges["rsrq_good_range"][2]:
        return signal_ranges["rsrq_good_range"][5]
    
    elif signal_ranges["rsrq_fair_range"][1] > rsrq >= signal_ranges["rsrq_fair_range"][2]:
        return signal_ranges["rsrq_fair_range"][5]
    
    elif signal_ranges["rsrq_poor_range"][1] > rsrq >= signal_ranges["rsrq_poor_range"][2]:
        return signal_ranges["rsrq_poor_range"][5]
    
    elif signal_ranges["rsrq_unusable_range"][1] > rsrq >= signal_ranges["rsrq_unusable_range"][2]:
        return signal_ranges["rsrq_unusable_range"][5]
    else:
        return "ERROR"
    
def get_rank(result):
    if result == EXCELLENT_RESULT:
        return 0
    elif result == GOOD_RESULT:
        return 1
    elif result == FAIR_RESULT:
        return 2
    elif result == POOR_RESULT:
        return 3
    else: # result == UNUSABLE_RESULT
        return 4

def get_recommendation(rsrp_evaled_rank_element, rsrq_evaled_rank_element):    
    
    max_rank = max(rsrp_evaled_rank_element, rsrq_evaled_rank_element)

    if max_rank == 0:
        return EXCELLENT_RESULT
    elif max_rank == 1:
        return GOOD_RESULT
    elif max_rank == 2:
        return FAIR_RESULT
    elif max_rank == 3:
        return POOR_RESULT
    else: # max == 4
        return UNUSABLE_RESULT
    
    
'''def get_rec_helper(rsrp_evaled_rank_cell, rsrq_evaled_rank_cell):

    max_rank = max(rsrp_evaled_rank_cell, rsrq_evaled_rank_cell)

    if max_rank == 0:
        return EXCELLENT_RESULT
    elif max_rank == 1:
        return GOOD_RESULT
    elif max_rank == 2:
        return FAIR_RESULT
    elif max_rank == 3:
        return POOR_RESULT
    else: # max == 4
        return UNUSABLE_RESULT'''