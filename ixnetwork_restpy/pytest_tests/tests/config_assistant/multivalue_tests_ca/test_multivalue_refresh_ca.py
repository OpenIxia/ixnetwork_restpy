import pytest


def test_multivalue_refresh(config_assistant):
    """Test setting macsec systemid
    """
    config = config_assistant.config
    vports = config.Vport.add()
    eth = config.Topology.add(Ports=vports) \
        .DeviceGroup.add(Multiplier=1) \
        .Ethernet.add()
    eth.Mac.Single('00:00:fa:ce:fa:ce')
    macsec = eth.StaticMacsec.add()
    id = '94:e8:9a:37:26:7b'
    macsec.SystemId.Single(id)
    config_assistant.commit()
    eth = config.Topology.find()[0] \
        .DeviceGroup.find()[0] \
        .Ethernet.find()[0]
    macsec = eth.StaticMacsec.find()[0]

    assert(macsec.SystemId.Values[0] == id)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
