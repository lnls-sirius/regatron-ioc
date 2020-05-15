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

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-1B,P=P2")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-2A,P=P3")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-2B,P=P4")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-3B,P=P6")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-4B,P=P8")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P10")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-2A,P=P11")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-2B,P=P12")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P13")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-3B,P=P14")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-4A,P=P15")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-4B,P=P16")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD03:PS-DCLink-2A,P=P3")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD07:PS-DCLink-2A,P=P11")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P13")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD07:PS-DCLink-4A,P=P15")

dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-1A,R=,P=P1,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-1B,R=,P=P2,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-2A,R=,P=P3,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-2B,R=,P=P4,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-3A,R=,P=P5,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD01:PS-DCLink-3B,R=,P=P6,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-4A,R=,P=P7,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD03:PS-DCLink-4B,R=,P=P8,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-1A,R=,P=P9,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-1B,R=,P=P10,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-2A,R=,P=P11,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-2B,R=,P=P12,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-3A,R=,P=P13,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD05:PS-DCLink-3B,R=,P=P14,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-4A,R=,P=P15,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSD07:PS-DCLink-4B,R=,P=P16,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
