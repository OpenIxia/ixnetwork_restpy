""" Demonstrates how to create a Linux API Server QuickTest Web session

"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform


test_platform=TestPlatform('10.36.67.212')
test_platform.Authenticate('admin', 'admin')

test_platform.info('Create a linux api server quicktest session')
session = test_platform.Sessions.add(ApplicationType='quicktest')
print(session)
assert(session.ApplicationType == 'quicktest')
session.remove()

test_platform.info('Create a linux api server ixnetwork session')
session = test_platform.Sessions.add(ApplicationType='ixnrest')
print(session)
assert(session.ApplicationType == 'ixnrest')
session.remove()