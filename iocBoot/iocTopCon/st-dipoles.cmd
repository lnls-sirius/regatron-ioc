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

drvAsynSerialPortConfigure("P11", "/dev/tty_dgrp_11_0")
asynSetOption("P11", 0, "baud", "38400")
asynSetOption("P11", 0, "bits", "8")
asynSetOption("P11", 0, "parity", "none")
asynSetOption("P11", 0, "stop", "1")

drvAsynSerialPortConfigure("P12", "/dev/tty_dgrp_12_0")
asynSetOption("P12", 0, "baud", "38400")
asynSetOption("P12", 0, "bits", "8")
asynSetOption("P12", 0, "parity", "none")
asynSetOption("P12", 0, "stop", "1")

drvAsynSerialPortConfigure("P13", "/dev/tty_dgrp_13_0")
asynSetOption("P13", 0, "baud", "38400")
asynSetOption("P13", 0, "bits", "8")
asynSetOption("P13", 0, "parity", "none")
asynSetOption("P13", 0, "stop", "1")

drvAsynSerialPortConfigure("P14", "/dev/tty_dgrp_14_0")
asynSetOption("P14", 0, "baud", "38400")
asynSetOption("P14", 0, "bits", "8")
asynSetOption("P14", 0, "parity", "none")
asynSetOption("P14", 0, "stop", "1")

drvAsynSerialPortConfigure("P15", "/dev/tty_dgrp_15_0")
asynSetOption("P15", 0, "baud", "38400")
asynSetOption("P15", 0, "bits", "8")
asynSetOption("P15", 0, "parity", "none")
asynSetOption("P15", 0, "stop", "1")

drvAsynSerialPortConfigure("P16", "/dev/tty_dgrp_16_0")
asynSetOption("P16", 0, "baud", "38400")
asynSetOption("P16", 0, "bits", "8")
asynSetOption("P16", 0, "parity", "none")
asynSetOption("P16", 0, "stop", "1")

dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_1A, PORT=P1")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_1B, PORT=P2")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_2A, PORT=P3")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_2B, PORT=P4")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_3A, PORT=P5")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_3B, PORT=P6")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_4A, PORT=P7")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-1_4B, PORT=P8")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_1A, PORT=P9")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_1B, PORT=P10")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_2A, PORT=P11")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_2B, PORT=P12")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_3A, PORT=P13")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_3B, PORT=P14")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_4A, PORT=P15")
dbLoadRecords("db/TopCon.db",       "DEVICE=SI-Reg:PS-B12-2_4B, PORT=P16")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-1_1A, PORT=P1")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-1_2A, PORT=P3")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-1_3A, PORT=P5")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-1_4A, PORT=P7")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-2_1A, PORT=P9")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-2_2A, PORT=P11")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-2_3A, PORT=P13")
dbLoadRecords("db/TopConMaster.db", "DEVICE=SI-Reg:PS-B12-2_4A, PORT=P15")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_1A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_1B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_2A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_2B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_3A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_3B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_4A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-1_4B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_1A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_1B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_2A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_2B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_3A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_3B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_4A,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=SI-Reg:PS-B12-2_4B,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
