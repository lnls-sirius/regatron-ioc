#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")
epicsEnvSet("D", "PA-RaPSD01:PS-DCLink-1A")
epicsEnvSet("P", "P101")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("$(TOP)/db/Security.as")

drvAsynIPPortConfigure("$(P)","$(REGATRON_INTERFACE_MS_HOST):20101")

dbLoadRecords("db/GenericCmd.db",    "D=$(D),P=$(P)")
dbLoadRecords("db/GenericGetSet.db", "D=$(D),P=$(P)")
dbLoadRecords("db/GenericMon.db",    "D=$(D),P=$(P)")
dbLoadRecords("db/TempMon.db",       "D=$(D),P=$(P)")
dbLoadRecords("db/ModMon.db",        "D=$(D),P=$(P)")
dbLoadRecords("db/ModTree.db",       "D=$(D),P=$(P)")


dbLoadRecords("db/SysCmd.db",           "D=$(D),P=$(P)")
dbLoadRecords("db/SysGetSet.db",        "D=$(D),P=$(P)")
dbLoadRecords("db/SysMon.db",           "D=$(D),P=$(P)")
dbLoadRecords("db/SysTree.db",          "D=$(D),P=$(P)")
dbLoadRecords("db/SysCustomNamming.db", "D=$(D),P=$(P)")

cd "$(TOP)/iocBoot/$(IOC)"
iocInit
iocLogInit

< PropertiesMaster

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
