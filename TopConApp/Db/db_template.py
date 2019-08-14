#!/usr/bin/python3
from string import Template
select = '''
record(bo, "$(DEVICE):SelectMaster-Cmd"){
    field(DTYP, "stream")
    field(OUT,  "@TopCon.proto selectMaster($$(DEVICE):SelectMaster-Cmd) $(PORT)")
    field(DISS, "INVALID")
}
record(bo, "$(DEVICE):SelectSystem-Cmd"){
    field(DTYP, "stream")
    field(OUT,  "@TopCon.proto selectSystem($$(DEVICE):SelectSystem-Cmd) $(PORT)")
    field(DISS, "INVALID")
}
'''
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
record(longin, "$$(DEVICE):${pv}-RB_error"){
    field(DESC, "${DESC}")
    field(DTYP, "Soft Channel")
    field(PINI, "YES")
    field(PHAS, "0")
    field(VAL,  "0")
}
record(longin, "$$(DEVICE):${pv}-SP_error"){
    field(DESC, "${DESC}")
    field(DTYP, "Soft Channel")
    field(PINI, "YES")
    field(PHAS, "0")
    field(VAL,  "0")
}
record(ai, "$$(DEVICE):${pv}-RB"){
    field(PINI, "YES")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "0")
    field(LINR, "${LINR}")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")

    field(INP,  "@TopCon.proto get${proto}($$(DEVICE):${pv}-RB)  $$(PORT)")
}
record(ao, "$$(DEVICE):${pv}-SP"){
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(LINR, "${LINR}")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DRVL, "${DRVL}")
    field(DRVH, "${DRVH}")
    field(DISA, "${DISA}")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(OUT,  "@TopCon.proto set${proto}($$(DEVICE):${pv}-SP) $$(PORT)")
    field(FLNK, "$$(DEVICE):${pv}-RB")
}
record(seq, "$$(DEVICE):${pv}_init"){
    field(PINI, "YES")
    field(PHAS, "1")

    field(DOL1, "1")
    field(LNK1, "$$(DEVICE):${pv}-SP.DISA")

    field(DLY2, "10")
    field(DOL2, "$$(DEVICE):${pv}-RB")
    field(LNK2, "$$(DEVICE):${pv}-SP")

    field(DOL1, "0")
    field(LNK1, "$$(DEVICE):${pv}-SP.DISA")
}
''')
loop_analog_ref = Template('''
record(longin, "$$(DEVICE):${pv}-RB_error"){
    field(DESC, "${DESC}")
    field(DTYP, "Soft Channel")
    field(PINI, "YES")
    field(PHAS, "0")
    field(VAL,  "0")
}
record(longin, "$$(DEVICE):${pv}-SP_error"){
    field(DESC, "${DESC}")
    field(DTYP, "Soft Channel")
    field(PINI, "YES")
    field(PHAS, "0")
    field(VAL,  "0")
}
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
record(ao, "$$(DEVICE):${pv}-SP_${HL}"){
    field(DTYP, "Soft Channel")
    field(OMSL, "closed_loop")
    field(DOL,  "$$(DEVICE):${ref}")
    field(OUT,  "$$(DEVICE):${pv}-SP.DRV${HL}")
}
record(ai, "$$(DEVICE):${pv}-RB"){
    field(PINI, "YES")
    field(SCAN, "${SCAN}")
    field(DESC, "${DESC}")
    field(DTYP, "stream")
    field(EGU,  "${EGU}")
    field(PREC, "${PREC}")
    field(PHAS, "1")
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
    field(LINR, "LINEAR")
    field(EOFF, "${EOFF}")
    field(ESLO, "${ESLO}")
    field(DISA, "1")
    field(DISV, "1")
    field(DISS, "INVALID")
    field(OUT,  "@TopCon.proto set${proto}($$(DEVICE):${pv}-SP)  $$(PORT)")
    field(FLNK, "$$(DEVICE):${pv}-RB")
}
''')
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
