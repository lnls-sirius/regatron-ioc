#!/bin/sh
set -x
set -e

# 1 - Prefix
# 2 - Warn/Error
# 3 - Sys/Mod
# 4 - Sleep amount
# 5 - Ext/Std

if [ -z $1 ]; then exit 1; fi
if [ -z $2 ]; then exit 1; fi
if [ -z $3 ]; then exit 1; fi
if [ -z $4 ]; then exit 1; fi
if [ -z $5 ]; then exit 1; fi

if [ $5 = 'Std' ]; then
    caput ${1}:${3}:Std${2}Temperature-Mon.PROC 1;             sleep ${4};
    caput ${1}:${3}:Std${2}Internal-Mon.PROC 1;                sleep ${4};
    caput ${1}:${3}:Std${2}OutputVoltage-Mon.PROC 1;           sleep ${4};
    caput ${1}:${3}:Std${2}InternalADoverrange1-Mon.PROC 1;     sleep ${4};
    caput ${1}:${3}:Std${2}InternalPDSP-Mon.PROC 1;            sleep ${4};
    caput ${1}:${3}:Std${2}Communication-Mon.PROC 1;           sleep ${4};
    caput ${1}:${3}:Std${2}InternalADoverrange2-Mon.PROC 1;    sleep ${4};
    caput ${1}:${3}:Std${2}OutputCurrent-Mon.PROC 1;           sleep ${4};
    caput ${1}:${3}:Std${2}InternalADunderrange2-Mon.PROC 1;   sleep ${4};
    caput ${1}:${3}:Std${2}Configuration-Mon.PROC 1;           sleep ${4};
    caput ${1}:${3}:Std${2}Supply-Mon.PROC 1;                  sleep ${4};
    caput ${1}:${3}:Std${2}InternalMod-Mon.PROC 1;       sleep ${4};
    caput ${1}:${3}:Std${2}Login-Mon.PROC 1;                   sleep ${4};
    caput ${1}:${3}:Std${2}InternalADunderrange1-Mon.PROC 1;   sleep ${4};
    caput ${1}:${3}:Std${2}Configuration2-Mon.PROC 1;          sleep ${4};
    caput ${1}:${3}:Std${2}Miscellaneous-Mon.PROC 1;           sleep ${4};
fi

if [ $5 = 'Ext' ]; then
    caput ${1}:${3}:Ext${2}Group-Mon.PROC 1;                    sleep ${4};
    caput ${1}:${3}:Ext${2}IBCSystem-Mon.PROC 1;                sleep ${4};
    caput ${1}:${3}:Ext${2}IBCSuppply-Mon.PROC 1;               sleep ${4};
    caput ${1}:${3}:Ext${2}IBCCommunication-Mon.PROC 1;         sleep ${4};
    caput ${1}:${3}:Ext${2}IBCPower-Mon.PROC 1;                 sleep ${4};
    caput ${1}:${3}:Ext${2}IBCInverter-Mon.PROC 1;              sleep ${4};
    caput ${1}:${3}:Ext${2}IBCMiscellaneous-Mon.PROC 1;         sleep ${4};
    caput ${1}:${3}:Ext${2}IBCInverter2-Mon.PROC 1;             sleep ${4};
    caput ${1}:${3}:Ext${2}Supply2-Mon.PROC 1;                  sleep ${4};
    caput ${1}:${3}:Ext${2}Login2-Mon.PROC 1;                   sleep ${4};
    caput ${1}:${3}:Ext${2}Configuration3-Mon.PROC 1;           sleep ${4};
    caput ${1}:${3}:Ext${2}Communication3-Mon.PROC 1;           sleep ${4};
    caput ${1}:${3}:Ext${2}Internal2-Mon.PROC 1;                sleep ${4};
    caput ${1}:${3}:Ext${2}Communication2-Mon.PROC 1;           sleep ${4};
fi

