#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P108","10.128.255.206:20108")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-4B,P=P108")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-4B,P=P108")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-4B,P=P108")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-4B,P=P108")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-4B,P=P108")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-4B,P=P108")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
