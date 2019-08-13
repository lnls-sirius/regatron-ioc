#!/usr/bin/python3
from string import Template
err =  Template('''
record(longin, "$$(DEVICE):${pv}_error"){
    field(DESC, "${DESC}")
    field(DTYP, "Soft Channel")
    field(PINI, "YES")
    field(VAL,  "0")
}
''')

bo_cmd = Template('''
record(bo, "$$(DEVICE):${pv}"){
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(ONAM, "Clear")
    field(DISA, "${DISA}")
    field(DISV, "${DISV}")
    field(OUT,  "@TopCon.proto ${proto}($$(DEVICE):${pv}) $$(PORT)")
    field(DISS, "INVALID")
}
''')
bo = Template('''
record(bo, "$$(DEVICE):${pv}"){
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(ZNAM, "OFF")
    field(ONAM, "ON")
    field(DISA, "${DISA}")
    field(DISV, "${DISV}")
    field(DISS, "INVALID")

    field(OUT,  "@TopCon.proto ${proto}($$(DEVICE):${pv}) $$(PORT)")
}
''')
ao = Template('''
record(ao, "$$(DEVICE):${pv}"){
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "${LINR}")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DRVL, "${DRVL}")
    field(DRVH, "${DRVH}")
    field(DISA, "${DISA}")
    field(DISV, "${DISV}")
    field(DISS, "INVALID")

    field(OUT,  "@TopCon.proto ${proto}($$(DEVICE):${pv}) $$(PORT)")
}
''')

loop_analog = Template('''
record(calcout, "$$(DEVICE):${pv}-RB_eslo"){
    field(CALC, "A/${MINUS}4000.")
    field(INPA, "$$(DEVICE):${ref} CP MSS")
    field(EGU,  "${EGU}")
    field(OUT,  "$$(DEVICE):${pv}-RB.ESLO")
}
record(calcout, "$$(DEVICE):${pv}-RB_d"){
    field(CALC, "A#0") # If != NO_ALARM
    field(INPA, "$$(DEVICE):${ref}.SEVR CP")
    field(INPB, "$$(DEVICE):${ref} CP")
    field(OUT,  "$$(DEVICE):${pv}-RB.DISA")
}
record(calcout, "$$(DEVICE):${pv}-SP_eslo"){
    field(CALC, "A/${MINUS}4000.")
    field(INPA, "$$(DEVICE):${ref} CP MSS")
    field(EGU,  "${EGU}")
    field(OUT,  "$$(DEVICE):${pv}-SP.ESLO MSS")
}
record(calcout, "$$(DEVICE):${pv}-SP_d"){
    field(CALC, "A#0") # If != NO_ALARM
    field(INPA, "$$(DEVICE):${ref}.SEVR CP")
    field(INPB, "$$(DEVICE):${ref} CP")
    field(OUT,  "$$(DEVICE):${pv}-SP.DISA")
    field(FLNK, "$$(DEVICE):${pv}-SP_${HL}")
}
record(ao, "$$(DEVICE):${pv}_${HL}"){
    field(DTYP, "Soft Channel")
    field(OMSL, "closed_loop")
    field(DOL,  "$$(DEVICE):${ref}")
    field(OUT,  "$$(DEVICE):${pv}-SP.DRV${HL}")
}
record(ai, "$$(DEVICE):${pv}-RB"){
    field(PINI, "${PINI}")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "LINEAR")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DISA, "1")
    field(DISV, "1")
    field(DISS, "INVALID")

    field(INP,  "@TopCon.proto get${proto}($$(DEVICE):${pv}-RB)  $$(PORT)")
}
record(ao, "$$(DEVICE):${pv}-SP"){
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "LINEAR")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DISA, "1")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(OUT,  "@TopCon.proto set${proto}($$(DEVICE):${pv}-SP)  $$(PORT)")
    field(FLNK, "$$(DEVICE):${pv}-RB")
}
record(seq, "$$(DEVICE):${pv}_init"){
    field(PINI, "YES")
    field(PHAS, "2")

    field(DOL1, "1")
    field(LNK1, "$$(DEVICE):${pv}-SP.DISA")

    field(DLY2, "10")
    field(DOL2, "$$(DEVICE):${pv}-RB")
    field(LNK2, "$$(DEVICE):${pv}-SP")
}

''')

"""
HL : Wich limit is valid? High or Low? H / L
"""
ao_ref = Template('''
record(calcout, "$$(DEVICE):${pv}_eslo"){
    field(CALC, "A/${MINUS}4000.")
    field(INPA, "$$(DEVICE):${ref} CP MSS")
    field(EGU,  "${EGU}")
    field(OUT,  "$$(DEVICE):${pv}.ESLO MSS")
}
record(calcout, "$$(DEVICE):${pv}_d"){
    field(CALC, "A#0") # If != NO_ALARM
    field(INPA, "$$(DEVICE):${ref}.SEVR CP")
    field(INPB, "$$(DEVICE):${ref} CP")
    field(OUT,  "$$(DEVICE):${pv}.DISA")
    field(FLNK, "$$(DEVICE):${pv}_${HL}")
}
record(ao, "$$(DEVICE):${pv}_${HL}"){
    field(DTYP, "Soft Channel")
    field(OMSL, "closed_loop")
    field(DOL,  "$$(DEVICE):${ref}")
    field(OUT,  "$$(DEVICE):${pv}.DRV${HL}")
}
record(ao, "$$(DEVICE):${pv}"){
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "LINEAR")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DISA, "1")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(OUT,  "@TopCon.proto ${proto}($$(DEVICE):${pv})  $$(PORT)")
}
''')
ai = Template('''
record(ai, "$$(DEVICE):${pv}"){
    field(PINI, "${PINI}")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "${LINR}")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")

    field(INP,  "@TopCon.proto ${proto}($$(DEVICE):${pv})  $$(PORT)")
}
''')

#ai_ref_2123 = Template('''
#record(calc, "$$(DEVICE):${pv}"){
#    field(CALC, "B/${MINUS}4000.*A") # @todo: For now we assume always Q1
#    field(INPA, "$$(DEVICE):${pv}_raw PP CP MSS")
#    field(INPB, "$$(DEVICE):${ref0} NPP CP MSS") # Nominal when standard (Q1)
#    #field(INPC, "$$(DEVICE):${ref1} NPP CP MSS") # Nominal when power feedback mode (Q4)
#    field(EGU,  "${EGU}")
#}
#
#record(ai, "$$(DEVICE):${pv}_raw"){
#    field(DESC, "${DESC}")
#    field(DTYP, "stream")
#    field(EGU,  "RAW")
#    field(PREC, "${PREC}")
#    field(PHAS, "${PHAS}")
#
#    field(INP,  "@TopCon.proto ${proto}($$(DEVICE):${pv})  $$(PORT)")
#}
#''')
ai_ref = Template('''
record(calcout, "$$(DEVICE):${pv}_eslo"){
    field(CALC, "A/${MINUS}4000.")
    field(INPA, "$$(DEVICE):${ref} CP MSS")
    field(EGU,  "${EGU}")
    field(OUT,  "$$(DEVICE):${pv}.ESLO")
}
record(calcout, "$$(DEVICE):${pv}_d"){
    field(CALC, "A#0") # If != NO_ALARM
    field(INPA, "$$(DEVICE):${ref}.SEVR CP")
    field(INPB, "$$(DEVICE):${ref} CP")
    field(OUT,  "$$(DEVICE):${pv}.DISA")
}

record(ai, "$$(DEVICE):${pv}"){
    field(PINI, "${PINI}")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "LINEAR")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DISA, "1")
    field(DISV, "1")
    field(DISS, "INVALID")

    field(INP,  "@TopCon.proto ${proto}($$(DEVICE):${pv})  $$(PORT)")
}
''')
ai_ref_2 = Template('''
record(calcout, "$$(DEVICE):${pv}_eslo"){
    field(CALC, "A/${MINUS}4000.")
    field(INPA, "$$(DEVICE):${ref0} CP MSS")
    field(EGU,  "${EGU}")
    field(OUT,  "$$(DEVICE):${pv}.ESLO")
}
record(calcout, "$$(DEVICE):${pv}_d"){
    field(CALC, "A#0") # If != NO_ALARM
    field(INPA, "$$(DEVICE):${ref0}.SEVR CP")
    field(INPB, "$$(DEVICE):${ref0} CP")
    field(OUT,  "$$(DEVICE):${pv}.DISA")
}

record(ai, "$$(DEVICE):${pv}"){
    field(PINI, "${PINI}")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "${PHAS}")
    field(LINR, "LINEAR")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DISA, "1")
    field(DISV, "1")
    field(DISS, "INVALID")

    field(INP,  "@TopCon.proto ${proto}($$(DEVICE):${pv})  $$(PORT)")
}
''')
longin = Template('''
record(longin, "$$(DEVICE):${pv}"){
    field(PINI, "${PINI}")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PHAS, "${PHAS}")

    field(INP,  "@TopCon.proto ${proto}($$(DEVICE):${pv})  $$(PORT)")
}
''')

mbbi = Template('''
record(mbbi, "$$(DEVICE):${pv}") {
    field(PINI, "${PINI}")
    field(SCAN, "${SCAN}")
    field(PHAS, "${PHAS}")
    field(DESC, "${DESC}")

    field(ZRST, "${ZRST}")
    field(ONST, "${ONST}")
    field(TWST, "${TWST}")
    field(THST, "${THST}")
    field(FRST, "${FRST}")
    field(FVST, "${FVST}")
    field(SXST, "${SXST}")
    field(SVST, "${SVST}")
    field(EIST, "${EIST}")
    field(NIST, "${NIST}")
    field(TEST, "${TEST}")
    field(ELST, "${ELST}")
    field(TVST, "${TVST}")
    field(TTST, "${TTST}")
    field(FTST, "${FTST}")
    field(FFST, "${FFST}")

    field(ZRSV, "${ZRSV}")
    field(ONSV, "${ONSV}")
    field(TWSV, "${TWSV}")
    field(THSV, "${THSV}")
    field(FRSV, "${FRSV}")
    field(FVSV, "${FVSV}")
    field(SXSV, "${SXSV}")
    field(SVSV, "${SVSV}")
    field(EISV, "${EISV}")
    field(NISV, "${NISV}")
    field(TESV, "${TESV}")
    field(ELSV, "${ELSV}")
    field(TVSV, "${TVSV}")
    field(TTSV, "${TTSV}")
    field(FTSV, "${FTSV}")
    field(FFSV, "${FFSV}")

    field(DTYP, "stream")
    field(INP,  "@TopCon.proto ${proto}($$(DEVICE):${pv}) $$(PORT)")
}
''')
