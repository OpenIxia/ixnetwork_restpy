import pytest


def test_select_call_with_list_of_hrefs(ixnetwork):
    ixnetwork.Vport.add().add().add().add()
    vps = ixnetwork.Vport.find()
    assert len(vps) == 4

    ixnetwork.Topology.add(Vports=vps[0:2]).add(Vports=vps[2:])
    tp = ixnetwork.Topology.find(Ports=vps[1].href + "|" + vps[0].href)
    assert len(tp) == 1
    tp = ixnetwork.Topology.find(Ports=vps[3].href + "|" + vps[0].href)
    assert len(tp) == 2


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
