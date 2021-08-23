import pytest


def test_multivalue_valuelist(config_assistant):
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

    config = config_assistant.config
    vports = config.Vport.add()
    eth = config.Topology.add(Ports=vports) \
        .DeviceGroup.add(Multiplier=3) \
        .Ethernet.add()

    mac = eth.Mac
        
    # list of values
    mac.ValueList(values)
    config_assistant.commit()
    eth = config.Topology.find() \
        .DeviceGroup.find() \
        .Ethernet.find()
    mac = eth.Mac

    assert(mac.Values == values)

    # a file object
    with open(values_filename, 'r') as fp:
        mac.ValueList(fp)
    config_assistant.commit()
    eth = config.Topology.find() \
        .DeviceGroup.find() \
        .Ethernet.find()
    mac = eth.Mac
    assert(mac.Values == values)

    # a filename
    mac.ValueList(values_filename)
    config_assistant.commit()
    eth = config.Topology.find() \
        .DeviceGroup.find() \
        .Ethernet.find()
    mac = eth.Mac
    assert(mac.Values == values)


