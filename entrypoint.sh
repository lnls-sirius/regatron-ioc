#!/bin/bash
set -u
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
        procServ \
                -n ${iocName} \
                -q --killsig 9 -L ${logFile} \
                --chdir ${TOP}/iocBoot/iocTopCon unix:${socket_name} \
                ./${cmd}

        echo "# IOC:   \"${iocName}\" cmd:\"${cmd}\"  log_file: \"${logFile}\" unix_socket: \"${socket_name}\""

        export IOC_PROCSERV_PREFIX="PCTRL:DCLink-Reg-${dev}"
        export IOC_PROCSERV_ADDR=${socket_name}
        export PCTRL_SOCK="${TOP}/procCtrl/sockets/${dev}.sock"
        /usr/local/bin/procServ \
                -q -L ${TOP}/log/PCtrl${iocName}.log -c "${TOP}/procCtrl/iocBoot/iocprocCtrl" \
                -n "PCTRL-DCLink-Reg-${dev}" \
                -i ^D^C \
                'unix:'${PCTRL_SOCK} ./st.cmd &
        echo "# PCtrl: unix:\"${PCTRL_SOCK}\""

done
echo "###################################################################"
sleep infinity
