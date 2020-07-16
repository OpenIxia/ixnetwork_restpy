def test_can_set_incremental_port_step_ipv4_address(vports):
    vport_1, vport_2 = vports
    ixnetwork = vport_1._parent
    topo = ixnetwork.Topology.add(Vports=vports)
    ipv4_1 = topo.DeviceGroup.add(Multiplier=1).\
        Ethernet.add().\
        Ipv4.add()
    address_obj = ipv4_1.Address
    address_obj.Increment(start_value='1.1.1.1',step_value='0.0.0.0')
    # setting port step
    address_obj.Steps.Step = '1.0.0.0'
    assert address_obj.Values[1] == '2.1.1.1'
    assert address_obj.Steps.Step == '1.0.0.0'

def test_can_disbale_port_step(vports):
    vport_1, vport_2 = vports
    ixnetwork = vport_1._parent
    topo = ixnetwork.Topology.add(Vports=vports)
    ipv4_1 = topo.DeviceGroup.add(Multiplier=1). \
        Ethernet.add(). \
        Ipv4.add()
    address_obj = ipv4_1.Address
    address_obj.Increment(start_value='1.1.1.1', step_value='0.0.0.0')
    # setting port step
    address_obj.Steps.Step = '1.0.0.0'
    address_obj.Steps.Enabled = False
    assert address_obj.Values[1] == '1.1.1.1'
    assert address_obj.Steps.Enabled == False

def test_port_step_can_retrieve_owner(vports):
    vport_1, vport_2 = vports
    ixnetwork = vport_1._parent
    topo = ixnetwork.Topology.add(Vports=vports)
    ipv4_1 = topo.DeviceGroup.add(Multiplier=1). \
        Ethernet.add(). \
        Ipv4.add()
    address_obj = ipv4_1.Address
    address_obj.Increment(start_value='1.1.1.1', step_value='0.0.0.0')
    # setting port step
    owner = address_obj.Steps.Owner
    assert owner.split('/')[-2] == 'topology'

def test_port_step_can_retrieve_description(vports):
    vport_1, vport_2 = vports
    ixnetwork = vport_1._parent
    topo = ixnetwork.Topology.add(Vports=vports)
    ipv4_1 = topo.DeviceGroup.add(Multiplier=1). \
        Ethernet.add(). \
        Ipv4.add()
    address_obj = ipv4_1.Address
    address_obj.Increment(start_value='1.1.1.1', step_value='0.0.0.0')
    # setting port step
    desc = address_obj.Steps.Description
    assert desc.lower() == 'port step'

