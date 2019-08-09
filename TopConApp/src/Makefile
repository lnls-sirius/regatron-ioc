TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = TopCon
# TopCon.dbd will be created and installed
DBD += TopCon.dbd

# TopCon.dbd will be made up from these files:
TopCon_DBD += base.dbd

TopCon_DBD += calcSupport.dbd
TopCon_DBD += asyn.dbd
TopCon_DBD += stream.dbd
TopCon_DBD += drvAsynSerialPort.dbd
 
TopCon_LIBS += stream
TopCon_LIBS += asyn
TopCon_LIBS += calc


# TopCon_registerRecordDeviceDriver.cpp derives from TopCon.dbd
TopCon_SRCS += TopCon_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
TopCon_SRCS_DEFAULT += TopConMain.cpp
TopCon_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#TopCon_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
TopCon_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

