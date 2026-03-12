import logging

from config import (
    bounds
)     

'''
def eval_rssi_old(rssi): # arg comes from excel table (cell of the series)
    if rssi >= RSSI_EXCLNT_GOOD_BOUND:
        return "Excellent"
    elif rssi >= RSSI_GOOD_FAIR_BOUND:
        return "Good"
    elif rssi >= RSSI_FAIR_POOR_BOUND:
        return "Fair"
    elif rssi >= RSSI_POOR_UNUSBL_BOUND:
        return "Poor"
    elif rssi > float('-inf'):
        return "Unusable"
    else:
        return "ERROR"
'''
    
def eval_rssi(rssi): # arg comes from excel table (cell of the series)
    if rssi >= bounds["RSSI_EXCLNT_GOOD_BOUND"][0]:
        return bounds["RSSI_EXCLNT_GOOD_BOUND"][3]
    
    elif rssi >= bounds["RSSI_GOOD_FAIR_BOUND"][0]:
        return bounds["RSSI_GOOD_FAIR_BOUND"][3]
    
    elif rssi >= bounds["RSSI_FAIR_POOR_BOUND"][0]:
        return bounds["RSSI_FAIR_POOR_BOUND"][3]
    
    elif rssi >= bounds["RSSI_POOR_UNUSBL_BOUND"][0]:
        return bounds["RSSI_POOR_UNUSBL_BOUND"][3]
    
    elif rssi > float('-inf'):
        return bounds["RSSI_POOR_UNUSBL_BOUND"][4]
    else:
        return "ERROR"

def eval_rsrp(rsrp):
    if rsrp >= bounds["RSRP_EXCLNT_GOOD_BOUND"][0]:
        return bounds["RSRP_EXCLNT_GOOD_BOUND"][3]
    
    elif rsrp >= bounds["RSRP_GOOD_FAIR_BOUND"][0]:
        return bounds["RSRP_GOOD_FAIR_BOUND"][3]
    
    elif rsrp >= bounds["RSRP_FAIR_POOR_BOUND"][0]:
        return bounds["RSRP_FAIR_POOR_BOUND"][3]
    
    elif rsrp >= bounds["RSRP_POOR_UNUSBL_BOUND"][0]:
        return bounds["RSRP_POOR_UNUSBL_BOUND"][3]
    
    elif rsrp > float('-inf'):
        return bounds["RSRP_POOR_UNUSBL_BOUND"][4]
    
    else:
        return "ERROR"

def eval_rsrq(rsrq):
    if rsrq >= bounds["RSRQ_EXCLNT_GOOD_BOUND"][0]:
        return bounds["RSRQ_EXCLNT_GOOD_BOUND"][3]
    
    elif rsrq >= bounds["RSRQ_GOOD_FAIR_BOUND"][0]:
        return bounds["RSRQ_GOOD_FAIR_BOUND"][3]
    
    elif rsrq >= bounds["RSRQ_FAIR_POOR_BOUND"][0]:
        return bounds["RSRQ_FAIR_POOR_BOUND"][3]
    
    elif rsrq >= bounds["RSRQ_POOR_UNUSBL_BOUND"][0]:
        return bounds["RSRQ_POOR_UNUSBL_BOUND"][3]
    
    elif rsrq > float('-inf'):
        return bounds["RSRQ_POOR_UNUSBL_BOUND"][4]
    
    else:
        return "ERROR"
    

def eval_final_recommendation():
    
    return