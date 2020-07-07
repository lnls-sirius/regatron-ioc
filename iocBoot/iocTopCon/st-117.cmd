#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P117","x.x.x.x:{COM}")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P117")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
