FROM opencog/redux-os:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
apt install -y python3-pip python3-tk && \
pip3 install -r requirements.txt && \
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && \
apt install -y swi-prolog && \
apt install -y gcc


