#!/usr/bin/env python
from Common import FTVL, TemplateType

mod_mon = [
    {
        "params": {
            "pv": "$(D):Mod-MinMaxNom-Mon",
            "param": "getModMinMaxNom",
            "scan": "30 second",
            "nelm": "12",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Mod-MinVolt-Mon", "desc": "Voltage Min", "egu": "V"},
            {"pv": "$(D):Mod-MinCurrent-Mon", "desc": "Current Min", "egu": "A"},
            {"pv": "$(D):Mod-MinPwr-Mon", "desc": "Power Min", "egu": "kW"},
            {"pv": "$(D):Mod-MinRes-Mon", "desc": "Resistance Min", "egu": "mOhm"},
            {"pv": "$(D):Mod-MaxVolt-Mon", "desc": "Voltage Max", "egu": "V"},
            {"pv": "$(D):Mod-MaxCurrent-Mon", "desc": "Current Max", "egu": "A"},
            {"pv": "$(D):Mod-MaxPwr-Mon", "desc": "Power Max", "egu": "kW"},
            {"pv": "$(D):Mod-MaxRes-Mon", "desc": "Resistance Max", "egu": "mOhm"},
            {"pv": "$(D):Mod-NomVolt-Mon", "desc": "Voltage Nominal", "egu": "V"},
            {"pv": "$(D):Mod-NomCurrent-Mon", "desc": "Current Nominal", "egu": "A"},
            {"pv": "$(D):Mod-NomPwr-Mon", "desc": "Power Nominal", "egu": "kW"},
            {"pv": "$(D):Mod-NomRes-Mon", "desc": "Resistance Nominal", "egu": "mOhm"},
        ],
    },
    {
        "params": {
            "pv": "$(D):Mod-Mon",
            "param": "getModReadings",
            "scan": "5 second",
            "nelm": "5",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Mod-OutVolt-Mon", "desc": "Module out voltage", "egu": "V"},
            {"pv": "$(D):Mod-OutCurrent-Mon", "desc": "Module out current", "egu": "A"},
            {"pv": "$(D):Mod-OutPwr-Mon", "desc": "Module out power", "egu": "kW"},
            {
                "pv": "$(D):Mod-ResPreset-Mon",
                "desc": "Module resistence preset",
                "egu": "mOhm",
            },
            {
                "pv": "$(D):Mod-State-Mon",
                "desc": "Module state",
                "type": TemplateType.MBBI_ITEM,
                "onst": "",
                "twst": "POWERUP",
                "frst": "READY",
                "eist": "RUN",
                "nist": "",
                "test": "WARN",
                "tvst": "ERROR",
                "ftst": "STOP",
            },
        ],
    },
    {
        "pv": "$(D):Mod-ControlMode-Mon",
        "desc": "Module control mode",
        "param": "getModControlMode",
        "type": TemplateType.MBBI,
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]

sys_get_set = [
    {
        "pv": "$(D):Sys-CurrentRef",
        "desc": "Reference val. for current",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysCurrentRef",
        "egu": "A",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Sys-OutVoltEnbl",
        "desc": "Enable/Disable output voltage",
        "type": TemplateType.BINARY_GET_SET,
        "znam": "Disable",
        "onam": "Enable",
        "param": "SysOutVoltEnable",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Sys-VoltageRef",
        "desc": "Reference val. for voltage",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysVoltageRef",
        "egu": "V",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Sys-ResistanceRef",
        "desc": "Reference val. for resistance",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysResistanceRef",
        "egu": "mOhm",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Sys-PwrRef",
        "desc": "Reference val. for power",
        "type": TemplateType.ANALOG_GET_SET,
        "param": "SysPowerRef",
        "egu": "kW",
        "prio": "HIGH",
    },
    {
        "params": {
            "pv": "$(D):Sys-VoltSlope-Wf",
            "param": "getVoltageRampSlope",
            "scan": "Passive",
            "nelm": "2",
            "ftvl": FTVL.DOUBLE,
            "prio": "HIGH",
        },
        "items": [
            {
                "pv": "$(D):Sys-StartupVoltSlope-RB",
                "desc": "Applied to set values when enabling output volt",
                "egu": "s",
            },
            {
                "pv": "$(D):Sys-VoltSlope-RB",
                "desc": "Applied to set values when they are changed",
                "egu": "s",
            },
        ],
    },
    {
        "pv": "$(D):Sys-StartupVoltSlope-SP",
        "desc": "Applied to set values when enabling output volt",
        "type": TemplateType.ANALOG_SET,
        "param": "setStartupVoltageRampSeconds",
        "drvh": "1.6",
        "drvl": "0.00005",
        "egu": "s",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Sys-VoltSlope-SP",
        "desc": "Applied to set values when they are changed",
        "type": TemplateType.ANALOG_SET,
        "param": "setVoltageRampSeconds",
        "drvh": "1.6",
        "drvl": "0.00005",
        "egu": "s",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Sys-WriteVoltSlope-Cmd",
        "desc": "Apply voltage slope settings",
        "type": TemplateType.BO_CMD,
        "param": "cmdWriteVoltageRamp",
        "prio": "HIGH",
        "flnk": "$(D):Sys-VoltSlope-Wf",
    },
]

sys_cmd = [
    {
        "pv": "$(D):Save-Cmd",
        "desc": "Save settings to non-volatile memory",
        "type": TemplateType.BO_CMD,
        "param": "cmdStoreParam",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Clear-Cmd",
        "desc": "Clear Errors and/or warnings",
        "type": TemplateType.BO_CMD,
        "param": "cmdClearErrors",
        "prio": "HIGH",
    },
]

sys_mon = [
    {
        "params": {
            "pv": "$(D):Sys-MinMaxNom-Mon",
            "param": "getSysMinMaxNom",
            "scan": "30 second",
            "nelm": "12",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Sys-MinVolt-Mon", "desc": "Voltage Min", "egu": "V"},
            {"pv": "$(D):Sys-MinCurrent-Mon", "desc": "Current Min", "egu": "A"},
            {"pv": "$(D):Sys-MinPwr-Mon", "desc": "Power Min", "egu": "kW"},
            {"pv": "$(D):Sys-MinRes-Mon", "desc": "Resistance Min", "egu": "mOhm"},
            {"pv": "$(D):Sys-MaxVolt-Mon", "desc": "Voltage Max", "egu": "V"},
            {"pv": "$(D):Sys-MaxCurrent-Mon", "desc": "Current Max", "egu": "A"},
            {"pv": "$(D):Sys-MaxPwr-Mon", "desc": "Power Max", "egu": "kW"},
            {"pv": "$(D):Sys-MaxRes-Mon", "desc": "Resistance Max", "egu": "mOhm"},
            {"pv": "$(D):Sys-NomVolt-Mon", "desc": "Voltage Nominal", "egu": "V"},
            {"pv": "$(D):Sys-NomCurrent-Mon", "desc": "Current Nominal", "egu": "A"},
            {"pv": "$(D):Sys-NomPwr-Mon", "desc": "Power Nominal", "egu": "kW"},
            {"pv": "$(D):Sys-NomRes-Mon", "desc": "Resistance Nominal", "egu": "mOhm"},
        ],
    },
    {
        "params": {
            "pv": "$(D):Sys-Mon",
            "param": "getSysReadings",
            "scan": "5 second",
            "nelm": "5",
            "ftvl": FTVL.DOUBLE,
        },
        "items": [
            {"pv": "$(D):Sys-OutVolt-Mon", "desc": "System out voltage", "egu": "V"},
            {"pv": "$(D):Sys-OutCurrent-Mon", "desc": "System out current", "egu": "A"},
            {"pv": "$(D):Sys-OutPwr-Mon", "desc": "System out power", "egu": "kW"},
            {
                "pv": "$(D):Sys-ResPreset-Mon",
                "desc": "System resistence preset",
                "egu": "mOhm",
            },
            {
                "pv": "$(D):Sys-State-Mon",
                "desc": "System state",
                "type": TemplateType.MBBI_ITEM,
                "onst": "",
                "twst": "POWERUP",
                "frst": "READY",
                "eist": "RUN",
                "nist": "",
                "test": "WARN",
                "tvst": "ERROR",
                "ftst": "STOP",
            },
        ],
    },
    {
        "pv": "$(D):Sys-ControlMode-Mon",
        "param": "getSysControlMode",
        "desc": "System control mode",
        "type": TemplateType.MBBI,
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]


temperature = {
    "params": {
        "pv": "$(D):T-Mon",
        "param": "getTemperatures",
        "scan": "5 second",
        "nelm": "3",
        "ftvl": FTVL.DOUBLE,
    },
    "items": [
        {"pv": "$(D):IGBTT-Mon", "desc": "IGBT temperature", "egu": "C"},
        {"pv": "$(D):RectifierT-Mon", "desc": "Rectifier temperature", "egu": "C"},
        {"pv": "$(D):PCBT-Mon", "desc": "PCB temperature", "egu": "C"},
    ],
}


generic_mon = [
    {
        "pv": "$(D):ActiveInterface-Mon",
        "desc": "Active interface",
        "scan": "60 second",
        "type": TemplateType.MBBI,
        "param": "getControlInput",
        "zrst": "Analog/Digital Inputs",
        "onst": "HMI/HME",
        "twst": "RS232",
        "thst": "",
        "frst": "",
        "frvl": "",
    },
    {
        "pv": "$(D):DCLinkVolt-Mon",
        "desc": "DC link voltage measure",
        "param": "getDCLinkVoltage",
        "egu": "V",
        "scan": "5 second",
    },
    {
        "pv": "$(D):PrimaryCurr-Mon",
        "desc": "Transformer primary current",
        "param": "getPrimaryCurrent",
        "egu": "A",
        "scan": "5 second",
    },
    {
        "pv": "$(D):DSPVer-Mon",
        "desc": "DSP Firmware Version",
        "param": "getDSPVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):ModulatorVer-Mon",
        "desc": "Modulator Version",
        "param": "getModulatorVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):PheripherieVer-Mon",
        "desc": "Pheripherie Version",
        "param": "getPheripherieVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):BootloaderVer-Mon",
        "desc": "Bootloader Version",
        "param": "getBootloaderVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
    {
        "pv": "$(D):DLLVer-Mon",
        "desc": "DLL Version",
        "param": "getDLLVersion",
        "scan": "60 second",
        "type": TemplateType.STRING_IN,
    },
]

generic_cmd = [
    {
        "pv": "$(D):Connect-Cmd",
        "desc": "Attempt to connect to the device",
        "type": TemplateType.BO_CMD,
        "param": "cmdConnect",
        "prio": "HIGH",
    },
    {
        "pv": "$(D):Disconnect-Cmd",
        "desc": "Disconnect from device",
        "type": TemplateType.BO_CMD,
        "param": "cmdDisconnect",
        "prio": "HIGH",
    },
]

generic_get_set = [
    {
        "pv": "$(D):AutoReconnect",
        "desc": "Enable/Disable auto reconnect to device",
        "type": TemplateType.BINARY_GET_SET,
        "param": "AutoReconnect",
        "onam": "Enable",
        "znam": "Disable",
        "prio": "HIGH",
    },
]
