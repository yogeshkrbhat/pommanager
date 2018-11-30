Prerequisites:
1. Do "git clone https://github.com/yogeshkrbhat/pommanager.git"
2. pom.xml should be present in same folder as script. 

Run script: 
cd pommanager
python updateversion.py

Output
Script validates the pom.xml
Gets branch and org name using PYGIT module
Updates pom.xml with the new version as needed

Run Unit test: 
cd pommanager
python -m unittest test_updateversion

Docker:
Docker build –t pommanager .

Todo:
Config file to keep VERSION_FORMAT, LOG_FILE, POM_FILE
