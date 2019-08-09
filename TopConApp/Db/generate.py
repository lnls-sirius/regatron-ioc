#!/usr/bin/python3
# -*- coding: utf-8 -*-

from string import Template
from proto_template import SINT16_R, SINT16_W, UINT16_W, UINT16_W_1, UINT16_R, SELECT_SYSTEM, SELECT_MASTER, SELECT_R_INDEX, SELECT_W_INDEX
from db_template import ai, ai_ref, ai_ref_2, ao, bo, bo_cmd, mbbi, err, longin

class Select():
    MASTER = 'selectMaster'
    SYSTEM = 'selectSystem'

default = {
    'ZRST':'', 'ONST':'', 'TWST':'', 'THST':'', 'FRST':'', 'FVST':'', 'SXST':'', 'SVST':'', 'EIST':'', 'NIST':'', 'TEST':'', 'ELST':'', 'TVST':'', 'TTST':'', 'FTST':'', 'FFST':'',
    'ZRSV':'', 'ONSV':'', 'TWSV':'', 'THSV':'', 'FRSV':'', 'FVSV':'', 'SXSV':'', 'SVSV':'', 'EISV':'', 'NISV':'', 'TESV':'', 'ELSV':'', 'TVSV':'', 'TTSV':'', 'FTSV':'', 'FFSV':'',
    'SELECT':'', "PHAS":"0", 'EOFF':'0', 'ESLO':'1', 'DRVH':'0', 'DRVL':'0', 'LINR':'NO CONVERSION', 'MINUS':'', 'DISV':'0', 'DISA':'1', 'EGU':''
}

UINT16_W_mapping = [
    # System Control
    {'pv':'OutputVoltage-Sel', 'proto':'setOutputVoltageOnOff', 'addr':0x005089, 'desc':'Voltage On/Off', 'type':'bo',                           'DISA':'$(MASTER=0)'},
    {'pv':'Save-Cmd',          'proto':'saveSettings',          'addr':0x00508A, 'desc':'Save settings to non-volatile memory', 'type':'bo_cmd', 'DISA':'$(MASTER=0)'},
    {'pv':'Clear-Cmd',         'proto':'clearError',            'addr':0x00508B, 'desc':'Clear Errors and/or warnings', 'type':'bo_cmd',         'DISA':'$(MASTER=0)'}
]

UINT16_R_mapping = [
    # Error Monitoring
    {'pv':'Mod:StdErrorGroup-Mon',                 'proto':'getModStdErrorGroup',  'addr':0x00508D, 'desc':'Standard error group', 'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternal-Mon',              'proto':'getModStdErrorGroup0', 'addr':0x005093, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalPDSP-Mon',          'proto':'getModStdErrorGroup1', 'addr':0x005094, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorOutputCurrent-Mon',         'proto':'getModStdErrorGroup2', 'addr':0x005095, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorOutputVoltage-Mon',         'proto':'getModStdErrorGroup3', 'addr':0x005096, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorSupply-Mon',                'proto':'getModStdErrorGroup4', 'addr':0x005097, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorTemperature-Mon',           'proto':'getModStdErrorGroup5', 'addr':0x005098, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorCommunication-Mon',         'proto':'getModStdErrorGroup6', 'addr':0x005099, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalModulator-Mon',     'proto':'getModStdErrorGroup7', 'addr':0x0050A8, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADoverrange1-Mon',  'proto':'getModStdErrorGroup8', 'addr':0x0050A9, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADoverrange2-Mon',  'proto':'getModStdErrorGroup9', 'addr':0x0050AA, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADunderrange1-Mon', 'proto':'getModStdErrorGroupA', 'addr':0x0050AB, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorInternalADunderrange2-Mon', 'proto':'getModStdErrorGroupB', 'addr':0x0050AC, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorLogin-Mon',                 'proto':'getModStdErrorGroupC', 'addr':0x0050AD, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorConfiguration-Mon',         'proto':'getModStdErrorGroupD', 'addr':0x0050AE, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorConfiguration2-Mon',        'proto':'getModStdErrorGroupE', 'addr':0x0050AF, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:StdErrorMiscellaneous-Mon',         'proto':'getModStdErrorGroupF', 'addr':0x00509A, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorGroup-Mon',                 'proto':'getModExtErrorGroupG', 'addr':0x302A00, 'desc':'Extended error group', 'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCSystem-Mon',             'proto':'getModExtErrorGroupH', 'addr':0x302A01, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCSuppply-Mon',            'proto':'getModExtErrorGroupI', 'addr':0x302A02, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCCommunication-Mon',      'proto':'getModExtErrorGroupJ', 'addr':0x302A03, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCPower-Mon',              'proto':'getModExtErrorGroupK', 'addr':0x302A04, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCInverter-Mon',           'proto':'getModExtErrorGroupL', 'addr':0x302A05, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCMiscellaneous-Mon',      'proto':'getModExtErrorGroupM', 'addr':0x302A06, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorIBCInverter2-Mon',          'proto':'getModExtErrorGroupN', 'addr':0x302A07, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorSupply2-Mon',               'proto':'getModExtErrorGroupS', 'addr':0x302A0B, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorLogin2-Mon',                'proto':'getModExtErrorGroupT', 'addr':0x302A0C, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorConfiguration3-Mon',        'proto':'getModExtErrorGroupU', 'addr':0x302A0D, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorCommunication3-Mon',        'proto':'getModExtErrorGroupV', 'addr':0x302A0E, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorInternal2-Mon',             'proto':'getModExtErrorGroupW', 'addr':0x302A0F, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Mod:ExtErrorCommunication2-Mon',        'proto':'getModExtErrorGroupX', 'addr':0x302A10, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},

    {'pv':'Sys:StdErrorGroup-Mon',                 'proto':'getSysStdErrorGroup',  'addr':0x00508D, 'desc':'Standard error group', 'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternal-Mon',              'proto':'getSysStdErrorGroup0', 'addr':0x005093, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalPDSP-Mon',          'proto':'getSysStdErrorGroup1', 'addr':0x005094, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorOutputCurrent-Mon',         'proto':'getSysStdErrorGroup2', 'addr':0x005095, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorOutputVoltage-Mon',         'proto':'getSysStdErrorGroup3', 'addr':0x005096, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorSupply-Mon',                'proto':'getSysStdErrorGroup4', 'addr':0x005097, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorTemperature-Mon',           'proto':'getSysStdErrorGroup5', 'addr':0x005098, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorCommunication-Mon',         'proto':'getSysStdErrorGroup6', 'addr':0x005099, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalModulator-Mon',     'proto':'getSysStdErrorGroup7', 'addr':0x0050A8, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADoverrange1-Mon',  'proto':'getSysStdErrorGroup8', 'addr':0x0050A9, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADoverrange2-Mon',  'proto':'getSysStdErrorGroup9', 'addr':0x0050AA, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADunderrange1-Mon', 'proto':'getSysStdErrorGroupA', 'addr':0x0050AB, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorInternalADunderrange2-Mon', 'proto':'getSysStdErrorGroupB', 'addr':0x0050AC, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorLogin-Mon',                 'proto':'getSysStdErrorGroupC', 'addr':0x0050AD, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorConfiguration-Mon',         'proto':'getSysStdErrorGroupD', 'addr':0x0050AE, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorConfiguration2-Mon',        'proto':'getSysStdErrorGroupE', 'addr':0x0050AF, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:StdErrorMiscellaneous-Mon',         'proto':'getSysStdErrorGroupF', 'addr':0x00509A, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorGroup-Mon',                 'proto':'getSysExtErrorGroup',  'addr':0x302A00, 'desc':'Extended error group', 'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCSystem-Mon',             'proto':'getSysExtErrorGroupH', 'addr':0x302A01, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCSuppply-Mon',            'proto':'getSysExtErrorGroupI', 'addr':0x302A02, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCCommunication-Mon',      'proto':'getSysExtErrorGroupJ', 'addr':0x302A03, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCPower-Mon',              'proto':'getSysExtErrorGroupK', 'addr':0x302A04, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCInverter-Mon',           'proto':'getSysExtErrorGroupL', 'addr':0x302A05, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCMiscellaneous-Mon',      'proto':'getSysExtErrorGroupM', 'addr':0x302A06, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorIBCInverter2-Mon',          'proto':'getSysExtErrorGroupN', 'addr':0x302A07, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorSupply2-Mon',               'proto':'getSysExtErrorGroupS', 'addr':0x302A0B, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorLogin2-Mon',                'proto':'getSysExtErrorGroupT', 'addr':0x302A0C, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorConfiguration3-Mon',        'proto':'getSysExtErrorGroupU', 'addr':0x302A0D, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorCommunication3-Mon',        'proto':'getSysExtErrorGroupV', 'addr':0x302A0E, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorInternal2-Mon',             'proto':'getSysExtErrorGroupW', 'addr':0x302A0F, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'Sys:ExtErrorCommunication2-Mon',        'proto':'getSysExtErrorGroupX', 'addr':0x302A10, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},

    # System Control
    {'pv':'FirmwareMain-Mon',     'proto':'getFirmwareMain',     'addr':0x007E01, 'desc':'Main',     'type':'ai'},
    {'pv':'FirmwareVersion-Mon',  'proto':'getFirmwareVersion',  'addr':0x007E02, 'desc':'Version',  'type':'ai'},
    {'pv':'FirmwareRevision-Mon', 'proto':'getFirmwareRevision', 'addr':0x007E03, 'desc':'Revision', 'type':'ai'},

    {'pv':'SerialNumHigh-Mon','proto':'getSerialNumHigh', 'addr':0x005128, 'desc':'Revision', 'type':'ai'},
    {'pv':'SerialNumLow-Mon', 'proto':'getSerialNumLow',  'addr':0x005129, 'desc':'Revision', 'type':'ai'},

    {'pv':'Sys:State-Mon',        'proto':'getSysState',         'addr':0x00508C, 'desc':'', 'type':'mbbi',
        'opt':{ 'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP'},
        'SELECT':Select.SYSTEM},
    {'pv':'Mod:State-Mon',        'proto':'getModState',         'addr':0x00508C, 'desc':'', 'type':'mbbi',
        'opt':{ 'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP'},
        'SELECT':Select.MASTER},

    {'pv':'Sys:ControlMode-Mon',  'proto':'getSysControlMode',   'addr':0x0050B8, 'desc':'', 'type':'mbbi',
        'opt':{ 'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Power', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active'},
        'SELECT':Select.SYSTEM},
    {'pv':'Mod:ControlMode-Mon',  'proto':'getModControlMode',   'addr':0x0050B8, 'desc':'', 'type':'mbbi',
        'opt':{ 'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Power', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active'},
        'SELECT':Select.MASTER},

]

SINT16_W_mapping = [
    # Slope
    {'pv':'StartupVoltageSlope-SP', 'proto':'setStartupVoltageSlope', 'addr':0x005154, 'desc':'Startup volt 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'StartupCurrentSlope-SP', 'proto':'setStartupCurrentSlope', 'addr':0x005155, 'desc':'Startup curr 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'VoltageSlope-SP',        'proto':'setVoltageSlope',        'addr':0x005156, 'desc':'Voltage slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
    {'pv':'CurrentSlope-SP',        'proto':'setCurrentSlope',        'addr':0x005157, 'desc':'Current slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'DISA':'$(MASTER=0)'},
]

SINT16_R_mapping = [

    # ------------- Remote Controle Input -------------
    {'pv':'ActiveInterface-Mon',        'proto':'getActiveInterface', 'addr':0x005087, 'desc':'Active interface', 'type':'mbbi',
       'ZRST': 'Analog/Digital Inputs', 'ONST':'HMI', 'TWST':'RS232', 'THST':'Internal', 'FRST':'passiv',
         'FRVL': '32767'},

    # ------------- Controller Parameters -------------
    # Slope
    {'pv':'StartupVoltageSlope-RB', 'proto':'getStartupVoltageSlope', 'addr':0x005154, 'desc':'Startup volt 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR'},
    {'pv':'StartupCurrentSlope-RB', 'proto':'getStartupCurrentSlope', 'addr':0x005155, 'desc':'Startup curr 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR'},
    {'pv':'VoltageSlope-RB',        'proto':'getSVoltageSlope',       'addr':0x005156, 'desc':'voltage slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR'},
    {'pv':'CurrentSlope-RB',        'proto':'getCurrentSlope',        'addr':0x005157, 'desc':'current slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'LINR':'LINEAR'},

    # ------------- Set Values -------------
    # Voltage preset
    {'pv':'Mod:VoltagePreset-RB', 'proto':'getModVoltagePreset', 'addr':0x005080, 'desc':'Voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:VoltagePreset-RB', 'proto':'getSysVoltagePreset', 'addr':0x005080, 'desc':'Voltage preset Q1', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Voltage limit Q4
    {'pv':'Mod:VoltageLimitQ4-RB', 'proto':'getModVoltageLimitQ4', 'addr':0x30251F, 'desc':'Voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:VoltageLimitQ4-RB', 'proto':'getSysVoltageLimitQ4', 'addr':0x30251F, 'desc':'Voltage limit Q4', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Current preset
    {'pv':'Mod:CurrentPreset-RB', 'proto':'getModCurrentPreset', 'addr':0x005081, 'desc':'Current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:CurrentPreset-RB', 'proto':'getSysCurrentPreset', 'addr':0x005081, 'desc':'Current preset Q1', 'EGU':'V', 'ref':'Sys:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Current limit Q4
    {'pv':'Mod:CurrentLimitQ4-RB', 'proto':'getModCurrentLimitQ4', 'addr':0x30251D, 'desc':'Current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-'},
    {'pv':'Sys:CurrentLimitQ4-RB', 'proto':'getSysCurrentLimitQ4', 'addr':0x30251D, 'desc':'Current limit Q4', 'EGU':'A', 'ref':'Sys:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-'},
    # Power preset
    {'pv':'Mod:PowerPreset-RB', 'proto':'getModPowerPreset', 'addr':0x005082, 'desc':'Power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:PowerPreset-RB', 'proto':'getSysPowerPreset', 'addr':0x005082, 'desc':'Power preset Q1', 'EGU':'kW', 'ref':'Sys:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Power limit Q4
    {'pv':'Mod:PowerLimitQ4-RB', 'proto':'getModPowerLimitQ4', 'addr':0x30251E, 'desc':'Power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-'},
    {'pv':'Sys:PowerLimitQ4-RB', 'proto':'getSysPowerLimitQ4', 'addr':0x30251E, 'desc':'Power limit Q4', 'EGU':'kW', 'ref':'Sys:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-'},
    # Resistence Preset
    {'pv':'Mod:ResistencePreset-RB', 'proto':'getModResistencePreset', 'addr':0x005083, 'desc':'Resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:ResistencePreset-RB', 'proto':'getSysResistencePreset', 'addr':0x005083, 'desc':'Resistence preset', 'EGU':'mOhms', 'ref':'Sys:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},

    # ------------- Actual Values -------------
    # DC Link
    {'pv':'NomDCLinkVoltage-Mon', 'proto':'getNomDCLinkVoltage',  'addr':0x005105, 'desc':'DC link nominal voltage',  'EGU':'V'},
    {'pv':'DCLinkVoltage-Mon',    'proto':'getDCLinkVoltage',     'addr':0x005012, 'desc':'DC link voltage measure',  'EGU':'V', 'ref':'NomDCLinkVoltage-Mon', 'PHAS':'1'},
    # Output Voltage
    {'pv':'Mod:OutputVoltage-Mon', 'proto':'getModOutputVoltage', 'addr':0x005084, 'desc':'Out voltage', 'EGU':'V', 'ref':'Mod:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:OutputVoltage-Mon', 'proto':'getSysOutputVoltage', 'addr':0x005084, 'desc':'Out voltage', 'EGU':'V', 'ref':'Sys:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Output Current
    {'pv':'Mod:OutputCurrent-Mon', 'proto':'getModOutputCurrent', 'addr':0x005085, 'desc':'Out current', 'EGU':'A', 'ref':['Mod:MaxCurrent-Mon', 'Mod:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:OutputCurrent-Mon', 'proto':'getSysOutputCurrent', 'addr':0x005085, 'desc':'Out current', 'EGU':'A', 'ref':['Sys:MaxCurrent-Mon', 'Sys:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Output Power
    {'pv':'Mod:OutputPower-Mon', 'proto':'getModOutputPower', 'addr':0x005086, 'desc':'Out power', 'EGU':'kW', 'ref':['Mod:MaxPower-Mon', 'Mod:MinPower-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'Sys:OutputPower-Mon', 'proto':'getSysOutputPower', 'addr':0x005086, 'desc':'Out power', 'EGU':'kW', 'ref':['Sys:MaxPower-Mon', 'Sys:MinPower-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM},

    # ------------- Temperature -------------
    # Device
    {'pv':'IGBTTemp-Mon',      'proto':'getIGBTTemp',     'addr':0x005007, 'desc':'IGBT temperature',      'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR'},
    {'pv':'RectifierTemp-Mon', 'proto':'getRectfierTemp', 'addr':0x00500F, 'desc':'Rectifier temperature', 'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR'},

    # ------------- Module Values -------------
    {'pv':'Mod:MaxVoltage-Mon',     'proto':'getModMaxVoltage'     ,'addr':0x005100, 'desc':'Maximum module voltage',          'EGU':'V'},
    {'pv':'Mod:MaxCurrent-Mon',     'proto':'getModMaxCurrent'     ,'addr':0x005101, 'desc':'Maximum module current (Q1)',     'EGU':'A'},
    {'pv':'Mod:MaxPower-Mon',       'proto':'getModMaxPower'       ,'addr':0x005102, 'desc':'Maximum module power (Q1)',       'EGU':'kW'},
    {'pv':'Mod:MinVoltage-Mon',     'proto':'getModMinVoltage'     ,'addr':0x00510F, 'desc':'Minimum module voltage',          'EGU':'V'},
    {'pv':'Mod:MinCurrent-Mon',     'proto':'getModMinCurrent'     ,'addr':0x005110, 'desc':'Minimum module current (Q4)',     'EGU':'A'},
    {'pv':'Mod:MinPower-Mon',       'proto':'getModMinPower'       ,'addr':0x005111, 'desc':'Minimum module power (Q4)',       'EGU':'kW'},
    {'pv':'Mod:NomInternalRes-Mon', 'proto':'getModNomInternalRes' ,'addr':0x005103, 'desc':'Nom. module internal resistence', 'EGU':'mOhms'},

    # ------------- System Values -------------
    {'pv':'Sys:MaxVoltage-Mon',     'proto':'getSysMaxVoltage'     ,'addr':0x00510B, 'desc':'Maximum system voltage',          'EGU':'V'},
    {'pv':'Sys:MaxCurrent-Mon',     'proto':'getSysMaxCurrent'     ,'addr':0x00510C, 'desc':'Maximum system current (Q1)',     'EGU':'A'},
    {'pv':'Sys:MaxPower-Mon',       'proto':'getSysMaxPower'       ,'addr':0x00510D, 'desc':'Maximum system power (Q1)',       'EGU':'kW'},
    {'pv':'Sys:MinVoltage-Mon',     'proto':'getSysMinVoltage'     ,'addr':0x005112, 'desc':'Minimum system voltage',          'EGU':'V'},
    {'pv':'Sys:MinCurrent-Mon',     'proto':'getSysMinCurrent'     ,'addr':0x005113, 'desc':'Minimum system current (Q4)',     'EGU':'A'},
    {'pv':'Sys:MinPower-Mon',       'proto':'getSysMinPower'       ,'addr':0x005114, 'desc':'Minimum system power (Q4)',       'EGU':'kW'},
    {'pv':'Sys:NomInternalRes-Mon', 'proto':'getSysNomInternalRes' ,'addr':0x00510E, 'desc':'Nom. system internal resistence', 'EGU':'mOhms'}
]

db_str = ''
proto_str = '''
LockTimeout     = 5000;
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
        db_str += err.substitute(default, **mapping)
        db_str += ao.substitute(default, **mapping)

        if mapping.get('SELECT'):
            mapping['proto_'] = mapping['proto']
            mapping['proto'] = mapping['proto'] + '_'
            proto_str += SINT16_W.substitute(default, **mapping)
            proto_str += SELECT_W_INDEX.substitute(default, **mapping)
        else:
            proto_str += SINT16_W.substitute(default, **mapping)


    # SINT16 R
    for mapping in SINT16_R_mapping:
        mapping['address'] =  getAddr(mapping['addr'])

        db_str    += err.substitute(default, **mapping)

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
                db_str += mbbi.substitute(default, **mapping['opt'],**mapping)

                mapping['proto_'] = mapping['proto']
                mapping['proto'] = mapping['proto'] + '_'

                proto_str += UINT16_R.substitute(default, **mapping)
                proto_str += SELECT_R_INDEX.substitute(default, **mapping)
            else:
                db_str += mbbi.substitute(default, **mapping['opt'],**mapping)
                proto_str += UINT16_R.substitute(default, **mapping)


if __name__ == '__main__':

    getSINT16_R()

    with open("TopCon.proto", "w+") as output_file:
        output_file.write(proto_str)

    with open("TopCon.db", "w+") as output_file:
        output_file.write(db_str)
