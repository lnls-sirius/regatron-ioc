#!/bin/bash
echo "###################################################################"
echo "# ${INFO}"
echo "# Regatron Interface Windows HOST - ${REGATRON_INTERFACE_MS_HOST}  "
echo "# ProcServ. Use \"socat - UNIX-CLIENT:<socket>\"                   "
echo "# TOP: \"${TOP}\""
echo "###################################################################"
for dev in ${DEVS}; do
        cmd="st-${dev}.cmd"
        iocName="DCLink-Reg-$(echo ${cmd} | sed -e "s/\.cmd//g" -e "s/st-//g")"
        logFile=${TOP}/log/${iocName}.log
        socket_name="${TOP}/sockets/${iocName}.sock"
        procServ -n ${iocName} -q --killsig 9 -L ${logFile} --chdir ${TOP}/iocBoot/iocTopCon unix:${socket_name} ./${cmd}
        echo "# IOC: \"${iocName}\" cmd:\"${cmd}\"  log_file: \"${logFile}\" unix_socket: \"${socket_name}\""
done
echo "###################################################################"
sleep infinity
