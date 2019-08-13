#!/usr/bin/python3
# -*- coding: utf-8 -*-

from string import Template
from proto_template import SINT16_R, SINT16_W, UINT16_W, UINT16_W_1, UINT16_R, SELECT_SYSTEM, SELECT_MASTER, SELECT_R_INDEX, SELECT_W_INDEX
from db_template import ai, ai_ref, ai_ref_2, ao, ao_ref,bo, bo_cmd, mbbi, err, longin, loop_analog

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
    {'pv':'OutputVoltage-Sel', 'proto':'setOutputVoltageOnOff', 'addr':0x005089, 'DESC':'Voltage On/Off', 'type':'bo',                           'DISA':'$(MASTER=0)'},
    {'pv':'Save-Cmd',          'proto':'saveSettings',          'addr':0x00508A, 'DESC':'Save settings to non-volatile memory', 'type':'bo_cmd', 'DISA':'$(MASTER=0)'},
    {'pv':'Clear-Cmd',         'proto':'clearError',            'addr':0x00508B, 'DESC':'Clear Errors and/or warnings', 'type':'bo_cmd',         'DISA':'$(MASTER=0)'}
]

UINT16_R_mapping = [
    # Warning Monitoring
    {'pv':'Mod:StdWarnGroup-Mon',                 'proto':'getModStdWarnGroup',  'addr':0x00508E, 'DESC':'Standard waring group',            'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:StdWarnInternal-Mon',              'proto':'getModStdWarnGroup0', 'addr':0x00509B, 'DESC':'Std warning group 0',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnInternalPDSP-Mon',          'proto':'getModStdWarnGroup1', 'addr':0x00509C, 'DESC':'Std warning group 1',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnOutputCurrent-Mon',         'proto':'getModStdWarnGroup2', 'addr':0x00509D, 'DESC':'Std warning group 2',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnOutputVoltage-Mon',         'proto':'getModStdWarnGroup3', 'addr':0x00509E, 'DESC':'Std warning group 3',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnSupply-Mon',                'proto':'getModStdWarnGroup4', 'addr':0x00509F, 'DESC':'Std warning group 4',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnTemperature-Mon',           'proto':'getModStdWarnGroup5', 'addr':0x0050A0, 'DESC':'Std warning group 5',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnCommunication-Mon',         'proto':'getModStdWarnGroup6', 'addr':0x0050A1, 'DESC':'Std warning group 6',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnInternalModulator-Mon',     'proto':'getModStdWarnGroup7', 'addr':0x0050B0, 'DESC':'Std warning group 7',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnInternalADoverrange1-Mon',  'proto':'getModStdWarnGroup8', 'addr':0x0050B1, 'DESC':'Std warning group 8',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnInternalADoverrange2-Mon',  'proto':'getModStdWarnGroup9', 'addr':0x0050B2, 'DESC':'Std warning group 9',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnInternalADunderrange1-Mon', 'proto':'getModStdWarnGroupA', 'addr':0x0050B3, 'DESC':'Std warning group A',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnInternalADunderrange2-Mon', 'proto':'getModStdWarnGroupB', 'addr':0x0050B4, 'DESC':'Std warning group B',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnLogin-Mon',                 'proto':'getModStdWarnGroupC', 'addr':0x0050B5, 'DESC':'Std warning group C',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnConfiguration-Mon',         'proto':'getModStdWarnGroupD', 'addr':0x0050B6, 'DESC':'Std warning group D',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnConfiguration2-Mon',        'proto':'getModStdWarnGroupE', 'addr':0x0050B7, 'DESC':'Std warning group E',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdWarnMiscellaneous-Mon',         'proto':'getModStdWarnGroupF', 'addr':0x0050A2, 'DESC':'Std warning group F',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnGroup-Mon',                 'proto':'getModExtWarnGroup',  'addr':0x302A11, 'DESC':'Extended warning group',           'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:ExtWarnIBCSystem-Mon',             'proto':'getModExtWarnGroupG', 'addr':0x302A12, 'DESC':'Ext warning group G',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCSuppply-Mon',            'proto':'getModExtWarnGroupH', 'addr':0x302A13, 'DESC':'Ext warning group H',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCCommunication-Mon',      'proto':'getModExtWarnGroupJ', 'addr':0x302A14, 'DESC':'Ext warning group J',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCPower-Mon',              'proto':'getModExtWarnGroupK', 'addr':0x302A15, 'DESC':'Ext warning group K',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCInverter-Mon',           'proto':'getModExtWarnGroupL', 'addr':0x302A16, 'DESC':'Ext warning group L',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCMiscellaneous-Mon',      'proto':'getModExtWarnGroupM', 'addr':0x302A17, 'DESC':'Ext warning group M',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnIBCInverter2-Mon',          'proto':'getModExtWarnGroupN', 'addr':0x302A18, 'DESC':'Ext warning group N',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnSupply2-Mon',               'proto':'getModExtWarnGroupS', 'addr':0x302A1C, 'DESC':'Ext warning group S',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnLogin2-Mon',                'proto':'getModExtWarnGroupT', 'addr':0x302A1D, 'DESC':'Ext warning group T',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnConfiguration3-Mon',        'proto':'getModExtWarnGroupU', 'addr':0x302A1E, 'DESC':'Ext warning group U',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnCommunication3-Mon',        'proto':'getModExtWarnGroupV', 'addr':0x302A1F, 'DESC':'Ext warning group V',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnInternal2-Mon',             'proto':'getModExtWarnGroupW', 'addr':0x302A20, 'DESC':'Ext warning group W',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtWarnCommunication2-Mon',        'proto':'getModExtWarnGroupX', 'addr':0x302A21, 'DESC':'Ext warning group X',              'type':'longin', 'SELECT':Select.MASTER},

    {'pv':'Sys:StdWarnGroup-Mon',                 'proto':'getSysStdWarnGroup',  'addr':0x00508E, 'DESC':'Standard warning group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:StdWarnInternal-Mon',              'proto':'getSysStdWarnGroup0', 'addr':0x00509B, 'DESC':'Std warning group 0',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnInternalPDSP-Mon',          'proto':'getSysStdWarnGroup1', 'addr':0x00509C, 'DESC':'Std warning group 1',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnOutputCurrent-Mon',         'proto':'getSysStdWarnGroup2', 'addr':0x00509D, 'DESC':'Std warning group 2',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnOutputVoltage-Mon',         'proto':'getSysStdWarnGroup3', 'addr':0x00509E, 'DESC':'Std warning group 3',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnSupply-Mon',                'proto':'getSysStdWarnGroup4', 'addr':0x00509F, 'DESC':'Std warning group 4',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnTemperature-Mon',           'proto':'getSysStdWarnGroup5', 'addr':0x0050A0, 'DESC':'Std warning group 5',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnCommunication-Mon',         'proto':'getSysStdWarnGroup6', 'addr':0x0050A1, 'DESC':'Std warning group 6',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnInternalModulator-Mon',     'proto':'getSysStdWarnGroup7', 'addr':0x0050B0, 'DESC':'Std warning group 7',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnInternalADoverrange1-Mon',  'proto':'getSysStdWarnGroup8', 'addr':0x0050B1, 'DESC':'Std warning group 8',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnInternalADoverrange2-Mon',  'proto':'getSysStdWarnGroup9', 'addr':0x0050B2, 'DESC':'Std warning group 9',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnInternalADunderrange1-Mon', 'proto':'getSysStdWarnGroupA', 'addr':0x0050B3, 'DESC':'Std warning group A',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnInternalADunderrange2-Mon', 'proto':'getSysStdWarnGroupB', 'addr':0x0050B4, 'DESC':'Std warning group B',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnLogin-Mon',                 'proto':'getSysStdWarnGroupC', 'addr':0x0050B5, 'DESC':'Std warning group C',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnConfiguration-Mon',         'proto':'getSysStdWarnGroupD', 'addr':0x0050B6, 'DESC':'Std warning group D',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnConfiguration2-Mon',        'proto':'getSysStdWarnGroupE', 'addr':0x0050B7, 'DESC':'Std warning group E',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdWarnMiscellaneous-Mon',         'proto':'getSysStdWarnGroupF', 'addr':0x0050A2, 'DESC':'Std warning group F',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnGroup-Mon',                 'proto':'getSysExtWarnGroup',  'addr':0x302A11, 'DESC':'Extended warning group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:ExtWarnIBCSystem-Mon',             'proto':'getSysExtWarnGroupG', 'addr':0x302A12, 'DESC':'Ext warning group G',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCSuppply-Mon',            'proto':'getSysExtWarnGroupH', 'addr':0x302A13, 'DESC':'Ext warning group H',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCCommunication-Mon',      'proto':'getSysExtWarnGroupJ', 'addr':0x302A14, 'DESC':'Ext warning group J',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCPower-Mon',              'proto':'getSysExtWarnGroupK', 'addr':0x302A15, 'DESC':'Ext warning group K',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCInverter-Mon',           'proto':'getSysExtWarnGroupL', 'addr':0x302A16, 'DESC':'Ext warning group L',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCMiscellaneous-Mon',      'proto':'getSysExtWarnGroupM', 'addr':0x302A17, 'DESC':'Ext warning group M',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnIBCInverter2-Mon',          'proto':'getSysExtWarnGroupN', 'addr':0x302A18, 'DESC':'Ext warning group N',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnSupply2-Mon',               'proto':'getSysExtWarnGroupS', 'addr':0x302A1C, 'DESC':'Ext warning group S',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnLogin2-Mon',                'proto':'getSysExtWarnGroupT', 'addr':0x302A1D, 'DESC':'Ext warning group T',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnConfiguration3-Mon',        'proto':'getSysExtWarnGroupU', 'addr':0x302A1E, 'DESC':'Ext warning group U',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnCommunication3-Mon',        'proto':'getSysExtWarnGroupV', 'addr':0x302A1F, 'DESC':'Ext warning group V',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnInternal2-Mon',             'proto':'getSysExtWarnGroupW', 'addr':0x302A20, 'DESC':'Ext warning group W',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtWarnCommunication2-Mon',        'proto':'getSysExtWarnGroupX', 'addr':0x302A21, 'DESC':'Ext warning group X',              'type':'longin', 'SELECT':Select.SYSTEM},

    # Error Monitoring
    {'pv':'Mod:StdErrorGroup-Mon',                 'proto':'getModStdErrorGroup',  'addr':0x00508D, 'DESC':'Standard error group',           'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:StdErrorInternal-Mon',              'proto':'getModStdErrorGroup0', 'addr':0x005093, 'DESC':'Std error group 0',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalPDSP-Mon',          'proto':'getModStdErrorGroup1', 'addr':0x005094, 'DESC':'Std error group 1',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorOutputCurrent-Mon',         'proto':'getModStdErrorGroup2', 'addr':0x005095, 'DESC':'Std error group 2',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorOutputVoltage-Mon',         'proto':'getModStdErrorGroup3', 'addr':0x005096, 'DESC':'Std error group 3',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorSupply-Mon',                'proto':'getModStdErrorGroup4', 'addr':0x005097, 'DESC':'Std error group 4',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorTemperature-Mon',           'proto':'getModStdErrorGroup5', 'addr':0x005098, 'DESC':'Std error group 5',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorCommunication-Mon',         'proto':'getModStdErrorGroup6', 'addr':0x005099, 'DESC':'Std error group 6',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalModulator-Mon',     'proto':'getModStdErrorGroup7', 'addr':0x0050A8, 'DESC':'Std error group 7',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADoverrange1-Mon',  'proto':'getModStdErrorGroup8', 'addr':0x0050A9, 'DESC':'Std error group 8',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADoverrange2-Mon',  'proto':'getModStdErrorGroup9', 'addr':0x0050AA, 'DESC':'Std error group 9',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADunderrange1-Mon', 'proto':'getModStdErrorGroupA', 'addr':0x0050AB, 'DESC':'Std error group A',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADunderrange2-Mon', 'proto':'getModStdErrorGroupB', 'addr':0x0050AC, 'DESC':'Std error group B',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorLogin-Mon',                 'proto':'getModStdErrorGroupC', 'addr':0x0050AD, 'DESC':'Std error group C',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorConfiguration-Mon',         'proto':'getModStdErrorGroupD', 'addr':0x0050AE, 'DESC':'Std error group D',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorConfiguration2-Mon',        'proto':'getModStdErrorGroupE', 'addr':0x0050AF, 'DESC':'Std error group E',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorMiscellaneous-Mon',         'proto':'getModStdErrorGroupF', 'addr':0x00509A, 'DESC':'Std error group F',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorGroup-Mon',                 'proto':'getModExtErrorGroup',  'addr':0x302A00, 'DESC':'Extended error group',           'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Mod:ExtErrorIBCSystem-Mon',             'proto':'getModExtErrorGroupG', 'addr':0x302A01, 'DESC':'Ext error group G',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCSuppply-Mon',            'proto':'getModExtErrorGroupH', 'addr':0x302A02, 'DESC':'Ext error group H',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCCommunication-Mon',      'proto':'getModExtErrorGroupJ', 'addr':0x302A03, 'DESC':'Ext error group J',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCPower-Mon',              'proto':'getModExtErrorGroupK', 'addr':0x302A04, 'DESC':'Ext error group K',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCInverter-Mon',           'proto':'getModExtErrorGroupL', 'addr':0x302A05, 'DESC':'Ext error group L',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCMiscellaneous-Mon',      'proto':'getModExtErrorGroupM', 'addr':0x302A06, 'DESC':'Ext error group M',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCInverter2-Mon',          'proto':'getModExtErrorGroupN', 'addr':0x302A07, 'DESC':'Ext error group N',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorSupply2-Mon',               'proto':'getModExtErrorGroupS', 'addr':0x302A0B, 'DESC':'Ext error group S',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorLogin2-Mon',                'proto':'getModExtErrorGroupT', 'addr':0x302A0C, 'DESC':'Ext error group T',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorConfiguration3-Mon',        'proto':'getModExtErrorGroupU', 'addr':0x302A0D, 'DESC':'Ext error group U',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorCommunication3-Mon',        'proto':'getModExtErrorGroupV', 'addr':0x302A0E, 'DESC':'Ext error group V',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorInternal2-Mon',             'proto':'getModExtErrorGroupW', 'addr':0x302A0F, 'DESC':'Ext error group W',              'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorCommunication2-Mon',        'proto':'getModExtErrorGroupX', 'addr':0x302A10, 'DESC':'Ext error group X',              'type':'longin', 'SELECT':Select.MASTER},

    {'pv':'Sys:StdErrorGroup-Mon',                 'proto':'getSysStdErrorGroup',  'addr':0x00508D, 'DESC':'Standard error group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:StdErrorInternal-Mon',              'proto':'getSysStdErrorGroup0', 'addr':0x005093, 'DESC':'Std error group 0',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalPDSP-Mon',          'proto':'getSysStdErrorGroup1', 'addr':0x005094, 'DESC':'Std error group 1',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorOutputCurrent-Mon',         'proto':'getSysStdErrorGroup2', 'addr':0x005095, 'DESC':'Std error group 2',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorOutputVoltage-Mon',         'proto':'getSysStdErrorGroup3', 'addr':0x005096, 'DESC':'Std error group 3',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorSupply-Mon',                'proto':'getSysStdErrorGroup4', 'addr':0x005097, 'DESC':'Std error group 4',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorTemperature-Mon',           'proto':'getSysStdErrorGroup5', 'addr':0x005098, 'DESC':'Std error group 5',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorCommunication-Mon',         'proto':'getSysStdErrorGroup6', 'addr':0x005099, 'DESC':'Std error group 6',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalModulator-Mon',     'proto':'getSysStdErrorGroup7', 'addr':0x0050A8, 'DESC':'Std error group 7',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADoverrange1-Mon',  'proto':'getSysStdErrorGroup8', 'addr':0x0050A9, 'DESC':'Std error group 8',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADoverrange2-Mon',  'proto':'getSysStdErrorGroup9', 'addr':0x0050AA, 'DESC':'Std error group 9',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADunderrange1-Mon', 'proto':'getSysStdErrorGroupA', 'addr':0x0050AB, 'DESC':'Std error group A',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADunderrange2-Mon', 'proto':'getSysStdErrorGroupB', 'addr':0x0050AC, 'DESC':'Std error group B',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorLogin-Mon',                 'proto':'getSysStdErrorGroupC', 'addr':0x0050AD, 'DESC':'Std error group C',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorConfiguration-Mon',         'proto':'getSysStdErrorGroupD', 'addr':0x0050AE, 'DESC':'Std error group D',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorConfiguration2-Mon',        'proto':'getSysStdErrorGroupE', 'addr':0x0050AF, 'DESC':'Std error group E',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorMiscellaneous-Mon',         'proto':'getSysStdErrorGroupF', 'addr':0x00509A, 'DESC':'Std error group F',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorGroup-Mon',                 'proto':'getSysExtErrorGroup',  'addr':0x302A00, 'DESC':'Extended error group',           'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Sys:ExtErrorIBCSystem-Mon',             'proto':'getSysExtErrorGroupG', 'addr':0x302A01, 'DESC':'Ext error group G',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCSuppply-Mon',            'proto':'getSysExtErrorGroupH', 'addr':0x302A02, 'DESC':'Ext error group H',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCCommunication-Mon',      'proto':'getSysExtErrorGroupJ', 'addr':0x302A03, 'DESC':'Ext error group J',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCPower-Mon',              'proto':'getSysExtErrorGroupK', 'addr':0x302A04, 'DESC':'Ext error group K',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCInverter-Mon',           'proto':'getSysExtErrorGroupL', 'addr':0x302A05, 'DESC':'Ext error group L',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCMiscellaneous-Mon',      'proto':'getSysExtErrorGroupM', 'addr':0x302A06, 'DESC':'Ext error group M',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCInverter2-Mon',          'proto':'getSysExtErrorGroupN', 'addr':0x302A07, 'DESC':'Ext error group N',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorSupply2-Mon',               'proto':'getSysExtErrorGroupS', 'addr':0x302A0B, 'DESC':'Ext error group S',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorLogin2-Mon',                'proto':'getSysExtErrorGroupT', 'addr':0x302A0C, 'DESC':'Ext error group T',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorConfiguration3-Mon',        'proto':'getSysExtErrorGroupU', 'addr':0x302A0D, 'DESC':'Ext error group U',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorCommunication3-Mon',        'proto':'getSysExtErrorGroupV', 'addr':0x302A0E, 'DESC':'Ext error group V',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorInternal2-Mon',             'proto':'getSysExtErrorGroupW', 'addr':0x302A0F, 'DESC':'Ext error group W',              'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorCommunication2-Mon',        'proto':'getSysExtErrorGroupX', 'addr':0x302A10, 'DESC':'Ext error group X',              'type':'longin', 'SELECT':Select.SYSTEM},

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
        'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Power', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active',
        'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    {'pv':'Mod:ControlMode-Mon',  'proto':'getModControlMode',   'addr':0x0050B8, 'DESC':'Module control mode', 'type':'mbbi',
        'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Power', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active',
        'SELECT':Select.MASTER, 'SCAN':'10 second'},

]

SINT16_loop_mapping = [

]

SINT16_W_mapping = [
    # ------------- Set Values -------------
    # Voltage preset
    {'pv':'Mod:VoltagePreset-SP', 'proto':'setModVoltagePreset', 'addr':0x005080, 'DESC':'Module voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:VoltagePreset-SP', 'proto':'setSysVoltagePreset', 'addr':0x005080, 'DESC':'System voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Voltage limit Q4
    {'pv':'Mod:VoltageLimitQ4-SP', 'proto':'setModVoltageLimitQ4', 'addr':0x30251F, 'DESC':'Module voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:VoltageLimitQ4-SP', 'proto':'setSysVoltageLimitQ4', 'addr':0x30251F, 'DESC':'System voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Current preset
    {'pv':'Mod:CurrentPreset-SP', 'proto':'setModCurrentPreset', 'addr':0x005081, 'DESC':'Module current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:CurrentPreset-SP', 'proto':'setSysCurrentPreset', 'addr':0x005081, 'DESC':'System current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Current limit Q4
    {'pv':'Mod:CurrentLimitQ4-SP', 'proto':'setModCurrentLimitQ4', 'addr':0x30251D, 'DESC':'Module current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-'},
    {'pv':'Sys:CurrentLimitQ4-SP', 'proto':'setSysCurrentLimitQ4', 'addr':0x30251D, 'DESC':'System current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-'},
    # Power preset
    {'pv':'Mod:PowerPreset-SP', 'proto':'setModPowerPreset', 'addr':0x005082, 'DESC':'Module power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:PowerPreset-SP', 'proto':'setSysPowerPreset', 'addr':0x005082, 'DESC':'System power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Power limit Q4
    {'pv':'Mod:PowerLimitQ4-SP', 'proto':'setModPowerLimitQ4', 'addr':0x30251E, 'DESC':'Module power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-'},
    {'pv':'Sys:PowerLimitQ4-SP', 'proto':'setSysPowerLimitQ4', 'addr':0x30251E, 'DESC':'System power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-'},
    # Resistence Preset
    {'pv':'Mod:ResistencePreset-SP', 'proto':'setModResistencePreset', 'addr':0x005083, 'DESC':'Module resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:ResistencePreset-SP', 'proto':'setSysResistencePreset', 'addr':0x005083, 'DESC':'System resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},


    # ------------- Controller Parameters -------------
    # Slope
    {'pv':'StartupVoltageSlope-SP', 'proto':'setStartupVoltageSlope', 'addr':0x005154, 'DESC':'Startup volt 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'StartupCurrentSlope-SP', 'proto':'setStartupCurrentSlope', 'addr':0x005155, 'DESC':'Startup curr 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'VoltageSlope-SP',        'proto':'setVoltageSlope',        'addr':0x005156, 'DESC':'Voltage slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'CurrentSlope-SP',        'proto':'setCurrentSlope',        'addr':0x005157, 'DESC':'Current slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
]

SINT16_R_mapping = [

    # ------------- Remote Controle Input -------------
    {'pv':'ActiveInterface-Mon',        'proto':'getActiveInterface', 'addr':0x005087, 'DESC':'Active interface', 'type':'mbbi',
        'ZRST': 'Analog/Digital Inputs', 'ONST':'HMI', 'TWST':'RS232', 'THST':'Internal', 'DESC':'Which interface is active', 'FRST':'passiv',
         'FRVL': '32767', 'SCAN':'10 second'},

    # ------------- Controller Parameters -------------
    # Slope
    {'pv':'StartupVoltageSlope-RB', 'proto':'getStartupVoltageSlope', 'addr':0x005154, 'DESC':'Startup volt 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR', 'PINI':'YES'},
    {'pv':'StartupCurrentSlope-RB', 'proto':'getStartupCurrentSlope', 'addr':0x005155, 'DESC':'Startup curr 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR', 'PINI':'YES'},
    {'pv':'VoltageSlope-RB',        'proto':'getSVoltageSlope',       'addr':0x005156, 'DESC':'Voltage slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR', 'PINI':'YES'},
    {'pv':'CurrentSlope-RB',        'proto':'getCurrentSlope',        'addr':0x005157, 'DESC':'Current slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR', 'PINI':'YES'},

    # ------------- Set Values -------------
    # Voltage preset
    {'pv':'Mod:VoltagePreset-RB', 'proto':'getModVoltagePreset', 'addr':0x005080, 'DESC':'Module voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:VoltagePreset-RB', 'proto':'getSysVoltagePreset', 'addr':0x005080, 'DESC':'System voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Voltage limit Q4
    {'pv':'Mod:VoltageLimitQ4-RB', 'proto':'getModVoltageLimitQ4', 'addr':0x30251F, 'DESC':'Module voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:VoltageLimitQ4-RB', 'proto':'getSysVoltageLimitQ4', 'addr':0x30251F, 'DESC':'System voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Current preset
    {'pv':'Mod:CurrentPreset-RB', 'proto':'getModCurrentPreset', 'addr':0x005081, 'DESC':'Module current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:CurrentPreset-RB', 'proto':'getSysCurrentPreset', 'addr':0x005081, 'DESC':'System current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Current limit Q4
    {'pv':'Mod:CurrentLimitQ4-RB', 'proto':'getModCurrentLimitQ4', 'addr':0x30251D, 'DESC':'Module current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-', 'PINI':'YES'},
    {'pv':'Sys:CurrentLimitQ4-RB', 'proto':'getSysCurrentLimitQ4', 'addr':0x30251D, 'DESC':'System current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-', 'PINI':'YES'},
    # Power preset
    {'pv':'Mod:PowerPreset-RB', 'proto':'getModPowerPreset', 'addr':0x005082, 'DESC':'Module power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:PowerPreset-RB', 'proto':'getSysPowerPreset', 'addr':0x005082, 'DESC':'System power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},
    # Power limit Q4
    {'pv':'Mod:PowerLimitQ4-RB', 'proto':'getModPowerLimitQ4', 'addr':0x30251E, 'DESC':'Module power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-', 'PINI':'YES'},
    {'pv':'Sys:PowerLimitQ4-RB', 'proto':'getSysPowerLimitQ4', 'addr':0x30251E, 'DESC':'System power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-', 'PINI':'YES'},
    # Resistence Preset
    {'pv':'Mod:ResistencePreset-RB', 'proto':'getModResistencePreset', 'addr':0x005083, 'DESC':'Module resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'pv':'Sys:ResistencePreset-RB', 'proto':'getSysResistencePreset', 'addr':0x005083, 'DESC':'System resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES'},

    # ------------- Actual Values -------------
    # DC Link
    {'pv':'NomDCLinkVoltage-Mon', 'proto':'getNomDCLinkVoltage',  'addr':0x005105, 'DESC':'DC link nominal voltage',  'EGU':'V', 'PINI':'YES'},
    {'pv':'DCLinkVoltage-Mon',    'proto':'getDCLinkVoltage',     'addr':0x005012, 'DESC':'DC link voltage measure',  'EGU':'V', 'ref':'NomDCLinkVoltage-Mon', 'PHAS':'1', 'SCAN':'10 second'},
    # Output Voltage
    {'pv':'Mod:OutputVoltage-Mon', 'proto':'getModOutputVoltage', 'addr':0x005084, 'DESC':'Module out voltage', 'EGU':'V', 'ref':'Mod:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Sys:OutputVoltage-Mon', 'proto':'getSysOutputVoltage', 'addr':0x005084, 'DESC':'System out voltage', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    # Output Current
    {'pv':'Mod:OutputCurrent-Mon', 'proto':'getModOutputCurrent', 'addr':0x005085, 'DESC':'Module out current', 'EGU':'A', 'ref':['Mod:MaxCurrent-Mon', 'Mod:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Sys:OutputCurrent-Mon', 'proto':'getSysOutputCurrent', 'addr':0x005085, 'DESC':'System out current', 'EGU':'A', 'ref':['Sys:MaxCurrent-Mon', 'Sys:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},
    # Output Power
    {'pv':'Mod:OutputPower-Mon', 'proto':'getModOutputPower', 'addr':0x005086, 'DESC':'Module out power', 'EGU':'kW', 'ref':['Mod:MaxPower-Mon', 'Mod:MinPower-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'pv':'Sys:OutputPower-Mon', 'proto':'getSysOutputPower', 'addr':0x005086, 'DESC':'System out power', 'EGU':'kW', 'ref':['Sys:MaxPower-Mon', 'Sys:MinPower-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'10 second'},

    # ------------- Temperature -------------
    # Device
    {'pv':'IGBTTemp-Mon',      'proto':'getIGBTTemp',     'addr':0x005007, 'DESC':'IGBT temperature',      'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR', 'SCAN':'10 second'},
    {'pv':'RectifierTemp-Mon', 'proto':'getRectfierTemp', 'addr':0x00500F, 'DESC':'Rectifier temperature', 'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR', 'SCAN':'10 second'},

    # ------------- Module Values -------------
    {'pv':'Mod:MaxVoltage-Mon',     'proto':'getModMaxVoltage'     ,'addr':0x005100, 'DESC':'Maximum module voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Mod:MaxCurrent-Mon',     'proto':'getModMaxCurrent'     ,'addr':0x005101, 'DESC':'Maximum module current (Q1)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Mod:MaxPower-Mon',       'proto':'getModMaxPower'       ,'addr':0x005102, 'DESC':'Maximum module power (Q1)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Mod:MinVoltage-Mon',     'proto':'getModMinVoltage'     ,'addr':0x00510F, 'DESC':'Minimum module voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Mod:MinCurrent-Mon',     'proto':'getModMinCurrent'     ,'addr':0x005110, 'DESC':'Minimum module current (Q4)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Mod:MinPower-Mon',       'proto':'getModMinPower'       ,'addr':0x005111, 'DESC':'Minimum module power (Q4)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Mod:NomInternalRes-Mon', 'proto':'getModNomInternalRes' ,'addr':0x005103, 'DESC':'Nom. module internal resistence', 'EGU':'mOhms', 'PINI':'YES'},

    # ------------- System Values -------------
    {'pv':'Sys:MaxVoltage-Mon',     'proto':'getSysMaxVoltage'     ,'addr':0x00510B, 'DESC':'Maximum system voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Sys:MaxCurrent-Mon',     'proto':'getSysMaxCurrent'     ,'addr':0x00510C, 'DESC':'Maximum system current (Q1)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Sys:MaxPower-Mon',       'proto':'getSysMaxPower'       ,'addr':0x00510D, 'DESC':'Maximum system power (Q1)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Sys:MinVoltage-Mon',     'proto':'getSysMinVoltage'     ,'addr':0x005112, 'DESC':'Minimum system voltage',          'EGU':'V', 'PINI':'YES'},
    {'pv':'Sys:MinCurrent-Mon',     'proto':'getSysMinCurrent'     ,'addr':0x005113, 'DESC':'Minimum system current (Q4)',     'EGU':'A', 'PINI':'YES'},
    {'pv':'Sys:MinPower-Mon',       'proto':'getSysMinPower'       ,'addr':0x005114, 'DESC':'Minimum system power (Q4)',       'EGU':'kW', 'PINI':'YES'},
    {'pv':'Sys:NomInternalRes-Mon', 'proto':'getSysNomInternalRes' ,'addr':0x00510E, 'DESC':'Nom. system internal resistence', 'EGU':'mOhms', 'PINI':'YES'}
]

db_str = ''
proto_str = '''
LockTimeout     = 10000;
WriteTimeout    = 100;
ReplyTimeout    = 1000;
ReadTimeout     = 100;
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

    # SINT16 W
    for mapping in SINT16_W_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        mapping['HL'] = 'H' if not mapping.get('MINUS') else 'L'
        db_str += err.substitute(default, **mapping)

        if mapping.get('SELECT'):
            if mapping.get('ref'):
                db_str += ao_ref.substitute(default, **mapping)
            else:
                db_str += ao.substitute(default, **mapping)
            mapping['proto_'] = mapping['proto']
            mapping['proto'] = mapping['proto'] + '_'
            proto_str += SINT16_W.substitute(default, **mapping)
            proto_str += SELECT_W_INDEX.substitute(default, **mapping)
            continue

        db_str += ao.substitute(default, **mapping)
        proto_str += SINT16_W.substitute(default, **mapping)


    # SINT16 R
    for mapping in SINT16_R_mapping:
        mapping['address'] =  getAddr(mapping['addr'])

        db_str += err.substitute(default, **mapping)

        if mapping.get('type') == 'mbbi':
            db_str += mbbi.substitute(default, **mapping)
        elif mapping.get('ref'):
            if type(mapping.get('ref')) == list:
                db_str += ai_ref_2.substitute(default, **mapping, ref0 = mapping['ref'][0], ref1 = mapping['ref'][1])
            else:
                db_str += ai_ref.substitute(default, **mapping)
        else:
            db_str += ai.substitute(default, **mapping)

        if mapping.get('SELECT'):
            mapping['proto_'] = mapping['proto']
            mapping['proto'] = mapping['proto'] + '_'
            proto_str += SINT16_R.substitute(default, **mapping)
            proto_str += SELECT_R_INDEX.substitute(default, **mapping)
        else:
            proto_str += SINT16_R.substitute(default, **mapping)


    # UINT16 W
    for mapping in UINT16_W_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        db_str += err.substitute(default, **mapping)

        if mapping['type'] == 'bo':
            proto_str += UINT16_W.substitute(default, **mapping)
            db_str += bo.substitute(default, **mapping)
        elif mapping['type'] == 'bo_cmd':
            proto_str += UINT16_W_1.substitute(default, **mapping)
            db_str += bo_cmd.substitute(default, **mapping)

    # UINT16 R
    for mapping in UINT16_R_mapping:
        mapping['address'] =  getAddr(mapping['addr'])
        db_str += err.substitute(default, **mapping)

        if mapping['type'] == 'ai':
            db_str += ai.substitute(default, **mapping)

            if mapping.get('SELECT'):
                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.substitute(default, **mapping)
            else:
                proto_str += UINT16_R.substitute(default, **mapping)

        elif mapping['type'] == 'longin':
            if mapping.get('SELECT'):
                db_str += longin.substitute(default, **mapping)

                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.substitute(default, **mapping)
            else:
                proto_str += UINT16_R.substitute(default, **mapping)
                db_str += longin.substitute(default, **mapping)

        elif mapping['type'] == 'mbbi':
            if mapping.get('SELECT'):
                db_str += mbbi.substitute(default, **mapping)

                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.substitute(default, **mapping)
            else:
                db_str += mbbi.substitute(default, **mapping)
                proto_str += UINT16_R.substitute(default, **mapping)


if __name__ == '__main__':

    getSINT16_R()

    with open("TopCon.proto", "w+") as output_file:
        output_file.write(proto_str)

    with open("TopCon.db", "w+") as output_file:
        output_file.write(db_str)
