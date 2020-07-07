# Regatron TopCon Quadro TC.P series EPICS IOC

## Usage

The IOC will connect to a TCP socket or a serial port. In order to start the IOC in a per device level, use the service:
```
services/cons-regatron-ioc@.service
```
Passing as argument the DCLink number. For example, if we wish to connect to power supply at COM5 we should use:
```
cons-regatron-ioc@5.service
```
This will control a procServ instance at port 20205 that will use the st-05.cmd file.

The st-05.cmd will then estabilish a connection at 'x.x.x.x:20005'. The IOC will not talk directly to the power supply but with an [intermediate software](https://github.com/lnls-sirius/cons-regatron-interface) instead. The final release will use docker containers, the grouping is tbd.

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

## PV namming
[lnls/control-system-constants](https://github.com/lnls-sirius/control-system-constants/blob/master/beaglebone/ip-list.txt)
