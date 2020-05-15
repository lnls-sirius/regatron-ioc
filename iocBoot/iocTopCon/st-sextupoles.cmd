#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

# DIGI Real Port -> /dev/ttyD27
drvAsynIPPortConfigure("P27","unix:///var/tmp/REGD27")

# DIGI Real Port -> /dev/ttyD28
drvAsynIPPortConfigure("P28","unix:///var/tmp/REGD28")

# DIGI Real Port -> /dev/ttyD29
drvAsynIPPortConfigure("P29","unix:///var/tmp/REGD29")

# DIGI Real Port -> /dev/ttyD30
drvAsynIPPortConfigure("P30","unix:///var/tmp/REGD30")

# DIGI Real Port -> /dev/ttyD31
drvAsynIPPortConfigure("P31","unix:///var/tmp/REGD31")

# DIGI Real Port -> /dev/ttyD32
drvAsynIPPortConfigure("P32","unix:///var/tmp/REGD32")

# DIGI Real Port -> /dev/ttyD33
drvAsynIPPortConfigure("P33","unix:///var/tmp/REGD33")

# DIGI Real Port -> /dev/ttyD34
drvAsynIPPortConfigure("P34","unix:///var/tmp/REGD34")

# DIGI Real Port -> /dev/ttyD35
drvAsynIPPortConfigure("P35","unix:///var/tmp/REGD35")

# DIGI Real Port -> /dev/ttyD36
drvAsynIPPortConfigure("P36","unix:///var/tmp/REGD36")

# DIGI Real Port -> /dev/ttyD37
drvAsynIPPortConfigure("P37","unix:///var/tmp/REGD37")

# DIGI Real Port -> /dev/ttyD38
drvAsynIPPortConfigure("P38","unix:///var/tmp/REGD38")

# DIGI Real Port -> /dev/ttyD39
drvAsynIPPortConfigure("P39","unix:///var/tmp/REGD39")

# DIGI Real Port -> /dev/ttyD40
drvAsynIPPortConfigure("P40","unix:///var/tmp/REGD40")

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

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB01:PS-DCLink-SDB0,P=P27")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB04:PS-DCLink-SDB1,P=P28")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB05:PS-DCLink-SDB2,P=P29")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB07:PS-DCLink-SDB3,P=P30")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB03:PS-DCLink-SFB0,P=P31")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB08:PS-DCLink-SFB1,P=P32")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB10:PS-DCLink-SFB2,P=P33")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB04:PS-DCLink-SDA12,P=P34")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB01:PS-DCLink-SDAP0,P=P35")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB03:PS-DCLink-SFAP0,P=P36")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB10:PS-DCLink-SFP12,P=P37")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB08:PS-DCLink-SDP23,P=P38")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB05:PS-DCLink-SDA3SFA1,P=P39")

dbLoadRecords("db/SysMon.db",        "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")
dbLoadRecords("db/SysTree.db",       "D=PA-RaPSB07:PS-DCLink-SFA2SDP1,P=P40")

dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB01:PS-DCLink-SDB0,R=,P=P27,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB04:PS-DCLink-SDB1,R=,P=P28,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB05:PS-DCLink-SDB2,R=,P=P29,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB07:PS-DCLink-SDB3,R=,P=P30,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB03:PS-DCLink-SFB0,R=,P=P31,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB08:PS-DCLink-SFB1,R=,P=P32,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB10:PS-DCLink-SFB2,R=,P=P33,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB04:PS-DCLink-SDA12,R=,P=P34,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB01:PS-DCLink-SDAP0,R=,P=P35,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB03:PS-DCLink-SFAP0,R=,P=P36,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB10:PS-DCLink-SFP12,R=,P=P37,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB08:PS-DCLink-SDP23,R=,P=P38,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB05:PS-DCLink-SDA3SFA1,R=,P=P39,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB07:PS-DCLink-SFA2SDP1,R=,P=P40,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
