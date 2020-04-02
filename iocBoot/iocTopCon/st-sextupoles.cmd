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

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB01:PS-DCLink-SDB0,PORT=P27")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB04:PS-DCLink-SDB1,PORT=P28")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB05:PS-DCLink-SDB2,PORT=P29")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB07:PS-DCLink-SDB3,PORT=P30")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB03:PS-DCLink-SFB0,PORT=P31")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB08:PS-DCLink-SFB1,PORT=P32")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB10:PS-DCLink-SFB2,PORT=P33")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB04:PS-DCLink-SDA12,PORT=P34")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB01:PS-DCLink-SDAP0,PORT=P35")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB03:PS-DCLink-SFAP0,PORT=P36")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB10:PS-DCLink-SFP12,PORT=P37")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB08:PS-DCLink-SDP23,PORT=P38")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB05:PS-DCLink-SDA3SFA1,PORT=P39")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB07:PS-DCLink-SFA2SDP1,PORT=P40")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB01:PS-DCLink-SDB0,PORT=P27")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB04:PS-DCLink-SDB1,PORT=P28")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB05:PS-DCLink-SDB2,PORT=P29")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB07:PS-DCLink-SDB3,PORT=P30")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB03:PS-DCLink-SFB0,PORT=P31")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB08:PS-DCLink-SFB1,PORT=P32")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB10:PS-DCLink-SFB2,PORT=P33")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB04:PS-DCLink-SDA12,PORT=P34")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB01:PS-DCLink-SDAP0,PORT=P35")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB03:PS-DCLink-SFAP0,PORT=P36")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB10:PS-DCLink-SFP12,PORT=P37")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB08:PS-DCLink-SDP23,PORT=P38")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB05:PS-DCLink-SDA3SFA1,PORT=P39")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB07:PS-DCLink-SFA2SDP1,PORT=P40")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB01:PS-DCLink-SDB0,R=,PORT=P27,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB04:PS-DCLink-SDB1,R=,PORT=P28,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB05:PS-DCLink-SDB2,R=,PORT=P29,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB07:PS-DCLink-SDB3,R=,PORT=P30,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB03:PS-DCLink-SFB0,R=,PORT=P31,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB08:PS-DCLink-SFB1,R=,PORT=P32,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB10:PS-DCLink-SFB2,R=,PORT=P33,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB04:PS-DCLink-SDA12,R=,PORT=P34,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB01:PS-DCLink-SDAP0,R=,PORT=P35,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB03:PS-DCLink-SFAP0,R=,PORT=P36,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB10:PS-DCLink-SFP12,R=,PORT=P37,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB08:PS-DCLink-SDP23,R=,PORT=P38,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB05:PS-DCLink-SDA3SFA1,R=,PORT=P39,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB07:PS-DCLink-SFA2SDP1,R=,PORT=P40,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
