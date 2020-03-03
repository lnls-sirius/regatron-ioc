#!../../bin/linux-x86_64/TopCon

## You may have to change TopCon to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
drvAsynIPPortConfigure("P01", "unix://$(TOP)/test/unix-socket")
dbLoadRecords("db/TopCon.db",       "DEVICE=Tc, PORT=P01")
dbLoadRecords("db/TopConMaster.db", "DEVICE=Tc, PORT=P01")
dbLoadRecords("db/asynRecord.db",   "P=Tc,R=,PORT=P01,ADDR=,IMAX=,OMAX=")

cd "${TOP}/iocBoot/${IOC}"
iocInit

var streamDebug 1
