
def test_can_fetch_device_id_without_filter(device_groups):
    dg1 = device_groups[0]
    device_ids = dg1.get_device_ids()
    assert(len(device_ids) == 10)

def test_can_fetch_device_id_with_filter(ipv4_stacks):
    ipv4_1 = ipv4_stacks[0]
    ipv4_1.Address.Increment(start_value="10.10.10.10", step_value = "0.0.0.1")
    ipv4_device_ids = ipv4_1.get_device_ids(Address='^(%s)' % ("10.10.10.10"))
    assert(len(ipv4_device_ids) == 1)