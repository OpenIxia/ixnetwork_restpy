"""Demonstrates different types of patterns that can be set in
	TestPlatform.Sessions.IxNetwork.Topology...Multivalue objects

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# add virtual ports
vports = ixnetwork.Vport.add().add().add().add()
vports.info(vports)

# add ipv4 devices
ipv4 = ixnetwork.Topology.add(Ports=vports).DeviceGroup.add(Multiplier=10).Ethernet.add().Ipv4.add()

# set single multivalue
ipv4.Address.Single('6.6.6.6')
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern == '6.6.6.6')

# add overlays
ipv4.Address.Overlay(3, '1.2.3.4')
ipv4.Address.Overlay(6, '4.3.2.1')

# set increment multivalue
ipv4.Address.Increment(start_value='7.7.7.7', step_value='8.8.8.8')
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('Inc:') is True)

# set decrement multivalue
ipv4.Address.Decrement(start_value='6.6.6.6', step_value='5.5.5.5')
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('Dec:') is True)

# set custom multivalue
ipv4.Address.Custom(start_value='6.6.6.6', step_value='5.5.5.5', increments=[('3.3.3.3', 12, [('2.2.2.2', 20, [])])])
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('Custom:') is True)

# set valuelist multivalue
ipv4.Address.ValueList(['10.10.10.10', '11.11.11.11'])
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('List:') is True)

# set random multivalue
ipv4.Address.Random()
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('Rand') is True)

# set repeatable random range multivalue
ipv4.Address.RandomRange(min_value='1.1.1.1', max_value='2.2.2.2', step_value='0.0.0.1', seed=7)
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('Randr:') is True)

# set repeatable random multivalue
ipv4.Address.RandomMask(fixed_value='1.1.1.1', mask_value='0.0.0.1', seed=7, count=6)
ipv4.info(ipv4.Address)
assert(ipv4.Address.Pattern.startswith('Randb:') is True)
