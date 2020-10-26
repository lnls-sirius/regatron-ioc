# Author: Cláudio Ferreira Carneiro
# LNLS - Brazilian Synchrotron Light Source Laboratory
FROM  lnlscon/epics-r3.15.8:v1.1 as base
LABEL maintainer="Claudio Carneiro <claudio.carneiro@lnls.br>"

RUN apt-get update && apt-get -y install gettext-base socat procps

# Epics auto addr list
ENV EPICS_CA_AUTO_ADDR_LIST YES

# Base procServ port
ENV EPICS_IOC_CAPUTLOG_INET 0.0.0.0
ENV EPICS_IOC_CAPUTLOG_PORT 7012

ENV EPICS_IOC_LOG_INET 0.0.0.0
ENV EPICS_IOC_LOG_PORT 7011
ENV REGATRON_INTERFACE_MS_HOST 10.128.255.206

ENV TOP /opt/cons-topcon

RUN \
    mkdir -p ${TOP}/autosave/save &&\
    mkdir -p ${TOP}/log &&\
    mkdir -p ${TOP}/sockets

WORKDIR ${TOP}

COPY entrypoint.sh entrypoint.sh
COPY configure     configure
COPY Makefile      Makefile
COPY iocBoot       iocBoot
COPY TopConApp     TopConApp

RUN envsubst < configure/RELEASE.tmplt > configure/RELEASE &&\
    make clean; make distclean; \
    cd ${TOP} && make

CMD [ "/bin/bash", "/opt/cons-topcon/entrypoint.sh"]

FROM base AS test
RUN apt install -y vim
ENV INFO "Regatron DCLinks - Test"
ENV DEVS ""
ENV REGATRON_INTERFACE_MS_HOST 0.0.0.0

FROM base AS dipoles
ENV INFO "Regatron DCLinks - DIPOLES"
ENV DEVS "101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116"

FROM base AS quadrupoles
ENV INFO "Regatron DCLinks - QUADRUPOLES"
ENV DEVS "117 118 119 120 121 122 123 124 125 126"

FROM base AS sextupoles
ENV INFO "Regatron DCLinks - SEXTUPOLES"
ENV DEVS "127 128 129 130 131 132 133 134 135 136 137 138 139 140"

