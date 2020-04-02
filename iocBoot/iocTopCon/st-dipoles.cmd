#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD01
drvAsynIPPortConfigure("P1","unix:///var/tmp/REGD01")

# DIGI Real Port -> /dev/ttyD02
drvAsynIPPortConfigure("P2","unix:///var/tmp/REGD02")

# DIGI Real Port -> /dev/ttyD03
drvAsynIPPortConfigure("P3","unix:///var/tmp/REGD03")

# DIGI Real Port -> /dev/ttyD04
drvAsynIPPortConfigure("P4","unix:///var/tmp/REGD04")

# DIGI Real Port -> /dev/ttyD05
drvAsynIPPortConfigure("P5","unix:///var/tmp/REGD05")

# DIGI Real Port -> /dev/ttyD06
drvAsynIPPortConfigure("P6","unix:///var/tmp/REGD06")

# DIGI Real Port -> /dev/ttyD07
drvAsynIPPortConfigure("P7","unix:///var/tmp/REGD07")

# DIGI Real Port -> /dev/ttyD08
drvAsynIPPortConfigure("P8","unix:///var/tmp/REGD08")

# DIGI Real Port -> /dev/ttyD09
drvAsynIPPortConfigure("P9","unix:///var/tmp/REGD09")

# DIGI Real Port -> /dev/ttyD10
drvAsynIPPortConfigure("P10","unix:///var/tmp/REGD10")

# DIGI Real Port -> /dev/ttyD11
drvAsynIPPortConfigure("P11","unix:///var/tmp/REGD11")

# DIGI Real Port -> /dev/ttyD12
drvAsynIPPortConfigure("P12","unix:///var/tmp/REGD12")

# DIGI Real Port -> /dev/ttyD13
drvAsynIPPortConfigure("P13","unix:///var/tmp/REGD13")

# DIGI Real Port -> /dev/ttyD14
drvAsynIPPortConfigure("P14","unix:///var/tmp/REGD14")

# DIGI Real Port -> /dev/ttyD15
drvAsynIPPortConfigure("P15","unix:///var/tmp/REGD15")

# DIGI Real Port -> /dev/ttyD16
drvAsynIPPortConfigure("P16","unix:///var/tmp/REGD16")

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD01:PS-DCLink-1A,PORT=P1")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD01:PS-DCLink-1B,PORT=P2")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD03:PS-DCLink-2A,PORT=P3")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD03:PS-DCLink-2B,PORT=P4")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD01:PS-DCLink-3A,PORT=P5")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD01:PS-DCLink-3B,PORT=P6")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD03:PS-DCLink-4A,PORT=P7")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD03:PS-DCLink-4B,PORT=P8")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD05:PS-DCLink-1A,PORT=P9")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD05:PS-DCLink-1B,PORT=P10")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD07:PS-DCLink-2A,PORT=P11")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD07:PS-DCLink-2B,PORT=P12")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD05:PS-DCLink-3A,PORT=P13")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD05:PS-DCLink-3B,PORT=P14")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD07:PS-DCLink-4A,PORT=P15")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSD07:PS-DCLink-4B,PORT=P16")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD01:PS-DCLink-1A,PORT=P1")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD03:PS-DCLink-2A,PORT=P3")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD01:PS-DCLink-3A,PORT=P5")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD03:PS-DCLink-4A,PORT=P7")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD05:PS-DCLink-1A,PORT=P9")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD07:PS-DCLink-2A,PORT=P11")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD05:PS-DCLink-3A,PORT=P13")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSD07:PS-DCLink-4A,PORT=P15")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-1A,R=,PORT=P1,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-1B,R=,PORT=P2,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-2A,R=,PORT=P3,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-2B,R=,PORT=P4,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-3A,R=,PORT=P5,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-3B,R=,PORT=P6,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-4A,R=,PORT=P7,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-4B,R=,PORT=P8,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-1A,R=,PORT=P9,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-1B,R=,PORT=P10,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-2A,R=,PORT=P11,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-2B,R=,PORT=P12,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-3A,R=,PORT=P13,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-3B,R=,PORT=P14,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-4A,R=,PORT=P15,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-4B,R=,PORT=P16,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
