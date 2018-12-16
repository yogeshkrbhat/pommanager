FROM python:2.7
RUN mkdir -p /app/pommanager
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
VOLUME /data
RUN ln -s /data/pom.xml /app/pommanager/pom.xml
ENV PYTHONPATH=/app/pommanager
RUN touch /app/__init__.py
RUN touch /app/pommanager/__init__.py
COPY test_updateversion.py /app/pommanager
COPY updateversion.py /app/pommanager
