import pytest

def test_can_configure_bgp_neighbor(ca_vports):
    interface = ca_vports[0].Interface.add(Enabled=True)
    interface.Ipv4.add(Ip='1.1.1.1', Gateway='1.1.1.2')

    bgp = ca_vports[0].Protocols.Bgp
    bgp.Enabled = True 
    neighbor_range = bgp.NeighborRange.add(Interfaces = interface, Enabled = True, EnableBgpId = True)
    ca_vports[2].commit()
    neighbor_range = ca_vports[2].config.Vport.find()[0].Protocols.find().Bgp.NeighborRange
    assert (len(neighbor_range.find()) == 1)

def test_can_add_interfaces(ca_vports):
    interfaces = ca_vports[0].Interface

# add 10 interfaces
    for i in range(1, 11):
	    interfaces.add(Description='Interface Demo %s' % i, Enabled=True)

    ca_vports[2].commit()
    interfaces = ca_vports[2].config.Vport.find()[0].Interface
# verify they have been added on the server
    assert(len(interfaces.find()) == 10)
