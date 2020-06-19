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
            "desc": "Mod + Ext error group",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrn-Mon",
            "desc": "warn group 0",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrnPDSP-Mon",
            "desc": "warn group 1",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrOutCurrent-Mon",
            "desc": "warn group 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrOutVolt-Mon",
            "desc": "warn group 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrSupply-Mon",
            "desc": "warn group 4",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrT-Mon",
            "desc": "warn group 5",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrComm-Mon",
            "desc": "warn group 6",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrnMod-Mon",
            "desc": "warn group 7",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD1Ovr-Mon",
            "desc": "warn group 8",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD2Ovr-Mon",
            "desc": "warn group 9",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD1Undr-Mon",
            "desc": "warn group A",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD2Undr-Mon",
            "desc": "warn group B",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrLogin-Mon",
            "desc": "warn group C",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf-Mon",
            "desc": "warn group D",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf2-Mon",
            "desc": "warn group E",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrMisc-Mon",
            "desc": "warn group F",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCSystem-Mon",
            "desc": "warn group G",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCSuppply-Mon",
            "desc": "warn group H",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCComm-Mon",
            "desc": "warn group J",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCPwr-Mon",
            "desc": "warn group K",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCInv-Mon",
            "desc": "warn group L",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCMisc-Mon",
            "desc": "warn group M",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCInv2-Mon",
            "desc": "warn group N",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrP-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrQ-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrR-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrSupply2-Mon",
            "desc": "warn group S",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrLogin2-Mon",
            "desc": "warn group T",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf3-Mon",
            "desc": "warn group U",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrComm3-Mon",
            "desc": "warn group V",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrn2-Mon",
            "desc": "warn group W",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrComm2-Mon",
            "desc": "warn group X",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnGroup-Mon",
            "desc": "Mod  +  warn group",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrn-Mon",
            "desc": "warn group 0",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrnPDSP-Mon",
            "desc": "warn group 1",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnOutCurrent-Mon",
            "desc": "warn group 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnOutVolt-Mon",
            "desc": "warn group 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnSupply-Mon",
            "desc": "warn group 4",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnT-Mon",
            "desc": "warn group 5",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnComm-Mon",
            "desc": "warn group 6",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrnMod-Mon",
            "desc": "warn group 7",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD1Ovr-Mon",
            "desc": "warn group 8",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD2Ovr-Mon",
            "desc": "warn group 9",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD1Undr-Mon",
            "desc": "warn group A",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD2Undr-Mon",
            "desc": "warn group B",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnLogin-Mon",
            "desc": "warn group C",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf-Mon",
            "desc": "warn group D",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf2-Mon",
            "desc": "warn group E",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnMisc-Mon",
            "desc": "warn group F",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCSystem-Mon",
            "desc": "warn group G",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCSuppply-Mon",
            "desc": "warn group H",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCComm-Mon",
            "desc": "warn group J",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCPwr-Mon",
            "desc": "warn group K",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCInv-Mon",
            "desc": "warn group L",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCMisc-Mon",
            "desc": "warn group M",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCInv2-Mon",
            "desc": "warn group N",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnP-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnQ-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnR-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnSupply2-Mon",
            "desc": "warn group S",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnLogin2-Mon",
            "desc": "warn group T",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf3-Mon",
            "desc": "warn group U",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnComm3-Mon",
            "desc": "warn group V",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrn2-Mon",
            "desc": "warn group W",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnComm2-Mon",
            "desc": "warn group X",
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
                "desc": "Sys  +  error group",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrn-Mon",
                "desc": "warn group 0",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrnPDSP-Mon",
                "desc": "warn group 1",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrOutCurrent-Mon",
                "desc": "warn group 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrOutVolt-Mon",
                "desc": "warn group 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrSupply-Mon",
                "desc": "warn group 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrT-Mon",
                "desc": "warn group 5",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrComm-Mon",
                "desc": "warn group 6",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrnMod-Mon",
                "desc": "warn group 7",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD1Ovr-Mon",
                "desc": "warn group 8",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD2Ovr-Mon",
                "desc": "warn group 9",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD1Undr-Mon",
                "desc": "warn group A",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD2Undr-Mon",
                "desc": "warn group B",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrLogin-Mon",
                "desc": "warn group C",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf-Mon",
                "desc": "warn group D",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf2-Mon",
                "desc": "warn group E",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrMisc-Mon",
                "desc": "warn group F",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCSystem-Mon",
                "desc": "warn group G",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCSuppply-Mon",
                "desc": "warn group H",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCComm-Mon",
                "desc": "warn group J",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCPwr-Mon",
                "desc": "warn group K",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCInv-Mon",
                "desc": "warn group L",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCMisc-Mon",
                "desc": "warn group M",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCInv2-Mon",
                "desc": "warn group N",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrP-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrQ-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrR-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrSupply2-Mon",
                "desc": "warn group S",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrLogin2-Mon",
                "desc": "warn group T",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf3-Mon",
                "desc": "warn group U",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrComm3-Mon",
                "desc": "warn group V",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrn2-Mon",
                "desc": "warn group W",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrComm2-Mon",
                "desc": "warn group X",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnGroup-Mon",
                "desc": "System  +  warn group",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrn-Mon",
                "desc": "warn group 0",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrnPDSP-Mon",
                "desc": "warn group 1",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnOutCurrent-Mon",
                "desc": "warn group 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnOutVolt-Mon",
                "desc": "warn group 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnSupply-Mon",
                "desc": "warn group 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnT-Mon",
                "desc": "warn group 5",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnComm-Mon",
                "desc": "warn group 6",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrnMod-Mon",
                "desc": "warn group 7",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD1Ovr-Mon",
                "desc": "warn group 8",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD2Ovr-Mon",
                "desc": "warn group 9",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD1Undr-Mon",
                "desc": "warn group A",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD2Undr-Mon",
                "desc": "warn group B",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnLogin-Mon",
                "desc": "warn group C",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf-Mon",
                "desc": "warn group D",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf2-Mon",
                "desc": "warn group E",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnMisc-Mon",
                "desc": "warn group F",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCSystem-Mon",
                "desc": "warn group G",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCSuppply-Mon",
                "desc": "warn group H",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCComm-Mon",
                "desc": "warn group J",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCPwr-Mon",
                "desc": "warn group K",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCInv-Mon",
                "desc": "warn group L",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCMisc-Mon",
                "desc": "warn group M",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCInv2-Mon",
                "desc": "warn group N",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnP-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf4-Mon",
                "desc": "Configuration 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnMisc2-Mon",
                "desc": "Miscellaneous 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnSupply2-Mon",
                "desc": "warn group S",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnLogin2-Mon",
                "desc": "warn group T",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf3-Mon",
                "desc": "warn group U",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnComm3-Mon",
                "desc": "warn group V",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrn2-Mon",
                "desc": "warn group W",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnComm2-Mon",
                "desc": "warn group X",
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
