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
drvAsynIPPortConfigure("${P}","unix:///var/tmp/REG${UNIX}")
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
dbLoadRecords("db/SysCmd.db",        "D=${PV},P=${P}")
dbLoadRecords("db/SysGetSet.db",     "D=${PV},P=${P}")
dbLoadRecords("db/SysMon.db",        "D=${PV},P=${P}")
dbLoadRecords("db/SysTree.db",       "D=${PV},P=${P}")
''')

rega = [
    {'file':'st-test.cmd', 'items':[
       {'M':True, 'PV':'RegTest'},
    ]},
    {'file':'st-dipoles.cmd', 'items':[
       {'M':True,  'PV':'PA-RaPSD01:PS-DCLink-1A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD01:PS-DCLink-1B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD03:PS-DCLink-2A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD03:PS-DCLink-2B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD01:PS-DCLink-3A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD01:PS-DCLink-3B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD03:PS-DCLink-4A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD03:PS-DCLink-4B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD05:PS-DCLink-1A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD05:PS-DCLink-1B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD07:PS-DCLink-2A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD07:PS-DCLink-2B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD05:PS-DCLink-3A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD05:PS-DCLink-3B', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSD07:PS-DCLink-4A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSD07:PS-DCLink-4B', 'port':'1'},
    ]},
    {'file':'st-quadrupoles.cmd', 'items':[
       {'M':True,  'PV':'PA-RaPSA01:PS-DCLink-QFAP', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSA01:PS-DCLink-QFB', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSA03:PS-DCLink-QDAP', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSA04:PS-DCLink-QDB', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSA06:PS-DCLink-Q13A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSA06:PS-DCLink-Q13B', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSA06:PS-DCLink-Q13C', 'port':'1'},
       {'M':True,  'PV':'PA-RaPSA07:PS-DCLink-Q24A', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSA07:PS-DCLink-Q24B', 'port':'1'},
       {'M':False, 'PV':'PA-RaPSA07:PS-DCLink-Q24C', 'port':'1'},
    ]},
    {'file':'st-sextupoles.cmd', 'items':[
       {'M':True, 'PV':'PA-RaPSB01:PS-DCLink-SDB0', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB04:PS-DCLink-SDB1', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB05:PS-DCLink-SDB2', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB07:PS-DCLink-SDB3', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB03:PS-DCLink-SFB0', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB08:PS-DCLink-SFB1', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB10:PS-DCLink-SFB2', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB04:PS-DCLink-SDA12', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB01:PS-DCLink-SDAP0', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB03:PS-DCLink-SFAP0', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB10:PS-DCLink-SFP12', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB08:PS-DCLink-SDP23', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB05:PS-DCLink-SDA3SFA1', 'port':'1'},
       {'M':True, 'PV':'PA-RaPSB07:PS-DCLink-SFA2SDP1', 'port':'1'},
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
                 item['P'] = 'P{}'.format(port)
                 s_ports += s_port.safe_substitute(UNIX='{:02}'.format(port), **item)
                 dbs += module_db.safe_substitute(**item)
                 if item['M'] == True:
                     m_dbs += system_db.safe_substitute(**item)
                 port += 1
             f.write(s_ports)
             f.write(dbs)
             f.write(m_dbs)
             f.write(asyn_dbs)
             f.write(footer)
             os.chmod(d['file'], 0o755)
