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
    {'pv':'Module:StdErrorGroup-Mon',                 'proto':'getModuleStdErrorGroup',  'addr':0x00508D, 'desc':'Standard error group', 'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternal-Mon',              'proto':'getModuleStdErrorGroup0', 'addr':0x005093, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternalPDSP-Mon',          'proto':'getModuleStdErrorGroup1', 'addr':0x005094, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorOutputCurrent-Mon',         'proto':'getModuleStdErrorGroup2', 'addr':0x005095, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorOutputVoltage-Mon',         'proto':'getModuleStdErrorGroup3', 'addr':0x005096, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorSupply-Mon',                'proto':'getModuleStdErrorGroup4', 'addr':0x005097, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorTemperature-Mon',           'proto':'getModuleStdErrorGroup5', 'addr':0x005098, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorCommunication-Mon',         'proto':'getModuleStdErrorGroup6', 'addr':0x005099, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternalModulator-Mon',     'proto':'getModuleStdErrorGroup7', 'addr':0x0050A8, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternalADoverrange1-Mon',  'proto':'getModuleStdErrorGroup8', 'addr':0x0050A9, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternalADoverrange2-Mon',  'proto':'getModuleStdErrorGroup9', 'addr':0x0050AA, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternalADunderrange1-Mon', 'proto':'getModuleStdErrorGroupA', 'addr':0x0050AB, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorInternalADunderrange2-Mon', 'proto':'getModuleStdErrorGroupB', 'addr':0x0050AC, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorLogin-Mon',                 'proto':'getModuleStdErrorGroupC', 'addr':0x0050AD, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorConfiguration-Mon',         'proto':'getModuleStdErrorGroupD', 'addr':0x0050AE, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorConfiguration2-Mon',        'proto':'getModuleStdErrorGroupE', 'addr':0x0050AF, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:StdErrorMiscellaneous-Mon',         'proto':'getModuleStdErrorGroupF', 'addr':0x00509A, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorGroup-Mon',                 'proto':'getModuleExtErrorGroupG', 'addr':0x302A00, 'desc':'Extended error group', 'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCSystem-Mon',             'proto':'getModuleExtErrorGroupH', 'addr':0x302A01, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCSuppply-Mon',            'proto':'getModuleExtErrorGroupI', 'addr':0x302A02, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCCommunication-Mon',      'proto':'getModuleExtErrorGroupJ', 'addr':0x302A03, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCPower-Mon',              'proto':'getModuleExtErrorGroupK', 'addr':0x302A04, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCInverter-Mon',           'proto':'getModuleExtErrorGroupL', 'addr':0x302A05, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCMiscellaneous-Mon',      'proto':'getModuleExtErrorGroupM', 'addr':0x302A06, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorIBCInverter2-Mon',          'proto':'getModuleExtErrorGroupN', 'addr':0x302A07, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorSupply2-Mon',               'proto':'getModuleExtErrorGroupS', 'addr':0x302A0B, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorLogin2-Mon',                'proto':'getModuleExtErrorGroupT', 'addr':0x302A0C, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorConfiguration3-Mon',        'proto':'getModuleExtErrorGroupU', 'addr':0x302A0D, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorCommunication3-Mon',        'proto':'getModuleExtErrorGroupV', 'addr':0x302A0E, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorInternal2-Mon',             'proto':'getModuleExtErrorGroupW', 'addr':0x302A0F, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},
    {'pv':'Module:ExtErrorCommunication2-Mon',        'proto':'getModuleExtErrorGroupX', 'addr':0x302A10, 'desc':'',                     'type':'longin', 'SELECT':Select.MASTER},

    {'pv':'System:StdErrorGroup-Mon',                 'proto':'getSystemStdErrorGroup',  'addr':0x00508D, 'desc':'Standard error group', 'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternal-Mon',              'proto':'getSystemStdErrorGroup0', 'addr':0x005093, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternalPDSP-Mon',          'proto':'getSystemStdErrorGroup1', 'addr':0x005094, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorOutputCurrent-Mon',         'proto':'getSystemStdErrorGroup2', 'addr':0x005095, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorOutputVoltage-Mon',         'proto':'getSystemStdErrorGroup3', 'addr':0x005096, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorSupply-Mon',                'proto':'getSystemStdErrorGroup4', 'addr':0x005097, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorTemperature-Mon',           'proto':'getSystemStdErrorGroup5', 'addr':0x005098, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorCommunication-Mon',         'proto':'getSystemStdErrorGroup6', 'addr':0x005099, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternalModulator-Mon',     'proto':'getSystemStdErrorGroup7', 'addr':0x0050A8, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternalADoverrange1-Mon',  'proto':'getSystemStdErrorGroup8', 'addr':0x0050A9, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternalADoverrange2-Mon',  'proto':'getSystemStdErrorGroup9', 'addr':0x0050AA, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternalADunderrange1-Mon', 'proto':'getSystemStdErrorGroupA', 'addr':0x0050AB, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorInternalADunderrange2-Mon', 'proto':'getSystemStdErrorGroupB', 'addr':0x0050AC, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorLogin-Mon',                 'proto':'getSystemStdErrorGroupC', 'addr':0x0050AD, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorConfiguration-Mon',         'proto':'getSystemStdErrorGroupD', 'addr':0x0050AE, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorConfiguration2-Mon',        'proto':'getSystemStdErrorGroupE', 'addr':0x0050AF, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:StdErrorMiscellaneous-Mon',         'proto':'getSystemStdErrorGroupF', 'addr':0x00509A, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorGroup-Mon',                 'proto':'getSystemExtErrorGroup',  'addr':0x302A00, 'desc':'Extended error group', 'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCSystem-Mon',             'proto':'getSystemExtErrorGroupH', 'addr':0x302A01, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCSuppply-Mon',            'proto':'getSystemExtErrorGroupI', 'addr':0x302A02, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCCommunication-Mon',      'proto':'getSystemExtErrorGroupJ', 'addr':0x302A03, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCPower-Mon',              'proto':'getSystemExtErrorGroupK', 'addr':0x302A04, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCInverter-Mon',           'proto':'getSystemExtErrorGroupL', 'addr':0x302A05, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCMiscellaneous-Mon',      'proto':'getSystemExtErrorGroupM', 'addr':0x302A06, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorIBCInverter2-Mon',          'proto':'getSystemExtErrorGroupN', 'addr':0x302A07, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorSupply2-Mon',               'proto':'getSystemExtErrorGroupS', 'addr':0x302A0B, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorLogin2-Mon',                'proto':'getSystemExtErrorGroupT', 'addr':0x302A0C, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorConfiguration3-Mon',        'proto':'getSystemExtErrorGroupU', 'addr':0x302A0D, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorCommunication3-Mon',        'proto':'getSystemExtErrorGroupV', 'addr':0x302A0E, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorInternal2-Mon',             'proto':'getSystemExtErrorGroupW', 'addr':0x302A0F, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},
    {'pv':'System:ExtErrorCommunication2-Mon',        'proto':'getSystemExtErrorGroupX', 'addr':0x302A10, 'desc':'',                     'type':'longin', 'SELECT':Select.SYSTEM},

    # System Control
    {'pv':'FirmwareMain-Mon',     'proto':'getFirmwareMain',     'addr':0x007E01, 'desc':'Main',     'type':'ai'},
    {'pv':'FirmwareVersion-Mon',  'proto':'getFirmwareVersion',  'addr':0x007E02, 'desc':'Version',  'type':'ai'},
    {'pv':'FirmwareRevision-Mon', 'proto':'getFirmwareRevision', 'addr':0x007E03, 'desc':'Revision', 'type':'ai'},

    {'pv':'SerialNumHigh-Mon','proto':'getSerialNumHigh', 'addr':0x005128, 'desc':'Revision', 'type':'ai'},
    {'pv':'SerialNumLow-Mon', 'proto':'getSerialNumLow',  'addr':0x005129, 'desc':'Revision', 'type':'ai'},

    {'pv':'System:State-Mon',        'proto':'getSystemState',         'addr':0x00508C, 'desc':'', 'type':'mbbi',
        'opt':{ 'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP'},
        'SELECT':Select.SYSTEM},
    {'pv':'Module:State-Mon',        'proto':'getModuleState',         'addr':0x00508C, 'desc':'', 'type':'mbbi',
        'opt':{ 'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP'},
        'SELECT':Select.MASTER},

    {'pv':'System:ControlMode-Mon',  'proto':'getSystemControlMode',   'addr':0x0050B8, 'desc':'', 'type':'mbbi',
        'opt':{ 'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Power', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active'},
        'SELECT':Select.SYSTEM},
    {'pv':'Module:ControlMode-Mon',  'proto':'getModuleControlMode',   'addr':0x0050B8, 'desc':'', 'type':'mbbi',
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
    {'pv':'Module:VoltagePreset-RB', 'proto':'getModuleVoltagePreset', 'addr':0x005080, 'desc':'Voltage preset Q1', 'EGU':'V', 'ref':'System:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:VoltagePreset-RB', 'proto':'getSystemVoltagePreset', 'addr':0x005080, 'desc':'Voltage preset Q1', 'EGU':'V', 'ref':'System:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Voltage limit Q4
    {'pv':'Module:VoltageLimitQ4-RB', 'proto':'getModuleVoltageLimitQ4', 'addr':0x30251F, 'desc':'Voltage limit Q4', 'EGU':'V', 'ref':'System:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:VoltageLimitQ4-RB', 'proto':'getSystemVoltageLimitQ4', 'addr':0x30251F, 'desc':'Voltage limit Q4', 'EGU':'V', 'ref':'System:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Current preset
    {'pv':'Module:CurrentPreset-RB', 'proto':'getModuleCurrentPreset', 'addr':0x005081, 'desc':'Current preset Q1', 'EGU':'V', 'ref':'System:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:CurrentPreset-RB', 'proto':'getSystemCurrentPreset', 'addr':0x005081, 'desc':'Current preset Q1', 'EGU':'V', 'ref':'System:MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Current limit Q4
    {'pv':'Module:CurrentLimitQ4-RB', 'proto':'getModuleCurrentLimitQ4', 'addr':0x30251D, 'desc':'Current limit Q4', 'EGU':'A', 'ref':'System:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-'},
    {'pv':'System:CurrentLimitQ4-RB', 'proto':'getSystemCurrentLimitQ4', 'addr':0x30251D, 'desc':'Current limit Q4', 'EGU':'A', 'ref':'System:MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-'},
    # Power preset
    {'pv':'Module:PowerPreset-RB', 'proto':'getModulePowerPreset', 'addr':0x005082, 'desc':'Power preset Q1', 'EGU':'kW', 'ref':'System:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:PowerPreset-RB', 'proto':'getSystemPowerPreset', 'addr':0x005082, 'desc':'Power preset Q1', 'EGU':'kW', 'ref':'System:MaxPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Power limit Q4
    {'pv':'Module:PowerLimitQ4-RB', 'proto':'getModulePowerLimitQ4', 'addr':0x30251E, 'desc':'Power limit Q4', 'EGU':'kW', 'ref':'System:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-'},
    {'pv':'System:PowerLimitQ4-RB', 'proto':'getSystemPowerLimitQ4', 'addr':0x30251E, 'desc':'Power limit Q4', 'EGU':'kW', 'ref':'System:MinPower-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-'},
    # Resistence Preset
    {'pv':'Module:ResistencePreset-RB', 'proto':'getModuleResistencePreset', 'addr':0x005083, 'desc':'Resistence preset', 'EGU':'mOhms', 'ref':'System:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:ResistencePreset-RB', 'proto':'getSystemResistencePreset', 'addr':0x005083, 'desc':'Resistence preset', 'EGU':'mOhms', 'ref':'System:NomInternalRes-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},

    # ------------- Actual Values -------------
    # DC Link
    {'pv':'NomDCLinkVoltage-Mon', 'proto':'getNomDCLinkVoltage',  'addr':0x005105, 'desc':'DC link nominal voltage',  'EGU':'V'},
    {'pv':'DCLinkVoltage-Mon',    'proto':'getDCLinkVoltage',     'addr':0x005012, 'desc':'DC link voltage measure',  'EGU':'V', 'ref':'NomDCLinkVoltage-Mon', 'PHAS':'1'},
    # Output Voltage
    {'pv':'Module:OutputVoltage-Mon', 'proto':'getModuleOutputVoltage', 'addr':0x005084, 'desc':'Out voltage', 'EGU':'V', 'ref':'Module:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:OutputVoltage-Mon', 'proto':'getSystemOutputVoltage', 'addr':0x005084, 'desc':'Out voltage', 'EGU':'V', 'ref':'System:MaxVoltage-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Output Current
    {'pv':'Module:OutputCurrent-Mon', 'proto':'getModuleOutputCurrent', 'addr':0x005085, 'desc':'Out current', 'EGU':'A', 'ref':['Module:MaxCurrent-Mon', 'Module:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:OutputCurrent-Mon', 'proto':'getSystemOutputCurrent', 'addr':0x005085, 'desc':'Out current', 'EGU':'A', 'ref':['System:MaxCurrent-Mon', 'System:MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM},
    # Output Power
    {'pv':'Module:OutputPower-Mon', 'proto':'getModuleOutputPower', 'addr':0x005086, 'desc':'Out power', 'EGU':'kW', 'ref':['Module:MaxPower-Mon', 'Module:MinPower-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER},
    {'pv':'System:OutputPower-Mon', 'proto':'getSystemOutputPower', 'addr':0x005086, 'desc':'Out power', 'EGU':'kW', 'ref':['System:MaxPower-Mon', 'System:MinPower-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM},

    # ------------- Temperature -------------
    # Device
    {'pv':'IGBTTemp-Mon',      'proto':'getIGBTTemp',     'addr':0x005007, 'desc':'IGBT temperature',      'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR'},
    {'pv':'RectifierTemp-Mon', 'proto':'getRectfierTemp', 'addr':0x00500F, 'desc':'Rectifier temperature', 'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR'},

    # ------------- Module Values -------------
    {'pv':'Module:MaxVoltage-Mon',     'proto':'getModuleMaxVoltage'     ,'addr':0x005100, 'desc':'Maximum module voltage',          'EGU':'V'},
    {'pv':'Module:MaxCurrent-Mon',     'proto':'getModuleMaxCurrent'     ,'addr':0x005101, 'desc':'Maximum module current (Q1)',     'EGU':'A'},
    {'pv':'Module:MaxPower-Mon',       'proto':'getModuleMaxPower'       ,'addr':0x005102, 'desc':'Maximum module power (Q1)',       'EGU':'kW'},
    {'pv':'Module:MinVoltage-Mon',     'proto':'getModuleMinVoltage'     ,'addr':0x00510F, 'desc':'Minimum module voltage',          'EGU':'V'},
    {'pv':'Module:MinCurrent-Mon',     'proto':'getModuleMinCurrent'     ,'addr':0x005110, 'desc':'Minimum module current (Q4)',     'EGU':'A'},
    {'pv':'Module:MinPower-Mon',       'proto':'getModuleMinPower'       ,'addr':0x005111, 'desc':'Minimum module power (Q4)',       'EGU':'kW'},
    {'pv':'Module:NomInternalRes-Mon', 'proto':'getModuleNomInternalRes' ,'addr':0x005103, 'desc':'Nom. module internal resistence', 'EGU':'mOhms'},

    # ------------- System Values -------------
    {'pv':'System:MaxVoltage-Mon',     'proto':'getSystemMaxVoltage'     ,'addr':0x00510B, 'desc':'Maximum system voltage',          'EGU':'V'},
    {'pv':'System:MaxCurrent-Mon',     'proto':'getSystemMaxCurrent'     ,'addr':0x00510C, 'desc':'Maximum system current (Q1)',     'EGU':'A'},
    {'pv':'System:MaxPower-Mon',       'proto':'getSystemMaxPower'       ,'addr':0x00510D, 'desc':'Maximum system power (Q1)',       'EGU':'kW'},
    {'pv':'System:MinVoltage-Mon',     'proto':'getSystemMinVoltage'     ,'addr':0x005112, 'desc':'Minimum system voltage',          'EGU':'V'},
    {'pv':'System:MinCurrent-Mon',     'proto':'getSystemMinCurrent'     ,'addr':0x005113, 'desc':'Minimum system current (Q4)',     'EGU':'A'},
    {'pv':'System:MinPower-Mon',       'proto':'getSystemMinPower'       ,'addr':0x005114, 'desc':'Minimum system power (Q4)',       'EGU':'kW'},
    {'pv':'System:NomInternalRes-Mon', 'proto':'getSystemNomInternalRes' ,'addr':0x00510E, 'desc':'Nom. system internal resistence', 'EGU':'mOhms'}
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
