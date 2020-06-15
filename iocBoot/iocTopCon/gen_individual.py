#!/usr/bin/python3
import os
from string import Template

# import jinja2

header = """#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")
"""
footer = """
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
"""

s_port = Template(
    """
# DIGI Real Port -> /dev/ttyD${UNIX}
drvAsynIPPortConfigure("${P}","unix:///var/tmp/REG${UNIX}")
"""
)

asyn_db = Template(
    """
dbLoadRecords("db/asynRecord.db",   "P=${PV},R=,P=${P},ADDR=,IMAX=,OMAX=")"""
)

module_db = Template(
    """
dbLoadRecords("db/GenericCmd.db",    "D=${PV},P=${P}")
dbLoadRecords("db/GenericGetSet.db", "D=${PV},P=${P}")
dbLoadRecords("db/GenericMon.db",    "D=${PV},P=${P}")
dbLoadRecords("db/TempMon.db",       "D=${PV},P=${P}")
dbLoadRecords("db/ModMon.db",        "D=${PV},P=${P}")
dbLoadRecords("db/ModTree.db",       "D=${PV},P=${P}")
"""
)
system_db = Template(
    """
dbLoadRecords("db/SysCmd.db",        "D=${PV},P=${P}")
dbLoadRecords("db/SysGetSet.db",     "D=${PV},P=${P}")
dbLoadRecords("db/SysMon.db",        "D=${PV},P=${P}")
dbLoadRecords("db/SysTree.db",       "D=${PV},P=${P}")
"""
)

# fmt: off
devices = [
    # Dipoles
    {"M": True, "PV": "PA-RaPSD01:PS-DCLink-1A",  "port": 1},
    {"M": False, "PV": "PA-RaPSD01:PS-DCLink-1B", "port": 2},
    {"M": True, "PV": "PA-RaPSD03:PS-DCLink-2A",  "port": 3},
    {"M": False, "PV": "PA-RaPSD03:PS-DCLink-2B", "port": 4},
    {"M": True, "PV": "PA-RaPSD01:PS-DCLink-3A",  "port": 5},
    {"M": False, "PV": "PA-RaPSD01:PS-DCLink-3B", "port": 6},
    {"M": True, "PV": "PA-RaPSD03:PS-DCLink-4A",  "port": 7},
    {"M": False, "PV": "PA-RaPSD03:PS-DCLink-4B", "port": 8},
    {"M": True, "PV": "PA-RaPSD05:PS-DCLink-1A",  "port": 9},
    {"M": False, "PV": "PA-RaPSD05:PS-DCLink-1B", "port": 10},
    {"M": True, "PV": "PA-RaPSD07:PS-DCLink-2A",  "port": 11},
    {"M": False, "PV": "PA-RaPSD07:PS-DCLink-2B", "port": 12},
    {"M": True, "PV": "PA-RaPSD05:PS-DCLink-3A",  "port": 13},
    {"M": False, "PV": "PA-RaPSD05:PS-DCLink-3B", "port": 14},
    {"M": True, "PV": "PA-RaPSD07:PS-DCLink-4A",  "port": 15},
    {"M": False, "PV": "PA-RaPSD07:PS-DCLink-4B", "port": 16},
    # Quadrupoles
    {"M": True, "PV": "PA-RaPSA01:PS-DCLink-QFAP",  "port": 17},
    {"M": True, "PV": "PA-RaPSA01:PS-DCLink-QFB",   "port": 18},
    {"M": True, "PV": "PA-RaPSA03:PS-DCLink-QDAP",  "port": 19},
    {"M": True, "PV": "PA-RaPSA04:PS-DCLink-QDB",   "port": 20},
    {"M": True, "PV": "PA-RaPSA06:PS-DCLink-Q13A",  "port": 21},
    {"M": False, "PV": "PA-RaPSA06:PS-DCLink-Q13B", "port": 22},
    {"M": False, "PV": "PA-RaPSA06:PS-DCLink-Q13C", "port": 23},
    {"M": True, "PV": "PA-RaPSA07:PS-DCLink-Q24A",  "port": 24},
    {"M": False, "PV": "PA-RaPSA07:PS-DCLink-Q24B", "port": 25},
    {"M": False, "PV": "PA-RaPSA07:PS-DCLink-Q24C", "port": 26},
    # Sextupoles
    {"M": True, "PV": "PA-RaPSB01:PS-DCLink-SDB0",     "port": 27},
    {"M": True, "PV": "PA-RaPSB04:PS-DCLink-SDB1",     "port": 28},
    {"M": True, "PV": "PA-RaPSB05:PS-DCLink-SDB2",     "port": 29},
    {"M": True, "PV": "PA-RaPSB07:PS-DCLink-SDB3",     "port": 30},
    {"M": True, "PV": "PA-RaPSB03:PS-DCLink-SFB0",     "port": 31},
    {"M": True, "PV": "PA-RaPSB08:PS-DCLink-SFB1",     "port": 32},
    {"M": True, "PV": "PA-RaPSB10:PS-DCLink-SFB2",     "port": 33},
    {"M": True, "PV": "PA-RaPSB04:PS-DCLink-SDA12",    "port": 34},
    {"M": True, "PV": "PA-RaPSB01:PS-DCLink-SDAP0",    "port": 35},
    {"M": True, "PV": "PA-RaPSB03:PS-DCLink-SFAP0",    "port": 36},
    {"M": True, "PV": "PA-RaPSB10:PS-DCLink-SFP12",    "port": 37},
    {"M": True, "PV": "PA-RaPSB08:PS-DCLink-SDP23",    "port": 38},
    {"M": True, "PV": "PA-RaPSB05:PS-DCLink-SDA3SFA1", "port": 39},
    {"M": True, "PV": "PA-RaPSB07:PS-DCLink-SFA2SDP1", "port": 40},
]
# fmt: on

if __name__ == "__main__":
    link = []
    for device in devices:
        port = device["port"]
        filename = "st-{:02}.cmd".format(port)

        with open(filename, "w+") as f:
            f.write(header)
            s_ports, dbs, m_dbs, asyn_dbs = "", "", "", ""
            device["P"] = "P{}".format(port)
            s_ports += s_port.safe_substitute(UNIX="{:02}".format(port), **device)
            dbs += module_db.safe_substitute(**device)
            if device["M"] == True:
                m_dbs += system_db.safe_substitute(**device)
            f.write(s_ports)
            f.write(dbs)
            f.write(m_dbs)
            f.write(asyn_dbs)
            f.write(footer)
            os.chmod(filename, 0o755)
