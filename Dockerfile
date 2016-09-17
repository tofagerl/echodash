FROM python:2.7
RUN apt-get update && apt-get install libpcap-dev tcpdump python-crypto libpcap0.7 -qy
RUN pip install requests scapy
ADD . /work
WORKDIR /work
CMD ["/bin/bash","start.sh"]
