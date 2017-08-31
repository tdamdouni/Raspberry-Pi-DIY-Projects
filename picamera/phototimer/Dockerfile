FROM alexellis2/raspistill:latest
ENTRYPOINT []
RUN apt-get update -qy && apt-get install -qy python
COPY . .

VOLUME /var/image/

CMD ["python", "take.py", "60"]
