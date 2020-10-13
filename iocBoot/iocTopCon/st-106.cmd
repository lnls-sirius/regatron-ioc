#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")
epicsEnvSet("D", "PA-RaPSD01:PS-DCLink-3B")
epicsEnvSet("P", "P106")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("$(TOP)/db/Security.as")

drvAsynIPPortConfigure("$(P)","$(REGATRON_INTERFACE_MS_HOST):20106")

dbLoadRecords("db/GenericCmd.db",    "D=$(D),P=$(P)")
dbLoadRecords("db/GenericGetSet.db", "D=$(D),P=$(P)")
dbLoadRecords("db/GenericMon.db",    "D=$(D),P=$(P)")
dbLoadRecords("db/TempMon.db",       "D=$(D),P=$(P)")
dbLoadRecords("db/ModMon.db",        "D=$(D),P=$(P)")
dbLoadRecords("db/ModTree.db",       "D=$(D),P=$(P)")


cd "$(TOP)/iocBoot/$(IOC)"
iocInit
iocLogInit

<PropertiesBase

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
