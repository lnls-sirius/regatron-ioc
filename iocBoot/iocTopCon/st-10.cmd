#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD10
drvAsynIPPortConfigure("P10","unix:///var/tmp/REG10")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P10")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
