FROM debian:trixie-slim
ENV DEBIAN_FRONTEND=noninteractive

# `time` is required by the esolang-battle-2 worker (/usr/bin/time -v)
# `libc6:i386` and `libstdc++6:i386` are required to run dynamically-linked 32-bit x86 binaries
RUN dpkg --add-architecture i386 && \
    apt-get -y update --fix-missing && \
    apt-get install -y --no-install-recommends time libc6:i386 libstdc++6:i386 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
COPY run.sh /bin/script
RUN chmod +x /bin/script
