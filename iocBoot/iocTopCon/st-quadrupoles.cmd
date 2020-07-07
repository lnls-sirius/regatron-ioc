#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P17","x.x.x.x:20017")

drvAsynIPPortConfigure("P18","x.x.x.x:20018")

drvAsynIPPortConfigure("P19","x.x.x.x:20019")

drvAsynIPPortConfigure("P20","x.x.x.x:20020")

drvAsynIPPortConfigure("P21","x.x.x.x:20021")

drvAsynIPPortConfigure("P22","x.x.x.x:20022")

drvAsynIPPortConfigure("P23","x.x.x.x:20023")

drvAsynIPPortConfigure("P24","x.x.x.x:20024")

drvAsynIPPortConfigure("P25","x.x.x.x:20025")

drvAsynIPPortConfigure("P26","x.x.x.x:20026")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA06:PS-DCLink-Q13B,P=P22")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA06:PS-DCLink-Q13B,P=P22")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA06:PS-DCLink-Q13B,P=P22")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA06:PS-DCLink-Q13B,P=P22")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA06:PS-DCLink-Q13B,P=P22")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA06:PS-DCLink-Q13B,P=P22")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA06:PS-DCLink-Q13C,P=P23")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA06:PS-DCLink-Q13C,P=P23")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA06:PS-DCLink-Q13C,P=P23")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA06:PS-DCLink-Q13C,P=P23")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA06:PS-DCLink-Q13C,P=P23")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA06:PS-DCLink-Q13C,P=P23")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q24B,P=P25")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q24B,P=P25")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q24B,P=P25")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q24B,P=P25")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24B,P=P25")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24B,P=P25")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSA07:PS-DCLink-Q24C,P=P26")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSA07:PS-DCLink-Q24C,P=P26")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSA07:PS-DCLink-Q24C,P=P26")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSA07:PS-DCLink-Q24C,P=P26")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24C,P=P26")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24C,P=P26")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA01:PS-DCLink-QFAP,P=P17")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA01:PS-DCLink-QFB,P=P18")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA03:PS-DCLink-QDAP,P=P19")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA04:PS-DCLink-QDB,P=P20")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA06:PS-DCLink-Q13A,P=P21")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSA07:PS-DCLink-Q24A,P=P24")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
