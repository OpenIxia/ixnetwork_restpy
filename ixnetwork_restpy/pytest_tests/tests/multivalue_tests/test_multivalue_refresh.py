import pytest


def test_multivalue_refresh(ixnetwork):
    """Test setting macsec systemid
    """
    ixnetwork.NewConfig()
    vports = ixnetwork.Vport.add()
    eth = ixnetwork.Topology.add(Ports=vports) \
        .DeviceGroup.add(Multiplier=1) \
        .Ethernet.add()
    macsec = eth.StaticMacsec.add()

    # default of macsec systemid multivalue is incrementing counter
    assert(macsec.SystemId.Pattern.startswith('Inc'))

    # set the parent mac object to a single pattern
    eth.Mac.Single('00:00:fa:ce:fa:ce')
    
    # setting systemid to single pattern should not fail
    id = '94:e8:9a:37:26:7b'
    macsec.SystemId.Single(id)
    assert(macsec.SystemId.Values[0] == id)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
