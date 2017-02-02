FROM ubuntu

RUN apt-get update && apt-get install -y \
    vim \
    python \
    curl && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 3000

ADD webapp/ /webapp/

RUN groupadd -r webapp \
  && useradd -r -g webapp webapp
RUN chown -R webapp:webapp /webapp \
  && chmod -R 777 /webapp


USER webapp
WORKDIR /webapp/
CMD ["python", "httpserver.py"]
