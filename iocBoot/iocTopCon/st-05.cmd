#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD05
drvAsynIPPortConfigure("P5","unix:///var/tmp/REG05")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1