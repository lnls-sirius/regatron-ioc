#!/usr/bin/python3
import os
from string import Template
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
       {'DEVICE':'/dev/ttyReg101', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-1_1A'},
       {'DEVICE':'/dev/ttyReg102', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-1_1B'},
       {'DEVICE':'/dev/ttyReg103', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-1_2A'},
       {'DEVICE':'/dev/ttyReg104', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-1_2B'},
       {'DEVICE':'/dev/ttyReg105', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-1_3A'},
       {'DEVICE':'/dev/ttyReg106', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-1_3B'},
       {'DEVICE':'/dev/ttyReg107', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-1_4A'},
       {'DEVICE':'/dev/ttyReg108', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-1_4B'},
       {'DEVICE':'/dev/ttyReg109', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-2_1A'},
       {'DEVICE':'/dev/ttyReg110', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-2_1B'},
       {'DEVICE':'/dev/ttyReg111', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-2_2A'},
       {'DEVICE':'/dev/ttyReg112', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-2_2B'},
       {'DEVICE':'/dev/ttyReg113', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-2_3A'},
       {'DEVICE':'/dev/ttyReg114', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-2_3B'},
       {'DEVICE':'/dev/ttyReg115', 'M':True,  'PV':'PA-RaPS?:SI-Reg:PS-B12-2_4A'},
       {'DEVICE':'/dev/ttyReg116', 'M':False, 'PV':'PA-RaPS?:SI-Reg:PS-B12-2_4B'},
    ]},
    {'file':'st-quadrupoles.cmd', 'items':[
       {'DEVICE':'/dev/ttyReg117', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-QFAP'},
       {'DEVICE':'/dev/ttyReg118', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-QFB'},
       {'DEVICE':'/dev/ttyReg119', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-QDAP12'},
       {'DEVICE':'/dev/ttyReg120', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-QDB12'},
       {'DEVICE':'/dev/ttyReg121', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-Q12_A'},
       {'DEVICE':'/dev/ttyReg122', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-Q12_B'},
       {'DEVICE':'/dev/ttyReg123', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-Q12_C'},
       {'DEVICE':'/dev/ttyReg124', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-Q33_A'},
       {'DEVICE':'/dev/ttyReg125', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-Q33_B'},
       {'DEVICE':'/dev/ttyReg126', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-Q33_C'},
    ]},
    {'file':'st-sextupoles.cmd', 'items':[
       {'DEVICE':'/dev/ttyReg127', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDAP0'},
       {'DEVICE':'/dev/ttyReg128', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDB0'},
       {'DEVICE':'/dev/ttyReg129', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SFAP0'},
       {'DEVICE':'/dev/ttyReg130', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SFB0'},
       {'DEVICE':'/dev/ttyReg131', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDB1'},
       {'DEVICE':'/dev/ttyReg132', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDA12'},
       {'DEVICE':'/dev/ttyReg133', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDA3FA1'},
       {'DEVICE':'/dev/ttyReg134', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDB2'},
       {'DEVICE':'/dev/ttyReg135', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SFA2DP1'},
       {'DEVICE':'/dev/ttyReg136', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDB3'},
       {'DEVICE':'/dev/ttyReg137', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SDP23'},
       {'DEVICE':'/dev/ttyReg138', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SFB1'},
       {'DEVICE':'/dev/ttyReg139', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SFP12'},
       {'DEVICE':'/dev/ttyReg140', 'M':True, 'PV':'PA-RaPS?:SI-Reg:PS-SFB2'},
    ]}
]

if __name__ == '__main__':
    for d in rega:
        with open(d['file'], 'w+') as f:
             f.write(header)
             s_ports, dbs, m_dbs, asyn_dbs = '','','',''
             port = 0
             for item in d['items']:
                 item['PORT'] = 'P{}'.format(port)
                 port += 1
                 s_ports += s_port.safe_substitute(**item)
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

