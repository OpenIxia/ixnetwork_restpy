from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.files import Files
try:
    from ixnetwork_restpy.assistants.statistics.statviewassistant import StatViewAssistant
    from ixnetwork_restpy.assistants.ports.portmapassistant import PortMapAssistant
    from ixnetwork_restpy.assistants.sessions.sessionassistant import SessionAssistant
except Exception as e:
    print('non-generated class usage for generator build...')