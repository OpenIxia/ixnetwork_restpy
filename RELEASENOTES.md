# Release Notes

### Nov 2019
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
  *   StackManager is now supported under TestPlatform.Sessions.Ixnetwork.Vport.ProtocolStack...

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
