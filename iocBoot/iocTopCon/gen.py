#!/usr/bin/python3
import os
from string import Template
#import jinja2

header = ('''#!../../bin/linux-x86_64/TopCon

## You may have to change TopCon to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/TopCon.dbd"
TopCon_registerRecordDeviceDriver pdbbase
''')
footer = ('''
cd "${TOP}/iocBoot/${IOC}"
iocInit

#var streamDebug 1
''')

s_port = Template('''
drvAsynSerialPortConfigure("${PORT}", "${DEVICE}")
asynSetOption("${PORT}", 0, "baud", "38400")
asynSetOption("${PORT}", 0, "bits", "8")
asynSetOption("${PORT}", 0, "parity", "none")
asynSetOption("${PORT}", 0, "stop", "1")
''')

db = Template('''
dbLoadRecords("db/TopCon.db",       "DEVICE=${PV}, PORT=${PORT}")''')
asyn_db = Template('''
dbLoadRecords("db/asynRecord.db",   "P=${PV},R=,PORT=${PÒRT},ADDR=,IMAX=,OMAX=")''')
m_db = Template('''
dbLoadRecords("db/TopConMaster.db", "DEVICE=${PV}, PORT=${PORT}")''')

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
       {'M':True,  'PV':'PA-RaPSA03:PS-DCLink-QDAP12'},
       {'M':True,  'PV':'PA-RaPSA04:PS-DCLink-QDB'},
       {'M':True,  'PV':'PA-RaPSA06:PS-DCLink-Q12AA'},
       {'M':False, 'PV':'PA-RaPSA06:PS-DCLink-Q12BB'},
       {'M':False, 'PV':'PA-RaPSA06:PS-DCLink-Q12CC'},
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
       {'M':True, 'PV':'PA-RaPSB04:SI-DCLink-SDA12'},
       {'M':True, 'PV':'PA-RaPSB01:SI-DCLink-SDAP0'},
       {'M':True, 'PV':'PA-RaPSB03:SI-DCLink-SFAP0'},
       {'M':True, 'PV':'PA-RaPSB10:SI-DCLink-SFP12'},
       {'M':True, 'PV':'PA-RaPSB08:SI-DCLink-SDP23'},
       {'M':True, 'PV':'PA-RaPSB05:SI-DCLink-SDA3SFA1'},
       {'M':True, 'PV':'PA-RaPSB07:SI-DCLink-SFA2SDP1'},
    ]}
]

if __name__ == '__main__':
    link = []
    for d in rega:
        with open(d['file'], 'w+') as f:
             f.write(header)
             s_ports, dbs, m_dbs, asyn_dbs = '','','',''
             port = 0
             for item in d['items']:
                 port += 1
                 item['PORT'] = 'P{}'.format(port)
                 s_ports += s_port.safe_substitute(DEVICE='/dev/tty_dgrp_{}_0'.format(port), **item)
                 asyn_dbs += asyn_db.safe_substitute(**item)
                 dbs += db.safe_substitute(**item)
                 if item['M'] == True:
                     m_dbs += m_db.safe_substitute(**item)
             f.write(s_ports)
             f.write(dbs)
             f.write(m_dbs)
             f.write(asyn_dbs)
             f.write(footer)
             os.chmod(d['file'], 0o755)
