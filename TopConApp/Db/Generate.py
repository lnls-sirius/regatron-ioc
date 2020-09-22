#!/usr/bin/env python3

from Common import (
    DEFAULTS,
    TemplateType,
)
from Records import (
    generic_cmd,
    generic_get_set,
    generic_mon,
    mod_mon,
    sys_cmd,
    sys_get_set,
    sys_mon,
    temperature,
)
from ErrorTree32 import sys as sys_tree, mod as mod_tree


def renderWfMon(entries):
    params = DEFAULTS.copy()
    params.update(entries["params"])
    n = 0
    db = ""
    db += TemplateType.WF_DB.safe_substitute(**params)
    for item in entries["items"]:
        kwargs = DEFAULTS.copy()
        kwargs.update(item)
        kwargs["wf"] = params["pv"]
        kwargs["n"] = str(n)
        template = item.get("type", TemplateType.ANALOG_ITEM)
        db += template.safe_substitute(**kwargs)
        n += 1
    return db


def renderRecord(entries):
    db = ""
    if type(entries) == list:
        for e in entries:
            db += renderRecord(e)
        return db

    # Consider entries as a single dict
    if "items" in entries:  # If so ... It's a waveform
        db += renderWfMon(entries)
    else:
        params = DEFAULTS.copy()
        params.update(entries)
        template = entries.get("type", TemplateType.ANALOG_GET)
        db += template.safe_substitute(**params)

    return db


if __name__ == "__main__":
    regs = [
        {"file": "GenericCmd.db", "entries": generic_cmd},
        {"file": "GenericGetSet.db", "entries": generic_get_set},
        {"file": "GenericMon.db", "entries": generic_mon},
        {"file": "Mod-Mon.db", "entries": mod_mon},
        {"file": "ModTree.db", "entries": mod_tree},
        {"file": "SysCmd.db", "entries": sys_cmd},
        {"file": "SysGetSet.db", "entries": sys_get_set},
        {"file": "Sys-Mon.db", "entries": sys_mon},
        {"file": "SysTree.db", "entries": sys_tree},
        {"file": "TempMon.db", "entries": temperature},
    ]
    for reg in regs:
        with open(reg["file"], "w+") as _f:
            db = renderRecord(reg["entries"])
            _f.write(db)
