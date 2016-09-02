FROM python:3.5
RUN apt-get update && apt-get install libpcap-dev -qy
RUN pip install requests
COPY . /tmp
CMD /bin/bash -c "source /tmp/.env && python /tmp/server.py"