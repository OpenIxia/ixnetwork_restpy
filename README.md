# IxNetwork REST API Client
This package is an IxNetwork object oriented pure python client package over a REST transport.  
To get started [browse the class and samples documentation here](https://openixia.github.io/ixnetwork_restpy/index.html).

## What's New!
- Nov 2019 - 1.0.45
  - StackManager is now supported under TestPlatform.Sessions.IxNetwork.Vport.ProtocolStack...
- Sep 2019 - 1.0.41
  - support for Session naming (linux API Server only)
  - support for IxNetwork 9.0 features
  - documentation enhancements to display deprecated, readwrite properties, navigate from Rest API Browser to restpy documentation
  - support creation of **Linux API Server IxNetwork QuickTest Web** sessions
  - slots support which will now raise an AttributeError when accessing non-existent properties 
    - !!NOTE!! this may cause some script collateral
- Jul 2019 - 1.0.37
  - unit tests
  - samples and api reference moved from package to online at https://openixia.github.io/ixnetwork_restpy/index.html
  - .tar.gz source distribution in addition to .whl
  - Simplified TestPlatform constructor automatically determines platform and rest_port
- May 2019 - 1.0.31
  - StatViewAssistant class allows alternate csv download storage to be specified
- Apr 2019 - 1.0.30
  - eCPRI protocol classes
  - QuickTest classes that allow for apply, start, stop, report generation and results
- Mar 2019 - 1.0.27
  - StatViewAssistant fix filter evaluation, normalize csv snapshot names
  - Lag class has been updated with missing child classes
  - traffic over lags sample demonstrates how to create a raw traffic item with lags as endpoints
  - some classes had duplicate method names which is not supported by python, this consolidates multiple methods into one method by using args and kwargs, use the method docstring to ensure the correctness of the args being supplied to the method.
- Feb 2019 - 1.0.23
  - TestPlatform supports Connection Manager
  - iterator fixes
  - Session file upload and file down load functionality
  - Multivalue.Steps fixes that allow for setting/enabling steps such as port step
  - samples for connecting to Connection Manager platform and session file transfer
- Jan 2019 - 1.0.17
  - StatViewAssistant class that has ease of use features when working with statistics, such as row filters and condition checking, check out the sample.
  - container and iterator fixes with an iterator sample demonstrating some use cases
- Nov 2018 - 1.0.10
  - Base class infrastructure to allow for getting a list of device ids using regex searches that can be used on NGPF class methods that require device ids. See the sample ngpf_device_ids.py for multiple examples of retrieving device ids and using them in ngpf methods.


## Features
### Static classes
- classes are generated from the latest released version of IxNetwork
  - the only class that can be directly instantiated is the TestPlatform class
  - all other classes are accessed via a child property on the parent class
  - classes have helper methods depending on the type of class
    - classes that represent a required node are automatically populated with one and only one instance of the node's data
    - classes that represent a user managed list have `add, remove, find` helper methods
    - classes that represent a system managed list have a `find` helper method
  - every instantiated class encapsulates instances retrieved from the server 
  - encapsulated instances can be accessed using iterators or indexes
  - class iterator/index support includes: `__iter__ __next__ __getitem__ __len__`
  
### Find method
- the main premise of the package is based around the `.find()` method
- it offers named parameters for all properties in the class
- each named parameter supports a regex to allow for **finding** specific instances
- this allows the encapsulated data to be reduced to specific instances that you are interested in
- some examples:
    - `IxNetwork.Vport.find(Type='ethernet')` uses regex on the server to find and return all vports whose type is **ethernet**
    - `IxNetwork.Vport.find(Name='^Ethernet - 001$')` uses regex on the server to find and return a vport whose name exactly matches **Ethernet - 001**
    - `IxNetwork.Vport.find(ConnectionState='connectedLinkUp')` uses regex on the server to find and return all vports whose state is **connectedLinkUp**

### Documentation
- documentation is inlined in all generated classes and also [available online](https://openixia.github.io/ixnetwork_restpy/index.html)

### Samples
- samples are distributed with the package under the samples folder

## Limitations
- python support >= 2.7, 3.x
- IxNetwork support >= 8.52

## Getting Started
Install the package (**pip install -U ixnetwork-restpy**) and review the samples under ixnetwork_restpy/samples/...  

The samples demonstrate how to do the following:
- create a **TestPlatform**
- get an IxNetwork **Sessions** object and either find a session or add a new one
- get the root **Ixnetwork** object of the hierarchy
- add virtual ports, topologies, traffic

Finally visit the [OpenIxia IxNetwork restpy site](https://github.com/OpenIxia/IxNetwork/tree/master/RestPy) for in depth end-to-end samples that demonstrate the following:
- building a configuration
    - from scratch
    - from an existing IxNetwork configuration
- running the configuration
    - connecting ports to hardware
    - starting protocols
    - starting traffic
- getting statistics
    - port stats
    - traffic stats

