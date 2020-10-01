#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/db/Security.as")

drvAsynIPPortConfigure("P110","$(REGATRON_INTERFACE_MS_HOST):20110")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P110")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1B,P=P110")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P110")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P110")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1B,P=P110")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P110")


cd "${TOP}/iocBoot/${IOC}"
iocInit
iocLogInit

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
