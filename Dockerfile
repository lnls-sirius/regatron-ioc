# Author: Cláudio Ferreira Carneiro
# LNLS - Brazilian Synchrotron Light Source Laboratory
FROM  lnlscon/epics-r3.15.8:v1.0
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
    cd ${TOP}/iocBoot/iocTopCon && python gen_individual.py &&\
    cd ${TOP}/TopConApp/Db && make db &&\
    cd ${TOP} && make

CMD [ "/bin/bash", "/opt/cons-topcon/entrypoint.sh"]
