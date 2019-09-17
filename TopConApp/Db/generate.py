#!/usr/bin/python3
# -*- coding: utf-8 -*-

from string import Template
from proto_template import SINT16_R, SINT16_W, UINT16_W, UINT16_W_1, UINT16_R, SELECT, SELECT_R_INDEX, SELECT_W_INDEX
from db_template import ai, ai_ref, ai_ref_2, ao, ao_ref,bo, bo_cmd, mbbi, err, longin, loop_analog, loop_analog_ref, select, ai_ref_sel, ai_sel

class Select():
    MASTER = 'selectMaster'
    SYSTEM = 'selectSystem'

class Restrict():
    ANY = 0
    MASTER = 1

default = {
    'ZRST':'', 'ONST':'', 'TWST':'', 'THST':'', 'FRST':'', 'FVST':'', 'SXST':'', 'SVST':'', 'EIST':'', 'NIST':'', 'TEST':'', 'ELST':'', 'TVST':'', 'TTST':'', 'FTST':'', 'FFST':'',
    'ZRSV':'', 'ONSV':'', 'TWSV':'', 'THSV':'', 'FRSV':'', 'FVSV':'', 'SXSV':'', 'SVSV':'', 'EISV':'', 'NISV':'', 'TESV':'', 'ELSV':'', 'TVSV':'', 'TTSV':'', 'FTSV':'', 'FFSV':'',
    'SELECT':'', 'PHAS':'0', 'EOFF':'0', 'ESLO':'1', 'DRVH':'0', 'DRVL':'0', 'LINR':'NO CONVERSION', 'MINUS':'', 'DISV':'0', 'DISA':'1', 'EGU':'', 'PREC':'2',
    'SCAN':'Passive', 'PINI':'NO', 'RESTRICT':Restrict.ANY
}

MAPPING = [
    # System Control
    {'r':'uint16_w', 'pv':'OutVolt-Sel', 'proto':'setOutVoltOnOff', 'addr':0x005089, 'DESC':'Volt On/Off', 'type':'bo',                              'RESTRICT':Restrict.MASTER},
    {'r':'uint16_w', 'pv':'Save-Cmd',    'proto':'saveSettings',    'addr':0x00508A, 'DESC':'Save settings to non-volatile memory', 'type':'bo_cmd', 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_w', 'pv':'Clear-Cmd',   'proto':'clearErr',        'addr':0x00508B, 'DESC':'Clear Errors and/or warnings', 'type':'bo_cmd',         'RESTRICT':Restrict.MASTER},

    # Warning Monitoring
    {'r':'uint16_r', 'pv':'Mod-StdWarnGroup-Mon',          'proto':'getModStdWarnGroup',  'addr':0x00508E, 'DESC':'Standard waring group',  'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Mod-StdWarnIntrn-Mon',          'proto':'getModStdWarnGroup0', 'addr':0x00509B, 'DESC':'Std warning group 0',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnIntrnPDSP-Mon',      'proto':'getModStdWarnGroup1', 'addr':0x00509C, 'DESC':'Std warning group 1',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnOutCurrent-Mon',     'proto':'getModStdWarnGroup2', 'addr':0x00509D, 'DESC':'Std warning group 2',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnOutVolt-Mon',        'proto':'getModStdWarnGroup3', 'addr':0x00509E, 'DESC':'Std warning group 3',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnSupply-Mon',         'proto':'getModStdWarnGroup4', 'addr':0x00509F, 'DESC':'Std warning group 4',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnT-Mon',              'proto':'getModStdWarnGroup5', 'addr':0x0050A0, 'DESC':'Std warning group 5',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnComm-Mon',           'proto':'getModStdWarnGroup6', 'addr':0x0050A1, 'DESC':'Std warning group 6',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnIntrnMod-Mon',       'proto':'getModStdWarnGroup7', 'addr':0x0050B0, 'DESC':'Std warning group 7',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnAD1Ovr-Mon', 'proto':'getModStdWarnGroup8', 'addr':0x0050B1, 'DESC':'Std warning group 8',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnAD2Ovr-Mon', 'proto':'getModStdWarnGroup9', 'addr':0x0050B2, 'DESC':'Std warning group 9',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnAD1Undr-Mon','proto':'getModStdWarnGroupA', 'addr':0x0050B3, 'DESC':'Std warning group A',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnAD2Undr-Mon','proto':'getModStdWarnGroupB', 'addr':0x0050B4, 'DESC':'Std warning group B',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnLogin-Mon',          'proto':'getModStdWarnGroupC', 'addr':0x0050B5, 'DESC':'Std warning group C',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnConf-Mon',           'proto':'getModStdWarnGroupD', 'addr':0x0050B6, 'DESC':'Std warning group D',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnConf2-Mon',          'proto':'getModStdWarnGroupE', 'addr':0x0050B7, 'DESC':'Std warning group E',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdWarnMisc-Mon',           'proto':'getModStdWarnGroupF', 'addr':0x0050A2, 'DESC':'Std warning group F',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnGroup-Mon',          'proto':'getModExtWarnGroup',  'addr':0x302A11, 'DESC':'Extended warning group', 'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCSystem-Mon',      'proto':'getModExtWarnGroupG', 'addr':0x302A12, 'DESC':'Ext warning group G',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCSuppply-Mon',     'proto':'getModExtWarnGroupH', 'addr':0x302A13, 'DESC':'Ext warning group H',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCComm-Mon',        'proto':'getModExtWarnGroupJ', 'addr':0x302A14, 'DESC':'Ext warning group J',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCPwr-Mon',         'proto':'getModExtWarnGroupK', 'addr':0x302A15, 'DESC':'Ext warning group K',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCInverter-Mon',    'proto':'getModExtWarnGroupL', 'addr':0x302A16, 'DESC':'Ext warning group L',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCMisc-Mon',        'proto':'getModExtWarnGroupM', 'addr':0x302A17, 'DESC':'Ext warning group M',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIBCInverter2-Mon',   'proto':'getModExtWarnGroupN', 'addr':0x302A18, 'DESC':'Ext warning group N',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnSupply2-Mon',        'proto':'getModExtWarnGroupS', 'addr':0x302A1C, 'DESC':'Ext warning group S',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnLogin2-Mon',         'proto':'getModExtWarnGroupT', 'addr':0x302A1D, 'DESC':'Ext warning group T',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnConf3-Mon',          'proto':'getModExtWarnGroupU', 'addr':0x302A1E, 'DESC':'Ext warning group U',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnComm3-Mon',          'proto':'getModExtWarnGroupV', 'addr':0x302A1F, 'DESC':'Ext warning group V',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnIntrn2-Mon',         'proto':'getModExtWarnGroupW', 'addr':0x302A20, 'DESC':'Ext warning group W',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtWarnComm2-Mon',          'proto':'getModExtWarnGroupX', 'addr':0x302A21, 'DESC':'Ext warning group X',    'PINI':'NO', 'type':'longin', 'SELECT':Select.MASTER},

    {'r':'uint16_r', 'pv':'Sys-StdWarnGroup-Mon',          'proto':'getSysStdWarnGroup',  'addr':0x00508E, 'DESC':'Standard warning group', 'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'SCAN':'10 second', 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnIntrn-Mon',          'proto':'getSysStdWarnGroup0', 'addr':0x00509B, 'DESC':'Std warning group 0',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnIntrnPDSP-Mon',      'proto':'getSysStdWarnGroup1', 'addr':0x00509C, 'DESC':'Std warning group 1',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnOutCurrent-Mon',     'proto':'getSysStdWarnGroup2', 'addr':0x00509D, 'DESC':'Std warning group 2',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnOutVolt-Mon',        'proto':'getSysStdWarnGroup3', 'addr':0x00509E, 'DESC':'Std warning group 3',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnSupply-Mon',         'proto':'getSysStdWarnGroup4', 'addr':0x00509F, 'DESC':'Std warning group 4',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnT-Mon',              'proto':'getSysStdWarnGroup5', 'addr':0x0050A0, 'DESC':'Std warning group 5',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnComm-Mon',           'proto':'getSysStdWarnGroup6', 'addr':0x0050A1, 'DESC':'Std warning group 6',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnIntrnMod-Mon',       'proto':'getSysStdWarnGroup7', 'addr':0x0050B0, 'DESC':'Std warning group 7',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnAD1Ovr-Mon', 'proto':'getSysStdWarnGroup8', 'addr':0x0050B1, 'DESC':'Std warning group 8',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnAD2Ovr-Mon', 'proto':'getSysStdWarnGroup9', 'addr':0x0050B2, 'DESC':'Std warning group 9',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnAD1Undr-Mon','proto':'getSysStdWarnGroupA', 'addr':0x0050B3, 'DESC':'Std warning group A',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnAD2Undr-Mon','proto':'getSysStdWarnGroupB', 'addr':0x0050B4, 'DESC':'Std warning group B',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnLogin-Mon',          'proto':'getSysStdWarnGroupC', 'addr':0x0050B5, 'DESC':'Std warning group C',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnConf-Mon',           'proto':'getSysStdWarnGroupD', 'addr':0x0050B6, 'DESC':'Std warning group D',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnConf2-Mon',          'proto':'getSysStdWarnGroupE', 'addr':0x0050B7, 'DESC':'Std warning group E',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdWarnMisc-Mon',           'proto':'getSysStdWarnGroupF', 'addr':0x0050A2, 'DESC':'Std warning group F',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnGroup-Mon',          'proto':'getSysExtWarnGroup',  'addr':0x302A11, 'DESC':'Extended warning group', 'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCSystem-Mon',      'proto':'getSysExtWarnGroupG', 'addr':0x302A12, 'DESC':'Ext warning group G',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCSuppply-Mon',     'proto':'getSysExtWarnGroupH', 'addr':0x302A13, 'DESC':'Ext warning group H',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCComm-Mon',        'proto':'getSysExtWarnGroupJ', 'addr':0x302A14, 'DESC':'Ext warning group J',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCPwr-Mon',         'proto':'getSysExtWarnGroupK', 'addr':0x302A15, 'DESC':'Ext warning group K',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCInverter-Mon',    'proto':'getSysExtWarnGroupL', 'addr':0x302A16, 'DESC':'Ext warning group L',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCMisc-Mon',        'proto':'getSysExtWarnGroupM', 'addr':0x302A17, 'DESC':'Ext warning group M',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIBCInverter2-Mon',   'proto':'getSysExtWarnGroupN', 'addr':0x302A18, 'DESC':'Ext warning group N',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnSupply2-Mon',        'proto':'getSysExtWarnGroupS', 'addr':0x302A1C, 'DESC':'Ext warning group S',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnLogin2-Mon',         'proto':'getSysExtWarnGroupT', 'addr':0x302A1D, 'DESC':'Ext warning group T',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnConf3-Mon',          'proto':'getSysExtWarnGroupU', 'addr':0x302A1E, 'DESC':'Ext warning group U',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnComm3-Mon',          'proto':'getSysExtWarnGroupV', 'addr':0x302A1F, 'DESC':'Ext warning group V',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnIntrn2-Mon',         'proto':'getSysExtWarnGroupW', 'addr':0x302A20, 'DESC':'Ext warning group W',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtWarnComm2-Mon',          'proto':'getSysExtWarnGroupX', 'addr':0x302A21, 'DESC':'Ext warning group X',    'PINI':'NO','type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},

    # Err Monitoring
    {'r':'uint16_r', 'pv':'Mod-StdErrGroup-Mon',           'proto':'getModStdErrGroup',  'addr':0x00508D, 'DESC':'Standard err group',    'PINI':'NO','type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Mod-StdErrIntrn-Mon',           'proto':'getModStdErrGroup0', 'addr':0x005093, 'DESC':'Std err group 0',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrIntrnPDSP-Mon',       'proto':'getModStdErrGroup1', 'addr':0x005094, 'DESC':'Std err group 1',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrOutCurrent-Mon',      'proto':'getModStdErrGroup2', 'addr':0x005095, 'DESC':'Std err group 2',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrOutVolt-Mon',         'proto':'getModStdErrGroup3', 'addr':0x005096, 'DESC':'Std err group 3',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrSupply-Mon',          'proto':'getModStdErrGroup4', 'addr':0x005097, 'DESC':'Std err group 4',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrT-Mon',               'proto':'getModStdErrGroup5', 'addr':0x005098, 'DESC':'Std err group 5',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrComm-Mon',            'proto':'getModStdErrGroup6', 'addr':0x005099, 'DESC':'Std err group 6',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrIntrnMod-Mon',        'proto':'getModStdErrGroup7', 'addr':0x0050A8, 'DESC':'Std err group 7',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrAD1Ovr-Mon',  'proto':'getModStdErrGroup8', 'addr':0x0050A9, 'DESC':'Std err group 8',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrAD2Ovr-Mon',  'proto':'getModStdErrGroup9', 'addr':0x0050AA, 'DESC':'Std err group 9',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrAD1Undr-Mon', 'proto':'getModStdErrGroupA', 'addr':0x0050AB, 'DESC':'Std err group A',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrAD2Undr-Mon', 'proto':'getModStdErrGroupB', 'addr':0x0050AC, 'DESC':'Std err group B',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrLogin-Mon',           'proto':'getModStdErrGroupC', 'addr':0x0050AD, 'DESC':'Std err group C',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrConf-Mon',            'proto':'getModStdErrGroupD', 'addr':0x0050AE, 'DESC':'Std err group D',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrConf2-Mon',           'proto':'getModStdErrGroupE', 'addr':0x0050AF, 'DESC':'Std err group E',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-StdErrMisc-Mon',            'proto':'getModStdErrGroupF', 'addr':0x00509A, 'DESC':'Std err group F',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrGroup-Mon',           'proto':'getModExtErrGroup',  'addr':0x302A00, 'DESC':'Extended err group',    'PINI':'NO','type':'longin', 'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCSystem-Mon',       'proto':'getModExtErrGroupG', 'addr':0x302A01, 'DESC':'Ext err group G',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCSuppply-Mon',      'proto':'getModExtErrGroupH', 'addr':0x302A02, 'DESC':'Ext err group H',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCComm-Mon',         'proto':'getModExtErrGroupJ', 'addr':0x302A03, 'DESC':'Ext err group J',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCPwr-Mon',          'proto':'getModExtErrGroupK', 'addr':0x302A04, 'DESC':'Ext err group K',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCInverter-Mon',     'proto':'getModExtErrGroupL', 'addr':0x302A05, 'DESC':'Ext err group L',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCMisc-Mon',         'proto':'getModExtErrGroupM', 'addr':0x302A06, 'DESC':'Ext err group M',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIBCInverter2-Mon',    'proto':'getModExtErrGroupN', 'addr':0x302A07, 'DESC':'Ext err group N',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrSupply2-Mon',         'proto':'getModExtErrGroupS', 'addr':0x302A0B, 'DESC':'Ext err group S',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrLogin2-Mon',          'proto':'getModExtErrGroupT', 'addr':0x302A0C, 'DESC':'Ext err group T',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrConf3-Mon',           'proto':'getModExtErrGroupU', 'addr':0x302A0D, 'DESC':'Ext err group U',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrComm3-Mon',           'proto':'getModExtErrGroupV', 'addr':0x302A0E, 'DESC':'Ext err group V',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrIntrn2-Mon',          'proto':'getModExtErrGroupW', 'addr':0x302A0F, 'DESC':'Ext err group W',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},
    {'r':'uint16_r', 'pv':'Mod-ExtErrComm2-Mon',           'proto':'getModExtErrGroupX', 'addr':0x302A10, 'DESC':'Ext err group X',       'PINI':'NO','type':'longin', 'SELECT':Select.MASTER},

    {'r':'uint16_r', 'pv':'Sys-StdErrGroup-Mon',           'proto':'getSysStdErrGroup',  'addr':0x00508D, 'DESC':'Standard err group',    'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Sys-StdErrIntrn-Mon',           'proto':'getSysStdErrGroup0', 'addr':0x005093, 'DESC':'Std err group 0',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrIntrnPDSP-Mon',       'proto':'getSysStdErrGroup1', 'addr':0x005094, 'DESC':'Std err group 1',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrOutCurrent-Mon',      'proto':'getSysStdErrGroup2', 'addr':0x005095, 'DESC':'Std err group 2',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrOutVolt-Mon',         'proto':'getSysStdErrGroup3', 'addr':0x005096, 'DESC':'Std err group 3',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrSupply-Mon',          'proto':'getSysStdErrGroup4', 'addr':0x005097, 'DESC':'Std err group 4',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrT-Mon',               'proto':'getSysStdErrGroup5', 'addr':0x005098, 'DESC':'Std err group 5',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrComm-Mon',            'proto':'getSysStdErrGroup6', 'addr':0x005099, 'DESC':'Std err group 6',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrIntrnMod-Mon',        'proto':'getSysStdErrGroup7', 'addr':0x0050A8, 'DESC':'Std err group 7',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrAD1Ovr-Mon',  'proto':'getSysStdErrGroup8', 'addr':0x0050A9, 'DESC':'Std err group 8',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrAD2Ovr-Mon',  'proto':'getSysStdErrGroup9', 'addr':0x0050AA, 'DESC':'Std err group 9',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrAD1Undr-Mon', 'proto':'getSysStdErrGroupA', 'addr':0x0050AB, 'DESC':'Std err group A',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrAD2Undr-Mon', 'proto':'getSysStdErrGroupB', 'addr':0x0050AC, 'DESC':'Std err group B',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrLogin-Mon',           'proto':'getSysStdErrGroupC', 'addr':0x0050AD, 'DESC':'Std err group C',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrConf-Mon',            'proto':'getSysStdErrGroupD', 'addr':0x0050AE, 'DESC':'Std err group D',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrConf2-Mon',           'proto':'getSysStdErrGroupE', 'addr':0x0050AF, 'DESC':'Std err group E',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-StdErrMisc-Mon',            'proto':'getSysStdErrGroupF', 'addr':0x00509A, 'DESC':'Std err group F',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrGroup-Mon',           'proto':'getSysExtErrGroup',  'addr':0x302A00, 'DESC':'Extended err group',    'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCSystem-Mon',       'proto':'getSysExtErrGroupG', 'addr':0x302A01, 'DESC':'Ext err group G',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCSuppply-Mon',      'proto':'getSysExtErrGroupH', 'addr':0x302A02, 'DESC':'Ext err group H',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCComm-Mon',         'proto':'getSysExtErrGroupJ', 'addr':0x302A03, 'DESC':'Ext err group J',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCPwr-Mon',          'proto':'getSysExtErrGroupK', 'addr':0x302A04, 'DESC':'Ext err group K',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCInverter-Mon',     'proto':'getSysExtErrGroupL', 'addr':0x302A05, 'DESC':'Ext err group L',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCMisc-Mon',         'proto':'getSysExtErrGroupM', 'addr':0x302A06, 'DESC':'Ext err group M',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIBCInverter2-Mon',    'proto':'getSysExtErrGroupN', 'addr':0x302A07, 'DESC':'Ext err group N',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrSupply2-Mon',         'proto':'getSysExtErrGroupS', 'addr':0x302A0B, 'DESC':'Ext err group S',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrLogin2-Mon',          'proto':'getSysExtErrGroupT', 'addr':0x302A0C, 'DESC':'Ext err group T',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrConf3-Mon',           'proto':'getSysExtErrGroupU', 'addr':0x302A0D, 'DESC':'Ext err group U',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrComm3-Mon',           'proto':'getSysExtErrGroupV', 'addr':0x302A0E, 'DESC':'Ext err group V',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrIntrn2-Mon',          'proto':'getSysExtErrGroupW', 'addr':0x302A0F, 'DESC':'Ext err group W',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ExtErrComm2-Mon',           'proto':'getSysExtErrGroupX', 'addr':0x302A10, 'DESC':'Ext err group X',       'PINI':'NO', 'type':'longin', 'SELECT':Select.SYSTEM, 'RESTRICT':Restrict.MASTER},

    # System Control
    {'r':'uint16_r', 'pv':'FirmwareMain-Mon',     'proto':'getFirmwareMain',     'addr':0x007E01, 'DESC':'Main',     'type':'ai', 'PREC':'0', 'PINI':'YES'},
    {'r':'uint16_r', 'pv':'FirmwareVersion-Mon',  'proto':'getFirmwareVersion',  'addr':0x007E02, 'DESC':'Version',  'type':'ai', 'PREC':'0', 'PINI':'YES'},
    {'r':'uint16_r', 'pv':'FirmwareRevision-Mon', 'proto':'getFirmwareRevision', 'addr':0x007E03, 'DESC':'Revision', 'type':'ai', 'PREC':'0', 'PINI':'YES'},

    {'r':'uint16_r', 'pv':'SerialNumHigh-Mon',   'proto':'getSerialNumHigh', 'addr':0x005128, 'DESC':'Revision', 'type':'ai', 'PREC':'0', 'PINI':'YES'},
    {'r':'uint16_r', 'pv':'SerialNumLow-Mon',    'proto':'getSerialNumLow',  'addr':0x005129, 'DESC':'Revision', 'type':'ai', 'PREC':'0', 'PINI':'YES'},

    {'r':'uint16_r', 'pv':'Mod-State-Mon',       'proto':'getModState',         'addr':0x00508C, 'DESC':'Module state', 'type':'mbbi',
       'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP',
       'SELECT':Select.MASTER, 'SCAN':'10 second'},
    {'r':'uint16_r', 'pv':'Mod-ControlMode-Mon', 'proto':'getModControlMode',   'addr':0x0050B8, 'DESC':'Module control mode', 'type':'mbbi',
       'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Pwr', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active',
       'SELECT':Select.MASTER, 'SCAN':'10 second'},

    {'r':'uint16_r', 'pv':'Sys-State-Mon',       'proto':'getSysState',         'addr':0x00508C, 'DESC':'System state', 'type':'mbbi',
       'ONST':'', 'TWST':'POWERUP', 'FRST':'READY', 'EIST':'RUN', 'NIST':'', 'TEST':'WARN', 'TVST':'ERROR', 'FTST':'STOP',
       'SELECT':Select.SYSTEM, 'SCAN':'10 second', 'RESTRICT':Restrict.MASTER},
    {'r':'uint16_r', 'pv':'Sys-ControlMode-Mon', 'proto':'getSysControlMode',   'addr':0x0050B8, 'DESC':'System control mode', 'type':'mbbi',
       'ZRST':'Constant Voltage', 'ONST':'Constant Current', 'TWST':'Constant Pwr', 'THST':'Usense limit active', 'FRST':'Psense limit active', 'FVST':'Current derating active',
       'SELECT':Select.SYSTEM, 'SCAN':'10 second', 'RESTRICT':Restrict.MASTER},

    # ------------- Loop Values -------------
    {'r':'sint16_loop', 'pv':'Mod-VoltPreset',   'proto':'ModVoltPreset', 'addr':0x005080, 'DESC':'Module voltage preset Q1', 'EGU':'V', 'ref':'Sys-MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'r':'sint16_loop', 'pv':'Mod-VoltLimQ4',    'proto':'ModVoltLimQ4', 'addr':0x30251F, 'DESC':'Module voltage limit Q4', 'EGU':'V', 'ref':'Sys-MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'r':'sint16_loop', 'pv':'Mod-CurrentPreset','proto':'ModCurrentPreset', 'addr':0x005081, 'DESC':'Module current preset Q1', 'EGU':'V', 'ref':'Sys-MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'r':'sint16_loop', 'pv':'Mod-CurrentLimQ4', 'proto':'ModCurrentLimQ4', 'addr':0x30251D, 'DESC':'Module current limit Q4', 'EGU':'A', 'ref':'Sys-MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-', 'PINI':'YES'},
    {'r':'sint16_loop', 'pv':'Mod-PwrPreset',    'proto':'ModPwrPreset', 'addr':0x005082, 'DESC':'Module power preset Q1', 'EGU':'kW', 'ref':'Sys-MaxPwr-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},
    {'r':'sint16_loop', 'pv':'Mod-PwrLimQ4',     'proto':'ModPwrLimQ4', 'addr':0x30251E, 'DESC':'Module power limit Q4', 'EGU':'kW', 'ref':'Sys-MinPwr-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'MINUS':'-', 'PINI':'YES'},
    {'r':'sint16_loop', 'pv':'Mod-ResPreset',    'proto':'ModResPreset', 'addr':0x005083, 'DESC':'Module resistence preset', 'EGU':'mOhms', 'ref':'Sys-NomIntrnRes-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'PINI':'YES'},

    {'r':'sint16_loop', 'pv':'Sys-VoltPreset',    'proto':'SysVoltPreset', 'addr':0x005080, 'DESC':'System voltage preset Q1', 'EGU':'V', 'ref':'Sys-MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'Sys-VoltLimQ4',    'proto':'SysVoltLimQ4', 'addr':0x30251F, 'DESC':'System voltage limit Q4', 'EGU':'V', 'ref':'Sys-MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'Sys-CurrentPreset','proto':'SysCurrentPreset', 'addr':0x005081, 'DESC':'System current preset Q1', 'EGU':'V', 'ref':'Sys-MaxCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'Sys-CurrentLimQ4', 'proto':'SysCurrentLimQ4', 'addr':0x30251D, 'DESC':'System current limit Q4', 'EGU':'A', 'ref':'Sys-MinCurrent-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-', 'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'Sys-PwrLimQ4',     'proto':'SysPwrLimQ4', 'addr':0x30251E, 'DESC':'System power limit Q4', 'EGU':'kW', 'ref':'Sys-MinPwr-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'MINUS':'-', 'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'Sys-PwrPreset',    'proto':'SysPwrPreset', 'addr':0x005082, 'DESC':'System power preset Q1', 'EGU':'kW', 'ref':'Sys-MaxPwr-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'Sys-ResPreset',    'proto':'SysResPreset', 'addr':0x005083, 'DESC':'System resistence preset', 'EGU':'mOhms', 'ref':'Sys-NomIntrnRes-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'PINI':'YES', 'RESTRICT':Restrict.MASTER},

    # ------------- Controller Parameters -------------
    # Slope
    {'r':'sint16_loop', 'pv':'StartupVoltSlope',   'proto':'StartupVoltSlope',   'addr':0x005154, 'DESC':'Startup volt 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'StartupCurrentSlope','proto':'StartupCurrentSlope','addr':0x005155, 'DESC':'Startup curr 100% in x ms', 'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'VoltSlope',          'proto':'VoltSlope',          'addr':0x005156, 'DESC':'Volt slope',                'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_loop', 'pv':'CurrentSlope',       'proto':'CurrentSlope',       'addr':0x005157, 'DESC':'Current slope',             'EGU':'ms', 'ESLO':'-0.00003125', 'EOFF':'1.05', 'DRVH':'1.05', 'DRVL': '0.05', 'LINR':'LINEAR', 'RESTRICT':Restrict.MASTER},

    # ------------- Remote Controle Input -------------
    {'r':'sint16_r', 'pv':'ActiveInterface-Mon',        'proto':'getActiveInterface', 'addr':0x005087, 'DESC':'Active interface', 'type':'mbbi', 'PINI':'YES', 'ZRST': 'Analog/Digital Inputs', 'ONST':'HMI', 'TWST':'RS232', 'THST':'Intrn', 'DESC':'Which interface is active', 'FRST':'passiv', 'FRVL': '32767'},

    # ------------- Actual Values -------------
    {'r':'sint16_r', 'pv':'NomDCLinkVolt-Mon', 'proto':'getNomDCLinkVolt', 'addr':0x005105, 'DESC':'DC link nominal voltage',  'EGU':'V', 'PINI':'YES'},
    {'r':'sint16_r', 'pv':'DCLinkVolt-Mon',    'proto':'getDCLinkVolt',    'addr':0x005012, 'DESC':'DC link voltage measure',  'EGU':'V', 'ref':'NomDCLinkVolt-Mon', 'PHAS':'1', 'SCAN':'5 second'},

    {'r':'sint16_r', 'pv':'Mod-OutVolt-Mon',   'proto':'getModOutVolt',    'addr':0x005084, 'DESC':'Module out voltage', 'EGU':'V', 'ref':'Mod-MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'5 second'},
    {'r':'sint16_r', 'pv':'Mod-OutPwr-Mon',    'proto':'getModOutPwr',     'addr':0x005086, 'DESC':'Module out power',   'EGU':'kW', 'ref':['Mod-MaxPwr-Mon', 'Mod-MinPwr-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'5 second'},
    {'r':'sint16_r', 'pv':'Mod-OutCurrent-Mon','proto':'getModOutCurrent', 'addr':0x005085, 'DESC':'Module out current', 'EGU':'A', 'ref':['Mod-MaxCurrent-Mon', 'Mod-MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.MASTER, 'SCAN':'5 second'},

    {'r':'sint16_r', 'pv':'Sys-OutVolt-Mon',   'proto':'getSysOutVolt',    'addr':0x005084, 'DESC':'System out voltage', 'EGU':'V', 'ref':'Sys-MaxVolt-Mon', 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'5 second', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-OutCurrent-Mon','proto':'getSysOutCurrent', 'addr':0x005085, 'DESC':'System out current', 'EGU':'A', 'ref':['Sys-MaxCurrent-Mon', 'Sys-MinCurrent-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'5 second', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-OutPwr-Mon',    'proto':'getSysOutPwr',     'addr':0x005086, 'DESC':'System out power',   'EGU':'kW', 'ref':['Sys-MaxPwr-Mon', 'Sys-MinPwr-Mon'], 'PHAS':'1', 'SELECT':Select.SYSTEM, 'SCAN':'5 second', 'RESTRICT':Restrict.MASTER},

    # ------------- Temperature -------------
    # Device
    {'r':'sint16_r', 'pv':'IGBTT-Mon',          'proto':'getIGBTTemp',     'addr':0x005007, 'DESC':'IGBT temperature',      'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR', 'SCAN':'10 second'},
    {'r':'sint16_r', 'pv':'RectifierT-Mon',     'proto':'getRectfierTemp', 'addr':0x00500F, 'DESC':'Rectifier temperature', 'EGU':'C', 'ESLO': 25./4000., 'LINR':'LINEAR', 'SCAN':'10 second'},

    # ------------- Module Values -------------
    {'r':'sint16_r', 'pv':'Mod-MaxVolt-Mon',     'proto':'getModMaxVolt'     ,'addr':0x005100, 'DESC':'Maximum module voltage',          'EGU':'V',     'PINI':'YES'},
    {'r':'sint16_r', 'pv':'Mod-MaxCurrent-Mon',  'proto':'getModMaxCurrent'  ,'addr':0x005101, 'DESC':'Maximum module current (Q1)',     'EGU':'A',     'PINI':'YES'},
    {'r':'sint16_r', 'pv':'Mod-MaxPwr-Mon',      'proto':'getModMaxPwr'      ,'addr':0x005102, 'DESC':'Maximum module power (Q1)',       'EGU':'kW',    'PINI':'YES'},
    {'r':'sint16_r', 'pv':'Mod-MinVolt-Mon',     'proto':'getModMinVolt'     ,'addr':0x00510F, 'DESC':'Minimum module voltage',          'EGU':'V',     'PINI':'YES'},
    {'r':'sint16_r', 'pv':'Mod-MinCurrent-Mon',  'proto':'getModMinCurrent'  ,'addr':0x005110, 'DESC':'Minimum module current (Q4)',     'EGU':'A',     'PINI':'YES'},
    {'r':'sint16_r', 'pv':'Mod-MinPwr-Mon',      'proto':'getModMinPwr'      ,'addr':0x005111, 'DESC':'Minimum module power (Q4)',       'EGU':'kW',    'PINI':'YES'},
    {'r':'sint16_r', 'pv':'Mod-NomIntrnRes-Mon', 'proto':'getModNomIntrnRes' ,'addr':0x005103, 'DESC':'Nom. module internal resistence', 'EGU':'mOhms', 'PINI':'YES'},

    # ------------- System Values -------------
    {'r':'sint16_r', 'pv':'Sys-MaxVolt-Mon',     'proto':'getSysMaxVolt'    ,'addr':0x00510B, 'DESC':'Maximum system voltage',          'EGU':'V',     'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-MaxCurrent-Mon',  'proto':'getSysMaxCurrent' ,'addr':0x00510C, 'DESC':'Maximum system current (Q1)',     'EGU':'A',     'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-MaxPwr-Mon',      'proto':'getSysMaxPwr'     ,'addr':0x00510D, 'DESC':'Maximum system power (Q1)',       'EGU':'kW',    'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-MinVolt-Mon',     'proto':'getSysMinVolt'    ,'addr':0x005112, 'DESC':'Minimum system voltage',          'EGU':'V',     'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-MinCurrent-Mon',  'proto':'getSysMinCurrent' ,'addr':0x005113, 'DESC':'Minimum system current (Q4)',     'EGU':'A',     'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-MinPwr-Mon',      'proto':'getSysMinPwr'     ,'addr':0x005114, 'DESC':'Minimum system power (Q4)',       'EGU':'kW',    'PINI':'YES', 'RESTRICT':Restrict.MASTER},
    {'r':'sint16_r', 'pv':'Sys-NomIntrnRes-Mon', 'proto':'getSysNomIntrnRes','addr':0x00510E, 'DESC':'Nom. system internal resistence', 'EGU':'mOhms', 'PINI':'YES', 'RESTRICT':Restrict.MASTER}
]

def getAddr(addr):
    address_as_string = "{:06X}".format(addr)
    return "\\x" + address_as_string[4:] + "\\x" + address_as_string[2:4] + "\\x" + address_as_string[:2]

def get_uint16_r(mapping):
    db_str, proto_str = '',''
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
    return db_str, proto_str

def get_uint16_w(mapping):
    db_str, proto_str = '',''
    mapping['address'] =  getAddr(mapping['addr'])
    db_str += err.safe_substitute(default, **mapping)

    if mapping['type'] == 'bo':
        proto_str += UINT16_W.safe_substitute(default, **mapping)
        db_str += bo.safe_substitute(default, **mapping)
    elif mapping['type'] == 'bo_cmd':
        proto_str += UINT16_W_1.safe_substitute(default, **mapping)
        db_str += bo_cmd.safe_substitute(default, **mapping)

    return db_str, proto_str

def get_sint16_loop(mapping):
    db_str, proto_str = '',''
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
        return db_str, proto_str


    db_str += loop_analog.safe_substitute(default, **mapping)
    proto  = mapping['proto']

    mapping['proto'] = 'set' + proto
    proto_str += SINT16_W.safe_substitute(default, **mapping)
    mapping['proto'] = 'get' + proto
    proto_str += SINT16_R.safe_substitute(default, **mapping)
    return db_str, proto_str

def get_sint16_w(mapping):
    db_str, proto_str = '',''
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
        return db_str, proto_str

    db_str += ao_ref.safe_substitute(default, **mapping)
    proto_str += SINT16_W.safe_substitute(default, **mapping)
    return db_str, proto_str

def get_sint16_r(mapping):
    db_str, proto_str = '',''
    mapping['address'] =  getAddr(mapping['addr'])

    db_str += err.safe_substitute(default, **mapping)

    #if mapping.get('type') != 'mbbi' and mapping.get('SELECT') and mapping.get('ref') and type(mapping.get('ref')) != list:
    #    db_str += ai_ref_sel.safe_substitute(default, **mapping)
    #    proto_str += SINT16_R.safe_substitute(default, **mapping)
    #    print(mapping['pv'])
    #    return db_str, proto_str

    #if mapping.get('type') != 'mbbi' and mapping.get('SELECT') and mapping.get('ref') and type(mapping.get('ref')) == list:
    #    mapping['ref'] = mapping['ref'][0]
    #    db_str += ai_ref_sel.safe_substitute(default, **mapping)
    #    proto_str += SINT16_R.safe_substitute(default, **mapping)
    #    continue

    #if mapping.get('type') != 'mbbi' and mapping.get('SELECT') and not mapping.get('ref'):
    #    db_str += ai_sel.safe_substitute(default, **mapping)
    #    proto_str += SINT16_R.safe_substitute(default, **mapping)
    #    continue


    if mapping.get('type') == 'mbbi':
        db_str += mbbi.safe_substitute(default, **mapping)
    elif mapping.get('ref'):
        if type(mapping.get('ref')) == list:
            db_str += ai_ref_2.safe_substitute(default, **mapping, ref0 = mapping['ref'][0], ref1 = mapping['ref'][1])
        else:
            print(mapping['pv'])
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

    return db_str, proto_str


if __name__ == '__main__':
    db_master_str = ''
    db_generic_str = select
    proto_generic_str = SELECT

    for mapping in MAPPING:
        if   mapping['r'] == 'uint16_r':
            db_str, proto_str = get_uint16_r(mapping)

        elif mapping['r'] == 'uint16_w':
            db_str, proto_str = get_uint16_w(mapping)

        elif mapping['r'] == 'sint16_r':
            db_str, proto_str = get_sint16_r(mapping)

        elif mapping['r'] == 'sint16_w':
            db_str, proto_str = get_sint16_w(mapping)

        elif mapping['r'] == 'sint16_loop':
            db_str, proto_str = get_sint16_loop(mapping)

        #@todo: fix me
        if mapping.get('RESTRICT') == Restrict.MASTER:
            db_master_str += db_str
        else:
            db_generic_str += db_str

        proto_generic_str += proto_str

    for f in [('TopCon.db', db_generic_str), ('TopConMaster.db', db_master_str), ('TopCon.proto', proto_generic_str)]:
        with open(f[0], "w+") as output_file:
            output_file.write(f[1])
