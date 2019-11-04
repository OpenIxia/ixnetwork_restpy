"""Demonstrates some best practices for using resource manager to import and export the configuration as json

"""

import json
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.files import Files


# connect to a test tool platform
test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()
ixnetwork = sessions.ixnetwork
ixnetwork.NewConfig()

# create a configuration fragment of two virtual ports
vports = [
    {
        'xpath': '/vport[1]',
        'name': 'vport 1'
    },
    {
        'xpath': '/vport[2]',
        'name': 'vport 2'
    }
]

# import the configuration fragment as a string
ixnetwork.ResourceManager.ImportConfig(json.dumps(vports), True)
assert(len(ixnetwork.Vport.find()) == 2)

# export the entire configuration as a string
config = ixnetwork.ResourceManager.ExportConfig(['/descendant-or-self::*'], False, 'json')

# import the entire configuration as a string
ixnetwork.ResourceManager.ImportConfig(config, True)
assert(len(ixnetwork.Vport.find()) == 2)

# export the entire configuration as a file
ixnetwork.ResourceManager.ExportConfigFile(['/descendant-or-self::*'], False, 'json', Files('two_vports.json'))

# import then entire configuration from a file
ixnetwork.ResourceManager.ImportConfigFile(Files('two_vports.json'), True)
assert(len(ixnetwork.Vport.find()) == 2)
