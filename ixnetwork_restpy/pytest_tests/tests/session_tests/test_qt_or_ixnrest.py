import pytest


def test_add_quicktest_session(test_platform):
	if test_platform.Platform == 'linux':
		test_platform.Authenticate('admin','admin')
		test_platform.info('Creating a linux api server quicktest session')
		session = test_platform.Sessions.add(ApplicationType='quicktest')
		assert(session.ApplicationType == 'quicktest')
		session.remove()
	else:
		pytest.skip('Test is not valid for %s platform' % test_platform.Platform)
		
def test_add_ixnrest_session(test_platform):
	if test_platform.Platform == 'linux':	
		test_platform.Authenticate('admin','admin')
		test_platform.info('Creating a linux api server ixnrest session')
		session = test_platform.Sessions.add(ApplicationType='ixnrest')
		assert(session.ApplicationType == 'ixnrest')
		session.remove()
	else:
		pytest.skip('Test is not valid for %s platform' % test_platform.Platform)	