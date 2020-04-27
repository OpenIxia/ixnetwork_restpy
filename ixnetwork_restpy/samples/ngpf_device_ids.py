"""Demonstrates some best practices for specifying device ids when executing ngpf operations

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# create a b2b ngpf scenario
vport_1 = ixnetwork.Vport.add().add().add()
print(vport_1)
vport_2 = ixnetwork.Vport.add()
topologies = ixnetwork.Topology.add(Vports=vport_1).add(Vports=vport_2)
ipv4_1 = topologies[0].DeviceGroup.add().Ethernet.add().Ipv4.add()
igmp_host = ipv4_1.IgmpHost.add()
ipv4_2 = topologies[1].DeviceGroup.add().Ethernet.add().Ipv4.add()
igmp_querier = ipv4_2.IgmpQuerier.add()

# set the port step on the address
address = ipv4_1.Address
print(address.Steps)
address.Steps.Step = '1.1.1.1'
assert(address.Steps.Step == '1.1.1.1')

# get device ids for two specific ip addresses
ipv4_device_ids = ipv4_1.get_device_ids(Address='^(%s|%s)' % (ipv4_1.Address.Values[6], ipv4_1.Address.Values[24]))
assert(len(ipv4_device_ids) == 2)

# get device ids on two specific ports
port_device_ids = ipv4_1.get_device_ids(PortNames='^(%s|%s)$' % (vport_1[0].Name, vport_1[2].Name))
assert(len(port_device_ids) == 20)

# get device ids for igmp v2 hosts on a specific port
v2_device_ids = igmp_host.get_device_ids(PortNames='(?i)^%s$' % (vport_1[1].Name), VersionType='(?i)version2')
assert(len(v2_device_ids) == 10)

# stop all devices
ipv4_1.Stop()

# start only a few devices
ipv4_1.Start(ipv4_device_ids)

# leave
igmp_host.IgmpMcastIPv4GroupList.IgmpLeaveGroup("1-4;6")

# issue a join on only a few devices
igmp_host.IgmpMcastIPv4GroupList.Join(v2_device_ids)




