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
            "desc": "Error 0 - Internal",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrnPDSP-Mon",
            "desc": "Error 1 - Internal (PDSP)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrOutCurrent-Mon",
            "desc": "Error 2 - Out Current",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrOutVolt-Mon",
            "desc": "Error 3 - Out Voltage",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrSupply-Mon",
            "desc": "Error 4 - Suppply",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrT-Mon",
            "desc": "Error 5 - Temperature",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrComm-Mon",
            "desc": "Error 6 - Communication",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrnMod-Mon",
            "desc": "Error 7 - Intern (Modulator)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD1Ovr-Mon",
            "desc": "Error 8 - Intern (AD Ovr 1)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD2Ovr-Mon",
            "desc": "Error 9 - Intern (AD Ovr 2)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD1Undr-Mon",
            "desc": "Error A - Intern (AD Undr 1)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrAD2Undr-Mon",
            "desc": "Error B - Intern (AD Undr 2)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrLogin-Mon",
            "desc": "Error C - Login",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf-Mon",
            "desc": "Error D - Config",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf2-Mon",
            "desc": "Error E - Config 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrMisc-Mon",
            "desc": "Error F - Misc",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCSystem-Mon",
            "desc": "Error G - IBC System",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCSuppply-Mon",
            "desc": "Error H - IBC Supply",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCComm-Mon",
            "desc": "Error J - IBC Comm",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCPwr-Mon",
            "desc": "Error K - IBC Pwr",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCInv-Mon",
            "desc": "Error L - IBC Inverter",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCMisc-Mon",
            "desc": "Error M - IBC Misc",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIBCInv2-Mon",
            "desc": "Error N - IBC Inverter 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrP-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf4-Mon",
            "desc": "Error Q - Configuration 4",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrMisc2-Mon",
            "desc": "Error E - Miscellaneous 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrSupply2-Mon",
            "desc": "Error S - Supply 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrLogin2-Mon",
            "desc": "Error T - Login 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrConf3-Mon",
            "desc": "Error U - Configuration 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrComm3-Mon",
            "desc": "Error V - Communication 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrIntrn2-Mon",
            "desc": "Error W - Internal 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-ErrComm2-Mon",
            "desc": "Error X - Communication 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnGroup-Mon",
            "desc": "Mod  +  Warn group",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrn-Mon",
            "desc": "Warn 0 - Internal",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrnPDSP-Mon",
            "desc": "Warn 0 - Internal (PDSP)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnOutCurrent-Mon",
            "desc": "Warn 2 - Out Current",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnOutVolt-Mon",
            "desc": "Warn 2 - Out Voltage",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnSupply-Mon",
            "desc": "Warn 4 - Suppply",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnT-Mon",
            "desc": "Warn 5 - Temperature",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnComm-Mon",
            "desc": "Warn 6 - Communication",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrnMod-Mon",
            "desc": "Warn 7 - Intern (Modulator)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD1Ovr-Mon",
            "desc": "Warn 8 - Intern (AD Ovr 1)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD2Ovr-Mon",
            "desc": "Warn 9 - Intern (AD Ovr 2)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD1Undr-Mon",
            "desc": "Warn A - Intern (AD Undr 1)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnAD2Undr-Mon",
            "desc": "Warn B - Intern (AD Undr 2)",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnLogin-Mon",
            "desc": "Warn C - Login",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf-Mon",
            "desc": "Warn D - Config",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf2-Mon",
            "desc": "Warn E - Config 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnMisc-Mon",
            "desc": "Warn F - Misc",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCSystem-Mon",
            "desc": "Warn G - IBC System",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCSuppply-Mon",
            "desc": "Warn H - IBC Supply",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCComm-Mon",
            "desc": "Warn J - IBC Comm",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCPwr-Mon",
            "desc": "Warn K - IBC Pwr",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCInv-Mon",
            "desc": "Warn L - IBC Inverter",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCMisc-Mon",
            "desc": "Warn M - IBC Misc",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIBCInv2-Mon",
            "desc": "Warn N - IBC Inverter 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnP-Mon",
            "desc": "not used",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf4-Mon",
            "desc": "Warn Q - Configuration 4",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnMisc2-Mon",
            "desc": "Warn E - Miscellaneous 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnSupply2-Mon",
            "desc": "Warn S - Supply 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnLogin2-Mon",
            "desc": "Warn T - Login 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnConf3-Mon",
            "desc": "Warn U - Configuration 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnComm3-Mon",
            "desc": "Warn V - Communication 3",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnIntrn2-Mon",
            "desc": "Warn W - Internal 2",
            "type": TemplateType.LONG_IN_ITEM,
        },
        {
            "pv": "$(D):Mod-WarnComm2-Mon",
            "desc": "Warn X - Communication 2",
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
                "desc": "Error 0 - Internal",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrnPDSP-Mon",
                "desc": "Error 1 - Internal (PDSP)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrOutCurrent-Mon",
                "desc": "Error 2 - Out Current",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrOutVolt-Mon",
                "desc": "Error 3 - Out Voltage",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrSupply-Mon",
                "desc": "Error 4 - Suppply",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrT-Mon",
                "desc": "Error 5 - Temperature",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrComm-Mon",
                "desc": "Error 6 - Communication",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrnMod-Mon",
                "desc": "Error 7 - Intern (Modulator)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD1Ovr-Mon",
                "desc": "Error 8 - Intern (AD Ovr 1)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD2Ovr-Mon",
                "desc": "Error 9 - Intern (AD Ovr 2)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD1Undr-Mon",
                "desc": "Error A - Intern (AD Undr 1)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrAD2Undr-Mon",
                "desc": "Error B - Intern (AD Undr 2)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrLogin-Mon",
                "desc": "Error C - Login",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf-Mon",
                "desc": "Error D - Config",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf2-Mon",
                "desc": "Error E - Config 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrMisc-Mon",
                "desc": "Error F - Misc",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCSystem-Mon",
                "desc": "Error G - IBC System",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCSuppply-Mon",
                "desc": "Error H - IBC Supply",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCComm-Mon",
                "desc": "Error J - IBC Comm",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCPwr-Mon",
                "desc": "Error K - IBC Pwr",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCInv-Mon",
                "desc": "Error L - IBC Inverter",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCMisc-Mon",
                "desc": "Error M - IBC Misc",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIBCInv2-Mon",
                "desc": "Error N - IBC Inverter 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrP-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf4-Mon",
                "desc": "Error Q - Configuration 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrMisc2-Mon",
                "desc": "Error E - Miscellaneous 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrSupply2-Mon",
                "desc": "Error S - Supply 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrLogin2-Mon",
                "desc": "Error T - Login 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrConf3-Mon",
                "desc": "Error U - Configuration 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrComm3-Mon",
                "desc": "Error V - Communication 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrIntrn2-Mon",
                "desc": "Error W - Internal 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-ErrComm2-Mon",
                "desc": "Error X - Communication 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnGroup-Mon",
                "desc": "System  +  Warn group",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrn-Mon",
                "desc": "Warn 0 - Internal",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrnPDSP-Mon",
                "desc": "Warn 0 - Internal (PDSP)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnOutCurrent-Mon",
                "desc": "Warn 2 - Out Current",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnOutVolt-Mon",
                "desc": "Warn 2 - Out Voltage",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnSupply-Mon",
                "desc": "Warn 4 - Suppply",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnT-Mon",
                "desc": "Warn 5 - Temperature",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnComm-Mon",
                "desc": "Warn 6 - Communication",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrnMod-Mon",
                "desc": "Warn 7 - Intern (Modulator)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD1Ovr-Mon",
                "desc": "Warn 8 - Intern (AD Ovr 1)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD2Ovr-Mon",
                "desc": "Warn 9 - Intern (AD Ovr 2)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD1Undr-Mon",
                "desc": "Warn A - Intern (AD Undr 1)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnAD2Undr-Mon",
                "desc": "Warn B - Intern (AD Undr 2)",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnLogin-Mon",
                "desc": "Warn C - Login",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf-Mon",
                "desc": "Warn D - Config",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf2-Mon",
                "desc": "Warn E - Config 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnMisc-Mon",
                "desc": "Warn F - Misc",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCSystem-Mon",
                "desc": "Warn G - IBC System",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCSuppply-Mon",
                "desc": "Warn H - IBC Supply",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCComm-Mon",
                "desc": "Warn J - IBC Comm",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCPwr-Mon",
                "desc": "Warn K - IBC Pwr",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCInv-Mon",
                "desc": "Warn L - IBC Inverter",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCMisc-Mon",
                "desc": "Warn M - IBC Misc",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIBCInv2-Mon",
                "desc": "Warn N - IBC Inverter 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnP-Mon",
                "desc": "not used",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf4-Mon",
                "desc": "Warn Q - Configuration 4",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnMisc2-Mon",
                "desc": "Warn E - Miscellaneous 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnSupply2-Mon",
                "desc": "Warn S - Supply 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnLogin2-Mon",
                "desc": "Warn T - Login 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnConf3-Mon",
                "desc": "Warn U - Configuration 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnComm3-Mon",
                "desc": "Warn V - Communication 3",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnIntrn2-Mon",
                "desc": "Warn W - Internal 2",
                "type": TemplateType.LONG_IN_ITEM,
            },
            {
                "pv": "$(D):Sys-WarnComm2-Mon",
                "desc": "Warn X - Communication 2",
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
