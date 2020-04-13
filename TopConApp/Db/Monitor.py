#!/usr/bin/env python
from Common import (
    wf_db,
    item_mbbi_db,
    item_long_db,
    item_ai_db,
    FTVL,
    PROTOCOL,
    DEFAULTS,
)

#  // [IGBT,Rectfier,PCB]
#  getTemperatures
#  // [Voltage,Current,Power,Res,State]
#  getModReadings
#  getSysReadings
#'pv':'NomDCLinkVolt-Mon', 'desc':'DC link nominal voltage',  'egu':'V'
#'pv':'DCLinkVolt-Mon',    'desc':'DC link voltage measure',  'egu':'V'

mod = {
    "params": {"pv": "$(D):Mod-Mon", "param": "getSysReadings", "scan": ""},
    "items": [
        {"pv": "$(D):Mod-OutVolt-Mon", "desc": "Module out voltage", "egu": "V"},
        {"pv": "$(D):Mod-OutCurrent-Mon", "desc": "Module out current", "egu": "A"},
        {"pv": "$(D):Mod-OutPwr-Mon", "desc": "Module out power", "egu": "kW"},
        {"pv": "$(D):Mod-ResPreset", "desc": "Module resistence preset", "EGU": "mOhm"},
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
}

sys = {
    "params": {"pv": "$(D):Sys-Mon", "param": "getSysReadings", "scan": ""},
    "items": [
        {"pv": "$(D):Sys-OutVolt-Mon", "desc": "System out voltage", "egu": "V"},
        {"pv": "$(D):Sys-OutCurrent-Mon", "desc": "System out current", "egu": "A"},
        {"pv": "$(D):Sys-OutPwr-Mon", "desc": "System out power", "egu": "kW"},
        {"pv": "$(D):Sys-ResPreset", "desc": "System resistence preset", "EGU": "mOhm"},
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
}


def renderMon(entries):
    db = ""
    n = 0
    params = DEFAULTS.copy()
    params.update(entries["params"])

    db += wf_db.safe_substitute(proto=PROTOCOL, type=FTVL.DOUBLE, nelm="5", **params)
    for item in entries["items"]:
        kwargs = DEFAULTS.copy()
        kwargs.update(item)

        if item.get("type", False) == "mbbi":
            db += item_mbbi_db.safe_substitute(wf=params["pv"], n=str(n), **kwargs)
        else:
            db += item_db.safe_substitute(wf=params["pv"], n=str(n), **kwargs)
        n += 1
    return db


if __name__ == "__main__":
    regs = [
        {"file": "SysMon.db", "entries": sys},
        {"file": "ModMon.db", "entries": mod},
    ]
    for reg in regs:
        with open(reg["file"], "w+") as _f:
            db = renderMon(reg["entries"])
            _f.write(db)
