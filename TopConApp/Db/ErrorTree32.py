from Common import FTVL, TemplateType

# Error and Warning Tree specifics

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
    "params": {
        "pv": "$(D):Mod-Tree",
        "param": "getModTree",
        "scan": "30 second",
        "ftvl": FTVL.DOUBLE,
        "nelm": "66",
    },
    "items": [
        {
            "pv": "$(D):Mod-ErrGroup-Mon",
            "desc": "Mod Std + Ext error group",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrIntrn-Mon",
            "desc": "Std warn group 0",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrIntrnPDSP-Mon",
            "desc": "Std warn group 1",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrOutCurrent-Mon",
            "desc": "Std warn group 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrOutVolt-Mon",
            "desc": "Std warn group 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrSupply-Mon",
            "desc": "Std warn group 4",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrT-Mon",
            "desc": "Std warn group 5",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrComm-Mon",
            "desc": "Std warn group 6",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrIntrnMod-Mon",
            "desc": "Std warn group 7",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrAD1Ovr-Mon",
            "desc": "Std warn group 8",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrAD2Ovr-Mon",
            "desc": "Std warn group 9",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrAD1Undr-Mon",
            "desc": "Std warn group A",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrAD2Undr-Mon",
            "desc": "Std warn group B",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrLogin-Mon",
            "desc": "Std warn group C",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrConf-Mon",
            "desc": "Std warn group D",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrConf2-Mon",
            "desc": "Std warn group E",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdErrMisc-Mon",
            "desc": "Std warn group F",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCSystem-Mon",
            "desc": "Ext warn group G",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCSuppply-Mon",
            "desc": "Ext warn group H",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCComm-Mon",
            "desc": "Ext warn group J",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCPwr-Mon",
            "desc": "Ext warn group K",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCInv-Mon",
            "desc": "Ext warn group L",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCMisc-Mon",
            "desc": "Ext warn group M",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIBCInv2-Mon",
            "desc": "Ext warn group N",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrP-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrQ-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrR-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrSupply2-Mon",
            "desc": "Ext warn group S",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrLogin2-Mon",
            "desc": "Ext warn group T",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrConf3-Mon",
            "desc": "Ext warn group U",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrComm3-Mon",
            "desc": "Ext warn group V",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrIntrn2-Mon",
            "desc": "Ext warn group W",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtErrComm2-Mon",
            "desc": "Ext warn group X",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnGroup-Mon",
            "desc": "Mod Std + Ext warn group",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnIntrn-Mon",
            "desc": "Std warn group 0",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnIntrnPDSP-Mon",
            "desc": "Std warn group 1",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnOutCurrent-Mon",
            "desc": "Std warn group 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnOutVolt-Mon",
            "desc": "Std warn group 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnSupply-Mon",
            "desc": "Std warn group 4",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnT-Mon",
            "desc": "Std warn group 5",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnComm-Mon",
            "desc": "Std warn group 6",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnIntrnMod-Mon",
            "desc": "Std warn group 7",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnAD1Ovr-Mon",
            "desc": "Std warn group 8",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnAD2Ovr-Mon",
            "desc": "Std warn group 9",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnAD1Undr-Mon",
            "desc": "Std warn group A",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnAD2Undr-Mon",
            "desc": "Std warn group B",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnLogin-Mon",
            "desc": "Std warn group C",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnConf-Mon",
            "desc": "Std warn group D",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnConf2-Mon",
            "desc": "Std warn group E",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-StdWarnMisc-Mon",
            "desc": "Std warn group F",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCSystem-Mon",
            "desc": "Ext warn group G",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCSuppply-Mon",
            "desc": "Ext warn group H",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCComm-Mon",
            "desc": "Ext warn group J",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCPwr-Mon",
            "desc": "Ext warn group K",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCInv-Mon",
            "desc": "Ext warn group L",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCMisc-Mon",
            "desc": "Ext warn group M",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIBCInv2-Mon",
            "desc": "Ext warn group N",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnP-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnQ-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnR-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnSupply2-Mon",
            "desc": "Ext warn group S",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnLogin2-Mon",
            "desc": "Ext warn group T",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnConf3-Mon",
            "desc": "Ext warn group U",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnComm3-Mon",
            "desc": "Ext warn group V",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnIntrn2-Mon",
            "desc": "Ext warn group W",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ExtWarnComm2-Mon",
            "desc": "Ext warn group X",
            "type": TemplateType.LONG_IN_ITEM,
        },
    ],
}


# Error Monitoring
sys = [
    {
        "params": {
            "pv": "$(D):Sys-Tree",
            "param": "getSysTree",
            "scan": "30 second",
            "ftvl": FTVL.DOUBLE,
            "nelm": "66",
        },
        "items": [
            {
                "pv": "$(D):Sys-ErrGroup-Mon",
                "desc": "Sys Std + Ext error group",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrIntrn-Mon",
                "desc": "Std warn group 0",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrIntrnPDSP-Mon",
                "desc": "Std warn group 1",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrOutCurrent-Mon",
                "desc": "Std warn group 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrOutVolt-Mon",
                "desc": "Std warn group 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrSupply-Mon",
                "desc": "Std warn group 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrT-Mon",
                "desc": "Std warn group 5",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrComm-Mon",
                "desc": "Std warn group 6",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrIntrnMod-Mon",
                "desc": "Std warn group 7",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrAD1Ovr-Mon",
                "desc": "Std warn group 8",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrAD2Ovr-Mon",
                "desc": "Std warn group 9",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrAD1Undr-Mon",
                "desc": "Std warn group A",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrAD2Undr-Mon",
                "desc": "Std warn group B",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrLogin-Mon",
                "desc": "Std warn group C",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrConf-Mon",
                "desc": "Std warn group D",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrConf2-Mon",
                "desc": "Std warn group E",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdErrMisc-Mon",
                "desc": "Std warn group F",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCSystem-Mon",
                "desc": "Ext warn group G",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCSuppply-Mon",
                "desc": "Ext warn group H",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCComm-Mon",
                "desc": "Ext warn group J",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCPwr-Mon",
                "desc": "Ext warn group K",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCInv-Mon",
                "desc": "Ext warn group L",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCMisc-Mon",
                "desc": "Ext warn group M",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIBCInv2-Mon",
                "desc": "Ext warn group N",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrP-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrQ-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrR-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrSupply2-Mon",
                "desc": "Ext warn group S",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrLogin2-Mon",
                "desc": "Ext warn group T",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrConf3-Mon",
                "desc": "Ext warn group U",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrComm3-Mon",
                "desc": "Ext warn group V",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrIntrn2-Mon",
                "desc": "Ext warn group W",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtErrComm2-Mon",
                "desc": "Ext warn group X",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnGroup-Mon",
                "desc": "System Std + Ext warn group",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnIntrn-Mon",
                "desc": "Std warn group 0",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnIntrnPDSP-Mon",
                "desc": "Std warn group 1",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnOutCurrent-Mon",
                "desc": "Std warn group 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnOutVolt-Mon",
                "desc": "Std warn group 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnSupply-Mon",
                "desc": "Std warn group 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnT-Mon",
                "desc": "Std warn group 5",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnComm-Mon",
                "desc": "Std warn group 6",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnIntrnMod-Mon",
                "desc": "Std warn group 7",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnAD1Ovr-Mon",
                "desc": "Std warn group 8",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnAD2Ovr-Mon",
                "desc": "Std warn group 9",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnAD1Undr-Mon",
                "desc": "Std warn group A",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnAD2Undr-Mon",
                "desc": "Std warn group B",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnLogin-Mon",
                "desc": "Std warn group C",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnConf-Mon",
                "desc": "Std warn group D",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnConf2-Mon",
                "desc": "Std warn group E",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-StdWarnMisc-Mon",
                "desc": "Std warn group F",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCSystem-Mon",
                "desc": "Ext warn group G",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCSuppply-Mon",
                "desc": "Ext warn group H",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCComm-Mon",
                "desc": "Ext warn group J",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCPwr-Mon",
                "desc": "Ext warn group K",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCInv-Mon",
                "desc": "Ext warn group L",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCMisc-Mon",
                "desc": "Ext warn group M",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIBCInv2-Mon",
                "desc": "Ext warn group N",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnP-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnQ-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnR-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnSupply2-Mon",
                "desc": "Ext warn group S",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnLogin2-Mon",
                "desc": "Ext warn group T",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnConf3-Mon",
                "desc": "Ext warn group U",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnComm3-Mon",
                "desc": "Ext warn group V",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnIntrn2-Mon",
                "desc": "Ext warn group W",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ExtWarnComm2-Mon",
                "desc": "Ext warn group X",
                "type": TemplateType.LONG_IN_ITEM,
            },
        ],
    },
    {
        "pv": "$(D):GenErr-Mon",
        "desc": "General Error Status",
        "inpa": "$(D):Sys-WarnGroup-Mon",
        "inpb": "$(D):Mod-WarnGroup-Mon",
        "type": TemplateType.ALARM_OR,
    },
    {
        "pv": "$(D):GenWarn-Mon",
        "desc": "General Warning Status",
        "inpa": "$(D):Sys-ErrGroup-Mon",
        "inpb": "$(D):Mod-ErrGroup-Mon",
        "type": TemplateType.ALARM_OR,
    },
]
