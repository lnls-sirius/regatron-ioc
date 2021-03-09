# Regatron TopCon Quadro TC.P series EPICS IOC

In order to update the EPICS db and st.cmd files:
```bash
cd ${TOP}/iocBoot/iocTopCon && python gen_individual.py &&\
    cd ${TOP}/TopConApp/Db && make db
```
This action will not be performed by the Dockerfile, it must be done manually in order to keep the git repository in sync with the container.

## Usage
The st-05.cmd will then establish a connection at 'x.x.x.x:20005'. The IOC will not talk directly to the power supply but with an [intermediate software](https://github.com/lnls-sirius/cons-regatron-interface) instead. The final release will use docker containers, the grouping is tbd.

This design choice is due to a limitation of the available proprietary DLL and the awkwardness of running an IOC natively in a Windows environment.

## Docker
```
docker build -t lnlscon/epics-r3.15.6:centos-v1.0 -f Dockerfile.EPICS .
docker build -t lnlscon/cons-topcon:v1.2 -f Dockerfile .
```
Cmds of interest:
```
st-dipoles.cmd  st-quadrupoles.cmd  st-sextupoles.cmd
```
Some **environment variables** will change behaviours:

|Env|Default|Desc|
|---|---|---|
|EPICS_IOC_CAPUTLOG_INET|0.0.0.0|EPICS Logging Inet (generic)|
|EPICS_IOC_CAPUTLOG_PORT|7012|EPICS Logging Port (generic)|
|EPICS_IOC_LOG_INET|0.0.0.0|EPICS Logging Inet (caput)|
|EPICS_IOC_LOG_PORT|7011|EPICS Logging Port (caput)|
|REGATRON_INTERFACE_MS_HOST|10.128.255.206|cons-regatron-interface Windows Host|
## PV namming
[lnls/control-system-constants](https://github.com/lnls-sirius/control-system-constants/blob/master/beaglebone/ip-list.txt)
