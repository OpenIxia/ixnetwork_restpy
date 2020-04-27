"""Demonstrates an approach for clearing ownership on vports that are connected 
by using the Vport.ConnectedTo reference and obtaining the Port object which has the ClearOwnership method

"""
from ixnetwork_restpy import SessionAssistant


session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    UserName='admin', Password='admin',
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# add a chassis
chassis = ixnetwork.AvailableHardware.Chassis.add(Hostname='10.36.74.17')

# add abstract ports and connect them to chassis ports
card = chassis.Card.find(CardId=1)
for port in card.Port.find():
	ixnetwork.Vport.add(ConnectedTo=port)

# clear the ownership on the port using a reference returned by the Vport.ConnectedTo property
for vport in ixnetwork.Vport.find():
	port = session_assistant.Session.GetObjectFromHref(vport.ConnectedTo)
	if port is not None:
		port.ClearOwnership()


