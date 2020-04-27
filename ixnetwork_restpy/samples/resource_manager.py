"""Demonstrates some best practices for using resource manager to import and export the configuration as json

"""

import json
from ixnetwork_restpy import SessionAssistant, Files


# create a test tool session
session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin', 
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

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
