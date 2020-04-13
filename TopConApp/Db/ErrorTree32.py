#!/usr/bin/env python3
from string import Template

wf_db = Template(
    """
record(waveform, "${pv}"){
    field(PINI, "YES")
    field(SCAN, "${scan}")
    field(DTYP, "stream")
    field(INP,  "${proto} getTree32(${func}) $(PORT) $(A)")
    field(FTVL, "DOUBLE")
    field(NELM, "66")
}
"""
)
item_db = Template(
    """
record(longin, "${pv}"){
    field(INP,  "${wf}[${n}] CP MSS")
    field(DESC, "${desc}")
}
"""
)

std_values = [
    "Internal",
    "Internal PDSP",
    "Output",
    "Output",
    "Supply",
    "Temperature",
    "Communication",
    "Internal Modulator",
    "Internal ADoverrange",
    "Internal ADoverrange",
    "Internal ADunderrange1",
    "Internal ADunderrange",
    "Login",
    "Configuration",
    "Configuration",
    "Miscellaneous",
]


# Erring Monitoring
mod = {
    "params": {"pv": "$(D):Mod-Tree", "func": "getModTree", "scan": ""},
    "items": [
        {"pv": "$(D):Mod-StdErrGroup-Mon", "desc": "Std warn group"},
        {"pv": "$(D):Mod-StdErrIntrn-Mon", "desc": "Std warn group 0",},
        {"pv": "$(D):Mod-StdErrIntrnPDSP-Mon", "desc": "Std warn group 1",},
        {"pv": "$(D):Mod-StdErrOutCurrent-Mon", "desc": "Std warn group 2",},
        {"pv": "$(D):Mod-StdErrOutVolt-Mon", "desc": "Std warn group 3",},
        {"pv": "$(D):Mod-StdErrSupply-Mon", "desc": "Std warn group 4",},
        {"pv": "$(D):Mod-StdErrT-Mon", "desc": "Std warn group 5"},
        {"pv": "$(D):Mod-StdErrComm-Mon", "desc": "Std warn group 6",},
        {"pv": "$(D):Mod-StdErrIntrnMod-Mon", "desc": "Std warn group 7",},
        {"pv": "$(D):Mod-StdErrAD1Ovr-Mon", "desc": "Std warn group 8",},
        {"pv": "$(D):Mod-StdErrAD2Ovr-Mon", "desc": "Std warn group 9",},
        {"pv": "$(D):Mod-StdErrAD1Undr-Mon", "desc": "Std warn group A",},
        {"pv": "$(D):Mod-StdErrAD2Undr-Mon", "desc": "Std warn group B",},
        {"pv": "$(D):Mod-StdErrLogin-Mon", "desc": "Std warn group C",},
        {"pv": "$(D):Mod-StdErrConf-Mon", "desc": "Std warn group D",},
        {"pv": "$(D):Mod-StdErrConf2-Mon", "desc": "Std warn group E",},
        {"pv": "$(D):Mod-StdErrMisc-Mon", "desc": "Std warn group F",},
        {"pv": "$(D):Mod-ExtErrIBCSystem-Mon", "desc": "Ext warn group G",},
        {"pv": "$(D):Mod-ExtErrIBCSuppply-Mon", "desc": "Ext warn group H",},
        {"pv": "$(D):Mod-ExtErrIBCComm-Mon", "desc": "Ext warn group J",},
        {"pv": "$(D):Mod-ExtErrIBCPwr-Mon", "desc": "Ext warn group K",},
        {"pv": "$(D):Mod-ExtErrIBCInv-Mon", "desc": "Ext warn group L",},
        {"pv": "$(D):Mod-ExtErrIBCMisc-Mon", "desc": "Ext warn group M",},
        {"pv": "$(D):Mod-ExtErrIBCInv2-Mon", "desc": "Ext warn group N",},
        {"pv": "$(D):Mod-ExtErrP-Mon", "desc": "not used",},
        {"pv": "$(D):Mod-ExtErrQ-Mon", "desc": "not used",},
        {"pv": "$(D):Mod-ExtErrR-Mon", "desc": "not used",},
        {"pv": "$(D):Mod-ExtErrSupply2-Mon", "desc": "Ext warn group S",},
        {"pv": "$(D):Mod-ExtErrLogin2-Mon", "desc": "Ext warn group T",},
        {"pv": "$(D):Mod-ExtErrConf3-Mon", "desc": "Ext warn group U",},
        {"pv": "$(D):Mod-ExtErrComm3-Mon", "desc": "Ext warn group V",},
        {"pv": "$(D):Mod-ExtErrIntrn2-Mon", "desc": "Ext warn group W",},
        {"pv": "$(D):Mod-ExtErrComm2-Mon", "desc": "Ext warn group X",},
        {"pv": "$(D):Mod-StdWarnGroup-Mon", "desc": "Std warn group"},
        {"pv": "$(D):Mod-StdWarnIntrn-Mon", "desc": "Std warn group 0",},
        {"pv": "$(D):Mod-StdWarnIntrnPDSP-Mon", "desc": "Std warn group 1",},
        {"pv": "$(D):Mod-StdWarnOutCurrent-Mon", "desc": "Std warn group 2",},
        {"pv": "$(D):Mod-StdWarnOutVolt-Mon", "desc": "Std warn group 3",},
        {"pv": "$(D):Mod-StdWarnSupply-Mon", "desc": "Std warn group 4",},
        {"pv": "$(D):Mod-StdWarnT-Mon", "desc": "Std warn group 5"},
        {"pv": "$(D):Mod-StdWarnComm-Mon", "desc": "Std warn group 6",},
        {"pv": "$(D):Mod-StdWarnIntrnMod-Mon", "desc": "Std warn group 7",},
        {"pv": "$(D):Mod-StdWarnAD1Ovr-Mon", "desc": "Std warn group 8",},
        {"pv": "$(D):Mod-StdWarnAD2Ovr-Mon", "desc": "Std warn group 9",},
        {"pv": "$(D):Mod-StdWarnAD1Undr-Mon", "desc": "Std warn group A",},
        {"pv": "$(D):Mod-StdWarnAD2Undr-Mon", "desc": "Std warn group B",},
        {"pv": "$(D):Mod-StdWarnLogin-Mon", "desc": "Std warn group C",},
        {"pv": "$(D):Mod-StdWarnConf-Mon", "desc": "Std warn group D",},
        {"pv": "$(D):Mod-StdWarnConf2-Mon", "desc": "Std warn group E",},
        {"pv": "$(D):Mod-StdWarnMisc-Mon", "desc": "Std warn group F",},
        {"pv": "$(D):Mod-ExtWarnIBCSystem-Mon", "desc": "Ext warn group G",},
        {"pv": "$(D):Mod-ExtWarnIBCSuppply-Mon", "desc": "Ext warn group H",},
        {"pv": "$(D):Mod-ExtWarnIBCComm-Mon", "desc": "Ext warn group J",},
        {"pv": "$(D):Mod-ExtWarnIBCPwr-Mon", "desc": "Ext warn group K",},
        {"pv": "$(D):Mod-ExtWarnIBCInv-Mon", "desc": "Ext warn group L",},
        {"pv": "$(D):Mod-ExtWarnIBCMisc-Mon", "desc": "Ext warn group M",},
        {"pv": "$(D):Mod-ExtWarnIBCInv2-Mon", "desc": "Ext warn group N",},
        {"pv": "$(D):Mod-ExtWarnP-Mon", "desc": "not used",},
        {"pv": "$(D):Mod-ExtWarnQ-Mon", "desc": "not used",},
        {"pv": "$(D):Mod-ExtWarnR-Mon", "desc": "not used",},
        {"pv": "$(D):Mod-ExtWarnSupply2-Mon", "desc": "Ext warn group S",},
        {"pv": "$(D):Mod-ExtWarnLogin2-Mon", "desc": "Ext warn group T",},
        {"pv": "$(D):Mod-ExtWarnConf3-Mon", "desc": "Ext warn group U",},
        {"pv": "$(D):Mod-ExtWarnComm3-Mon", "desc": "Ext warn group V",},
        {"pv": "$(D):Mod-ExtWarnIntrn2-Mon", "desc": "Ext warn group W",},
        {"pv": "$(D):Mod-ExtWarnComm2-Mon", "desc": "Ext warn group X",},
    ],
}


# Error Monitoring
sys = {
    "params": {"pv": "$(D):Sys-Tree", "func": "getSysTree", "scan": ""},
    "items": [
        {"pv": "$(D):Sys-StdErrGroup-Mon", "desc": "Std warn group"},
        {"pv": "$(D):Sys-StdErrIntrn-Mon", "desc": "Std warn group 0",},
        {"pv": "$(D):Sys-StdErrIntrnPDSP-Mon", "desc": "Std warn group 1",},
        {"pv": "$(D):Sys-StdErrOutCurrent-Mon", "desc": "Std warn group 2",},
        {"pv": "$(D):Sys-StdErrOutVolt-Mon", "desc": "Std warn group 3",},
        {"pv": "$(D):Sys-StdErrSupply-Mon", "desc": "Std warn group 4",},
        {"pv": "$(D):Sys-StdErrT-Mon", "desc": "Std warn group 5"},
        {"pv": "$(D):Sys-StdErrComm-Mon", "desc": "Std warn group 6",},
        {"pv": "$(D):Sys-StdErrIntrnMod-Mon", "desc": "Std warn group 7",},
        {"pv": "$(D):Sys-StdErrAD1Ovr-Mon", "desc": "Std warn group 8",},
        {"pv": "$(D):Sys-StdErrAD2Ovr-Mon", "desc": "Std warn group 9",},
        {"pv": "$(D):Sys-StdErrAD1Undr-Mon", "desc": "Std warn group A",},
        {"pv": "$(D):Sys-StdErrAD2Undr-Mon", "desc": "Std warn group B",},
        {"pv": "$(D):Sys-StdErrLogin-Mon", "desc": "Std warn group C",},
        {"pv": "$(D):Sys-StdErrConf-Mon", "desc": "Std warn group D",},
        {"pv": "$(D):Sys-StdErrConf2-Mon", "desc": "Std warn group E",},
        {"pv": "$(D):Sys-StdErrMisc-Mon", "desc": "Std warn group F",},
        {"pv": "$(D):Sys-ExtErrIBCSystem-Mon", "desc": "Ext warn group G",},
        {"pv": "$(D):Sys-ExtErrIBCSuppply-Mon", "desc": "Ext warn group H",},
        {"pv": "$(D):Sys-ExtErrIBCComm-Mon", "desc": "Ext warn group J",},
        {"pv": "$(D):Sys-ExtErrIBCPwr-Mon", "desc": "Ext warn group K",},
        {"pv": "$(D):Sys-ExtErrIBCInv-Mon", "desc": "Ext warn group L",},
        {"pv": "$(D):Sys-ExtErrIBCMisc-Mon", "desc": "Ext warn group M",},
        {"pv": "$(D):Sys-ExtErrIBCInv2-Mon", "desc": "Ext warn group N",},
        {"pv": "$(D):Sys-ExtErrP-Mon", "desc": "not used",},
        {"pv": "$(D):Sys-ExtErrQ-Mon", "desc": "not used",},
        {"pv": "$(D):Sys-ExtErrR-Mon", "desc": "not used",},
        {"pv": "$(D):Sys-ExtErrSupply2-Mon", "desc": "Ext warn group S",},
        {"pv": "$(D):Sys-ExtErrLogin2-Mon", "desc": "Ext warn group T",},
        {"pv": "$(D):Sys-ExtErrConf3-Mon", "desc": "Ext warn group U",},
        {"pv": "$(D):Sys-ExtErrComm3-Mon", "desc": "Ext warn group V",},
        {"pv": "$(D):Sys-ExtErrIntrn2-Mon", "desc": "Ext warn group W",},
        {"pv": "$(D):Sys-ExtErrComm2-Mon", "desc": "Ext warn group X",},
        {"pv": "$(D):Sys-StdWarnGroup-Mon", "desc": "Std warn group"},
        {"pv": "$(D):Sys-StdWarnIntrn-Mon", "desc": "Std warn group 0",},
        {"pv": "$(D):Sys-StdWarnIntrnPDSP-Mon", "desc": "Std warn group 1",},
        {"pv": "$(D):Sys-StdWarnOutCurrent-Mon", "desc": "Std warn group 2",},
        {"pv": "$(D):Sys-StdWarnOutVolt-Mon", "desc": "Std warn group 3",},
        {"pv": "$(D):Sys-StdWarnSupply-Mon", "desc": "Std warn group 4",},
        {"pv": "$(D):Sys-StdWarnT-Mon", "desc": "Std warn group 5"},
        {"pv": "$(D):Sys-StdWarnComm-Mon", "desc": "Std warn group 6",},
        {"pv": "$(D):Sys-StdWarnIntrnMod-Mon", "desc": "Std warn group 7",},
        {"pv": "$(D):Sys-StdWarnAD1Ovr-Mon", "desc": "Std warn group 8",},
        {"pv": "$(D):Sys-StdWarnAD2Ovr-Mon", "desc": "Std warn group 9",},
        {"pv": "$(D):Sys-StdWarnAD1Undr-Mon", "desc": "Std warn group A",},
        {"pv": "$(D):Sys-StdWarnAD2Undr-Mon", "desc": "Std warn group B",},
        {"pv": "$(D):Sys-StdWarnLogin-Mon", "desc": "Std warn group C",},
        {"pv": "$(D):Sys-StdWarnConf-Mon", "desc": "Std warn group D",},
        {"pv": "$(D):Sys-StdWarnConf2-Mon", "desc": "Std warn group E",},
        {"pv": "$(D):Sys-StdWarnMisc-Mon", "desc": "Std warn group F",},
        {"pv": "$(D):Sys-ExtWarnIBCSystem-Mon", "desc": "Ext warn group G",},
        {"pv": "$(D):Sys-ExtWarnIBCSuppply-Mon", "desc": "Ext warn group H",},
        {"pv": "$(D):Sys-ExtWarnIBCComm-Mon", "desc": "Ext warn group J",},
        {"pv": "$(D):Sys-ExtWarnIBCPwr-Mon", "desc": "Ext warn group K",},
        {"pv": "$(D):Sys-ExtWarnIBCInv-Mon", "desc": "Ext warn group L",},
        {"pv": "$(D):Sys-ExtWarnIBCMisc-Mon", "desc": "Ext warn group M",},
        {"pv": "$(D):Sys-ExtWarnIBCInv2-Mon", "desc": "Ext warn group N",},
        {"pv": "$(D):Sys-ExtWarnP-Mon", "desc": "not used",},
        {"pv": "$(D):Sys-ExtWarnQ-Mon", "desc": "not used",},
        {"pv": "$(D):Sys-ExtWarnR-Mon", "desc": "not used",},
        {"pv": "$(D):Sys-ExtWarnSupply2-Mon", "desc": "Ext warn group S",},
        {"pv": "$(D):Sys-ExtWarnLogin2-Mon", "desc": "Ext warn group T",},
        {"pv": "$(D):Sys-ExtWarnConf3-Mon", "desc": "Ext warn group U",},
        {"pv": "$(D):Sys-ExtWarnComm3-Mon", "desc": "Ext warn group V",},
        {"pv": "$(D):Sys-ExtWarnIntrn2-Mon", "desc": "Ext warn group W",},
        {"pv": "$(D):Sys-ExtWarnComm2-Mon", "desc": "Ext warn group X",},
    ],
}


def renderT_ErrorTree(tree, proto):
    db = ""
    n = 0
    params = tree["params"]
    items = tree["items"]
    db += wf_db.safe_substitute(proto=proto, **params)
    for item in items:
        db += item_db.safe_substitute(wf=params["pv"], n=str(n), **item)
        n += 1
    return db


if __name__ == "__main__":
    proto = "@Regatron.proto"
    regs = [
        {"file": "SysTree.db", "entries": sys},
        {"file": "ModTree.db", "entries": mod},
    ]
    for reg in regs:
        with open(reg["file"], "w+") as _f:
            db = renderT_ErrorTree(reg["entries"], proto=proto)
            _f.write(db)
