def test_can_get_object_from_ref(ixnetwork):
    sessions = ixnetwork._parent
    vport = ixnetwork.Vport.add()

    hardware_port = sessions.GetObjectFromHref(vport.ConnectedTo)
    assert(hardware_port is None)