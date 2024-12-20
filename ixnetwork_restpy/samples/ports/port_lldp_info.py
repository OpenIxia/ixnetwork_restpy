"""
The test basically explain how we can get LLDP information from chassis and port level
"""

from ixnetwork_restpy import SessionAssistant
import time


def main():
    chassis_ip = "10.39.49.58"
    # creating a test tool session
    session_assistant = SessionAssistant(
        IpAddress="10.39.39.205",
        RestPort=11009,
        LogLevel=SessionAssistant.LOGLEVEL_INFO,
        ClearConfig=True,
    )
    ixnetwork = session_assistant.Ixnetwork
    ixnetwork.info("Session created")

    ixnetwork.info("Adding chassis/location")
    ixnetwork.Locations.add(Hostname=chassis_ip)

    # waiting for the State of chassis to be 'Ready'
    while ixnetwork.Locations.find()[0].State != "ready":
        time.sleep(1)

    # LLDP properties from chassis/location
    locations = ixnetwork.Locations.find()
    obj = locations[0]
    print("\n\nLLDP Peer Info learned from " + chassis_ip + ".......\n")
    # Filter attributes
    attributes = [attr for attr in dir(obj) if attr.startswith("Peer")]
    print_data_table(obj, attributes)

    # LLDP info from all ports
    ports = locations[0].Ports.find()
    for port in ports:
        obj = port
        print("\n\nLLDP Peer Info learned from " + port.Location + " .......\n")
        # Filter attributes
        attributes = [attr for attr in dir(obj) if attr.startswith("Peer")]
        print_data_table(obj, attributes)


def print_data_table(obj, attributes):
    # Extract attribute values
    data = {attr: getattr(obj, attr, None) for attr in attributes}
    # Determine column widths
    max_attr_width = max(len(attr) for attr in data.keys())
    max_value_width = max(len(str(value)) for value in data.values())
    # Print table headers
    header = f"{'Attribute'.ljust(max_attr_width)} | {'Value'.ljust(max_value_width)}"
    separator = f"{'-' * max_attr_width}-+-{'-' * max_value_width}"
    print(header)
    print(separator)
    # Print table rows
    for attr, value in data.items():
        print(f"{attr.ljust(max_attr_width)} | {str(value).ljust(max_value_width)}")


if __name__ == "__main__":
    main()
