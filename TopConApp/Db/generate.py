#!/usr/bin/python3
# -*- coding: utf-8 -*-

from string import Template
from proto_template import SINT16_R, SINT16_W, UINT16_W, UINT16_W_1, UINT16_R, SELECT_SYSTEM, SELECT_MASTER, SELECT_R_INDEX, SELECT_W_INDEX
from db_template import ai, ai_ref, ai_ref_2, ao, ao_ref,bo, bo_cmd, mbbi, err, longin, loop_analog, loop_analog_ref, select

class Select():
    MASTER = 'selectMaster'
    SYSTEM = 'selectSystem'

default = {
    'ZRST':'', 'ONST':'', 'TWST':'', 'THST':'', 'FRST':'', 'FVST':'', 'SXST':'', 'SVST':'', 'EIST':'', 'NIST':'', 'TEST':'', 'ELST':'', 'TVST':'', 'TTST':'', 'FTST':'', 'FFST':'',
    'ZRSV':'', 'ONSV':'', 'TWSV':'', 'THSV':'', 'FRSV':'', 'FVSV':'', 'SXSV':'', 'SVSV':'', 'EISV':'', 'NISV':'', 'TESV':'', 'ELSV':'', 'TVSV':'', 'TTSV':'', 'FTSV':'', 'FFSV':'',
    'SELECT':'', 'PHAS':'0', 'EOFF':'0', 'ESLO':'1', 'DRVH':'0', 'DRVL':'0', 'LINR':'NO CONVERSION', 'MINUS':'', 'DISV':'0', 'DISA':'1', 'EGU':'', 'PREC':'2',
    'SCAN':'Passive', 'PINI':'NO'
}

UINT16_W_mapping = [
    # System Control
    {'pv':'OutVolt-Sel', 'proto':'setOutVoltOnOff', 'addr':0x005089, 'DESC':'Volt On/Off', 'type':'bo',                           'DISA':'$(MASTER=0)'},
    {'pv':'Save-Cmd',    'proto':'saveSettings',          'addr':0x00508A, 'DESC':'Save settings to non-volatile memory', 'type':'bo_cmd', 'DISA':'$(MASTER=0)'},
    {'pv':'Clear-Cmd',   'proto':'clearErr',            'addr':0x00508B, 'DESC':'Clear Errors and/or warnings', 'type':'bo_cmd',         'DISA':'$(MASTER=0)'}
]

UINT16_R_mapping = [
    # Warning Monitoring
    {'pv':'Mod:StdWarnGroup-Mon',                 'proto':'getModStdWarnGroup',  'addr':0x00508E, 'DESC':'Standard waring group',            'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:StdWarnIntrn-Mon',              'proto':'getModStdWarnGroup0', 'addr':0x00509B, 'DESC':'Std warning group 0',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnIntrnPDSP-Mon',          'proto':'getModStdWarnGroup1', 'addr':0x00509C, 'DESC':'Std warning group 1',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnOutCurrent-Mon',         'proto':'getModStdWarnGroup2', 'addr':0x00509D, 'DESC':'Std warning group 2',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnOutVolt-Mon',         'proto':'getModStdWarnGroup3', 'addr':0x00509E, 'DESC':'Std warning group 3',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnSupply-Mon',                'proto':'getModStdWarnGroup4', 'addr':0x00509F, 'DESC':'Std warning group 4',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnTemperature-Mon',           'proto':'getModStdWarnGroup5', 'addr':0x0050A0, 'DESC':'Std warning group 5',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnComm-Mon',         'proto':'getModStdWarnGroup6', 'addr':0x0050A1, 'DESC':'Std warning group 6',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnIntrnModulator-Mon',     'proto':'getModStdWarnGroup7', 'addr':0x0050B0, 'DESC':'Std warning group 7',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnIntrnADOvrRng1-Mon',  'proto':'getModStdWarnGroup8', 'addr':0x0050B1, 'DESC':'Std warning group 8',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnIntrnADOvrRng2-Mon',  'proto':'getModStdWarnGroup9', 'addr':0x0050B2, 'DESC':'Std warning group 9',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnIntrnADUndrRng1-Mon', 'proto':'getModStdWarnGroupA', 'addr':0x0050B3, 'DESC':'Std warning group A',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnIntrnADUndrRng2-Mon', 'proto':'getModStdWarnGroupB', 'addr':0x0050B4, 'DESC':'Std warning group B',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnLogin-Mon',                 'proto':'getModStdWarnGroupC', 'addr':0x0050B5, 'DESC':'Std warning group C',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnConf-Mon',         'proto':'getModStdWarnGroupD', 'addr':0x0050B6, 'DESC':'Std warning group D',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnConf2-Mon',        'proto':'getModStdWarnGroupE', 'addr':0x0050B7, 'DESC':'Std warning group E',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnMisc-Mon',         'proto':'getModStdWarnGroupF', 'addr':0x0050A2, 'DESC':'Std warning group F',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnGroup-Mon',                 'proto':'getModExtWarnGroup',  'addr':0x302A11, 'DESC':'Extended warning group',           'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:ExtWarnIBCSystem-Mon',             'proto':'getModExtWarnGroupG', 'addr':0x302A12, 'DESC':'Ext warning group G',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCSuppply-Mon',            'proto':'getModExtWarnGroupH', 'addr':0x302A13, 'DESC':'Ext warning group H',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCComm-Mon',      'proto':'getModExtWarnGroupJ', 'addr':0x302A14, 'DESC':'Ext warning group J',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCPwr-Mon',              'proto':'getModExtWarnGroupK', 'addr':0x302A15, 'DESC':'Ext warning group K',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCInverter-Mon',           'proto':'getModExtWarnGroupL', 'addr':0x302A16, 'DESC':'Ext warning group L',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCMisc-Mon',      'proto':'getModExtWarnGroupM', 'addr':0x302A17, 'DESC':'Ext warning group M',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCInverter2-Mon',          'proto':'getModExtWarnGroupN', 'addr':0x302A18, 'DESC':'Ext warning group N',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnSupply2-Mon',               'proto':'getModExtWarnGroupS', 'addr':0x302A1C, 'DESC':'Ext warning group S',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnLogin2-Mon',                'proto':'getModExtWarnGroupT', 'addr':0x302A1D, 'DESC':'Ext warning group T',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnConf3-Mon',        'proto':'getModExtWarnGroupU', 'addr':0x302A1E, 'DESC':'Ext warning group U',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnComm3-Mon',        'proto':'getModExtWarnGroupV', 'addr':0x302A1F, 'DESC':'Ext warning group V',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIntrn2-Mon',             'proto':'getModExtWarnGroupW', 'addr':0x302A20, 'DESC':'Ext warning group W',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnComm2-Mon',        'proto':'getModExtWarnGroupX', 'addr':0x302A21, 'DESC':'Ext warning group X',              'type':'longin', 'SELECT':Select.MASTER},

    {'pv':'Sys:StdWarnGroup-Mon',                 'proto':'getSysStdWarnGroup',  'addr':0x00508E, 'DESC':'Standard warning group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:StdWarnIntrn-Mon',              'proto':'getSysStdWarnGroup0', 'addr':0x00509B, 'DESC':'Std warning group 0',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnIntrnPDSP-Mon',          'proto':'getSysStdWarnGroup1', 'addr':0x00509C, 'DESC':'Std warning group 1',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnOutCurrent-Mon',         'proto':'getSysStdWarnGroup2', 'addr':0x00509D, 'DESC':'Std warning group 2',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnOutVolt-Mon',         'proto':'getSysStdWarnGroup3', 'addr':0x00509E, 'DESC':'Std warning group 3',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnSupply-Mon',                'proto':'getSysStdWarnGroup4', 'addr':0x00509F, 'DESC':'Std warning group 4',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnTemperature-Mon',           'proto':'getSysStdWarnGroup5', 'addr':0x0050A0, 'DESC':'Std warning group 5',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnComm-Mon',         'proto':'getSysStdWarnGroup6', 'addr':0x0050A1, 'DESC':'Std warning group 6',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnIntrnModulator-Mon',     'proto':'getSysStdWarnGroup7', 'addr':0x0050B0, 'DESC':'Std warning group 7',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnIntrnADOvrRng1-Mon',  'proto':'getSysStdWarnGroup8', 'addr':0x0050B1, 'DESC':'Std warning group 8',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnIntrnADOvrRng2-Mon',  'proto':'getSysStdWarnGroup9', 'addr':0x0050B2, 'DESC':'Std warning group 9',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnIntrnADUndrRng1-Mon', 'proto':'getSysStdWarnGroupA', 'addr':0x0050B3, 'DESC':'Std warning group A',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnIntrnADUndrRng2-Mon', 'proto':'getSysStdWarnGroupB', 'addr':0x0050B4, 'DESC':'Std warning group B',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnLogin-Mon',                 'proto':'getSysStdWarnGroupC', 'addr':0x0050B5, 'DESC':'Std warning group C',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnConf-Mon',         'proto':'getSysStdWarnGroupD', 'addr':0x0050B6, 'DESC':'Std warning group D',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnConf2-Mon',        'proto':'getSysStdWarnGroupE', 'addr':0x0050B7, 'DESC':'Std warning group E',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnMisc-Mon',         'proto':'getSysStdWarnGroupF', 'addr':0x0050A2, 'DESC':'Std warning group F',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnGroup-Mon',                 'proto':'getSysExtWarnGroup',  'addr':0x302A11, 'DESC':'Extended warning group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:ExtWarnIBCSystem-Mon',             'proto':'getSysExtWarnGroupG', 'addr':0x302A12, 'DESC':'Ext warning group G',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCSuppply-Mon',            'proto':'getSysExtWarnGroupH', 'addr':0x302A13, 'DESC':'Ext warning group H',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCComm-Mon',      'proto':'getSysExtWarnGroupJ', 'addr':0x302A14, 'DESC':'Ext warning group J',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCPwr-Mon',              'proto':'getSysExtWarnGroupK', 'addr':0x302A15, 'DESC':'Ext warning group K',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCInverter-Mon',           'proto':'getSysExtWarnGroupL', 'addr':0x302A16, 'DESC':'Ext warning group L',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCMisc-Mon',      'proto':'getSysExtWarnGroupM', 'addr':0x302A17, 'DESC':'Ext warning group M',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCInverter2-Mon',          'proto':'getSysExtWarnGroupN', 'addr':0x302A18, 'DESC':'Ext warning group N',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnSupply2-Mon',               'proto':'getSysExtWarnGroupS', 'addr':0x302A1C, 'DESC':'Ext warning group S',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnLogin2-Mon',                'proto':'getSysExtWarnGroupT', 'addr':0x302A1D, 'DESC':'Ext warning group T',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnConf3-Mon',        'proto':'getSysExtWarnGroupU', 'addr':0x302A1E, 'DESC':'Ext warning group U',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnComm3-Mon',        'proto':'getSysExtWarnGroupV', 'addr':0x302A1F, 'DESC':'Ext warning group V',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIntrn2-Mon',             'proto':'getSysExtWarnGroupW', 'addr':0x302A20, 'DESC':'Ext warning group W',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnComm2-Mon',        'proto':'getSysExtWarnGroupX', 'addr':0x302A21, 'DESC':'Ext warning group X',              'type':'longin', 'SELECT':Select.SYSTEM},

    # Err Monitoring
    {'pv':'Mod:StdErrGroup-Mon',                 'proto':'getModStdErrGroup',  'addr':0x00508D, 'DESC':'Standard error group',           'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:StdErrIntrn-Mon',              'proto':'getModStdErrGroup0', 'addr':0x005093, 'DESC':'Std error group 0',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrIntrnPDSP-Mon',          'proto':'getModStdErrGroup1', 'addr':0x005094, 'DESC':'Std error group 1',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrOutCurrent-Mon',         'proto':'getModStdErrGroup2', 'addr':0x005095, 'DESC':'Std error group 2',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrOutVolt-Mon',         'proto':'getModStdErrGroup3', 'addr':0x005096, 'DESC':'Std error group 3',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrSupply-Mon',                'proto':'getModStdErrGroup4', 'addr':0x005097, 'DESC':'Std error group 4',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrTemperature-Mon',           'proto':'getModStdErrGroup5', 'addr':0x005098, 'DESC':'Std error group 5',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrComm-Mon',         'proto':'getModStdErrGroup6', 'addr':0x005099, 'DESC':'Std error group 6',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrIntrnModulator-Mon',     'proto':'getModStdErrGroup7', 'addr':0x0050A8, 'DESC':'Std error group 7',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrIntrnADOvrRng1-Mon',  'proto':'getModStdErrGroup8', 'addr':0x0050A9, 'DESC':'Std error group 8',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrIntrnADOvrRng2-Mon',  'proto':'getModStdErrGroup9', 'addr':0x0050AA, 'DESC':'Std error group 9',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrIntrnADUndrRng1-Mon', 'proto':'getModStdErrGroupA', 'addr':0x0050AB, 'DESC':'Std error group A',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrIntrnADUndrRng2-Mon', 'proto':'getModStdErrGroupB', 'addr':0x0050AC, 'DESC':'Std error group B',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrLogin-Mon',                 'proto':'getModStdErrGroupC', 'addr':0x0050AD, 'DESC':'Std error group C',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrConf-Mon',         'proto':'getModStdErrGroupD', 'addr':0x0050AE, 'DESC':'Std error group D',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrConf2-Mon',        'proto':'getModStdErrGroupE', 'addr':0x0050AF, 'DESC':'Std error group E',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrMisc-Mon',         'proto':'getModStdErrGroupF', 'addr':0x00509A, 'DESC':'Std error group F',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrGroup-Mon',                 'proto':'getModExtErrGroup',  'addr':0x302A00, 'DESC':'Extended error group',           'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:ExtErrIBCSystem-Mon',             'proto':'getModExtErrGroupG', 'addr':0x302A01, 'DESC':'Ext error group G',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIBCSuppply-Mon',            'proto':'getModExtErrGroupH', 'addr':0x302A02, 'DESC':'Ext error group H',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIBCComm-Mon',      'proto':'getModExtErrGroupJ', 'addr':0x302A03, 'DESC':'Ext error group J',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIBCPwr-Mon',              'proto':'getModExtErrGroupK', 'addr':0x302A04, 'DESC':'Ext error group K',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIBCInverter-Mon',           'proto':'getModExtErrGroupL', 'addr':0x302A05, 'DESC':'Ext error group L',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIBCMisc-Mon',      'proto':'getModExtErrGroupM', 'addr':0x302A06, 'DESC':'Ext error group M',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIBCInverter2-Mon',          'proto':'getModExtErrGroupN', 'addr':0x302A07, 'DESC':'Ext error group N',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrSupply2-Mon',               'proto':'getModExtErrGroupS', 'addr':0x302A0B, 'DESC':'Ext error group S',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrLogin2-Mon',                'proto':'getModExtErrGroupT', 'addr':0x302A0C, 'DESC':'Ext error group T',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrConf3-Mon',        'proto':'getModExtErrGroupU', 'addr':0x302A0D, 'DESC':'Ext error group U',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrComm3-Mon',        'proto':'getModExtErrGroupV', 'addr':0x302A0E, 'DESC':'Ext error group V',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrIntrn2-Mon',             'proto':'getModExtErrGroupW', 'addr':0x302A0F, 'DESC':'Ext error group W',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrComm2-Mon',        'proto':'getModExtErrGroupX', 'addr':0x302A10, 'DESC':'Ext error group X',              'type':'longin', 'SELECT':Select.MASTER},

    {'pv':'Sys:StdErrGroup-Mon',                 'proto':'getSysStdErrGroup',  'addr':0x00508D, 'DESC':'Standard error group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:StdErrIntrn-Mon',              'proto':'getSysStdErrGroup0', 'addr':0x005093, 'DESC':'Std error group 0',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrIntrnPDSP-Mon',          'proto':'getSysStdErrGroup1', 'addr':0x005094, 'DESC':'Std error group 1',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrOutCurrent-Mon',         'proto':'getSysStdErrGroup2', 'addr':0x005095, 'DESC':'Std error group 2',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrOutVolt-Mon',         'proto':'getSysStdErrGroup3', 'addr':0x005096, 'DESC':'Std error group 3',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrSupply-Mon',                'proto':'getSysStdErrGroup4', 'addr':0x005097, 'DESC':'Std error group 4',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrTemperature-Mon',           'proto':'getSysStdErrGroup5', 'addr':0x005098, 'DESC':'Std error group 5',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrComm-Mon',         'proto':'getSysStdErrGroup6', 'addr':0x005099, 'DESC':'Std error group 6',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrIntrnModulator-Mon',     'proto':'getSysStdErrGroup7', 'addr':0x0050A8, 'DESC':'Std error group 7',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrIntrnADOvrRng1-Mon',  'proto':'getSysStdErrGroup8', 'addr':0x0050A9, 'DESC':'Std error group 8',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrIntrnADOvrRng2-Mon',  'proto':'getSysStdErrGroup9', 'addr':0x0050AA, 'DESC':'Std error group 9',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrIntrnADUndrRng1-Mon', 'proto':'getSysStdErrGroupA', 'addr':0x0050AB, 'DESC':'Std error group A',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrIntrnADUndrRng2-Mon', 'proto':'getSysStdErrGroupB', 'addr':0x0050AC, 'DESC':'Std error group B',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrLogin-Mon',                 'proto':'getSysStdErrGroupC', 'addr':0x0050AD, 'DESC':'Std error group C',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrConf-Mon',         'proto':'getSysStdErrGroupD', 'addr':0x0050AE, 'DESC':'Std error group D',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrConf2-Mon',        'proto':'getSysStdErrGroupE', 'addr':0x0050AF, 'DESC':'Std error group E',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrMisc-Mon',         'proto':'getSysStdErrGroupF', 'addr':0x00509A, 'DESC':'Std error group F',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrGroup-Mon',                 'proto':'getSysExtErrGroup',  'addr':0x302A00, 'DESC':'Extended error group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:ExtErrIBCSystem-Mon',             'proto':'getSysExtErrGroupG', 'addr':0x302A01, 'DESC':'Ext error group G',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIBCSuppply-Mon',            'proto':'getSysExtErrGroupH', 'addr':0x302A02, 'DESC':'Ext error group H',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIBCComm-Mon',      'proto':'getSysExtErrGroupJ', 'addr':0x302A03, 'DESC':'Ext error group J',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIBCPwr-Mon',              'proto':'getSysExtErrGroupK', 'addr':0x302A04, 'DESC':'Ext error group K',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIBCInverter-Mon',           'proto':'getSysExtErrGroupL', 'addr':0x302A05, 'DESC':'Ext error group L',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIBCMisc-Mon',      'proto':'getSysExtErrGroupM', 'addr':0x302A06, 'DESC':'Ext error group M',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIBCInverter2-Mon',          'proto':'getSysExtErrGroupN', 'addr':0x302A07, 'DESC':'Ext error group N',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrSupply2-Mon',               'proto':'getSysExtErrGroupS', 'addr':0x302A0B, 'DESC':'Ext error group S',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrLogin2-Mon',                'proto':'getSysExtErrGroupT', 'addr':0x302A0C, 'DESC':'Ext error group T',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrConf3-Mon',        'proto':'getSysExtErrGroupU', 'addr':0x302A0D, 'DESC':'Ext error group U',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrComm3-Mon',        'proto':'getSysExtErrGroupV', 'addr':0x302A0E, 'DESC':'Ext error group V',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrIntrn2-Mon',             'proto':'getSysExtErrGroupW', 'addr':0x302A0F, 'DESC':'Ext error group W',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrComm2-Mon',        'proto':'getSysExtErrGroupX', 'addr':0x302A10, 'DESC':'Ext error group X',              'type':'longin', 'SELECT':Select.SYSTEM},

    # System Control
    {'pv':'FirmwareMain-Mon',     'proto':'getFirmwareMain',     'addr':0x007E01, 'DESC':'Main',     'type':'ai', 'PREC':'0', 'PINI':'YES'},
    {'pv':'FirmwareVersion-Mon',  'proto':'getFirmwareVersion',  'addr':0x007E02, 'DESC':'Version',  'type':'ai', 'PREC':'0', 'PINI':'YES'},
    {'pv':'FirmwareRevision-Mon', 'proto':'getFirmwareRevision', 'addr':0x007E03, 'DESC':'Revision', 'type':'ai', 'PREC':'0', 'PINI':'YES'},

    {'pv':'SerialNumHigh-Mon','proto':'getSerialNumHigh', 'addr':0x005128, 'DESC':'Revision', 'type':'ai', 'PREC':'0', 'PINI':'YES'},
    {'pv':'SerialNumLow-Mon', 'proto':'getSerialNumLow',  'addr':0x005129, 'DESC':'Revision', 'type':'ai', 'PREC':'0', 'PINI':'YES'},

    {'pv':'Sys:State-Mon',        'proto':'getSysState',         'addr':0x00508C, 'DESC':'System state', 'type':'mbbi',
        'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP',
        'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Mod:State-Mon',        'proto':'getModState',         'addr':0x00508C, 'DESC':'Module state', 'type':'mbbi',
        'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP',
        'SELECT':Select.MASTER, 'SCAN':'10 second'},

    {'pv':'Sys:ControlMode-Mon',  'proto':'getSysControlMode',   'addr':0x0050B8, 'DESC':'System control mode', 'type':'mbbi',
        'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Pwr', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active',
        'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Mod:ControlMode-Mon',  'proto':'getModControlMode',   'addr':0x0050B8, 'DESC':'Module control mode', 'type':'mbbi',
        'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Pwr', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active',
        'SELECT':Select.MASTER, 'SCAN':'10 second'},

]

SINT16_loop_mapping = [
    # ------------- Loop Values -------------
    # Voltage preset
    {'pv':'Mod:VoltPreset',    'proto':'ModVoltPreset', 'addr':0x005080, 'DESC':'Module voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:VoltPreset',    'proto':'SysVoltPreset', 'addr':0x005080, 'DESC':'System voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Voltage limit Q4
    {'pv':'Mod:VoltLimQ4',   'proto':'ModVoltLimQ4', 'addr':0x30251F, 'DESC':'Module voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:VoltLimQ4',   'proto':'SysVoltLimQ4', 'addr':0x30251F, 'DESC':'System voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Current preset
    {'pv':'Mod:CurrentPreset',    'proto':'ModCurrentPreset', 'addr':0x005081, 'DESC':'Module current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:CurrentPreset',    'proto':'SysCurrentPreset', 'addr':0x005081, 'DESC':'System current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Current limit Q4
    {'pv':'Mod:CurrentLimQ4',   'proto':'ModCurrentLimQ4', 'addr':0x30251D, 'DESC':'Module current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-', 'PINI':'YES'},
    {'pv':'Sys:CurrentLimQ4',   'proto':'SysCurrentLimQ4', 'addr':0x30251D, 'DESC':'System current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-', 'PINI':'YES'},
    # Pwr preset
    {'pv':'Mod:PwrPreset',      'proto':'ModPwrPreset', 'addr':0x005082, 'DESC':'Module power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPwr-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:PwrPreset',      'proto':'SysPwrPreset', 'addr':0x005082, 'DESC':'System power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPwr-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Pwr limit Q4
    {'pv':'Mod:PwrLimQ4',     'proto':'ModPwrLimQ4', 'addr':0x30251E, 'DESC':'Module power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPwr-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-', 'PINI':'YES'},
    {'pv':'Sys:PwrLimQ4',     'proto':'SysPwrLimQ4', 'addr':0x30251E, 'DESC':'System power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPwr-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-', 'PINI':'YES'},
    # Resistence Preset
    {'pv':'Mod:ResPreset', 'proto':'ModResPreset', 'addr':0x005083, 'DESC':'Module resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomIntrnRes-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:ResPreset', 'proto':'SysResPreset', 'addr':0x005083, 'DESC':'System resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomIntrnRes-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},

    # ------------- Controller Parameters -------------
    # Slope
    {'pv':'StartupVoltSlope', 'proto':'StartupVoltSlope', 'addr':0x005154, 'DESC':'Startup volt 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'StartupCurrentSlope', 'proto':'StartupCurrentSlope', 'addr':0x005155, 'DESC':'Startup curr 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'VoltSlope',        'proto':'VoltSlope',        'addr':0x005156, 'DESC':'Volt slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'CurrentSlope',        'proto':'CurrentSlope',        'addr':0x005157, 'DESC':'Current slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
]

SINT16_W_mapping = [ ]

SINT16_R_mapping = [
    # ------------- Remote Controle Input -------------
    {'pv':'ActiveInterface-Mon',        'proto':'getActiveInterface', 'addr':0x005087, 'DESC':'Active interface', 'type':'mbbi',
        'ZRST': 'Analog/Digital Inputs', 'ONST':'HMI', 'TWST':'RS232', 'THST':'Intrn', 'DESC':'Which interface is active', 'FRST':'passiv',
         'FRVL': '32767', 'SCAN':'10 second'},

    # ------------- Actual Values -------------
    # DC Link
    {'pv':'NomDCLinkVolt-Mon', 'proto':'getNomDCLinkVolt',  'addr':0x005105, 'DESC':'DC link nominal voltage',  'EGU':'V', 'PINI':'YES'},
    {'pv':'DCLinkVolt-Mon',    'proto':'getDCLinkVolt',     'addr':0x005012, 'DESC':'DC link voltage measure',  'EGU':'V', 'ref':'NomDCLinkVolt-Mon', 'PHAS':'1', 'SCAN':'10 second'},
    # Out Voltage
    {'pv':'Mod:OutVolt-Mon', 'proto':'getModOutVolt', 'addr':0x005084, 'DESC':'Module out voltage', 'EGU':'V', 'ref':'Mod:MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Sys:OutVolt-Mon', 'proto':'getSysOutVolt', 'addr':0x005084, 'DESC':'System out voltage', 'EGU':'V', 'ref':'Sys:MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    # Out Current
    {'pv':'Mod:OutCurrent-Mon', 'proto':'getModOutCurrent', 'addr':0x005085, 'DESC':'Module out current', 'EGU':'A', 'ref':['Mod:MaxCurrent-Mon', 'Mod:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Sys:OutCurrent-Mon', 'proto':'getSysOutCurrent', 'addr':0x005085, 'DESC':'System out current', 'EGU':'A', 'ref':['Sys:MaxCurrent-Mon', 'Sys:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    # Out Pwr
    {'pv':'Mod:OutPwr-Mon', 'proto':'getModOutPwr', 'addr':0x005086, 'DESC':'Module out power', 'EGU':'kW', 'ref':['Mod:MaxPwr-Mon', 'Mod:MinPwr-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Sys:OutPwr-Mon', 'proto':'getSysOutPwr', 'addr':0x005086, 'DESC':'System out power', 'EGU':'kW', 'ref':['Sys:MaxPwr-Mon', 'Sys:MinPwr-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},

    # ------------- Temperature -------------
    # Device
    {'pv':'IGBTT-Mon',      'proto':'getIGBTTemp',     'addr':0x005007, 'DESC':'IGBT temperature',      'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR', 'SCAN':'10 second'},
    {'pv':'RectifierT-Mon', 'proto':'getRectfierTemp', 'addr':0x00500F, 'DESC':'Rectifier temperature', 'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR', 'SCAN':'10 second'},

    # ------------- Module Values -------------
    {'pv':'Mod:MaxVolt-Mon',     'proto':'getModMaxVolt'     ,'addr':0x005100, 'DESC':'Maximum module voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Mod:MaxCurrent-Mon',     'proto':'getModMaxCurrent'     ,'addr':0x005101, 'DESC':'Maximum module current (Q1)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Mod:MaxPwr-Mon',       'proto':'getModMaxPwr'       ,'addr':0x005102, 'DESC':'Maximum module power (Q1)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Mod:MinVolt-Mon',     'proto':'getModMinVolt'     ,'addr':0x00510F, 'DESC':'Minimum module voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Mod:MinCurrent-Mon',     'proto':'getModMinCurrent'     ,'addr':0x005110, 'DESC':'Minimum module current (Q4)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Mod:MinPwr-Mon',       'proto':'getModMinPwr'       ,'addr':0x005111, 'DESC':'Minimum module power (Q4)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Mod:NomIntrnRes-Mon', 'proto':'getModNomIntrnRes' ,'addr':0x005103, 'DESC':'Nom. module internal resistence', 'EGU':'mOhms', 'PINI':'YES'},

    # ------------- System Values -------------
    {'pv':'Sys:MaxVolt-Mon',     'proto':'getSysMaxVolt'     ,'addr':0x00510B, 'DESC':'Maximum system voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Sys:MaxCurrent-Mon',     'proto':'getSysMaxCurrent'     ,'addr':0x00510C, 'DESC':'Maximum system current (Q1)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Sys:MaxPwr-Mon',       'proto':'getSysMaxPwr'       ,'addr':0x00510D, 'DESC':'Maximum system power (Q1)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Sys:MinVolt-Mon',     'proto':'getSysMinVolt'     ,'addr':0x005112, 'DESC':'Minimum system voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Sys:MinCurrent-Mon',     'proto':'getSysMinCurrent'     ,'addr':0x005113, 'DESC':'Minimum system current (Q4)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Sys:MinPwr-Mon',       'proto':'getSysMinPwr'       ,'addr':0x005114, 'DESC':'Minimum system power (Q4)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Sys:NomIntrnRes-Mon', 'proto':'getSysNomIntrnRes' ,'addr':0x00510E, 'DESC':'Nom. system internal resistence', 'EGU':'mOhms', 'PINI':'YES'}
]

db_str = ''
proto_str = '''
LockTimeout     = 10000;
WriteTimeout    = 10;
ReplyTimeout    = 1000;
ReadTimeout     = 10;
ExtraInput      = Error;
Terminator      = ;

'''

def getAddr(addr):
    address_as_string = "{:06X}".format(addr)
    return "\\x" + address_as_string[4:] + "\\x" + address_as_string[2:4] + "\\x" + address_as_string[:2]

def getSINT16_R():
    global proto_str
    global db_str

    proto_str += SELECT_SYSTEM
    proto_str += SELECT_MASTER

    db_str += select

    # SINT16 Analog Loop
    for mapping in SINT16_loop_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        mapping['HL'] = 'H' if not mapping.get('MINUS') else 'L'

        if mapping.get('SELECT'):
            if mapping.get('ref'):
                db_str += loop_analog_ref.safe_substitute(default, **mapping)
            else:
                db_str += loop_analog.safe_substitute(default, **mapping)

            proto  = mapping['proto']
            proto_ = mapping['proto'] + '_'
            pv     = mapping['pv']

            mapping['proto_'] = 'set' + proto
            mapping['proto']  = 'set' + proto_
            mapping['pv'] = pv + '-SP'
            proto_str += SINT16_W.safe_substitute(default, **mapping)
            proto_str += SELECT_W_INDEX.safe_substitute(default, **mapping)

            mapping['proto_'] = 'get' + proto
            mapping['proto']  = 'get' + proto_
            mapping['pv'] = pv + '-RB'
            proto_str += SINT16_R.safe_substitute(default, **mapping)
            proto_str += SELECT_R_INDEX.safe_substitute(default, **mapping)
            continue

        db_str += loop_analog.safe_substitute(default, **mapping)
        proto  = mapping['proto']

        mapping['proto'] = 'set' + proto
        proto_str += SINT16_W.safe_substitute(default, **mapping)
        mapping['proto'] = 'get' + proto
        proto_str += SINT16_R.safe_substitute(default, **mapping)

    # SINT16 W
    for mapping in SINT16_W_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        mapping['HL'] = 'H' if not mapping.get('MINUS') else 'L'
        db_str += err.safe_substitute(default, **mapping)

        if mapping.get('SELECT'):
            if mapping.get('ref'):
                db_str += ao_ref.safe_substitute(default, **mapping)
            else:
                db_str += ao.safe_substitute(default, **mapping)
            mapping['proto_'] = mapping['proto']
            mapping['proto'] = mapping['proto'] + '_'
            proto_str += SINT16_W.safe_substitute(default, **mapping)
            proto_str += SELECT_W_INDEX.safe_substitute(default, **mapping)
            continue

        db_str += ao_ref.safe_substitute(default, **mapping)
        proto_str += SINT16_W.safe_substitute(default, **mapping)


    # SINT16 R
    for mapping in SINT16_R_mapping:
        mapping['address'] =  getAddr(mapping['addr'])

        db_str += err.safe_substitute(default, **mapping)

        if mapping.get('type') == 'mbbi':
            db_str += mbbi.safe_substitute(default, **mapping)
        elif mapping.get('ref'):
            if type(mapping.get('ref')) == list:
                db_str += ai_ref_2.safe_substitute(default, **mapping, ref0 = mapping['ref'][0], ref1 = mapping['ref'][1])
            else:
                db_str += ai_ref.safe_substitute(default, **mapping)
        else:
            db_str += ai.safe_substitute(default, **mapping)

        if mapping.get('SELECT'):
            mapping['proto_'] = mapping['proto']
            mapping['proto'] = mapping['proto'] + '_'
            proto_str += SINT16_R.safe_substitute(default, **mapping)
            proto_str += SELECT_R_INDEX.safe_substitute(default, **mapping)
        else:
            proto_str += SINT16_R.safe_substitute(default, **mapping)


    # UINT16 W
    for mapping in UINT16_W_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        db_str += err.safe_substitute(default, **mapping)

        if mapping['type'] == 'bo':
            proto_str += UINT16_W.safe_substitute(default, **mapping)
            db_str += bo.safe_substitute(default, **mapping)
        elif mapping['type'] == 'bo_cmd':
            proto_str += UINT16_W_1.safe_substitute(default, **mapping)
            db_str += bo_cmd.safe_substitute(default, **mapping)

    # UINT16 R
    for mapping in UINT16_R_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        db_str += err.safe_substitute(default, **mapping)

        if mapping['type'] == 'ai':
            db_str += ai.safe_substitute(default, **mapping)

            if mapping.get('SELECT'):
                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.safe_substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.safe_substitute(default, **mapping)
            else:
                proto_str += UINT16_R.safe_substitute(default, **mapping)

        elif mapping['type'] == 'longin':
            if mapping.get('SELECT'):
                db_str += longin.safe_substitute(default, **mapping)

                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.safe_substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.safe_substitute(default, **mapping)
            else:
                proto_str += UINT16_R.safe_substitute(default, **mapping)
                db_str += longin.safe_substitute(default, **mapping)

        elif mapping['type'] == 'mbbi':
            if mapping.get('SELECT'):
                db_str += mbbi.safe_substitute(default, **mapping)

                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.safe_substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.safe_substitute(default, **mapping)
            else:
                db_str += mbbi.safe_substitute(default, **mapping)
                proto_str += UINT16_R.safe_substitute(default, **mapping)


if __name__ == '__main__':

    getSINT16_R()

    with open("TopCon.proto", "w+") as output_file:
        output_file.write(proto_str)

    with open("TopCon.db", "w+") as output_file:
        output_file.write(db_str)
