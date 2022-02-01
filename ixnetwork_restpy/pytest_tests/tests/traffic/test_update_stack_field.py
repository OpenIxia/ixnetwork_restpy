import pytest


def test_update_stack_field(ixnetwork):
    """Tests that server based SDMObjIdPiece instance ids that are either
    strings or integers are correctly translated to integer rest ids.
    """
    vport_1 = ixnetwork.Vport.add()
    vport_2 = ixnetwork.Vport.add()
    traffic_item = ixnetwork.Traffic.TrafficItem.add(
        Name="Update Stack Field Test",
        TrafficType="raw",
        TrafficItemType="l2L3",
    )
    traffic_item.EndpointSet.add(
        Sources=vport_1.Protocols.find(),
        Destinations=vport_2.Protocols.find(),
    )
    for field in traffic_item.ConfigElement.find().Stack.find().Field.find():
        field.update(ValueType="singleValue", SingleValue=field.ValueList[0])


if __name__ == "__main__":
    pytest.main(
        [
            "-v",
            "-s",
            "--server",
            "localhost:11009:windows",
            __file__,
        ]
    )
