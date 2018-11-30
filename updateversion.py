from lxml import etree
import logging

POM_FILE = 'pom.xml'

logging.basicConfig(level=logging.DEBUG)

def read_pom(file):
    try:
        logging.info("Reading pom xml from %s" % file)
        tree = etree.parse(file)
        nsmap = tree.getroot().nsmap.copy()
        nsmap['xmlns'] = nsmap.pop(None)
    except:
        logging.exception("Error reading pom xml")
        return (None, None)
    return (tree, nsmap)

def is_snapshot(tree, nsmap):
    try:
        version = tree.xpath('.//xmlns:version', namespaces=nsmap)[0]
        if 'SNAPSHOT' in version.text:
            logging.info("Found to be SNAPSHOT pom")
            return True
        logging.info("Not a SNAPSHOT pom")
        return False
    except:
        logging.exception("Error while getting version info")
        raise

def get_repo_n_branch():
    from git import Repo
    g = Repo(".")
    return (g.remotes[0].url.split('/')[-1], g.active_branch.name)

def update_verion(tree, nsmap, file):
    try:
        version = tree.xpath('.//xmlns:version', namespaces=nsmap)[0]
        artifactId = tree.xpath('.//xmlns:artifactId', namespaces=nsmap)[0]
        groupId = tree.xpath('.//xmlns:groupId', namespaces=nsmap)[0]
        version.text = "ci_%s_%s-SNAPSHOT" % get_repo_n_branch()
        tree.write(file)
        logging.info("Created new pom here: %s" % file)
    except:
        logging.exception("Error while updating version")


def main():
    (tree, nsmap) = read_pom(POM_FILE)
    if tree and is_snapshot(tree, nsmap):
        update_verion(tree, nsmap, POM_FILE)
    
if __name__ == '__main__':
    main()
