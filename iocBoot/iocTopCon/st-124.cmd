#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/db/Security.as")

drvAsynIPPortConfigure("P124","$(REGATRON_INTERFACE_MS_HOST):20124")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24A,P=P124")

cd "${TOP}/iocBoot/${IOC}"
iocInit
iocLogInit

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
