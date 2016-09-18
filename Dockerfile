FROM python:2.7
USER root
RUN apt-get update && apt-get install libpcap-dev tcpdump python-crypto libpcap0.8 -qy
ADD . /work
WORKDIR /work
RUN pip install requests scapy
RUN mv /usr/sbin/tcpdump /usr/bin/tcpdump
CMD ["python","server.py"]
