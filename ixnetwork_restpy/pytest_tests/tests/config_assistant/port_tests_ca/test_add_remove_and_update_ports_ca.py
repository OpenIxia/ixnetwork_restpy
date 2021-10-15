import pytest


def test_add_vports(config_assistant):
    """
        vports can be added from client

    :given: session: an config_assistant session
    :when: perform vport add operation
    :then: should create a vport
    """
    config = config_assistant.config
    vport_1 = config.Vport.add()[-1]
    assert len(vport_1) == 1
    vport_2 = config.Vport.add()[-1]
    assert len(vport_2) == 1

    # testing recursive add calls
    vports = config.Vport.add().add()
    assert len(vports) == 4
    config_assistant.commit()

    # checking if hrefs are getting filled properly
    assert vport_1.href == "/api/v1/sessions/1/ixnetwork/vport/1"
    assert vport_2.href == "/api/v1/sessions/1/ixnetwork/vport/2"

    # testing total number of ports
    assert len(config.Vport.find()) == 4
    for vport in config.Vport:
        assert "xpath" in vport._properties


def test_can_change_vport_attributes(config_assistant):
    """
        vport attributes can be changed from client

    :given: session: a couple of vports
    :when: perform vport attributes operation
    :then: should edit a vport
    """
    config = config_assistant.config
    vport_1 = config.Vport.add()
    vport_1.TxMode = "sequential"
    vport_1.TransmitIgnoreLinkStatus = True
    vport_1.L1Config.Ethernet.Media = "fiber"
    vport_1.L1Config.Ethernet.AutoNegotiate = False
    config_assistant.commit()
    # checking if the change was reflected properly
    vport = config.Vport.find()
    l1Config = vport.L1Config
    assert vport.TxMode == "sequential"
    assert vport.TransmitIgnoreLinkStatus
    assert l1Config.Ethernet.Media == "fiber"
    assert not l1Config.Ethernet.AutoNegotiate

    vport_1.L1Config.CurrentType = "krakenFourHundredGigLan"
    config_assistant.commit()
    l1Config = vport_1.L1Config
    assert l1Config.CurrentType == "krakenFourHundredGigLan"


def test_can_change_uppercase_property_names(config_assistant):
    """
        attributes that have uppercase python class property names
        and uppercase rest api property names should not raise an error
        when patched

    :given: session: a couple of vports
    :when: perform FilterPallette attributes operation
    :then: should successfully be patched
    """
    config = config_assistant.config
    vport_1 = config.Vport.add()
    vport_1.Capture.FilterPallette.DA1 = "00:00:de:ad:be:ef"
    config_assistant.commit()
    filterPallette = config.Vport.find()[0].Capture.FilterPallette
    assert filterPallette.DA1 == "00:00:de:ad:be:ef"
    vport_1.Capture.FilterPallette.DA1 = "00:00:de:ad:be:ef"
    config_assistant.commit()
    filterPallette = config.Vport.find()[0].Capture.FilterPallette
    assert filterPallette.DA1 == "00:00:de:ad:be:ef"


# def test_can_add_lag_ports(ixnetwork):
#     """
#         vports can be added to a lag
#
#     :given: session: a couple of vports
#     :when: perform lag add operation
#     :then: should add vports
#     """
#     vports = ixnetwork.Vport.add().add()
#     lag = ixnetwork.Lag.add(Name='Lag 1', Vports=vports)
#     lag.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
#     assert (len(lag.Vports) == 2)


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
