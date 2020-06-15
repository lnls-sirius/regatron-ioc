#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD01
drvAsynIPPortConfigure("P1","unix:///var/tmp/REG01")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
