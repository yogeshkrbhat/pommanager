Prerequisites:
    Do "git clone https://github.com/yogeshkrbhat/pommanager.git"

Content:
    pom.xml: Sample pom.xml used to demonstrate the functionality
    updateversion.py: The main script to update the version string in pom
    test_updateversion.py: Unit tests updateversion.py
    requirements.txt: python modules required
    readme.txt: User Guide
    Dockerfile: Docker file to create the image with python and its dependencies

Module Installation
    cd pommanager
    pip install -r requirements.txt

Run script: 
    python updateversion.py

Output/Observations
    Script validates the pom.xml
    Gets branch and org name using PYGIT module
    Updates pom.xml with the new version as needed

Unit test: 
    python -m unittest test_updateversion

Docker:
    Docker build: "docker build –t pommanager ."
    Docker run: "docker -v `pwd`:/data run pommanager python2 /app/pommanager/updateversion.py"

References:
    Python lxml: https://lxml.de/
    Unit test: https://docs.python.org/2/library/unittest.html
    Docker: https://www.docker.com/get-started
    Python2.7 Docker: https://github.com/docker-library/python/tree/39c500cc8aefcb67a76d518d789441ef85fc771f/2.7
    
Todo:
    Config file to keep VERSION_FORMAT, LOG_FILE, POM_FILE
