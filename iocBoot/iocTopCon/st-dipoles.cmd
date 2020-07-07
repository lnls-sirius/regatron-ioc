#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P1","x.x.x.x:20001")

drvAsynIPPortConfigure("P2","x.x.x.x:20002")

drvAsynIPPortConfigure("P3","x.x.x.x:20003")

drvAsynIPPortConfigure("P4","x.x.x.x:20004")

drvAsynIPPortConfigure("P5","x.x.x.x:20005")

drvAsynIPPortConfigure("P6","x.x.x.x:20006")

drvAsynIPPortConfigure("P7","x.x.x.x:20007")

drvAsynIPPortConfigure("P8","x.x.x.x:20008")

drvAsynIPPortConfigure("P9","x.x.x.x:20009")

drvAsynIPPortConfigure("P10","x.x.x.x:20010")

drvAsynIPPortConfigure("P11","x.x.x.x:20011")

drvAsynIPPortConfigure("P12","x.x.x.x:20012")

drvAsynIPPortConfigure("P13","x.x.x.x:20013")

drvAsynIPPortConfigure("P14","x.x.x.x:20014")

drvAsynIPPortConfigure("P15","x.x.x.x:20015")

drvAsynIPPortConfigure("P16","x.x.x.x:20016")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-1B,P=P2")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-1B,P=P2")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-2A,P=P3")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-2B,P=P4")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-2B,P=P4")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD01:PS-DCLink-3B,P=P6")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD01:PS-DCLink-3B,P=P6")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD03:PS-DCLink-4B,P=P8")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD03:PS-DCLink-4B,P=P8")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-1B,P=P10")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-1B,P=P10")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-2A,P=P11")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-2B,P=P12")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-2B,P=P12")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P13")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD05:PS-DCLink-3B,P=P14")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD05:PS-DCLink-3B,P=P14")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-4A,P=P15")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSD07:PS-DCLink-4B,P=P16")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSD07:PS-DCLink-4B,P=P16")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD01:PS-DCLink-1A,P=P1")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD01:PS-DCLink-1A,P=P1")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD03:PS-DCLink-2A,P=P3")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD03:PS-DCLink-2A,P=P3")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD01:PS-DCLink-3A,P=P5")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD01:PS-DCLink-3A,P=P5")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD03:PS-DCLink-4A,P=P7")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD03:PS-DCLink-4A,P=P7")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD05:PS-DCLink-1A,P=P9")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD05:PS-DCLink-1A,P=P9")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD07:PS-DCLink-2A,P=P11")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD07:PS-DCLink-2A,P=P11")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD05:PS-DCLink-3A,P=P13")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD05:PS-DCLink-3A,P=P13")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSD07:PS-DCLink-4A,P=P15")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSD07:PS-DCLink-4A,P=P15")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
