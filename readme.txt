Prerequisites:
Create “data” folder in current path with pom.xml. This can be changed by modifying DATA_ROOT in pommanager\updateversion.py. 

Run script: 
python pommanager\updateversion.py

Run Unit test: 
python -m unittest pommanager.test_updateversion

Docker:
Docker build –t pommanager .

Todo:
Config file to keep DATA_ROOT, LOG_FILE, INPUT_POM, OUTPUT_POM initial values
