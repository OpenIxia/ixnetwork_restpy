## The IxNetwork Python Client 
[![pypi](https://img.shields.io/pypi/v/ixnetwork-restpy.svg)](https://pypi.org/project/ixnetwork-restpy)
[![python](https://img.shields.io/pypi/pyversions/ixnetwork-restpy.svg)](https://pypi.python.org/pypi/ixnetwork-restpy)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![downloads](https://pepy.tech/badge/ixnetwork-restpy)](https://pepy.tech/project/ixnetwork-restpy)

## Install the package
```
pip install --upgrade ixnetwork-restpy
```

## Start scripting
```python
"""This script demonstrates how to get started with ixnetwork_restpy scripting.

The script demonstrates the following:
    - connect to an IxNetwork test platform and authenticate
    - add a new session
    - clear any existing configuration
    - create 1 tx port and 2 rx ports
    - create traffic from the tx port to the rx ports
    - start traffic
    - print statistics
    - stop traffic
"""
from ixnetwork_restpy.testplatform.testplatform import TestPlatform
from ixnetwork_restpy.assistants.ports.portmapassistant import PortMapAssistant
from ixnetwork_restpy.assistants.statistics.statviewassistant import StatViewAssistant


# connect to a test tool platform
test_platform = TestPlatform('127.0.0.1')
test_platform.Authenticate('admin', 'admin')
sessions = test_platform.Sessions.add()
ixnetwork = sessions.Ixnetwork
ixnetwork.NewConfig()

# create one tx port and two rx port resources
port_map = PortMapAssistant(ixnetwork)
port_map.Map('10.36.74.26', 2, 13, Name='Tx')
port_map.Map('10.36.74.26', 2, 14, Name='Rx1')
port_map.Map('10.36.74.26', 2, 15, Name='Rx2')

# create a TrafficItem resource
# TrafficItem acts a a high level container for ConfigElement resources
# ConfigElement is a high level container for individual HighLevelStream resources
traffic_item = ixnetwork.Traffic.TrafficItem.add(Name='Traffic Test', TrafficType='raw')
traffic_item.EndpointSet.add(
    Sources=ixnetwork.Vport.find(Name='^Tx').Protocols.find(), 
    Destinations=ixnetwork.Vport.find(Name='^Rx').Protocols.find())

# using the traffic ConfigElement resource
# update the frame rate
# update the transmission control
traffic_config = traffic_item.ConfigElement.find()
traffic_config.FrameRate.update(Type='percentLineRate', Rate='100')
traffic_config.TransmissionControl.update(Type='continuous')

# adjust Ethernet stack fields
destination_mac = traffic_config.Stack.find(StackTypeId='ethernet').Field.find(FieldTypeId='ethernet.header.destinationAddress')
destination_mac.update(ValueType='valueList', ValueList=['00:00:fa:ce:fa:ce', '00:00:de:ad:be:ef'], TrackingEnabled=True)

# push ConfigElement settings down to HighLevelStream resources
traffic_item.Generate()

# connect ports to hardware test ports
# apply traffic to hardware
# start traffic
port_map.Connect(ForceOwnership=True)
ixnetwork.Traffic.Apply()
ixnetwork.Traffic.StartStatelessTrafficBlocking()

# print statistics
print(StatViewAssistant(ixnetwork, 'Port Statistics'))
print(StatViewAssistant(ixnetwork, 'Traffic Item Statistics'))
print(StatViewAssistant(ixnetwork, 'Flow Statistics'))

# stop traffic
ixnetwork.Traffic.StopStatelessTrafficBlocking()
```

## Documentation
Documentation is available using the following methods:
* [Online web based documentation](https://openixia.github.io/ixnetwork_restpy/#/overview)
  * [Samples](https://openixia.github.io/ixnetwork_restpy/#/samples)
  * [API Reference](https://openixia.github.io/ixnetwork_restpy/#/reference)

* Documentation available in the online doc browser is also inlined in each class, property and method and can be viewed using the python help command
  ```python
  from ixnetwork_restpy.testplatform.testplatform import TestPlatform
  
  help(TestPlatform)
  ```

## Additional Samples
Visit the [OpenIxia ixnetwork-restpy sample site maintained by solution architects](https://github.com/OpenIxia/IxNetwork/tree/master/RestPy) for in depth end-to-end samples that demonstrate the following:
* building a configuration
  * from scratch
  * from an existing IxNetwork configuration
* running the configuration
  * connecting ports to hardware
  * starting protocols
  * starting traffic
* getting statistics
  * port stats
  * traffic stats


