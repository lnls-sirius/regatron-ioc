# Author: Cláudio Ferreira Carneiro
# LNLS - Brazilian Synchrotron Light Source Laboratory
 
FROM  lnlscon/epics-r3.15.6:v1.2
LABEL maintainer="Claudio Carneiro <claudio.carneiro@lnls.br>"

RUN apt-get update && apt-get -y install gettext-base python3

ENV TZ America/Sao_Paulo
ENV TOP /opt/cons-topcon
RUN mkdir -p ${TOP}
WORKDIR ${TOP}

COPY configure       configure
COPY Makefile        Makefile
COPY iocBoot         iocBoot
COPY TopConApp       TopConApp

RUN envsubst < configure/RELEASE.tmplt > configure/RELEASE &&\
    make clean; make distclean; \
    cd iocBoot/iocTopCon; ./gen.py;  cd ../../; \
    cd TopConApp/Db; make db; cd ../../; \
    make

WORKDIR ${TOP}/iocBoot/iocTopCon
CMD /usr/local/bin/procServ -L - -f --chdir ${TOP}/iocBoot/iocTopCon ./${CMD}
