import pytest


def test_add_vports(ixnetwork):
    """
        vports can be added from client
    
    :given: session: an ixnetwork session
    :when: perform vport add operation
    :then: should create a vport
    """
    vport_1 = ixnetwork.Vport.add()
    assert len(vport_1) == 1
    vport_2 = ixnetwork.Vport.add()
    assert len(vport_2) == 1
    # testing recursive add calls
    vports = ixnetwork.Vport.add().add()
    assert len(vports) == 2

    # testing total number of ports
    assert len(ixnetwork.Vport.find()) == 4


def test_can_change_vport_attributes(vports):
    """
        vport attributes can be changed from client
    
    :given: session: a couple of vports
    :when: perform vport attributes operation
    :then: should edit a vport
    """
    vport_1,vport_2 = vports
    vport_1.TxMode = 'sequential'
    vport_1.TransmitIgnoreLinkStatus=True
    vport_1.L1Config.Ethernet.Media = 'fiber'
    vport_1.L1Config.Ethernet.AutoNegotiate = False
    vport_1.L1Config.CurrentType = 'krakenFourHundredGigLan'


def test_can_change_uppercase_property_names(vports):
    """
        attributes that have uppercase python class property names  
        and uppercase rest api property names should not raise an error
        when patched

    :given: session: a couple of vports
    :when: perform FilterPallette attributes operation
    :then: should successfully be patched
    """
    vport_1,vport_2 = vports
    vport_1.Capture.FilterPallette.DA1 = '00:00:de:ad:be:ef'
    vport_1.Capture.FilterPallette.update(DA1='00:00:de:ad:be:ef')


def test_can_remove_vport(ixnetwork):
    """
        vport can be deleted from client

    :given: session: a couple of vports
    :when: perform vport remove operation
    :then: should delete a vport
    """
    vport_1 = ixnetwork.Vport.add()
    vport_2 = ixnetwork.Vport.add()

    assert len(ixnetwork.Vport.find()) == 2

    vport_1.remove()
    assert len(ixnetwork.Vport.find()) == 1
    vport_2.remove()
    assert len(ixnetwork.Vport.find()) == 0


def test_can_add_lag_ports(ixnetwork):
    """
        vports can be added to a lag

    :given: session: a couple of vports
    :when: perform lag add operation
    :then: should add vports 
    """
    vports = ixnetwork.Vport.add().add()
    lag = ixnetwork.Lag.add(Name='Lag 1', Vports=vports)
    lag.ProtocolStack.add().Ethernet.add().Lagportlacp.add()
    assert(len(lag.Vports) == 2)