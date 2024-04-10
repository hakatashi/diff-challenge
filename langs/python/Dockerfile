FROM hakatashi/diff-challenge-base

RUN apt-get update && apt-get install -y git build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev curl \
  libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
RUN git clone https://github.com/pyenv/pyenv.git .pyenv
RUN .pyenv/bin/pyenv install 3.12.2

COPY build.sh /tmp/build.sh
RUN chmod +x /tmp/build.sh

RUN cp -f /tmp/run.sh /bin/script
