import unittest

class TestPackageIntegrity(unittest.TestCase):
    def testErrorPackage(self):
        try:
            import ixnetwork_restpy.errors
        except:
            raise Exception('Issue with Error Package')
    
    def testBasePackage(self):
        try:
            import ixnetwork_restpy.base
        except:
            raise Exception('Issue with Base Package')

    def testConnectionPackage(self):
        try:
            import ixnetwork_restpy.connection
        except:
            raise Exception('Issue with Connection Package')

    def testFilesPackage(self):
        try:
            import ixnetwork_restpy.files
        except:
            raise Exception('Issue with Files package')

    def testMultivaluePackage(self):
        try:
            import ixnetwork_restpy.multivalue
        except:
            raise Exception('Issue with Multivalue Package')
    
    def testSelectPackage(self):
        try:
            import ixnetwork_restpy.select
        except:
            raise Exception('Issue with Select Package')

    def testStepsPackage(self):
        try:
            import ixnetwork_restpy.steps
        except:
            raise Exception('Issue with steps package')
    
if __name__ == '__main__':
    unittest.main()