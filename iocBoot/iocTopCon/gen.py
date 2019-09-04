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
       {'M':True,  'PV':'SI-Reg:PS-B12-1_1A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-1_1B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-1_2A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-1_2B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-1_3A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-1_3B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-1_4A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-1_4B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-2_1A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-2_1B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-2_2A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-2_2B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-2_3A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-2_3B'},
       {'M':True,  'PV':'SI-Reg:PS-B12-2_4A'},
       {'M':False, 'PV':'SI-Reg:PS-B12-2_4B'},
    ]},
    {'file':'st-quadrupoles.cmd', 'items':[
       {'M':True,  'PV':'SI-Reg:PS-QFAP'},
       {'M':True,  'PV':'SI-Reg:PS-QFB'},
       {'M':True,  'PV':'SI-Reg:PS-QDAP12'},
       {'M':True,  'PV':'SI-Reg:PS-QDB12'},
       {'M':True,  'PV':'SI-Reg:PS-Q12_A'},
       {'M':False, 'PV':'SI-Reg:PS-Q12_B'},
       {'M':False, 'PV':'SI-Reg:PS-Q12_C'},
       {'M':True,  'PV':'SI-Reg:PS-Q33_A'},
       {'M':False, 'PV':'SI-Reg:PS-Q33_B'},
       {'M':False, 'PV':'SI-Reg:PS-Q33_C'},
    ]},
    {'file':'st-sextupoles.cmd', 'items':[
       {'M':True, 'PV':'SI-Reg:PS-SDAP0'},
       {'M':True, 'PV':'SI-Reg:PS-SDB0'},
       {'M':True, 'PV':'SI-Reg:PS-SFAP0'},
       {'M':True, 'PV':'SI-Reg:PS-SFB0'},
       {'M':True, 'PV':'SI-Reg:PS-SDB1'},
       {'M':True, 'PV':'SI-Reg:PS-SDA12'},
       {'M':True, 'PV':'SI-Reg:PS-SDA3FA1'},
       {'M':True, 'PV':'SI-Reg:PS-SDB2'},
       {'M':True, 'PV':'SI-Reg:PS-SFA2DP1'},
       {'M':True, 'PV':'SI-Reg:PS-SDB3'},
       {'M':True, 'PV':'SI-Reg:PS-SDP23'},
       {'M':True, 'PV':'SI-Reg:PS-SFB1'},
       {'M':True, 'PV':'SI-Reg:PS-SFP12'},
       {'M':True, 'PV':'SI-Reg:PS-SFB2'},
    ]}
]
#j_t = jinja2.Template('''
#    device:
#{% for l in link %}      {{ l }}
#{% endfor %}
#''')
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
                 #link.append('- /dev/tty_dgrp_{}_0:/dev/tty_dgrp_{}_0'.format(port, port))
                 asyn_dbs += asyn_db.safe_substitute(**item)
                 dbs += db.safe_substitute(**item)
                 if item['M'] == True:
                     m_dbs += m_db.safe_substitute(**item)
             #print(j_t.render(link=link))
             f.write(s_ports)
             f.write(dbs)
             f.write(m_dbs)
             f.write(asyn_dbs)
             f.write(footer)
             os.chmod(d['file'], 0o755)
