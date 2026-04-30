# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class SelectedDhcpConfig(Base):
    """Defines the selected dhcp configuration.
    The SelectedDhcpConfig class encapsulates a required selectedDhcpConfig resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "selectedDhcpConfig"
    _SDM_ATT_MAP = {
        "Count": "count",
        "IpType": "ipType",
        "Name": "name",
        "RangeNumber": "rangeNumber",
        "RangeRelayIncrement": "rangeRelayIncrement",
        "RelayAddress": "relayAddress",
        "RelayAddressIncrement": "relayAddressIncrement",
        "RelayCircuitId": "relayCircuitId",
        "RelayDestination": "relayDestination",
        "RelayGateway": "relayGateway",
        "RelayRemoteId": "relayRemoteId",
        "RelaySubnet": "relaySubnet",
        "RelayUseCircuitId": "relayUseCircuitId",
        "RelayUseRemoteId": "relayUseRemoteId",
        "RenewTimer": "renewTimer",
        "UseRelayAgent": "useRelayAgent",
        "UseVendorClassId": "useVendorClassId",
        "VendorClassId": "vendorClassId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SelectedDhcpConfig, self).__init__(parent, list_op)

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of relay count to configure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @Count.setter
    def Count(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Count"], value)

    @property
    def IpType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Defines the ip type for dhcp configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IpType"])

    @IpType.setter
    def IpType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["IpType"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Implies the name of the selected dhcp configuration settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def RangeNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Defines the range number for the selected dhcp settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeNumber"])

    @RangeNumber.setter
    def RangeNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeNumber"], value)

    @property
    def RangeRelayIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Describes the relay increment for dhcp address range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RangeRelayIncrement"])

    @RangeRelayIncrement.setter
    def RangeRelayIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RangeRelayIncrement"], value)

    @property
    def RelayAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The source address from which the requests from DHCP clients are made.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayAddress"])

    @RelayAddress.setter
    def RelayAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayAddress"], value)

    @property
    def RelayAddressIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which to increment the IP address for each relay agent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayAddressIncrement"])

    @RelayAddressIncrement.setter
    def RelayAddressIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayAddressIncrement"], value)

    @property
    def RelayCircuitId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If true, the CIRCUIT-ID option is sent along with the other options.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayCircuitId"])

    @RelayCircuitId.setter
    def RelayCircuitId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayCircuitId"], value)

    @property
    def RelayDestination(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The address to which the requests from DHCP clients are forwarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayDestination"])

    @RelayDestination.setter
    def RelayDestination(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayDestination"], value)

    @property
    def RelayGateway(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The gateway address used for all relay agents.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayGateway"])

    @RelayGateway.setter
    def RelayGateway(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayGateway"], value)

    @property
    def RelayRemoteId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This sub-option can be added by DHCP relay agents that terminate switched or permanent circuits and have mechanisms to identify the remote host end of the circuit.The default value is REMOTEID-$I.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayRemoteId"])

    @RelayRemoteId.setter
    def RelayRemoteId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayRemoteId"], value)

    @property
    def RelaySubnet(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The network mask (expressed as a prefix length) used for all relay agents.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelaySubnet"])

    @RelaySubnet.setter
    def RelaySubnet(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelaySubnet"], value)

    @property
    def RelayUseCircuitId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This sub-option can be added by DHCP relay agents who terminate switched or permanent circuits. The default value is CIRCUITID-$P.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayUseCircuitId"])

    @RelayUseCircuitId.setter
    def RelayUseCircuitId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayUseCircuitId"], value)

    @property
    def RelayUseRemoteId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the REMOTE-ID option is sent along with the other options.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RelayUseRemoteId"])

    @RelayUseRemoteId.setter
    def RelayUseRemoteId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RelayUseRemoteId"], value)

    @property
    def RenewTimer(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The lease renewal time, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RenewTimer"])

    @RenewTimer.setter
    def RenewTimer(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RenewTimer"], value)

    @property
    def UseRelayAgent(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the subnet will emulate a DHCP relay agent.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseRelayAgent"])

    @UseRelayAgent.setter
    def UseRelayAgent(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseRelayAgent"], value)

    @property
    def UseVendorClassId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables use of the identifier configured in the Vendor Class ID field.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseVendorClassId"])

    @UseVendorClassId.setter
    def UseVendorClassId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseVendorClassId"], value)

    @property
    def VendorClassId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identifies the vendor providing the hardware on which the client is running.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VendorClassId"])

    @VendorClassId.setter
    def VendorClassId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["VendorClassId"], value)

    def update(
        self,
        Count=None,
        IpType=None,
        Name=None,
        RangeNumber=None,
        RangeRelayIncrement=None,
        RelayAddress=None,
        RelayAddressIncrement=None,
        RelayCircuitId=None,
        RelayDestination=None,
        RelayGateway=None,
        RelayRemoteId=None,
        RelaySubnet=None,
        RelayUseCircuitId=None,
        RelayUseRemoteId=None,
        RenewTimer=None,
        UseRelayAgent=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (int, str, str, int, str, str, str, str, str, str, str, int, bool, bool, int, bool, bool, str) -> SelectedDhcpConfig
        """Updates selectedDhcpConfig resource on the server.

        Args
        ----
        - Count (number): The number of relay count to configure.
        - IpType (str): Defines the ip type for dhcp configuration.
        - Name (str): Implies the name of the selected dhcp configuration settings.
        - RangeNumber (number): Defines the range number for the selected dhcp settings.
        - RangeRelayIncrement (str): Describes the relay increment for dhcp address range.
        - RelayAddress (str): The source address from which the requests from DHCP clients are made.
        - RelayAddressIncrement (str): The value by which to increment the IP address for each relay agent.
        - RelayCircuitId (str): If true, the CIRCUIT-ID option is sent along with the other options.
        - RelayDestination (str): The address to which the requests from DHCP clients are forwarded.
        - RelayGateway (str): The gateway address used for all relay agents.
        - RelayRemoteId (str): This sub-option can be added by DHCP relay agents that terminate switched or permanent circuits and have mechanisms to identify the remote host end of the circuit.The default value is REMOTEID-$I.
        - RelaySubnet (number): The network mask (expressed as a prefix length) used for all relay agents.
        - RelayUseCircuitId (bool): This sub-option can be added by DHCP relay agents who terminate switched or permanent circuits. The default value is CIRCUITID-$P.
        - RelayUseRemoteId (bool): If true, the REMOTE-ID option is sent along with the other options.
        - RenewTimer (number): The lease renewal time, in seconds.
        - UseRelayAgent (bool): If true, the subnet will emulate a DHCP relay agent.
        - UseVendorClassId (bool): If true, enables use of the identifier configured in the Vendor Class ID field.
        - VendorClassId (str): Identifies the vendor providing the hardware on which the client is running.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        IpType=None,
        Name=None,
        RangeNumber=None,
        RangeRelayIncrement=None,
        RelayAddress=None,
        RelayAddressIncrement=None,
        RelayCircuitId=None,
        RelayDestination=None,
        RelayGateway=None,
        RelayRemoteId=None,
        RelaySubnet=None,
        RelayUseCircuitId=None,
        RelayUseRemoteId=None,
        RenewTimer=None,
        UseRelayAgent=None,
        UseVendorClassId=None,
        VendorClassId=None,
    ):
        # type: (int, str, str, int, str, str, str, str, str, str, str, int, bool, bool, int, bool, bool, str) -> SelectedDhcpConfig
        """Finds and retrieves selectedDhcpConfig resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve selectedDhcpConfig resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all selectedDhcpConfig resources from the server.

        Args
        ----
        - Count (number): The number of relay count to configure.
        - IpType (str): Defines the ip type for dhcp configuration.
        - Name (str): Implies the name of the selected dhcp configuration settings.
        - RangeNumber (number): Defines the range number for the selected dhcp settings.
        - RangeRelayIncrement (str): Describes the relay increment for dhcp address range.
        - RelayAddress (str): The source address from which the requests from DHCP clients are made.
        - RelayAddressIncrement (str): The value by which to increment the IP address for each relay agent.
        - RelayCircuitId (str): If true, the CIRCUIT-ID option is sent along with the other options.
        - RelayDestination (str): The address to which the requests from DHCP clients are forwarded.
        - RelayGateway (str): The gateway address used for all relay agents.
        - RelayRemoteId (str): This sub-option can be added by DHCP relay agents that terminate switched or permanent circuits and have mechanisms to identify the remote host end of the circuit.The default value is REMOTEID-$I.
        - RelaySubnet (number): The network mask (expressed as a prefix length) used for all relay agents.
        - RelayUseCircuitId (bool): This sub-option can be added by DHCP relay agents who terminate switched or permanent circuits. The default value is CIRCUITID-$P.
        - RelayUseRemoteId (bool): If true, the REMOTE-ID option is sent along with the other options.
        - RenewTimer (number): The lease renewal time, in seconds.
        - UseRelayAgent (bool): If true, the subnet will emulate a DHCP relay agent.
        - UseVendorClassId (bool): If true, enables use of the identifier configured in the Vendor Class ID field.
        - VendorClassId (str): Identifies the vendor providing the hardware on which the client is running.

        Returns
        -------
        - self: This instance with matching selectedDhcpConfig resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of selectedDhcpConfig data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the selectedDhcpConfig resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
