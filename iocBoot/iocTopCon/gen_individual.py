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
drvAsynIPPortConfigure("${P}","${IP}:${COM}")
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
    {"M": True, "PV": "PA-RaPSD01:PS-DCLink-1A",  "port": 101},
    {"M": False, "PV": "PA-RaPSD01:PS-DCLink-1B", "port": 102},
    {"M": True, "PV": "PA-RaPSD03:PS-DCLink-2A",  "port": 103},
    {"M": False, "PV": "PA-RaPSD03:PS-DCLink-2B", "port": 104},
    {"M": True, "PV": "PA-RaPSD01:PS-DCLink-3A",  "port": 105},
    {"M": False, "PV": "PA-RaPSD01:PS-DCLink-3B", "port": 106},
    {"M": True, "PV": "PA-RaPSD03:PS-DCLink-4A",  "port": 107},
    {"M": False, "PV": "PA-RaPSD03:PS-DCLink-4B", "port": 108},
    {"M": True, "PV": "PA-RaPSD05:PS-DCLink-1A",  "port": 109},
    {"M": False, "PV": "PA-RaPSD05:PS-DCLink-1B", "port": 110},
    {"M": True, "PV": "PA-RaPSD07:PS-DCLink-2A",  "port": 111},
    {"M": False, "PV": "PA-RaPSD07:PS-DCLink-2B", "port": 112},
    {"M": True, "PV": "PA-RaPSD05:PS-DCLink-3A",  "port": 113},
    {"M": False, "PV": "PA-RaPSD05:PS-DCLink-3B", "port": 114},
    {"M": True, "PV": "PA-RaPSD07:PS-DCLink-4A",  "port": 115},
    {"M": False, "PV": "PA-RaPSD07:PS-DCLink-4B", "port": 116},

    # Quadrupoles
    {"M": True, "PV": "PA-RaPSA01:PS-DCLink-QFAP",  "port": 117},
    {"M": True, "PV": "PA-RaPSA01:PS-DCLink-QFB",   "port": 118},
    {"M": True, "PV": "PA-RaPSA03:PS-DCLink-QDAP",  "port": 119},
    {"M": True, "PV": "PA-RaPSA04:PS-DCLink-QDB",   "port": 120},
    {"M": True, "PV": "PA-RaPSA06:PS-DCLink-Q13A",  "port": 121},
    {"M": False, "PV": "PA-RaPSA06:PS-DCLink-Q13B", "port": 122},
    {"M": False, "PV": "PA-RaPSA06:PS-DCLink-Q13C", "port": 123},
    {"M": True, "PV": "PA-RaPSA07:PS-DCLink-Q24A",  "port": 124},
    {"M": False, "PV": "PA-RaPSA07:PS-DCLink-Q24B", "port": 125},
    {"M": False, "PV": "PA-RaPSA07:PS-DCLink-Q24C", "port": 126},

    # Sextupoles
    {"M": True, "PV": "PA-RaPSB01:PS-DCLink-SDB0",     "port": 127},
    {"M": True, "PV": "PA-RaPSB04:PS-DCLink-SDB1",     "port": 128},
    {"M": True, "PV": "PA-RaPSB05:PS-DCLink-SDB2",     "port": 129},
    {"M": True, "PV": "PA-RaPSB07:PS-DCLink-SDB3",     "port": 130},
    {"M": True, "PV": "PA-RaPSB03:PS-DCLink-SFB0",     "port": 131},
    {"M": True, "PV": "PA-RaPSB08:PS-DCLink-SFB1",     "port": 132},
    {"M": True, "PV": "PA-RaPSB10:PS-DCLink-SFB2",     "port": 133},
    {"M": True, "PV": "PA-RaPSB04:PS-DCLink-SDA12",    "port": 134},
    {"M": True, "PV": "PA-RaPSB01:PS-DCLink-SDAP0",    "port": 135},
    {"M": True, "PV": "PA-RaPSB03:PS-DCLink-SFAP0",    "port": 136},
    {"M": True, "PV": "PA-RaPSB10:PS-DCLink-SFP12",    "port": 137},
    {"M": True, "PV": "PA-RaPSB08:PS-DCLink-SDP23",    "port": 138},
    {"M": True, "PV": "PA-RaPSB05:PS-DCLink-SDA3SFA1", "port": 139},
    {"M": True, "PV": "PA-RaPSB07:PS-DCLink-SFA2SDP1", "port": 140},
]
# fmt: on
IP = 'x.x.x.x'
BASE_COM = 20000
if __name__ == "__main__":
    link = []
    for device in devices:
        port = device["port"]
        filename = "st-{:03}.cmd".format(port)

        with open(filename, "w+") as f:
            f.write(header)
            s_ports, dbs, m_dbs, asyn_dbs = "", "", "", ""
            device["P"] = "P{}".format(port)
            s_ports += s_port.safe_substitute(IP=IP,COM=str(BASE_COM + port), **device)
            dbs += module_db.safe_substitute(**device)
            if device["M"] == True:
                m_dbs += system_db.safe_substitute(**device)
            f.write(s_ports)
            f.write(dbs)
            f.write(m_dbs)
            f.write(asyn_dbs)
            f.write(footer)
            os.chmod(filename, 0o755)
