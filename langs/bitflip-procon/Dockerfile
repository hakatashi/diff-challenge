FROM debian:trixie-slim
ENV DEBIAN_FRONTEND=noninteractive

# `time` is required by the esolang-battle-2 worker (/usr/bin/time -v)
RUN apt-get -y update --fix-missing && \
    apt-get install -y --no-install-recommends time && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
COPY run.sh /bin/script
RUN chmod +x /bin/script
