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

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:PS-DCLink-QFAP,PORT=P17")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:PS-DCLink-QFB,PORT=P18")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA03:PS-DCLink-QDAP,PORT=P19")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA04:PS-DCLink-QDB,PORT=P20")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12A,PORT=P21")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12B,PORT=P22")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12C,PORT=P23")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34A,PORT=P24")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34B,PORT=P25")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34C,PORT=P26")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:PS-DCLink-QFAP,PORT=P17")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:PS-DCLink-QFB,PORT=P18")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA03:PS-DCLink-QDAP,PORT=P19")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA04:PS-DCLink-QDB,PORT=P20")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA06:PS-DCLink-Q12A,PORT=P21")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA07:PS-DCLink-Q34A,PORT=P24")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:PS-DCLink-QFAP,R=,PORT=P17,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:PS-DCLink-QFB,R=,PORT=P18,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA03:PS-DCLink-QDAP,R=,PORT=P19,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA04:PS-DCLink-QDB,R=,PORT=P20,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12A,R=,PORT=P21,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12B,R=,PORT=P22,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12C,R=,PORT=P23,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34A,R=,PORT=P24,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34B,R=,PORT=P25,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34C,R=,PORT=P26,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
