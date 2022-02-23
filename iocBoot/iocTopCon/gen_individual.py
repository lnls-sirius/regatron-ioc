#!/usr/bin/env python3
import os
import string
import subprocess
import sys

assert sys.version_info >= (3, 7)

header = string.Template(
    """#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "$(EPICS_IOC_LOG_INET)")
epicsEnvSet("EPICS_IOC_LOG_PORT", "$(EPICS_IOC_LOG_PORT)")
epicsEnvSet("D", "${PV}")
epicsEnvSet("P", "${P}")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("$(TOP)/db/Security.as")
"""
)

footer = string.Template(
    """
cd "$(TOP)/iocBoot/$(IOC)"
iocInit
iocLogInit

< ${PROPERTIES}

caPutLogInit "$(EPICS_IOC_CAPUTLOG_INET):$(EPICS_IOC_CAPUTLOG_PORT)" 2

#var streamDebug 1
"""
)

s_port = string.Template(
    """
drvAsynIPPortConfigure("$(P)","$(REGATRON_INTERFACE_MS_HOST):${COM}")
"""
)

asyn_db = string.Template(
    """
dbLoadRecords("db/asynRecord.db",   "P=${PV},R=,P=${P},ADDR=,IMAX=,OMAX=")"""
)

module_db = string.Template(
    """
dbLoadRecords("db/GenericCmd.db",    "D=$(D),P=$(P)")
dbLoadRecords("db/GenericGetSet.db", "D=$(D),P=$(P)")
dbLoadRecords("db/GenericMon.db",    "D=$(D),P=$(P)")
dbLoadRecords("db/TempMon.db",       "D=$(D),P=$(P)")
dbLoadRecords("db/ModMon.db",        "D=$(D),P=$(P)")
dbLoadRecords("db/ModTree.db",       "D=$(D),P=$(P)")

"""
)
system_db = string.Template(
    """
dbLoadRecords("db/SysCmd.db",           "D=$(D),P=$(P)")
dbLoadRecords("db/SysGetSet.db",        "D=$(D),P=$(P)")
dbLoadRecords("db/SysMon.db",           "D=$(D),P=$(P)")
dbLoadRecords("db/SysTree.db",          "D=$(D),P=$(P)")
dbLoadRecords("db/SysCustomNamming.db", "D=$(D),P=$(P)")
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
    {"M": True, "PV": "PA-RaPSB01:PS-DCLink-SDAP0",    "port": 127},
    {"M": True, "PV": "PA-RaPSB01:PS-DCLink-SDB0",     "port": 128},
    {"M": True, "PV": "PA-RaPSB03:PS-DCLink-SFAP0",    "port": 129},
    {"M": True, "PV": "PA-RaPSB03:PS-DCLink-SFB0",     "port": 130},
    {"M": True, "PV": "PA-RaPSB04:PS-DCLink-SDB1",     "port": 131},
    {"M": True, "PV": "PA-RaPSB04:PS-DCLink-SDA12",    "port": 132},
    {"M": True, "PV": "PA-RaPSB05:PS-DCLink-SDA3SFA1", "port": 133},
    {"M": True, "PV": "PA-RaPSB05:PS-DCLink-SDB2",     "port": 134},
    {"M": True, "PV": "PA-RaPSB07:PS-DCLink-SFA2SDP1", "port": 135},
    {"M": True, "PV": "PA-RaPSB07:PS-DCLink-SDB3",     "port": 136},
    {"M": True, "PV": "PA-RaPSB08:PS-DCLink-SDP23",    "port": 137},
    {"M": True, "PV": "PA-RaPSB08:PS-DCLink-SFB1",     "port": 138},
    {"M": True, "PV": "PA-RaPSB10:PS-DCLink-SFP12",    "port": 139},
    {"M": True, "PV": "PA-RaPSB10:PS-DCLink-SFB2",     "port": 140},
]
# fmt: on
BASE_COM = 20000


def load_base_properties():
    return (
        subprocess.run(
            "cat properties.txt | sort -u | xargs", shell=True, capture_output=True
        )
        .stdout.decode("utf-8")
        .replace("\n", "")
    )


def load_master_properties():
    return (
        subprocess.run(
            "cat properties.txt properties-sys.txt | sort -u |xargs",
            shell=True,
            capture_output=True,
        )
        .stdout.decode("utf-8")
        .replace("\n", "")
    )


def generate_dbpf_base():
    base_props = load_base_properties()
    with open("PropertiesBase", "w+") as _f:
        _f.write(f'\ndbpf ("$(D):Properties-Cte", "{base_props}")\n')


def generate_dbpf_master():
    master_props = load_master_properties()
    with open("PropertiesMaster", "w+") as _f:
        _f.write(f'\ndbpf ("$(D):Properties-Cte", "{master_props}")\n')


def generate_ioc_cmd():
    for device in devices:
        port = device["port"]
        filename = "st-{:03}.cmd".format(port)

        with open(filename, "w+") as f:
            s_ports, dbs, m_dbs, asyn_dbs = "", "", "", ""
            device["P"] = "P{}".format(port)
            f.write(header.safe_substitute(**device))
            s_ports += s_port.safe_substitute(COM=str(BASE_COM + port), **device)
            dbs += module_db.safe_substitute(**device)
            if device["M"] is True:
                m_dbs += system_db.safe_substitute(**device)
            f.write(s_ports)
            f.write(dbs)
            f.write(m_dbs)
            f.write(asyn_dbs)
            f.write(
                footer.safe_substitute(
                    PROPERTIES="PropertiesMaster" if device["M"] else "PropertiesBase"
                )
            )
            os.chmod(filename, 0o755)


def pvlist():
    base_props = load_base_properties().split(" ")
    master_props = load_master_properties().split(" ")
    pvs = []

    for d in devices:
        prefix = d["PV"]
        for p in base_props:
            pvs.append("{}:{}".format(prefix, p))

        if d["M"]:
            for p in master_props:
                pvs.append("{}:{}".format(prefix, p))

    with open("pvlist.txt", "w+") as f:
        f.write("\n".join(pvs))


def generate():
    generate_dbpf_base()
    generate_dbpf_master()
    generate_ioc_cmd()


if __name__ == "__main__":
    generate()
    pvlist()
