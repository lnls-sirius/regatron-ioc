# Regatron TopCon Quadro TC.P series EPICS IOC

## Docker
```
docker build -t lnlscon/epics-r3.15.6:centos-v1.0 -f Dockerfile.EPICS .
docker build -t lnlscon/cons-topcon:v1.2 -f Dockerfile .
```
Cmds of interest:
```
st-dipoles.cmd  st-quadrupoles.cmd  st-sextupoles.cmd
```

# Drivers
[Digi Connect Me](https://www.digi.com/support/productdetail?pid=2466&type=drivers)
```
1. rpmbuild --rebuild 40002086_Z.src.rpm
2. rpm -i dgrp-1.9-39.i386.rpm
```

