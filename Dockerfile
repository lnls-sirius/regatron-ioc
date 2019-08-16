# Author: Cláudio Ferreira Carneiro
 # LNLS - Brazilian Synchrotron Light Source Laboratory
 
 FROM  lnlscon/epics-r3.15.6:v1.1
 LABEL maintainer="Claudio Carneiro <claudio.carneiro@lnls.br>"
 
 ENV TZ America/Sao_Paulo
 ENV TOP /opt/cons-topcon
 RUN mkdir -p ${TOP}
 WORKDIR ${TOP}

 COPY configure       configure
 COPY Makefile        Makefile
 COPY iocBoot         iocBoot
 COPY TopConApp       TopConApp

 RUN make clean; make distclean; cd TopConApp/Db; make db; cd ../../; make -j 32

 WORKDIR ${TOP}/iocBoot/iocTopCon
 CMD /usr/local/bin/procServ -L - -f --chdir ${TOP}/iocBoot/iocTopCon ${PORT} ./st.cmd
