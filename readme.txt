Prerequisites:
pom.xml should be present in same folder as script. 

Run script: 
cd pommanager
python updateversion.py

Run Unit test: 
cd pommanager
python -m unittest test_updateversion

Docker:
Docker build –t pommanager .

Todo:
Config file to keep VERSION_FORMAT, LOG_FILE, POM_FILE
