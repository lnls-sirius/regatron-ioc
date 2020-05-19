from string import Template

# Common resources

PROTOCOL = "@Regatron.proto"
DEFAULTS = {
    "proto": PROTOCOL,
    "zrst": "",
    "onst": "",
    "twst": "",
    "thst": "",
    "frst": "",
    "fvst": "",
    "sxst": "",
    "svst": "",
    "eist": "",
    "nist": "",
    "test": "",
    "elst": "",
    "tvst": "",
    "ttst": "",
    "ftst": "",
    "ffst": "",
    "zrsv": "",
    "onsv": "",
    "twsv": "",
    "thsv": "",
    "frsv": "",
    "fvsv": "",
    "sxsv": "",
    "svsv": "",
    "eisv": "",
    "nisv": "",
    "tesv": "",
    "elsv": "",
    "tvsv": "",
    "ttsv": "",
    "ftsv": "",
    "ffsv": "",
    "phas": "0",
    "eoff": "0",
    "eslo": "1",
    "drvh": "0",
    "drvl": "0",
    "linr": "NO CONVERSION",
    "disv": "0",
    "disa": "1",
    "egu": "",
    "prec": "2",
    "scan": "Passive",
    "pini": "NO",
    "prio": "LOW",
    "onam": "",
    "znam": "",
}


class FTVL:
    STRING = "STRING"
    CHAR = "CHAR"
    UCHAR = "UCHAR"
    SHORT = "SHORT"
    USHORT = "USHORT"
    LONG = "LONG"
    ULONG = "ULONG"
    FLOAT = "FLOAT"
    DOUBLE = "DOUBLE"
    ENUM = "ENUM"


wf_db = Template(
    """
record(waveform, "${pv}"){
    field(SCAN, "${scan}")
    field(DTYP, "stream")
    field(INP,  "${proto} getArray(${param}) $(P)")
    field(FTVL, "${type}")
    field(NELM, "${nelm}")
    field(PRIO, "${prio}")
}
"""
)
item_ai_db = Template(
    """
record(ai, "${pv}"){
    field(SCAN, "Passive")
    field(DESC, "${desc}")
    field(EGU,  "${egu}")
    field(PREC, "${prec}")
    field(DTYP, "Soft Channel")

    field(INP,  "${wf}.VAL[${n}] CP MSS")
}
"""
)
item_long_db = Template(
    """
record(longin, "${pv}"){
    field(SCAN, "Passive")
    field(INP,  "${wf}.VAL[${n}] CP MSS")
    field(DESC, "${desc}")
    field(DTYP, "Soft Channel")
}
"""
)

item_mbbi_db = Template(
    """
record(mbbi, "${pv}") {
    field(SCAN, "Passive")
    field(DESC, "${desc}")
    field(DTYP, "Soft Channel")

    field(ZRST, "${zrst}")
    field(ONST, "${onst}")
    field(TWST, "${twst}")
    field(THST, "${thst}")
    field(FRST, "${frst}")
    field(FVST, "${fvst}")
    field(SXST, "${sxst}")
    field(SVST, "${svst}")
    field(EIST, "${eist}")
    field(NIST, "${nist}")
    field(TEST, "${test}")
    field(ELST, "${elst}")
    field(TVST, "${tvst}")
    field(TTST, "${ttst}")
    field(FTST, "${ftst}")
    field(FFST, "${ffst}")

    field(ZRSV, "${zrsv}")
    field(ONSV, "${onsv}")
    field(TWSV, "${twsv}")
    field(THSV, "${thsv}")
    field(FRSV, "${frsv}")
    field(FVSV, "${fvsv}")
    field(SXSV, "${sxsv}")
    field(SVSV, "${svsv}")
    field(EISV, "${eisv}")
    field(NISV, "${nisv}")
    field(TESV, "${tesv}")
    field(ELSV, "${elsv}")
    field(TVSV, "${tvsv}")
    field(TTSV, "${ttsv}")
    field(FTSV, "${ftsv}")
    field(FFSV, "${ffsv}")

    field(INP,  "${wf}.VAL[${n}] CP MSS")
}
"""
)

mbbi_db = Template(
    """
record(mbbi, "${pv}") {
    field(PINI, "${pini}")
    field(SCAN, "${scan}")
    field(PHAS, "${phas}")
    field(DESC, "${desc}")

    field(ZRST, "${zrst}")
    field(ONST, "${onst}")
    field(TWST, "${twst}")
    field(THST, "${thst}")
    field(FRST, "${frst}")
    field(FVST, "${fvst}")
    field(SXST, "${sxst}")
    field(SVST, "${svst}")
    field(EIST, "${eist}")
    field(NIST, "${nist}")
    field(TEST, "${test}")
    field(ELST, "${elst}")
    field(TVST, "${tvst}")
    field(TTST, "${ttst}")
    field(FTST, "${ftst}")
    field(FFST, "${ffst}")

    field(ZRSV, "${zrsv}")
    field(ONSV, "${onsv}")
    field(TWSV, "${twsv}")
    field(THSV, "${thsv}")
    field(FRSV, "${frsv}")
    field(FVSV, "${fvsv}")
    field(SXSV, "${sxsv}")
    field(SVSV, "${svsv}")
    field(EISV, "${eisv}")
    field(NISV, "${nisv}")
    field(TESV, "${tesv}")
    field(ELSV, "${elsv}")
    field(TVSV, "${tvsv}")
    field(TTSV, "${ttsv}")
    field(FTSV, "${ftsv}")
    field(FFSV, "${ffsv}")

    field(DTYP, "stream")
    field(INP,  "${proto} getInt(${param}) $(P)")
}
"""
)
stringin_db = Template(
    """
record(stringin, "${pv}"){
    field(PINI, "${pini}")
    field(SCAN, "${scan}")
    field(DESC, "${desc}")
    field(PHAS, "${phas}")

    field(DTYP, "stream")
    field(INP,  "${proto} getString(${param}) $(P)")
}
"""
)

ai_db = Template(
    """
record(ai, "${pv}"){
    field(PINI, "${pini}")
    field(SCAN, "${scan}")
    field(DESC, "${desc}")
    field(EGU,  "${egu}")
    field(PREC, "${prec}")
    field(PHAS, "${phas}")
    field(LINR, "${linr}")
    field(EOFF, "${eoff}")
    field(ESLO, "${eslo}")

    field(DTYP, "stream")
    field(INP,  "${proto} getFloat(${param}) $(P)")
}
"""
)

bo_cmd_db = Template(
    """
record(bo, "${pv}"){
    field(DESC, "${desc}")
    field(ONAM, "${onam}")
    field(ZNAM, "${znam}")
    field(DISA, "${disa}")
    field(DISV, "${disv}")
    field(PRIO, "${prio}")
    field(DISS, "INVALID")

    field(DTYP, "stream")
    field(OUT,  "${proto} cmd(${param}) $(P)")
}
"""
)


binary_get_set_db = Template(
    """
record(bi, "${pv}-RB"){
    field(SCAN, "${scan}")
    field(DESC, "${desc}")
    field(PHAS, "${phas}")
    field(ZNAM, "${znam}")
    field(ONAM, "${onam}")
    field(PRIO, "${prio}")

    field(DTYP, "stream")
    field(INP,  "${proto} getInt(get${param}) $(P)")
}
record(bo, "${pv}-SP"){
    field(PINI, "NO")
    field(DESC, "${desc}")
    field(PHAS, "${phas}")
    field(ZNAM, "${znam}")
    field(ONAM, "${onam}")
    field(PRIO, "${prio}")

    field(DTYP, "stream")
    field(OUT,  "${proto} setInt(set${param}) $(P)")
    field(FLNK, "${pv}-RB")
}
"""
)
analog_get_set_db = Template(
    """
record(ai, "${pv}-RB"){
    field(SCAN, "${scan}")
    field(DESC, "${desc}")
    field(EGU,  "${egu}")
    field(PREC, "${prec}")
    field(PHAS, "${phas}")
    field(LINR, "${linr}")
    field(EOFF, "${eoff}")
    field(ESLO, "${eslo}")
    field(PRIO, "${prio}")

    field(DTYP, "stream")
    field(INP,  "${proto} getFloat(get${param}) $(P)")
}
record(ao, "${pv}-SP"){
    field(PINI, "NO")
    field(DESC, "${desc}")
    field(EGU,  "${egu}")
    field(PREC, "${prec}")
    field(PHAS, "${phas}")
    field(LINR, "${linr}")
    field(EOFF, "${eoff}")
    field(ESLO, "${eslo}")
    field(PRIO, "${prio}")

    field(DTYP, "stream")
    field(OUT,  "${proto} setFloat(set${param}) $(P)")
    field(FLNK, "${pv}-RB")
}
"""
)
long_get_set_db = Template(
    """
record(longin, "${pv}-RB"){
    field(DESC, "${desc}")
    field(EGU,  "${egu}")
    field(PREC, "${prec}")
    field(PHAS, "${phas}")
    field(PRIO, "${prio}")

    field(DTYP, "stream")
    field(INP,  "${proto} getInt(get${param}) $(PORT)")
}
record(longout, "${pv}-SP"){
    field(PINI, "NO")
    field(DESC, "${desc}")
    field(EGU,  "${egu}")
    field(PREC, "${prec}")
    field(PHAS, "${phas}")
    field(LINR, "${linr}")
    field(PRIO, "${prio}")

    field(DTYP, "stream")
    field(OUT,  "${proto} setInt(set${param}) $(PORT)")
    field(FLNK, "${pv}-RB")
}
"""
)


class TemplateType(object):
    BO_CMD = "bo_cmd"
    LONG_GET_SET = "long_get_set"
    BINARY_GET_SET = "binary_get_set"
    ANALOG_GET_SET = "analog_get_set"
    LONG_IN = "longin"
    MBBI = "mbbi"
    STRING_IN = "stringin"

    @classmethod
    def getTemplate(template) -> Template:
        # @todo: !fixme!
        # BO_CMD = "bo_cmd"
        # LONG_GET_SET = "long_get_set"
        # LONG_IN = "longin"
        # MBBI = "mbbi"
        # STRING_IN = "stringin"
        pass
