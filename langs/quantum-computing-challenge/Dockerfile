FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade

RUN apt-get install -y python3 python3-pip python3-venv

RUN python3 -m venv /opt/venv

# Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install pennylane

WORKDIR /tmp
COPY run.sh /tmp/run.sh
COPY run.sh /bin/script
COPY util.py /tmp/util.py
COPY sanitizer.py /tmp/sanitizer.py

RUN chmod +x /tmp/run.sh /bin/script