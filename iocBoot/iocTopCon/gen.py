#!/usr/bin/python3
import os
from string import Template
#import jinja2

header = ('''#!../../bin/linux-x86_64/TopCon
< envPaths

epicsEnvSet("EPICS_IOC_LOG_INET", "0.0.0.0")
epicsEnvSet("EPICS_IOC_LOG_PORT", "7011")

cd "${TOP}"

dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
asSetFilename("${TOP}/log/Security.as")
''')
footer = ('''
cd "${TOP}/iocBoot/${IOC}"
iocInit

caPutLogInit "0.0.0.0" 2

#var streamDebug 1
''')

s_port = Template('''
# DIGI Real Port -> /dev/ttyD${UNIX}
drvAsynIPPortConfigure("${P}","unix:///var/tmp/REGD${UNIX}")
''')

asyn_db = Template('''
dbLoadRecords("db/asynRecord.db",   "P=${PV},R=,P=${P},ADDR=,IMAX=,OMAX=")''')

module_db = Template('''
dbLoadRecords("db/GenericCmd.db",    "D=${PV},P=${P}")
dbLoadRecords("db/GenericGetSet.db", "D=${PV},P=${P}")
dbLoadRecords("db/GenericMon.db",    "D=${PV},P=${P}")
dbLoadRecords("db/TempMon.db",       "D=${PV},P=${P}")
dbLoadRecords("db/ModMon.db",        "D=${PV},P=${P}")
dbLoadRecords("db/ModTree.db",       "D=${PV},P=${P}")
''')
system_db = Template('''
dbLoadRecords("db/SysMon.db",        "D=${PV},P=${P}")
dbLoadRecords("db/SysTree.db",       "D=${PV},P=${P}")
''')

rega = [
    {'file':'st-dipoles.cmd', 'items':[
       {'M':True,  'PV':'PA-RaPSD01:PS-DCLink-1A'},
       {'M':False, 'PV':'PA-RaPSD01:PS-DCLink-1B'},
       {'M':True,  'PV':'PA-RaPSD03:PS-DCLink-2A'},
       {'M':False, 'PV':'PA-RaPSD03:PS-DCLink-2B'},
       {'M':True,  'PV':'PA-RaPSD01:PS-DCLink-3A'},
       {'M':False, 'PV':'PA-RaPSD01:PS-DCLink-3B'},
       {'M':True,  'PV':'PA-RaPSD03:PS-DCLink-4A'},
       {'M':False, 'PV':'PA-RaPSD03:PS-DCLink-4B'},
       {'M':True,  'PV':'PA-RaPSD05:PS-DCLink-1A'},
       {'M':False, 'PV':'PA-RaPSD05:PS-DCLink-1B'},
       {'M':True,  'PV':'PA-RaPSD07:PS-DCLink-2A'},
       {'M':False, 'PV':'PA-RaPSD07:PS-DCLink-2B'},
       {'M':True,  'PV':'PA-RaPSD05:PS-DCLink-3A'},
       {'M':False, 'PV':'PA-RaPSD05:PS-DCLink-3B'},
       {'M':True,  'PV':'PA-RaPSD07:PS-DCLink-4A'},
       {'M':False, 'PV':'PA-RaPSD07:PS-DCLink-4B'},
    ]},
    {'file':'st-quadrupoles.cmd', 'items':[
       {'M':True,  'PV':'PA-RaPSA01:PS-DCLink-QFAP'},
       {'M':True,  'PV':'PA-RaPSA01:PS-DCLink-QFB'},
       {'M':True,  'PV':'PA-RaPSA03:PS-DCLink-QDAP'},
       {'M':True,  'PV':'PA-RaPSA04:PS-DCLink-QDB'},
       {'M':True,  'PV':'PA-RaPSA06:PS-DCLink-Q12A'},
       {'M':False, 'PV':'PA-RaPSA06:PS-DCLink-Q12B'},
       {'M':False, 'PV':'PA-RaPSA06:PS-DCLink-Q12C'},
       {'M':True,  'PV':'PA-RaPSA07:PS-DCLink-Q34A'},
       {'M':False, 'PV':'PA-RaPSA07:PS-DCLink-Q34B'},
       {'M':False, 'PV':'PA-RaPSA07:PS-DCLink-Q34C'},
    ]},
    {'file':'st-sextupoles.cmd', 'items':[
       {'M':True, 'PV':'PA-RaPSB01:PS-DCLink-SDB0'},
       {'M':True, 'PV':'PA-RaPSB04:PS-DCLink-SDB1'},
       {'M':True, 'PV':'PA-RaPSB05:PS-DCLink-SDB2'},
       {'M':True, 'PV':'PA-RaPSB07:PS-DCLink-SDB3'},
       {'M':True, 'PV':'PA-RaPSB03:PS-DCLink-SFB0'},
       {'M':True, 'PV':'PA-RaPSB08:PS-DCLink-SFB1'},
       {'M':True, 'PV':'PA-RaPSB10:PS-DCLink-SFB2'},
       {'M':True, 'PV':'PA-RaPSB04:PS-DCLink-SDA12'},
       {'M':True, 'PV':'PA-RaPSB01:PS-DCLink-SDAP0'},
       {'M':True, 'PV':'PA-RaPSB03:PS-DCLink-SFAP0'},
       {'M':True, 'PV':'PA-RaPSB10:PS-DCLink-SFP12'},
       {'M':True, 'PV':'PA-RaPSB08:PS-DCLink-SDP23'},
       {'M':True, 'PV':'PA-RaPSB05:PS-DCLink-SDA3SFA1'},
       {'M':True, 'PV':'PA-RaPSB07:PS-DCLink-SFA2SDP1'},
    ]}
]

if __name__ == '__main__':
    link = []
    port = 0
    for d in rega:
        with open(d['file'], 'w+') as f:
             f.write(header)
             s_ports, dbs, m_dbs, asyn_dbs = '','','',''
             for item in d['items']:
                 port += 1
                 item['P'] = 'P{}'.format(port)
                 s_ports += s_port.safe_substitute(UNIX='{:02}'.format(port), **item)
                 asyn_dbs += asyn_db.safe_substitute(**item)
                 dbs += module_db.safe_substitute(**item)
                 if item['M'] == True:
                     m_dbs += system_db.safe_substitute(**item)
             f.write(s_ports)
             f.write(dbs)
             f.write(m_dbs)
             f.write(asyn_dbs)
             f.write(footer)
             os.chmod(d['file'], 0o755)
