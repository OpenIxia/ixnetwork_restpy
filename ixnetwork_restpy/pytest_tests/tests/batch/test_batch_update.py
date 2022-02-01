from ixnetwork_restpy import BatchUpdate


def test_batch_update(ixnetwork):
    vports = ixnetwork.Vport
    for i in range(0, 10):
        vports.add()
    with BatchUpdate(ixnetwork):
        for vport in vports:
            vport.Name = vport.href
            vport.TxMode = "sequential"
            vport.RxMode = "captureAndMeasure"
            vport.TraceEnabled = False
            vport.TraceLevel = "kError"
            vport.TransmitIgnoreLinkStatus = True
            vport.Type = "novusHundredGigLan"
    with BatchUpdate(ixnetwork):
        for vport in vports:
            interface = vport.L1Config.NovusHundredGigLan
            interface.EnablePPM = False
            interface.AutoInstrumentation = "floating"
            interface.EnablePPM = False
            interface.EnableRsFec = False
            interface.EnableRsFecStats = False
            interface.RsFecAdvertise = True


if __name__ == "__main__":
    import pytest

    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
