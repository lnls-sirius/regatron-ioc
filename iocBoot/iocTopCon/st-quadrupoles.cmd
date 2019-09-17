#!../../bin/linux-x86_64/TopCon

## You may have to change TopCon to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure("P1", "/dev/tty_dgrp_1_0")
asynSetOption("P1", 0, "baud", "38400")
asynSetOption("P1", 0, "bits", "8")
asynSetOption("P1", 0, "parity", "none")
asynSetOption("P1", 0, "stop", "1")

drvAsynSerialPortConfigure("P2", "/dev/tty_dgrp_2_0")
asynSetOption("P2", 0, "baud", "38400")
asynSetOption("P2", 0, "bits", "8")
asynSetOption("P2", 0, "parity", "none")
asynSetOption("P2", 0, "stop", "1")

drvAsynSerialPortConfigure("P3", "/dev/tty_dgrp_3_0")
asynSetOption("P3", 0, "baud", "38400")
asynSetOption("P3", 0, "bits", "8")
asynSetOption("P3", 0, "parity", "none")
asynSetOption("P3", 0, "stop", "1")

drvAsynSerialPortConfigure("P4", "/dev/tty_dgrp_4_0")
asynSetOption("P4", 0, "baud", "38400")
asynSetOption("P4", 0, "bits", "8")
asynSetOption("P4", 0, "parity", "none")
asynSetOption("P4", 0, "stop", "1")

drvAsynSerialPortConfigure("P5", "/dev/tty_dgrp_5_0")
asynSetOption("P5", 0, "baud", "38400")
asynSetOption("P5", 0, "bits", "8")
asynSetOption("P5", 0, "parity", "none")
asynSetOption("P5", 0, "stop", "1")

drvAsynSerialPortConfigure("P6", "/dev/tty_dgrp_6_0")
asynSetOption("P6", 0, "baud", "38400")
asynSetOption("P6", 0, "bits", "8")
asynSetOption("P6", 0, "parity", "none")
asynSetOption("P6", 0, "stop", "1")

drvAsynSerialPortConfigure("P7", "/dev/tty_dgrp_7_0")
asynSetOption("P7", 0, "baud", "38400")
asynSetOption("P7", 0, "bits", "8")
asynSetOption("P7", 0, "parity", "none")
asynSetOption("P7", 0, "stop", "1")

drvAsynSerialPortConfigure("P8", "/dev/tty_dgrp_8_0")
asynSetOption("P8", 0, "baud", "38400")
asynSetOption("P8", 0, "bits", "8")
asynSetOption("P8", 0, "parity", "none")
asynSetOption("P8", 0, "stop", "1")

drvAsynSerialPortConfigure("P9", "/dev/tty_dgrp_9_0")
asynSetOption("P9", 0, "baud", "38400")
asynSetOption("P9", 0, "bits", "8")
asynSetOption("P9", 0, "parity", "none")
asynSetOption("P9", 0, "stop", "1")

drvAsynSerialPortConfigure("P10", "/dev/tty_dgrp_10_0")
asynSetOption("P10", 0, "baud", "38400")
asynSetOption("P10", 0, "bits", "8")
asynSetOption("P10", 0, "parity", "none")
asynSetOption("P10", 0, "stop", "1")

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:PS-DCLink-QFAP, PORT=P1")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:PS-DCLink-QFB, PORT=P2")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA03:PS-DCLink-QDAP12, PORT=P3")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA04:PS-DCLink-QDB, PORT=P4")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12AA, PORT=P5")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12BB, PORT=P6")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12CC, PORT=P7")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34A, PORT=P8")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34B, PORT=P9")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34C, PORT=P10")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:PS-DCLink-QFAP, PORT=P1")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:PS-DCLink-QFB, PORT=P2")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA03:PS-DCLink-QDAP12, PORT=P3")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA04:PS-DCLink-QDB, PORT=P4")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA06:PS-DCLink-Q12AA, PORT=P5")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA07:PS-DCLink-Q34A, PORT=P8")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:PS-DCLink-QFAP,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:PS-DCLink-QFB,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA03:PS-DCLink-QDAP12,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA04:PS-DCLink-QDB,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12AA,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12BB,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12CC,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34C,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
