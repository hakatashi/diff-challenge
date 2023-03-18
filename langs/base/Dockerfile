FROM debian:bookworm-slim
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update --fix-missing && apt-get -y upgrade
RUN apt-get install -y gcc wget

RUN wget https://github.com/ptr-yudai/ptr-SECCON-CTF-2022-Finals/raw/main/koh/heptarchy/challenge/comparator/compare.c
RUN gcc compare.c -o /tmp/compare -O4 -static

WORKDIR /tmp
COPY run.sh /tmp/run.sh
COPY build.sh /tmp/build.sh

ENTRYPOINT ["./run.sh"]
