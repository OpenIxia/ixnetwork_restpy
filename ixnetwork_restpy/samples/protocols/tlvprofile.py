"""Demonstrates creating and copying over tlv templates into a tlv profile
"""
from ixnetwork_restpy import SessionAssistant


session = SessionAssistant('127.0.0.1', LogLevel=SessionAssistant.LOGLEVEL_INFO, ClearConfig=True)
ixnetwork = session.Ixnetwork

# create a custom tlv template
generic_tlv = ixnetwork.Globals.Topology.Dhcpv6client \
    .TlvEditor.find() \
    .Template.add(Name='generic') \
    .Tlv.add(Name='generic')
generic_tlv.Type.update(Name='type').Object.add(Name='type').Field.add(Name='type').Value.Single('10')
generic_tlv.Length.update(Name='length').Value.Single('11')
generic_tlv.Value.update(Name='value').Object.add(Name='value').Field.add(Name='value').Value.Single('12')
ixnetwork.info(generic_tlv)

# get a default tlv template
option_request = ixnetwork.Globals.Topology.Dhcpv6client \
    .TlvEditor.find() \
    .Defaults.find() \
    .Template.find() \
    .Tlv.find(Name='Option Request')
ixnetwork.info(option_request)

# get the dhcpv6client tlv profile
tlv_profile = ixnetwork.Topology.add() \
    .DeviceGroup.add() \
    .Ethernet.add() \
    .Dhcpv6client.add() \
    .TlvProfile.find()
ixnetwork.info(tlv_profile)

# copy tlv templates into the dhcpv6client tlv profile
generic_tlv = ixnetwork.parent.GetObjectFromHref(tlv_profile.CopyTlv(generic_tlv))
option_request = ixnetwork.parent.GetObjectFromHref(tlv_profile.CopyTlv(option_request))

# print option request tlv sub options
for sub_option in option_request.Value.Object.find().Field.find():
    ixnetwork.info(sub_option)

