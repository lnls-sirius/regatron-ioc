from string import Template

PROTOCOL = "Regatron.proto"


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
    field(INP,  "${proto} getArray(${param}) $(PORT) $(A)")
    field(FTVL, "${type}")
    field(NELM, "${nelm}")
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
