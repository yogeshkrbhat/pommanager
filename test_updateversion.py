import unittest
import os
import shutil
import mock

from updateversion import validate_pom, is_snapshot, update_verion, get_repo_n_branch

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

    def test_validate_pom(self):
        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><groupId>com.wsi.devops</groupId><artifactId>python-test</artifactId><version>1.0-SNAPSHOT</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = validate_pom("pom.xml")
        self.assertNotEquals(tree, None)
        self.assertNotEquals(nsmap, None)
        
        content = r'<error>'
        self.create_file("pom2.xml", content=content)
        #from lxml import etree
        #with self.assertRaises(etree.XMLSyntaxError):
        validate_pom("pom2.xml")
        self.assertNotEquals(tree, None)
        
        tree, nsmap = validate_pom("NO_File")
        self.assertEquals(tree, None)

    def test_is_snapshot(self):
        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><version>1.0-SNAPSHOT</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = validate_pom("pom.xml")
        self.assertTrue(is_snapshot(tree, nsmap))

        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><version>1.0</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = validate_pom("pom.xml")
        self.assertFalse(is_snapshot(tree, nsmap))

    def test_update_verion(self):
        content = r'<project xmlns="http://maven.apache.org/POM/4.0.0"><groupId>com.wsi.devops</groupId><artifactId>python-test</artifactId><version>1.0-SNAPSHOT</version></project>'
        self.create_file("pom.xml", content=content)
        tree, nsmap = validate_pom("pom.xml")
        update_verion(tree, nsmap, "pom_updated.xml")
        tree, nsmap = validate_pom("pom_updated.xml")
        version = tree.xpath('.//xmlns:version', namespaces=nsmap)[0]
        self.assertNotEquals(version, 'ci_com.wsi.devops_python-test-SNAPSHOT')
    
    @mock.patch('git.Repo')
    def test_get_repo_n_branch(self, repo):
        repo.return_value.active_branch.name = "master"
        repo.return_value.remotes[0].url = "https://github.com/Team_Foo/pommanager.git"
        (orgname, branch) = get_repo_n_branch()
        self.assertEquals(orgname, "Team_Foo")
        self.assertEquals(branch, "master")
        
        