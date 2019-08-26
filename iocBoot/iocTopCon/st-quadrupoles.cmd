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

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:SI-Reg:PS-QFAP, PORT=P1")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:SI-Reg:PS-QFB, PORT=P2")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA03:SI-Reg:PS-QDAP12, PORT=P3")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA04:SI-Reg:PS-QDB12, PORT=P4")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:SI-Reg:PS-Q12_A, PORT=P5")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:SI-Reg:PS-Q12_B, PORT=P6")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:SI-Reg:PS-Q12_C, PORT=P7")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:SI-Reg:PS-Q33_A, PORT=P8")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:SI-Reg:PS-Q33_B, PORT=P9")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:SI-Reg:PS-Q33_C, PORT=P10")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:SI-Reg:PS-QFAP, PORT=P1")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:SI-Reg:PS-QFB, PORT=P2")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA03:SI-Reg:PS-QDAP12, PORT=P3")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA04:SI-Reg:PS-QDB12, PORT=P4")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA06:SI-Reg:PS-Q12_A, PORT=P5")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA07:SI-Reg:PS-Q33_A, PORT=P8")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:SI-Reg:PS-QFAP,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:SI-Reg:PS-QFB,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA03:SI-Reg:PS-QDAP12,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA04:SI-Reg:PS-QDB12,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:SI-Reg:PS-Q12_A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:SI-Reg:PS-Q12_B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:SI-Reg:PS-Q12_C,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:SI-Reg:PS-Q33_A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:SI-Reg:PS-Q33_B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:SI-Reg:PS-Q33_C,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
