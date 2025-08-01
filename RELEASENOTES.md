# Release Notes
### July 2025
* 1.8.0
  * support for ixnetwork version 11.00.2407.67 (11.00 Update-1)
### May 2025
* 1.7.0
  * support for ixnetwork version 11.00.2504.10 (11.00 EA)
### December 2024
* 1.6.1
  * fix issue where bgpMVpnSenderSiteSpmsiV4 nodes were not being generated
* 1.6.0
  * support for ixnetwork version 10.80.2412.6 (10.80 EA)
  * new samples added
    * files -> get_file_info.py
    * ports -> l1config -> tap_settings.py, port_lldp_info.py
### November 2024
* 1.5.0
  * support for ixnetwork version 10.25.2406.6 (10.25 EA)
  * corrected sample csv_snapshot.py for getting statistics
  * added new sample: basic->nest_multivalue.py for configuring Nest Multivalue.
### August 2024
* 1.4.0
  * support for ixnetwork version 10.00.2407.87 (10.00 Update-2)
### May  2024
* 1.3.0
  * support for ixnetwork version 10.20.2403.2
### April 2024
* 1.2.0
  * support for ixnetwork version 10.00.2403.64 (10.00 Update-1)
  * fixed issue for batch add traffic creation.
### January 2024
* 1.1.12
  * support ixnetwork version 10.00.2312.4 (10.00 EA)
  * fixed an issue with find() on a restpy node with href
### November 2023
* 1.1.11
  * support ixnetwork version 9.30.2309.46 (9.30 Update-3)
  * New Feature in Stat View Assistant Utility to `filter` Statistics
    * please refer to sample script filter_stats_using_stat_view_assistant.py
  * Bug fixes in Stat View Assistant Utility
    * fixed fetching of the correct traffic item node after drill down
    * fixed drill down statics for views apart from Traffic Item Statistics
### July 2023
* 1.1.10
  * support ixnetwork version 9.30.2306.60 (9.30 Update-2)
  * Bug Fixes and features
    * Support to ignore strong password policy
      * New attribute in SessionAssistant name `IgnoreStrongPasswordPolicy`, by default `True`
    * fix missing files of pcep learned info
    * fix issue related to overlays
    * fix issue regarding improper cache clearance for poll urls
    * minor improvements to port map assistant
    
### April 2023
* 1.1.9
  * support ixnetwork version 9.30.2304.57 (9.30 Update-1)
  * bug fixes in batch update for traffic configuration
  * Addition of new samples
    * two samples related to l1 config - l1_config_pcs_error_generation.py, l1_config_tx_lane_and_skew.py
    * two samples related to custom views - port_cust_view.py, traffic_flow_custom_view.py
    * one sample related to learned info - bgp_learned_info.py
### January 2023
* 1.1.8
  * support ixnetwork version  9.30.2212.7 (9.30 EA)
### October 2022
* 1.1.7
  * support ixnetwork version 9.20.2206.84 (9.20 Update-3)
  * support uhd version 1.5 patch-2
  * bug fixes in batch add
  * drill down statistics sample corrected
### May 2022
* 1.1.6
  * support ixnetwork version 9.20.2201.69 (9.20 Update-1)
  * support uhd version 1.5
  * fixed issue #65: quicktest testconfig configuration not updating parameters
  * fixed issue #66: Read content of Multivalue
    * exposed new property PatternType in Multivalue class
      * samples - patternType_in_multivalue
  * catagorical representation of samples in restpy documentation
    * link: https://openixia.github.io/ixnetwork_restpy/#/samples
### Apr 2022
* 1.1.5
  * support ixnetwork version 9.20.2199.45 (9.20 patch-1)
  * introduction of batch operations (improves performance)
    * Batch Find - helps users to find multiples nodes in a single rest call
      * samples - batch_find.py
    * Batch Update - helps users to update multiple restpy objects in a single rest call
      * samples - batch_update.py, load_config_with_batch_update.py
    * Batch Add - adds a whole configuration in single rest call
      * samples - batch_add.py, traffic_with_batch_add.py
  * includes Timeline class
  * logging module now has thread ids
### Feb 2022
* 1.1.4
  * support uhd version 1.4.1
  * support ixnetwork version 9.20.2112.6 + HF001150
### Oct 2021
* 1.1.3
  * Included Timeline class
* 1.1.2
  * fixed issue #56: `UnboundLocalError: local variable 'response' referenced before assignment`
  * fixed issue #58: `.find() method is slow`
    * using the .find() method from objects returned by the IxNetwork object hierarchy will be responsive and is the recommended approach for retrieving objects
    * using the .find() method from objects returned by ConfigAssistant.Config will be much slower as system incurs additional overhead, this is not the recommended approach as this assistant is meant for creating a batch configuration.
  * fixed issue #54: `BadRequestError is not defined`
### Sep 2021
* 1.1.1
  * support ixnetwork 9.10.2011.227
  * Fix for `intermittent failure when connecting to an already started ConnectionManager session`
### Aug 2021
* 1.1.0
  * Async operation enhancement that allows all operations to be executed asynchronously
    * issue details https://github.com/OpenIxia/ixnetwork_restpy/issues/51
  * ConfigAssistant enhancement that allows for configuration with a single commit
    * reduces rest api transactions
    * uses traffic protocol templates stack and field names as class properties
    * can export configuration as json
  * fix Base.update() method to update all encapsulated resources
  * fix Sessions.remove() method to optimize linux API server sessions removal
  * new samples https://openixia.github.io/ixnetwork_restpy/#/samples
    * config assistant: CustomTraffic.py, Evpn.py, NgpfBgp.py
    * async operation: async_operation.py

### May 2021
* 1.0.67
  * fix __str__ output of href
  * generate missing protocolStack classes
* 1.0.66
  * support uhd 1.3.3003.48
  * support ixnetwork 9.10.2011.111
  * enhance index out of range error message
  * add error name to 4xx, 5xx global apperror errors

### Apr 2021
* 1.0.65
  * support ixnetwork 9.15.2101.8
  * escape filename in query string param

### Jan 2021
* 1.0.64
  * return multivalue object given a valid multivalue href
  * PortMapAssistant option to bypass link state check
  * allow Multivalue.ValueList method to accept a list of values in a file
* 1.0.62
  * refresh multivalue when parent object pattern has changed

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
