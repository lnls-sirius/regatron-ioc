#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")

drvAsynSerialPortConfigure("P17", "/dev/tty_dgrp_17_0")
asynSetOption("P17", 0, "baud", "38400")
asynSetOption("P17", 0, "bits", "8")
asynSetOption("P17", 0, "parity", "none")
asynSetOption("P17", 0, "stop", "1")

drvAsynSerialPortConfigure("P18", "/dev/tty_dgrp_18_0")
asynSetOption("P18", 0, "baud", "38400")
asynSetOption("P18", 0, "bits", "8")
asynSetOption("P18", 0, "parity", "none")
asynSetOption("P18", 0, "stop", "1")

drvAsynSerialPortConfigure("P19", "/dev/tty_dgrp_19_0")
asynSetOption("P19", 0, "baud", "38400")
asynSetOption("P19", 0, "bits", "8")
asynSetOption("P19", 0, "parity", "none")
asynSetOption("P19", 0, "stop", "1")

drvAsynSerialPortConfigure("P20", "/dev/tty_dgrp_20_0")
asynSetOption("P20", 0, "baud", "38400")
asynSetOption("P20", 0, "bits", "8")
asynSetOption("P20", 0, "parity", "none")
asynSetOption("P20", 0, "stop", "1")

drvAsynSerialPortConfigure("P21", "/dev/tty_dgrp_21_0")
asynSetOption("P21", 0, "baud", "38400")
asynSetOption("P21", 0, "bits", "8")
asynSetOption("P21", 0, "parity", "none")
asynSetOption("P21", 0, "stop", "1")

drvAsynSerialPortConfigure("P22", "/dev/tty_dgrp_22_0")
asynSetOption("P22", 0, "baud", "38400")
asynSetOption("P22", 0, "bits", "8")
asynSetOption("P22", 0, "parity", "none")
asynSetOption("P22", 0, "stop", "1")

drvAsynSerialPortConfigure("P23", "/dev/tty_dgrp_23_0")
asynSetOption("P23", 0, "baud", "38400")
asynSetOption("P23", 0, "bits", "8")
asynSetOption("P23", 0, "parity", "none")
asynSetOption("P23", 0, "stop", "1")

drvAsynSerialPortConfigure("P24", "/dev/tty_dgrp_24_0")
asynSetOption("P24", 0, "baud", "38400")
asynSetOption("P24", 0, "bits", "8")
asynSetOption("P24", 0, "parity", "none")
asynSetOption("P24", 0, "stop", "1")

drvAsynSerialPortConfigure("P25", "/dev/tty_dgrp_25_0")
asynSetOption("P25", 0, "baud", "38400")
asynSetOption("P25", 0, "bits", "8")
asynSetOption("P25", 0, "parity", "none")
asynSetOption("P25", 0, "stop", "1")

drvAsynSerialPortConfigure("P26", "/dev/tty_dgrp_26_0")
asynSetOption("P26", 0, "baud", "38400")
asynSetOption("P26", 0, "bits", "8")
asynSetOption("P26", 0, "parity", "none")
asynSetOption("P26", 0, "stop", "1")

dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:PS-DCLink-QFAP,PORT=P17")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA01:PS-DCLink-QFB,PORT=P18")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA03:PS-DCLink-QDAP12,PORT=P19")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA04:PS-DCLink-QDB,PORT=P20")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12AA,PORT=P21")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12BB,PORT=P22")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA06:PS-DCLink-Q12CC,PORT=P23")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34A,PORT=P24")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34B,PORT=P25")
dbLoadRecords("db/TopCon.db",       "DEVICE=PA-RaPSA07:PS-DCLink-Q34C,PORT=P26")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:PS-DCLink-QFAP,PORT=P17")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA01:PS-DCLink-QFB,PORT=P18")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA03:PS-DCLink-QDAP12,PORT=P19")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA04:PS-DCLink-QDB,PORT=P20")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA06:PS-DCLink-Q12AA,PORT=P21")
dbLoadRecords("db/TopConMaster.db", "DEVICE=PA-RaPSA07:PS-DCLink-Q34A,PORT=P24")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:PS-DCLink-QFAP,R=,PORT=P17,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA01:PS-DCLink-QFB,R=,PORT=P18,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA03:PS-DCLink-QDAP12,R=,PORT=P19,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA04:PS-DCLink-QDB,R=,PORT=P20,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12AA,R=,PORT=P21,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12BB,R=,PORT=P22,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA06:PS-DCLink-Q12CC,R=,PORT=P23,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34A,R=,PORT=P24,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34B,R=,PORT=P25,ADDR=,IMAX=,OMAX=")
dbLoadRecords("db/asynRecord.db",   "P=PA-RaPSA07:PS-DCLink-Q34C,R=,PORT=P26,ADDR=,IMAX=,OMAX=")
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
