FROM debian:latest

RUN apt update && apt upgrade -y
RUN pip3 install -r requirements.txt
CMD python3 -m LegendGirl
