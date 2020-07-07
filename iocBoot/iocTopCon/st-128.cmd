#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P128","10.128.123.20:20128")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P128")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
