#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P113","x.x.x.x:20113")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P113")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P113")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P113")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
