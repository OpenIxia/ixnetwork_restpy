def test_can_get_object_from_ref(config_assistant):
    vport = config_assistant.config.Vport.add()
    config_assistant.commit()

    vport =  config_assistant.config.Vport.find()[0]

    hardware_port = config_assistant.config._parent.GetObjectFromHref(vport.ConnectedTo)
    assert(hardware_port is None)
