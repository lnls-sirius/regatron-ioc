#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/db/Security.as")

drvAsynIPPortConfigure("P112","$(REGATRON_INTERFACE_MS_HOST):20112")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-2B,P=P112")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-2B,P=P112")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-2B,P=P112")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-2B,P=P112")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-2B,P=P112")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-2B,P=P112")

cd "${TOP}/iocBoot/${IOC}"
iocInit
iocLogInit

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
