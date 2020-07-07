#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynIPPortConfigure("P27","x.x.x.x:20027")

drvAsynIPPortConfigure("P28","x.x.x.x:20028")

drvAsynIPPortConfigure("P29","x.x.x.x:20029")

drvAsynIPPortConfigure("P30","x.x.x.x:20030")

drvAsynIPPortConfigure("P31","x.x.x.x:20031")

drvAsynIPPortConfigure("P32","x.x.x.x:20032")

drvAsynIPPortConfigure("P33","x.x.x.x:20033")

drvAsynIPPortConfigure("P34","x.x.x.x:20034")

drvAsynIPPortConfigure("P35","x.x.x.x:20035")

drvAsynIPPortConfigure("P36","x.x.x.x:20036")

drvAsynIPPortConfigure("P37","x.x.x.x:20037")

drvAsynIPPortConfigure("P38","x.x.x.x:20038")

drvAsynIPPortConfigure("P39","x.x.x.x:20039")

drvAsynIPPortConfigure("P40","x.x.x.x:20040")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")

dbLoadRecords("db/GenericCmd.db",    "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/GenericGetSet.db", "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/GenericMon.db",    "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/TempMon.db",       "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/ModMon.db",        "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/ModTree.db",       "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")

dbLoadRecords("db/SysCmd.db",        "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/SysGetSet.db",     "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")

cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
