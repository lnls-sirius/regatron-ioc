#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD06
drvAsynIPPortConfigure("P6","unix:///var/tmp/REG06")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-3B,P=P6")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
