import unittest
import os
import shutil

from pommanager.updateversion import read_pom, is_snapshot, update_verion

class BaseJobTestCase(unittest.TestCase):
    pwd = os.getcwd()

    def setUp(self):
        try:
            shutil.rmtree('utest')
        except OSError, e:
            pass
        os.makedirs('utest')
        os.chdir('utest')

    def tearDown(self):
        os.chdir(self.pwd)
        try:
            shutil.rmtree('utest')
        except OSError:
            pass

    def create_file(self, filename, content='', chmod=0644):
        dirname = os.path.dirname(filename)
        if dirname != '' and not os.path.exists(dirname):
            os.makedirs(dirname)
        open(filename, "w").write(content)
        os.chmod(filename, chmod)

    def test_read_pom(self):
        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><groupId>com.wsi.devops</groupId><artifactId>python-test</artifactId><version>1.0-SNAPSHOT</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = read_pom("pom.xml")
        self.assertNotEquals(tree, None)
        self.assertNotEquals(nsmap, None)
        content = r'<error>'
        self.create_file("pom2.xml", content=content)
        #from lxml import etree
        #with self.assertRaises(etree.XMLSyntaxError):
        read_pom("pom2.xml")
        self.assertNotEquals(tree, None)

    def test_is_snapshot(self):
        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><version>1.0-SNAPSHOT</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = read_pom("pom.xml")
        self.assertTrue(is_snapshot(tree, nsmap))

        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><version>1.0</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = read_pom("pom.xml")
        self.assertFalse(is_snapshot(tree, nsmap))

    def test_update_verion(self):
        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><groupId>com.wsi.devops</groupId><artifactId>python-test</artifactId><version>1.0-SNAPSHOT</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = read_pom("pom.xml")
        update_verion(tree, nsmap, "pom_updated.xml")
        tree, nsmap = read_pom("pom_updated.xml")
        version = tree.xpath('.//xmlns:version', namespaces=nsmap)[0]
        self.assertNotEquals(version, 'ci_com.wsi.devops_python-test-SNAPSHOT')
        