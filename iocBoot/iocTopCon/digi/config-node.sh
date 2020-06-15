#!/bin/sh
set -e

function digi_init {
    set -x
    /usr/bin/dgrp_cfg_node -v -i 4 init ${1} ${2} 1 && ln -s /dev/tty_dgrp_${1}_0 ${3}
    set +x
}

function digi_uninit {
    set -x
    /usr/bin/dgrp_cfg_node uninit ${1} ${2} 1 && rm -f ${3}
    set +x
}

function show_help {
    echo "Usage:" &&\
    echo "    Param 1: {init, uninit}" &&\
    echo "    Param 2: {${DIPOLES}, ${QUADRUPOLES}, ${SEXTUPOLES}, ${DEVEL}}" && exit -1
}

DEVEL="devel"
DIPOLES="dipoles"
QUADRUPOLES="quadrupoles"
SEXTUPOLES="sextupoles"

[ "${1}" != "init" ] && [ "${1}" != "uninit" ] && show_help && exit -1
[ "${2}" != "${DIPOLES}" ] && [ "${2}" != "${SEXTUPOLES}" ] && [ "${2}" != "${QUADRUPOLES}" ] && [ "${2}" != "${DEVEL}" ] && show_help && exit -1

if [ "${2}" = "${DEVEL}" ]; then
    echo "${1} ${DEVEL} ..."
    digi_$1 0  10.0.28.36     /dev/ttyD00

elif [ "${2}" = "${DIPOLES}" ]; then
    echo "${1} ${DIPOLES} ..."
    digi_$1 1  10.128.125.101 /dev/ttyD01
    digi_$1 2  10.128.125.102 /dev/ttyD02
    digi_$1 3  10.128.125.103 /dev/ttyD03
    digi_$1 4  10.128.125.104 /dev/ttyD04
    digi_$1 5  10.128.125.105 /dev/ttyD05
    digi_$1 6  10.128.125.106 /dev/ttyD06
    digi_$1 7  10.128.125.107 /dev/ttyD07
    digi_$1 8  10.128.125.108 /dev/ttyD08
    digi_$1 9  10.128.125.109 /dev/ttyD09
    digi_$1 10 10.128.125.110 /dev/ttyD10
    digi_$1 11 10.128.125.111 /dev/ttyD11
    digi_$1 12 10.128.125.112 /dev/ttyD12
    digi_$1 13 10.128.125.113 /dev/ttyD13
    digi_$1 14 10.128.125.114 /dev/ttyD14
    digi_$1 15 10.128.125.115 /dev/ttyD15
    digi_$1 16 10.128.125.116 /dev/ttyD16

elif [ "${2}" = "${QUADRUPOLES}" ]; then
    echo "${1} ${QUADRUPOLES} ..."
    digi_$1 17 10.128.125.117 /dev/ttyD17 # PA-RaPSA01:PS-DCLink-QFAP
    digi_$1 18 10.128.125.118 /dev/ttyD18 # PA-RaPSA01:PS-DCLink-QFB
    digi_$1 19 10.128.125.119 /dev/ttyD19 # PA-RaPSA03:PS-DCLink-QDAP
    digi_$1 20 10.128.125.120 /dev/ttyD20 # PA-RaPSA04:PS-DCLink-QDB
    digi_$1 21 10.128.125.121 /dev/ttyD21 # PA-RaPSA06:PS-DCLink-Q13A
    digi_$1 22 10.128.125.122 /dev/ttyD22 # PA-RaPSA06:PS-DCLink-Q13B
    digi_$1 23 10.128.125.123 /dev/ttyD23 # PA-RaPSA06:PS-DCLink-Q13C
    digi_$1 24 10.128.125.124 /dev/ttyD24 # PA-RaPSA07:PS-DCLink-Q24A
    digi_$1 25 10.128.125.125 /dev/ttyD25 # PA-RaPSA07:PS-DCLink-Q24B
    digi_$1 26 10.128.125.126 /dev/ttyD26 # PA-RaPSA07:PS-DCLink-Q24C

elif [ "${2}" = "${SEXTUPOLES}" ]; then
    echo "${1} ${SEXTUPOLES} ..."
    digi_$1 27 10.128.125.127 /dev/ttyD27 # 
    digi_$1 28 10.128.125.128 /dev/ttyD28 # 
    digi_$1 29 10.128.125.129 /dev/ttyD29 # 
    digi_$1 30 10.128.125.130 /dev/ttyD30 # 
    digi_$1 31 10.128.125.131 /dev/ttyD31 # 
    digi_$1 32 10.128.125.132 /dev/ttyD32 # 
    digi_$1 33 10.128.125.133 /dev/ttyD33 # 
    digi_$1 34 10.128.125.134 /dev/ttyD34 # 
    digi_$1 35 10.128.125.135 /dev/ttyD35
    digi_$1 36 10.128.125.136 /dev/ttyD36
    digi_$1 37 10.128.125.137 /dev/ttyD37
    digi_$1 38 10.128.125.138 /dev/ttyD38
    digi_$1 39 10.128.125.139 /dev/ttyD39
    digi_$1 40 10.128.125.140 /dev/ttyD40
else
    exit -1
fi

