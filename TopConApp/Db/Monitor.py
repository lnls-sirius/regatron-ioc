#!/usr/bin/env python
from Common import (
    DEFAULTS,
    FTVL,
    PROTOCOL,
    ai_db,
    item_ai_db,
    item_long_db,
    item_mbbi_db,
    mbbi_db,
    stringin_db,
    wf_db,
)

mod = [
    {
        "params": {
            "pv": "$(D):Mod-Mon",
            "param": "getSysReadings",
            "scan": "",
            "nelm": "5",
            "type": FTVL.DOUBLE,
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
                "type": "mbbi",
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
        "type": "mbbi",
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]


sys = [
    {
        "params": {
            "pv": "$(D):Sys-Mon",
            "param": "getSysReadings",
            "scan": "",
            "nelm": "5",
            "type": FTVL.DOUBLE,
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
                "type": "mbbi",
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
        "type": "mbbi",
        "zrst": "Constant Voltage",
        "onst": "Constant Current",
        "twst": "Constant Pwr",
        "thst": "Usense limit active",
        "frst": "Psense limit active",
        "fvst": "Current derating active",
        "scan": "10 second",
    },
]


temp = {
    "params": {
        "pv": "$(D):T-Mon",
        "param": "getTemperatures",
        "scan": "",
        "nelm": "3",
        "type": FTVL.DOUBLE,
    },
    "items": [
        {"pv": "$(D):IGBTT-Mon", "desc": "IGBT temperature", "egu": "C"},
        {"pv": "$(D):RectifierT-Mon", "desc": "Rectifier temperature", "egu": "C"},
        {"pv": "$(D):PCBT-Mon", "desc": "PCB temperature", "egu": "C"},
    ],
}


individual = [
    {
        "pv": "$(D):ActiveInterface-Mon",
        "desc": "Active interface",
        "type": "mbbi",
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
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):ModulatorVer-Mon",
        "desc": "Modulator Version",
        "param": "getModulatorVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):PheripherieVer-Mon",
        "desc": "Pheripherie Version",
        "param": "getPheripherieVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):BootloaderVer-Mon",
        "desc": "Bootloader Version",
        "param": "getBootloaderVersion",
        "scan": "10 second",
        "type": "stringin",
    },
    {
        "pv": "$(D):DLLVer-Mon",
        "desc": "DLL Version",
        "param": "getDLLVersion",
        "scan": "10 second",
        "type": "stringin",
    },
]


def renderWfMon(entries):
    params = DEFAULTS.copy()
    params.update(entries["params"])
    n = 0
    db = ""
    db += wf_db.safe_substitute(**params)
    for item in entries["items"]:
        kwargs = DEFAULTS.copy()
        kwargs.update(item)

        if item.get("type", False) == "mbbi":
            db += item_mbbi_db.safe_substitute(wf=params["pv"], n=str(n), **kwargs)
        else:
            db += item_ai_db.safe_substitute(wf=params["pv"], n=str(n), **kwargs)
        n += 1
    return db


def renderMon(entries):
    db = ""
    if type(entries) == list:
        for e in entries:
            db += renderMon(e)
        return db

    # Consider entries as a single dict
    if "items" in entries:  # If so ... It's a waveform
        db += renderWfMon(entries)
    else:
        params = DEFAULTS.copy()
        params.update(entries)

        if entries.get("type", False) == "mbbi":
            db += mbbi_db.safe_substitute(**params)
        elif entries.get("type", False) == "stringin":
            db += stringin_db.safe_substitute(**params)
        else:
            db += ai_db.safe_substitute(**params)

    return db


if __name__ == "__main__":
    regs = [
        {"file": "SysMon.db", "entries": sys},
        {"file": "ModMon.db", "entries": mod},
        {"file": "TempMon.db", "entries": temp},
        {"file": "Generic.db", "entries": individual},
    ]
    for reg in regs:
        with open(reg["file"], "w+") as _f:
            db = renderMon(reg["entries"])
            _f.write(db)
