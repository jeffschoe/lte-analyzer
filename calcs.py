from config import signal_ranges
    


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
    

def eval_final_recommendation():
    
    return