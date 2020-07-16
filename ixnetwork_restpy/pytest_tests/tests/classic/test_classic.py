import pytest

def test_can_configure_bgp_neighbor(vports):
    interface = vports[0].Interface.add(Enabled=True)
    interface.Ipv4.add(Ip='1.1.1.1', Gateway='1.1.1.2')

    bgp = vports[0].Protocols.find().Bgp
    bgp.Enabled = True 
    neighbor_range = bgp.NeighborRange.add(Interfaces = interface, Enabled = True, EnableBgpId = True)

    assert (len(neighbor_range.find()) == 1)

def test_can_add_interfaces(vports):
    interfaces = vports[0].Interface

# add 10 interfaces
    for i in range(1, 11):
	    interfaces.add(Description='Interface Demo %s' % i, Enabled=True)

# verify they have been added on the server
    assert(len(interfaces.find()) == 10)