#!/usr/bin/env python
# -*- coding: utf-8

################################################################
#
# Copyright (c) 2010 Signove. All rights reserved.
# See the COPYING file for licensing details.
#
# Autors: Elvis Pfützenreuter < epx at signove dot com >
#         Raul Herbster < raul dot herbster at signove dot com >
################################################################

'''
Test 2. Simple MDL creation.
Procedure:
1. Start the server (hdpy_bluez_server.py)
2. Run this script
'''

from hdpy_bluez_client import MyInstance
from hdpy_bluez_client import run_test
from hdpy_bluez_client import MCAP_MCL_STATE_CONNECTED
from hdpy_bluez_client import MCAP_MCL_STATE_PENDING


#               CREATE_MD_REQ(0x01)   mdlid, mdepid, conf
SEND_SCRIPT = [(MyInstance.CreateMDL, 0xff00, 0x0a, 0xbc), #invalid mdl 0xFF00
               (MyInstance.CreateMDL, 0x0023, 0x0a, 0xbc),
               (MyInstance.CreateMDL, 0x0024, 0x0a, 0xbc),
               (MyInstance.CreateMDL, 0x0025, 0x0a, 0xbc)
               ]

# Sent raw data
SENT = ["01FF000ABC",
        "0100230ABC",
        "0100240ABC",
        "0100250ABC",
        ]

# Received raw data
RECEIVED = ["0205FF00", # CREATE_MD_RSP (0x02) with RSP Invalid MDL (0x05)
            "02000023BC", # CREATE_MD_RSP (0x02) with RSP Sucess (0x00)
            "02000024BC",
            "02000025BC",
            ]

def check_asserts_cb(mcap, mcl):
    '''
    Check the mcap status
    '''
    if (mcap.counter == 0):
        assert(mcl.count_mdls() == 0)
        assert(mcl.sm.request_in_flight == 0)
        assert(mcl.state == MCAP_MCL_STATE_CONNECTED)
    elif (mcap.counter == 1):
        assert(mcl.count_mdls() == 1)
        assert(mcl.sm.request_in_flight == 0)
        assert(mcl.state == MCAP_MCL_STATE_PENDING)
    elif (mcap.counter == 2):
        assert(mcl.count_mdls() == 2)
        assert(mcl.sm.request_in_flight == 0)
        assert(mcl.state == MCAP_MCL_STATE_PENDING)
    elif (mcap.counter == 3):
        assert(mcl.count_mdls() == 3)
        assert(mcl.sm.request_in_flight == 0)
        assert(mcl.state == MCAP_MCL_STATE_PENDING)

run_test(SEND_SCRIPT, SENT, RECEIVED, check_asserts_cb)
