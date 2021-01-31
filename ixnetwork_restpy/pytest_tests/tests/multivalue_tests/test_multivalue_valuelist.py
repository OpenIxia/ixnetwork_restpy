import pytest


def test_multivalue_valuelist(ixnetwork):
    """Test setting valuelist using all possible variants
    """
    # setup a list of values
    values = [
        "00:00:00:00:00:0a",
        "00:00:00:00:00:0b",
        "00:00:00:00:00:0c"
    ]
    values_filename = './values.text'
    with open(values_filename, 'w') as fp:
        fp.write('\n'.join(values))

    ixnetwork.NewConfig()
    vports = ixnetwork.Vport.add()
    eth = ixnetwork.Topology.add(Ports=vports) \
        .DeviceGroup.add(Multiplier=3) \
        .Ethernet.add()

    mac = eth.Mac
        
    # list of values
    mac.ValueList(values)
    assert(mac.Values == values)

    # a file object
    with open(values_filename, 'r') as fp:
        mac.ValueList(fp)
    assert(mac.Values == values)

    # a filename
    mac.ValueList(values_filename)
    assert(mac.Values == values)


if __name__ == '__main__':
    pytest.main(['--server', '10.36.67.225:11009:windows', '-s', __file__])
