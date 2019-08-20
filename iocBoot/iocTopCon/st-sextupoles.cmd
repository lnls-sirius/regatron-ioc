#!../../bin/linux-x86_64/TopCon

## You may have to change TopCon to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure("P0", "/dev/ttyReg127")
asynSetOption("P0", 0, "baud", "38400")
asynSetOption("P0", 0, "bits", "8")
asynSetOption("P0", 0, "parity", "none")
asynSetOption("P0", 0, "stop", "1")

drvAsynSerialPortConfigure("P1", "/dev/ttyReg128")
asynSetOption("P1", 0, "baud", "38400")
asynSetOption("P1", 0, "bits", "8")
asynSetOption("P1", 0, "parity", "none")
asynSetOption("P1", 0, "stop", "1")

drvAsynSerialPortConfigure("P2", "/dev/ttyReg129")
asynSetOption("P2", 0, "baud", "38400")
asynSetOption("P2", 0, "bits", "8")
asynSetOption("P2", 0, "parity", "none")
asynSetOption("P2", 0, "stop", "1")

drvAsynSerialPortConfigure("P3", "/dev/ttyReg130")
asynSetOption("P3", 0, "baud", "38400")
asynSetOption("P3", 0, "bits", "8")
asynSetOption("P3", 0, "parity", "none")
asynSetOption("P3", 0, "stop", "1")

drvAsynSerialPortConfigure("P4", "/dev/ttyReg131")
asynSetOption("P4", 0, "baud", "38400")
asynSetOption("P4", 0, "bits", "8")
asynSetOption("P4", 0, "parity", "none")
asynSetOption("P4", 0, "stop", "1")

drvAsynSerialPortConfigure("P5", "/dev/ttyReg132")
asynSetOption("P5", 0, "baud", "38400")
asynSetOption("P5", 0, "bits", "8")
asynSetOption("P5", 0, "parity", "none")
asynSetOption("P5", 0, "stop", "1")

drvAsynSerialPortConfigure("P6", "/dev/ttyReg133")
asynSetOption("P6", 0, "baud", "38400")
asynSetOption("P6", 0, "bits", "8")
asynSetOption("P6", 0, "parity", "none")
asynSetOption("P6", 0, "stop", "1")

drvAsynSerialPortConfigure("P7", "/dev/ttyReg134")
asynSetOption("P7", 0, "baud", "38400")
asynSetOption("P7", 0, "bits", "8")
asynSetOption("P7", 0, "parity", "none")
asynSetOption("P7", 0, "stop", "1")

drvAsynSerialPortConfigure("P8", "/dev/ttyReg135")
asynSetOption("P8", 0, "baud", "38400")
asynSetOption("P8", 0, "bits", "8")
asynSetOption("P8", 0, "parity", "none")
asynSetOption("P8", 0, "stop", "1")

drvAsynSerialPortConfigure("P9", "/dev/ttyReg136")
asynSetOption("P9", 0, "baud", "38400")
asynSetOption("P9", 0, "bits", "8")
asynSetOption("P9", 0, "parity", "none")
asynSetOption("P9", 0, "stop", "1")

drvAsynSerialPortConfigure("P10", "/dev/ttyReg137")
asynSetOption("P10", 0, "baud", "38400")
asynSetOption("P10", 0, "bits", "8")
asynSetOption("P10", 0, "parity", "none")
asynSetOption("P10", 0, "stop", "1")

drvAsynSerialPortConfigure("P11", "/dev/ttyReg138")
asynSetOption("P11", 0, "baud", "38400")
asynSetOption("P11", 0, "bits", "8")
asynSetOption("P11", 0, "parity", "none")
asynSetOption("P11", 0, "stop", "1")

drvAsynSerialPortConfigure("P12", "/dev/ttyReg139")
asynSetOption("P12", 0, "baud", "38400")
asynSetOption("P12", 0, "bits", "8")
asynSetOption("P12", 0, "parity", "none")
asynSetOption("P12", 0, "stop", "1")

drvAsynSerialPortConfigure("P13", "/dev/ttyReg140")
asynSetOption("P13", 0, "baud", "38400")
asynSetOption("P13", 0, "bits", "8")
asynSetOption("P13", 0, "parity", "none")
asynSetOption("P13", 0, "stop", "1")

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDAP0, PORT=P0")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDB0, PORT=P1")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SFAP0, PORT=P2")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SFB0, PORT=P3")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDB1, PORT=P4")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDA12, PORT=P5")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDA3FA1, PORT=P6")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDB2, PORT=P7")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SFA2DP1, PORT=P8")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDB3, PORT=P9")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SDP23, PORT=P10")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SFB1, PORT=P11")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SFP12, PORT=P12")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPS?:SI-Reg:PS-SFB2, PORT=P13")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDAP0, PORT=P0")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDB0, PORT=P1")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SFAP0, PORT=P2")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SFB0, PORT=P3")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDB1, PORT=P4")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDA12, PORT=P5")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDA3FA1, PORT=P6")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDB2, PORT=P7")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SFA2DP1, PORT=P8")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDB3, PORT=P9")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SDP23, PORT=P10")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SFB1, PORT=P11")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SFP12, PORT=P12")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPS?:SI-Reg:PS-SFB2, PORT=P13")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDAP0,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDB0,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SFAP0,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SFB0,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDB1,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDA12,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDA3FA1,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDB2,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SFA2DP1,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDB3,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SDP23,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SFB1,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SFP12,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPS?:SI-Reg:PS-SFB2,R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
