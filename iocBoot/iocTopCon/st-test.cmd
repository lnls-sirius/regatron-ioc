#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P0","x.x.x.x:20000")

dbLoadRecords("db/GenericCmd.db",    "D=RegTest,P=P0")
dbLoadRecords("db/GenericGetSet.db", "D=RegTest,P=P0")
dbLoadRecords("db/GenericMon.db",    "D=RegTest,P=P0")
dbLoadRecords("db/TempMon.db",       "D=RegTest,P=P0")
dbLoadRecords("db/ModMon.db",        "D=RegTest,P=P0")
dbLoadRecords("db/ModTree.db",       "D=RegTest,P=P0")

dbLoadRecords("db/SysCmd.db",        "D=RegTest,P=P0")
dbLoadRecords("db/SysGetSet.db",     "D=RegTest,P=P0")
dbLoadRecords("db/SysMon.db",        "D=RegTest,P=P0")
dbLoadRecords("db/SysTree.db",       "D=RegTest,P=P0")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
