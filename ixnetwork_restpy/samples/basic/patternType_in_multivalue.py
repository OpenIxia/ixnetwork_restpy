"""
Demonstrates how pattern type property can be used for info or to modify exsisting multivalue instance
"""

from ixnetwork_restpy import SessionAssistant

session_assistant = SessionAssistant(
    IpAddress="127.0.0.1",
    UserName="admin",
    Password="admin",
    LogLevel=SessionAssistant.LOGLEVEL_INFO,
    ClearConfig=True,
)

ixnetwork = session_assistant.Ixnetwork

# adding ipv4 stack
ipv4 = ixnetwork.Topology.add().DeviceGroup.add().Ethernet.add().Ipv4.add()

# fetching ipv4 address multivalue object
address = ipv4.Address

# fetching Pattern type for Multivalue instance
ixnetwork.info(address.PatternType)

# modifying multivalue based on pattern type
if address.PatternType == "Increment":
    address.Increment(start_value="1.1.1.1", step_value="1.0.0.0")

elif address.PatternType == "Decrement":
    address.Decrement(start_value="100.1.1.1", step_value="1.0.0.0")
