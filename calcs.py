import logging

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

def eval_rssi(rssi):
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

def eval_rsrp(rsrp):
    if rsrp >= RSRP_EXCLNT_GOOD_BOUND:
        return "Excellent"
    elif rsrp >= RSRP_GOOD_FAIR_BOUND:
        return "Good"
    elif rsrp >= RSRP_FAIR_POOR_BOUND:
        return "Fair"
    elif rsrp >= RSRP_POOR_UNUSBL_BOUND:
        return "Poor"
    elif rsrp > float('-inf'):
        return "Unusable"
    else:
        return "ERROR"

def eval_rsrq(rsrq):
    if rsrq >= RSRQ_EXCLNT_GOOD_BOUND:
        return "Excellent"
    elif rsrq >= RSRQ_GOOD_FAIR_BOUND:
        return "Good"
    elif rsrq >= RSRQ_FAIR_POOR_BOUND:
        return "Fair"
    elif rsrq >= RSRQ_POOR_UNUSBL_BOUND:
        return "Poor"
    elif rsrq > float('-inf'):
        return "Unusable"
    else:
        return "ERROR"