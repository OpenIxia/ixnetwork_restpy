
def test_can_fetch_device_id_without_filter(config_assistant):
    config = config_assistant.config
    vport = config.Vport.add()
    topology = config.Topology.add(Vports = vport)
    device_group = topology.DeviceGroup.add()
    dg1 = device_group
    config_assistant.commit()
    device_ids = dg1.get_device_ids()
    assert(len(device_ids) == 10)

def test_can_fetch_device_id_with_filter(ca_ipv4_stacks):
    ipv4_1 = ca_ipv4_stacks[0]
    ipv4_1.Address.Increment(start_value="10.10.10.10", step_value = "0.0.0.1")
    config_assistant = ca_ipv4_stacks[2]
    config_assistant.commit()
    ipv4_1 = config_assistant.config.Topology.find()[0].DeviceGroup.find()[0].Ethernet.find()[0].Ipv4.find()[0]
    ipv4_device_ids = ipv4_1.get_device_ids(Address='^(%s)' % ("10.10.10.10"))
    assert(len(ipv4_device_ids) == 1)
