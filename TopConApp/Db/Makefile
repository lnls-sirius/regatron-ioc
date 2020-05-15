TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install) into <top>/db
# databases, templates, substitutions like this

DB += Regatron.proto

DB += Generic.db
DB += GenericMon.db
DB += ModMon.db
DB += ModTree.db
DB += SysCmd.db
DB += SysGetSet.db
DB += SysMon.db
DB += SysTree.db
DB += TempMon.db

DB += $(ASYN)/db/asynRecord.db

include $(TOP)/configure/RULES

db:
	./Generate.py

clean distclean:
	./clean.sh
