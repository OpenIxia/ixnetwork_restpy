from ixnetwork_restpy.assistants.batch.batchadd import BatchAdd
import pytest


def test_quick_flow_traffic(ixnetwork):
    vport1 = ixnetwork.Vport.add(Name="Port1")
    vport2 = ixnetwork.Vport.add(Name="Port2")
    traffic_item = ixnetwork.Traffic.TrafficItem.add(
        TrafficType="raw", TrafficItemType="quick"
    )
    for i in range(2):
        traffic_item.EndpointSet.add(
            Sources=vport1.Protocols.find(), Destinations=vport2.Protocols.find()
        )
        hls = traffic_item.HighLevelStream.find()[-1]
        hls.update(Name="hls" + str(i + 1))
        hls.FrameRate.update(Type="framesPerSecond", Rate=10)
        hls.FrameSize.update(Type="fixed", FixedSize=500)
        hls.TransmissionControl.update(Type="fixedFrameCount", FrameCount=10)
        eth_st = hls.Stack.find(StackTypeId="ethernet")
        eth_st.Field.find(FieldTypeId="ethernet.header.destinationAddress").update(
            FieldValue="00:0c:29:68:05:1E"
        )
        eth_st.Field.find(FieldTypeId="ethernet.header.sourceAddress").update(
            FieldValue="00:00:29:68:05:1E"
        )


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--server", "localhost:11009:windows", __file__])
