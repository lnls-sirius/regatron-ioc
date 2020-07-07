#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P125","x.x.x.x:{COM}")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q24B,P=P125")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q24B,P=P125")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q24B,P=P125")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q24B,P=P125")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24B,P=P125")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24B,P=P125")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
