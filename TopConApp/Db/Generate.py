#!/usr/bin/env python3

from Common import (
    DEFAULTS,
    ai_db,
    bo_cmd_db,
    item_ai_db,
    item_long_db,
    item_mbbi_db,
    mbbi_db,
    stringin_db,
    wf_db,
)
from Monitor import generic_mon, mod_mon, sys_mon, sys_cmd, sys_get_set, temp
from ErrorTree32 import sys as sys_tree, mod as mod_tree


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
        elif item.get("type", False) == "longin":
            db += item_long_db.safe_substitute(wf=params["pv"], n=str(n), **kwargs)
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
        elif entries.get("type", False) == "bo_cmd":
            db += bo_cmd_db.safe_substitute(**params)
        elif entries.get("type", False) == "stringin":
            db += stringin_db.safe_substitute(**params)
        else:
            db += ai_db.safe_substitute(**params)

    return db


if __name__ == "__main__":
    regs = [
        {"file": "GenericMon.db", "entries": generic_mon},
        {"file": "ModMon.db", "entries": mod_mon},
        {"file": "ModTree.db", "entries": mod_tree},
        {"file": "SysCmd.db", "entries": sys_cmd},
        {"file": "SysGetSet.db", "entries": sys_get_set},
        {"file": "SysMon.db", "entries": sys_mon},
        {"file": "SysTree.db", "entries": sys_tree},
        {"file": "TempMon.db", "entries": temp},
    ]
    for reg in regs:
        with open(reg["file"], "w+") as _f:
            db = renderMon(reg["entries"])
            _f.write(db)
