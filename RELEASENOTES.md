# Release Notes

### Dec 2020
* 1.0.61
  * support ixnetwork 9.10.2011.91
* 1.0.60
  * support uhd 9.10.2011.61
  * bug fix: print version number once
  * bug fix: support __getitem__ slice
  * bug fix: issue #37 Session.GetFileList fails when passed a remote_directory

### Oct 2020
* 1.0.59
  * bug fix: SessionAssistant ApiKey not passed
  * bug fix: python 2.7 import ixnetwork_restpy
  * bug fix: StatViewAssistant column csv exception 

### Sep 2020
* 1.0.58
  * WatchAssistant
* 1.0.57
  * classes generated from IxNetwork build 9.10

### Aug 2020
* 1.0.56
  * fixed intermittent KeyError: 'href' bug
  * enhanced KeyError message when error is valid

### Jul 2020
* 1.0.55
  * PortMapAssistant.Connect method bug fix
  * StatViewAssistant processes snapshots using in memory IO 
  * removal of duplicate attempts in test platform determination 
* 1.0.54
  * inclusion of uhd_restpy package in distribution
  * PortMapAssistant supports user defined timeouts on the .Connect method
  * StatViewAssistant bug fixes

### May 2020
* 1.0.53
  * fixed translation of python class property names to rest api property names
  * added update method to Multivalue.Steps class

### Apr 2020
* 1.0.52
  * classes generated from IxNetwork build 9.00.1915.16
  * TestPlatform.Sessions.find(Id=) fixed when using connection_manager 
  * TlvProfile sample demonstrates creating and copying a template tlv to a protocol tlvprofile
  * CollectLogs sample demonstrates collecting diagnostic logs and downloading them
  * samples use SessionAssistant when relevant
  * PortMapAssistant has user configurable option to timeout on chassis configuration
  * Testplatform("ipv6 address") is escaped
  * .update() method returns self
  * Multivalue class/methods/properties included in IDE intellisense
  * documentation site updates:
    * API Reference readibility enhancement for inline class/method/property documentation
    * release notes included in documentation
 
### Mar 2020
* 1.0.51
  * classes generated from IxNetwork build 9.01.1911.7 
  * New SessionAssistant class
    * combines TestPlatform, Session, logging, authentication and NewConfig functionality into constructor
    * reduces number of import statements and complexity
      * from ixnetwork_restpy import SessionAssistant
    * access other assistants from the SessionAssistant
    * see the getting_started.py for usage
  * PortMapAssistant has enhanced Map method
    * see examples in the class documentation
  * proxy bypass fix
  * generated quickTest...testConfig attributes
  
### Jan 2020
* 1.0.48
  * support ipv6 address with no square brackets in TestPlatform init
  * MultiValue.Steps.find() support 

### Nov 2019
* 1.0.47
  * fixed class generation for invalid property names, invalid docstrings and normalized line endings
  * RELEASENOTES.md included in distributions
* 1.0.46
  * QuickTest TestConfig classes are now supported
  * added additional logging levels (info, warn, all), the default logging level is TestPlatform.NONE
  * MultiValue.Steps fixes
  * enhanced reference parameter processing 
    * pass a list of references using the container
      * EndpointSet.add(Sources=Vport.find())
    * pass a list of references using a list of objects
      * EndpointSet.add(Sources=[vport1, vport2])
  * improved formatting of raised errors which also includes any server side app errors
  * fixed class generation
    * property/method names that are reserved/prohibited are corrected
    * compile all classes  
  * added PortMapAssistant class
    * easily add ports that are mapped to a location
    * connect all mapped ports in one call without having to specify a complex payload
    * for usage details see the ixnetwork_restpy.samples.assistants.port_map_assistant.py
* 1.0.45
  * StackManager is now supported under TestPlatform.Sessions.Ixnetwork.Vport.ProtocolStack...

### Sep 2019
* 1.0.41
  * support for Session naming (linux API Server only)
  * support for IxNetwork 9.0 features
  * documentation enhancements to display deprecated, readwrite properties, navigate from Rest API Browser to restpy documentation
  * support creation of **Linux API Server IxNetwork QuickTest Web** sessions
  * slots support which will now raise an AttributeError when accessing non-existent properties 
    * !!WARNING!! this may cause some script collateral

### Jul 2019
* 1.0.37
  * unit tests
  * samples and api reference moved from package to online at https://openixia.github.io/ixnetwork_restpy/index.html
  * .tar.gz source distribution in addition to .whl
  * Simplified TestPlatform constructor automatically determines platform and rest_port

### May 2019
* 1.0.31
  * StatViewAssistant class allows alternate csv download storage to be specified

### Apr 2019
* 1.0.30
  * eCPRI protocol classes
  * QuickTest classes that allow for apply, start, stop, report generation and results

### Mar 2019
* 1.0.27
  * StatViewAssistant fix filter evaluation, normalize csv snapshot names
  * Lag class has been updated with missing child classes
  * traffic over lags sample demonstrates how to create a raw traffic item with lags as endpoints
  * some classes had duplicate method names which is not supported by python, this consolidates multiple methods into one method by using args and kwargs, use the method docstring to ensure the correctness of the args being supplied to the method.

### Feb 2019
* 1.0.23
  * TestPlatform supports Connection Manager
  * iterator fixes
  * Session file upload and file down load functionality
  * Multivalue.Steps fixes that allow for setting/enabling steps such as port step
  * samples for connecting to Connection Manager platform and session file transfer

### Jan 2019
* 1.0.17
  * StatViewAssistant class that has ease of use features when working with statistics, such as row filters and condition checking, check out the sample.
  * container and iterator fixes with an iterator sample demonstrating some use cases

### Nov 2018
* 1.0.10
  * Base class infrastructure to allow for getting a list of device ids using regex searches that can be used on NGPF class methods that require device ids. See the sample ngpf_device_ids.py for multiple examples of retrieving device ids and using them in ngpf methods.
