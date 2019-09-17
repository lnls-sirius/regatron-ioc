#!../../bin/linux-x86_64/TopCon

## You may have to change TopCon to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure("P27", "/dev/tty_dgrp_27_0")
asynSetOption("P27", 0, "baud", "38400")
asynSetOption("P27", 0, "bits", "8")
asynSetOption("P27", 0, "parity", "none")
asynSetOption("P27", 0, "stop", "1")

drvAsynSerialPortConfigure("P28", "/dev/tty_dgrp_28_0")
asynSetOption("P28", 0, "baud", "38400")
asynSetOption("P28", 0, "bits", "8")
asynSetOption("P28", 0, "parity", "none")
asynSetOption("P28", 0, "stop", "1")

drvAsynSerialPortConfigure("P29", "/dev/tty_dgrp_29_0")
asynSetOption("P29", 0, "baud", "38400")
asynSetOption("P29", 0, "bits", "8")
asynSetOption("P29", 0, "parity", "none")
asynSetOption("P29", 0, "stop", "1")

drvAsynSerialPortConfigure("P30", "/dev/tty_dgrp_30_0")
asynSetOption("P30", 0, "baud", "38400")
asynSetOption("P30", 0, "bits", "8")
asynSetOption("P30", 0, "parity", "none")
asynSetOption("P30", 0, "stop", "1")

drvAsynSerialPortConfigure("P31", "/dev/tty_dgrp_31_0")
asynSetOption("P31", 0, "baud", "38400")
asynSetOption("P31", 0, "bits", "8")
asynSetOption("P31", 0, "parity", "none")
asynSetOption("P31", 0, "stop", "1")

drvAsynSerialPortConfigure("P32", "/dev/tty_dgrp_32_0")
asynSetOption("P32", 0, "baud", "38400")
asynSetOption("P32", 0, "bits", "8")
asynSetOption("P32", 0, "parity", "none")
asynSetOption("P32", 0, "stop", "1")

drvAsynSerialPortConfigure("P33", "/dev/tty_dgrp_33_0")
asynSetOption("P33", 0, "baud", "38400")
asynSetOption("P33", 0, "bits", "8")
asynSetOption("P33", 0, "parity", "none")
asynSetOption("P33", 0, "stop", "1")

drvAsynSerialPortConfigure("P34", "/dev/tty_dgrp_34_0")
asynSetOption("P34", 0, "baud", "38400")
asynSetOption("P34", 0, "bits", "8")
asynSetOption("P34", 0, "parity", "none")
asynSetOption("P34", 0, "stop", "1")

drvAsynSerialPortConfigure("P35", "/dev/tty_dgrp_35_0")
asynSetOption("P35", 0, "baud", "38400")
asynSetOption("P35", 0, "bits", "8")
asynSetOption("P35", 0, "parity", "none")
asynSetOption("P35", 0, "stop", "1")

drvAsynSerialPortConfigure("P36", "/dev/tty_dgrp_36_0")
asynSetOption("P36", 0, "baud", "38400")
asynSetOption("P36", 0, "bits", "8")
asynSetOption("P36", 0, "parity", "none")
asynSetOption("P36", 0, "stop", "1")

drvAsynSerialPortConfigure("P37", "/dev/tty_dgrp_37_0")
asynSetOption("P37", 0, "baud", "38400")
asynSetOption("P37", 0, "bits", "8")
asynSetOption("P37", 0, "parity", "none")
asynSetOption("P37", 0, "stop", "1")

drvAsynSerialPortConfigure("P38", "/dev/tty_dgrp_38_0")
asynSetOption("P38", 0, "baud", "38400")
asynSetOption("P38", 0, "bits", "8")
asynSetOption("P38", 0, "parity", "none")
asynSetOption("P38", 0, "stop", "1")

drvAsynSerialPortConfigure("P39", "/dev/tty_dgrp_39_0")
asynSetOption("P39", 0, "baud", "38400")
asynSetOption("P39", 0, "bits", "8")
asynSetOption("P39", 0, "parity", "none")
asynSetOption("P39", 0, "stop", "1")

drvAsynSerialPortConfigure("P40", "/dev/tty_dgrp_40_0")
asynSetOption("P40", 0, "baud", "38400")
asynSetOption("P40", 0, "bits", "8")
asynSetOption("P40", 0, "parity", "none")
asynSetOption("P40", 0, "stop", "1")

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB01:PS-DCLink-SDB0,PORT=P27")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB04:PS-DCLink-SDB1,PORT=P28")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB05:PS-DCLink-SDB2,PORT=P29")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB07:PS-DCLink-SDB3,PORT=P30")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB03:PS-DCLink-SFB0,PORT=P31")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB08:PS-DCLink-SFB1,PORT=P32")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB10:PS-DCLink-SFB2,PORT=P33")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB04:SI-DCLink-SDA12,PORT=P34")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB01:SI-DCLink-SDAP0,PORT=P35")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB03:SI-DCLink-SFAP0,PORT=P36")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB10:SI-DCLink-SFP12,PORT=P37")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB08:SI-DCLink-SDP23,PORT=P38")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB05:SI-DCLink-SDA3SFA1,PORT=P39")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSB07:SI-DCLink-SFA2SDP1,PORT=P40")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB01:PS-DCLink-SDB0,PORT=P27")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB04:PS-DCLink-SDB1,PORT=P28")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB05:PS-DCLink-SDB2,PORT=P29")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB07:PS-DCLink-SDB3,PORT=P30")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB03:PS-DCLink-SFB0,PORT=P31")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB08:PS-DCLink-SFB1,PORT=P32")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB10:PS-DCLink-SFB2,PORT=P33")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB04:SI-DCLink-SDA12,PORT=P34")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB01:SI-DCLink-SDAP0,PORT=P35")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB03:SI-DCLink-SFAP0,PORT=P36")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB10:SI-DCLink-SFP12,PORT=P37")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB08:SI-DCLink-SDP23,PORT=P38")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB05:SI-DCLink-SDA3SFA1,PORT=P39")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSB07:SI-DCLink-SFA2SDP1,PORT=P40")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB01:PS-DCLink-SDB0,R=,PORT=P27,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB04:PS-DCLink-SDB1,R=,PORT=P28,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB05:PS-DCLink-SDB2,R=,PORT=P29,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB07:PS-DCLink-SDB3,R=,PORT=P30,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB03:PS-DCLink-SFB0,R=,PORT=P31,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB08:PS-DCLink-SFB1,R=,PORT=P32,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB10:PS-DCLink-SFB2,R=,PORT=P33,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB04:SI-DCLink-SDA12,R=,PORT=P34,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB01:SI-DCLink-SDAP0,R=,PORT=P35,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB03:SI-DCLink-SFAP0,R=,PORT=P36,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB10:SI-DCLink-SFP12,R=,PORT=P37,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB08:SI-DCLink-SDP23,R=,PORT=P38,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB05:SI-DCLink-SDA3SFA1,R=,PORT=P39,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSB07:SI-DCLink-SFA2SDP1,R=,PORT=P40,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
