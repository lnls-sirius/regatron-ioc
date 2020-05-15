#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD17
drvAsynIPPortConfigure("P17","unix:///var/tmp/REGD17")

# DIGI Real Port -> /dev/ttyD18
drvAsynIPPortConfigure("P18","unix:///var/tmp/REGD18")

# DIGI Real Port -> /dev/ttyD19
drvAsynIPPortConfigure("P19","unix:///var/tmp/REGD19")

# DIGI Real Port -> /dev/ttyD20
drvAsynIPPortConfigure("P20","unix:///var/tmp/REGD20")

# DIGI Real Port -> /dev/ttyD21
drvAsynIPPortConfigure("P21","unix:///var/tmp/REGD21")

# DIGI Real Port -> /dev/ttyD22
drvAsynIPPortConfigure("P22","unix:///var/tmp/REGD22")

# DIGI Real Port -> /dev/ttyD23
drvAsynIPPortConfigure("P23","unix:///var/tmp/REGD23")

# DIGI Real Port -> /dev/ttyD24
drvAsynIPPortConfigure("P24","unix:///var/tmp/REGD24")

# DIGI Real Port -> /dev/ttyD25
drvAsynIPPortConfigure("P25","unix:///var/tmp/REGD25")

# DIGI Real Port -> /dev/ttyD26
drvAsynIPPortConfigure("P26","unix:///var/tmp/REGD26")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA06:PS-DCLink-Q12B,P=P22")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA06:PS-DCLink-Q12B,P=P22")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA06:PS-DCLink-Q12B,P=P22")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA06:PS-DCLink-Q12B,P=P22")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA06:PS-DCLink-Q12B,P=P22")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA06:PS-DCLink-Q12B,P=P22")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA06:PS-DCLink-Q12C,P=P23")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA06:PS-DCLink-Q12C,P=P23")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA06:PS-DCLink-Q12C,P=P23")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA06:PS-DCLink-Q12C,P=P23")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA06:PS-DCLink-Q12C,P=P23")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA06:PS-DCLink-Q12C,P=P23")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q34B,P=P25")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q34B,P=P25")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q34B,P=P25")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q34B,P=P25")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q34B,P=P25")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q34B,P=P25")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q34C,P=P26")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q34C,P=P26")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q34C,P=P26")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q34C,P=P26")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q34C,P=P26")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q34C,P=P26")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA06:PS-DCLink-Q12A,P=P21")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA07:PS-DCLink-Q34A,P=P24")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
