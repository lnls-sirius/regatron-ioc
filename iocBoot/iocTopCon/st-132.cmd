#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P132","10.128.123.20:20132")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P132")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
