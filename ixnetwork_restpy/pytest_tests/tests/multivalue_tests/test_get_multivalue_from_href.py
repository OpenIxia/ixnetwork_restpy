import pytest


def test_get_multivalue_from_href(ixnetwork):
    """Test getting a multivalue object using a multivalue href
    """
    ixnetwork.NewConfig()
    vports = ixnetwork.Vport.add()
    eth = ixnetwork.Topology.add(Ports=vports) \
        .DeviceGroup.add(Multiplier=1) \
        .Ethernet.add()
    multivalue_href = eth.Mac._href
    mac = ixnetwork.parent.GetObjectFromHref(multivalue_href)
    assert (multivalue_href == mac._href)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
