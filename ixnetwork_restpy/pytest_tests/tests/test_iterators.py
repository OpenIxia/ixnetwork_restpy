def test_can_add_remove_containers (ixnetwork):
    ixnetwork.Vport.add().add()
    vports = ixnetwork.Vport.find()
    assert(len(vports) == 2)

    vports.remove()

    assert(len(ixnetwork.Vport.find()) == 0)

