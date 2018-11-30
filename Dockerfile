FROM python:2.7
RUN mkdir -p /app/pommanager
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
VOLUME /data
RUN ln -s /data/pom.xml /app/pommanager/pom.xml
ENV PYTHONPATH=/app/pommanager
COPY test_updateversion.py /app/pommanager
COPY updateversion.py /app/pommanager
