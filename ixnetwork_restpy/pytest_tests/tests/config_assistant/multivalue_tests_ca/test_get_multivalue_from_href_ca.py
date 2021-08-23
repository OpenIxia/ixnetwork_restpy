import pytest


def test_get_multivalue_from_href(config_assistant):
    """Test getting a multivalue object using a multivalue href
    """
    config = config_assistant.config
    vports = config.Vport.add()
    eth = config.Topology.add(Ports=vports) \
        .DeviceGroup.add(Multiplier=1) \
        .Ethernet.add()
    config_assistant.commit()
    eth = config.Topology.find()[0] \
        .DeviceGroup.find()[0] \
        .Ethernet.find()[0]
    multivalue_href = eth.Mac._href
    mac = config._parent.GetObjectFromHref(multivalue_href)
    assert (multivalue_href == mac._href)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
