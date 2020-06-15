#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD29
drvAsynIPPortConfigure("P29","unix:///var/tmp/REG29")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
