## The IxNetwork Python Client 
[![pypi](https://img.shields.io/pypi/v/ixnetwork-restpy.svg)](https://pypi.org/project/ixnetwork-restpy)
[![python](https://img.shields.io/pypi/pyversions/ixnetwork-restpy.svg)](https://pypi.python.org/pypi/ixnetwork-restpy)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)
[![downloads](https://pepy.tech/badge/ixnetwork-restpy)](https://pepy.tech/project/ixnetwork-restpy)


## Install the client
```
pip install --upgrade ixnetwork-restpy
```


## Import the package
Import a package based on your product:
```python
# The ixnetwork_restpy package is the superset of all IxNetwork products
from ixnetwork_restpy import SessionAssistant
```
```python
# The uhd_restpy package is a subset of the ixnetwork_restpy package for the UHD appliance
from uhd_restpy import SessionAssistant
```


## Start scripting
```python
"""This script demonstrates how to get started with ixnetwork_restpy scripting.

The script demonstrates the following:
    - connect to an IxNetwork test platform, authenticate, add a new session and clear the config
    - create 1 tx port and 1 rx port
    - create traffic from the tx port to the rx port
    - start traffic
    - print statistics
    - stop traffic
"""
from ixnetwork_restpy import SessionAssistant


# create a test tool session
session_assistant = SessionAssistant(IpAddress='127.0.0.1', 
    LogLevel=SessionAssistant.LOGLEVEL_INFO, 
    ClearConfig=True)
ixnetwork = session_assistant.Ixnetwork

# create tx and rx port resources
port_map = session_assistant.PortMapAssistant()
port_map.Map('10.36.74.26', 2, 13, Name='Tx')
port_map.Map('10.36.74.26', 2, 14, Name='Rx')

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
print(session_assistant.StatViewAssistant('Port Statistics'))
print(session_assistant.StatViewAssistant('Traffic Item Statistics'))
print(session_assistant.StatViewAssistant('Flow Statistics'))

# stop traffic
ixnetwork.Traffic.StopStatelessTrafficBlocking()
```

## Supported Server Versions
This client package supports versions 8.52 and up of the following servers:
* Linux IxNetwork API Server
* Windows IxNetwork GUI
* Windows IxNetwork Connection Manager

## Documentation
Documentation is available using the following methods:
* [Online web based documentation](https://openixia.github.io/ixnetwork_restpy/#/overview)
  * [Samples](https://openixia.github.io/ixnetwork_restpy/#/samples)
  * [API Reference](https://openixia.github.io/ixnetwork_restpy/#/reference)

* Documentation available in the online doc browser is also inlined in each class, property and method and can be viewed using the python help command
  ```python
  from ixnetwork_restpy import SessionAssistant
  
  help(SessionAssistant)
  ```

## Additional Samples
Visit the [OpenIxia ixnetwork-restpy sample site maintained by solution architects](https://github.com/OpenIxia/IxNetwork/tree/master/RestPy) for in-depth end-to-end samples that demonstrate the following:
* building a configuration
  * from scratch
  * from an existing IxNetwork configuration
* running the configuration
  * connecting ports to hardware
  * starting protocols
  * starting traffic
* getting statistics
  * port stats
  * traffic stats

## Contributing
The purpose of this repository is to allow users to clone the auto generated code. We do not accept pull requests in this repository.

Feedback such as bugs/enhancements/questions regarding the ixnetwork-restpy package is welcomed by opening a [GitHub issue](https://github.com/OpenIxia/ixnetwork_restpy/issues).