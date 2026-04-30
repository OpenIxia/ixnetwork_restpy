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


class TlvList(Base):
    """This object is used to configure the DCBX TLV list.
    The TlvList class encapsulates a list of tlvList resources that are managed by the user.
    A list of resources can be retrieved from the server using the TlvList.find() method.
    The list can be managed by using the TlvList.add() and TlvList.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "tlvList"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "Error": "error",
        "ErrorOverride": "errorOverride",
        "FeatureEnable": "featureEnable",
        "FeatureType": "featureType",
        "MaxVersion": "maxVersion",
        "Name": "name",
        "SubType": "subType",
        "Willing": "willing",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TlvList, self).__init__(parent, list_op)

    @property
    def TlvSettings(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.tlvsettings_3290e9d075f99b4ccf41e74dec56389f.TlvSettings): An instance of the TlvSettings class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.tlvsettings_3290e9d075f99b4ccf41e74dec56389f import (
            TlvSettings,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TlvSettings", None) is not None:
                return self._properties.get("TlvSettings")
        return TlvSettings(self)._select()

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, this DCBX TLV is used in the configuration. If disabled, the range is neither validated, nor configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Error(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates that an error has occurred during the configuration exchange with the peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Error"])

    @Error.setter
    def Error(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Error"], value)

    @property
    def ErrorOverride(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, IxNetwork overrides the error bit. This parameter allows IxNetworkto forcefully signal an error for the selected DCB feature. This gives you theability to verify the DUT's handling of the Error flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorOverride"])

    @ErrorOverride.setter
    def ErrorOverride(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorOverride"], value)

    @property
    def FeatureEnable(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether or not the DCB feature is enabled for this TVL. This parameterallows the emulated DCB device to signal whether or not the advertised DCBfeature TLV is enabled for use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureEnable"])

    @FeatureEnable.setter
    def FeatureEnable(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureEnable"], value)

    @property
    def FeatureType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The DCBX feature that you are configuring in this TLV range.The IEEE 1.01 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Application.5-Custom.6-Custom.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.The Intel 1.0 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Custom (BCN).5-FCoE.6-Logical Link.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FeatureType"])

    @FeatureType.setter
    def FeatureType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FeatureType"], value)

    @property
    def MaxVersion(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The highest feature version supported by the selected feature.The default value is 255, and the valid range of values is from zero to 255.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxVersion"])

    @MaxVersion.setter
    def MaxVersion(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxVersion"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The unique name that IxNetwork assigns to the TLV list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def SubType(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Some Feature TLVs may define subtypes that are specific to that feature. Whensubtypes are not defined by a specific feature, the Subtype field should be set tozero.In general, the Type and SubType, taken together, identify a unique feature that ismanaged by an instance of the DCB Feature State Machine.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SubType"])

    @SubType.setter
    def SubType(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SubType"], value)

    @property
    def Willing(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Willing"])

    @Willing.setter
    def Willing(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Willing"], value)

    def update(
        self,
        Enabled=None,
        Error=None,
        ErrorOverride=None,
        FeatureEnable=None,
        FeatureType=None,
        MaxVersion=None,
        Name=None,
        SubType=None,
        Willing=None,
    ):
        # type: (bool, bool, bool, bool, int, int, str, int, bool) -> TlvList
        """Updates tlvList resource on the server.

        Args
        ----
        - Enabled (bool): If selected, this DCBX TLV is used in the configuration. If disabled, the range is neither validated, nor configured.
        - Error (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - ErrorOverride (bool): If selected, IxNetwork overrides the error bit. This parameter allows IxNetworkto forcefully signal an error for the selected DCB feature. This gives you theability to verify the DUT's handling of the Error flag.
        - FeatureEnable (bool): Indicates whether or not the DCB feature is enabled for this TVL. This parameterallows the emulated DCB device to signal whether or not the advertised DCBfeature TLV is enabled for use.
        - FeatureType (number): The DCBX feature that you are configuring in this TLV range.The IEEE 1.01 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Application.5-Custom.6-Custom.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.The Intel 1.0 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Custom (BCN).5-FCoE.6-Logical Link.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.
        - MaxVersion (number): The highest feature version supported by the selected feature.The default value is 255, and the valid range of values is from zero to 255.
        - Name (str): The unique name that IxNetwork assigns to the TLV list.
        - SubType (number): Some Feature TLVs may define subtypes that are specific to that feature. Whensubtypes are not defined by a specific feature, the Subtype field should be set tozero.In general, the Type and SubType, taken together, identify a unique feature that ismanaged by an instance of the DCB Feature State Machine.
        - Willing (bool): Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Enabled=None,
        Error=None,
        ErrorOverride=None,
        FeatureEnable=None,
        FeatureType=None,
        MaxVersion=None,
        Name=None,
        SubType=None,
        Willing=None,
    ):
        # type: (bool, bool, bool, bool, int, int, str, int, bool) -> TlvList
        """Adds a new tlvList resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If selected, this DCBX TLV is used in the configuration. If disabled, the range is neither validated, nor configured.
        - Error (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - ErrorOverride (bool): If selected, IxNetwork overrides the error bit. This parameter allows IxNetworkto forcefully signal an error for the selected DCB feature. This gives you theability to verify the DUT's handling of the Error flag.
        - FeatureEnable (bool): Indicates whether or not the DCB feature is enabled for this TVL. This parameterallows the emulated DCB device to signal whether or not the advertised DCBfeature TLV is enabled for use.
        - FeatureType (number): The DCBX feature that you are configuring in this TLV range.The IEEE 1.01 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Application.5-Custom.6-Custom.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.The Intel 1.0 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Custom (BCN).5-FCoE.6-Logical Link.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.
        - MaxVersion (number): The highest feature version supported by the selected feature.The default value is 255, and the valid range of values is from zero to 255.
        - Name (str): The unique name that IxNetwork assigns to the TLV list.
        - SubType (number): Some Feature TLVs may define subtypes that are specific to that feature. Whensubtypes are not defined by a specific feature, the Subtype field should be set tozero.In general, the Type and SubType, taken together, identify a unique feature that ismanaged by an instance of the DCB Feature State Machine.
        - Willing (bool): Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.

        Returns
        -------
        - self: This instance with all currently retrieved tlvList resources using find and the newly added tlvList resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained tlvList resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        Enabled=None,
        Error=None,
        ErrorOverride=None,
        FeatureEnable=None,
        FeatureType=None,
        MaxVersion=None,
        Name=None,
        SubType=None,
        Willing=None,
    ):
        # type: (bool, bool, bool, bool, int, int, str, int, bool) -> TlvList
        """Finds and retrieves tlvList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tlvList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tlvList resources from the server.

        Args
        ----
        - Enabled (bool): If selected, this DCBX TLV is used in the configuration. If disabled, the range is neither validated, nor configured.
        - Error (bool): Indicates that an error has occurred during the configuration exchange with the peer.
        - ErrorOverride (bool): If selected, IxNetwork overrides the error bit. This parameter allows IxNetworkto forcefully signal an error for the selected DCB feature. This gives you theability to verify the DUT's handling of the Error flag.
        - FeatureEnable (bool): Indicates whether or not the DCB feature is enabled for this TVL. This parameterallows the emulated DCB device to signal whether or not the advertised DCBfeature TLV is enabled for use.
        - FeatureType (number): The DCBX feature that you are configuring in this TLV range.The IEEE 1.01 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Application.5-Custom.6-Custom.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.The Intel 1.0 feature types are:2-Priority Group.3-PFC (Priority-based Flow Control).4-Custom (BCN).5-FCoE.6-Logical Link.7-NIV (Network Interface Virtualization).8-Custom through 127-Custom.
        - MaxVersion (number): The highest feature version supported by the selected feature.The default value is 255, and the valid range of values is from zero to 255.
        - Name (str): The unique name that IxNetwork assigns to the TLV list.
        - SubType (number): Some Feature TLVs may define subtypes that are specific to that feature. Whensubtypes are not defined by a specific feature, the Subtype field should be set tozero.In general, the Type and SubType, taken together, identify a unique feature that ismanaged by an instance of the DCB Feature State Machine.
        - Willing (bool): Indicates whether or not this feature accepts its configuration from the peer. When the Willing flag is TRUE, the system uses the DesiredCfg supplied by apeer as the OperCfg. A system that sets Willing to TRUE must be capable ofaccepting any valid DesiredCfg for the feature from the peer. In general, for onepeer to use the configuration of another peer, one peer must be willing and theother not willing. If both local and remote systems have the same value for theWilling flag, then the local DesiredCfg is used and the operational outcome of theexchange is determined by the Compatible method of the feature.

        Returns
        -------
        - self: This instance with matching tlvList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tlvList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tlvList resources from the server available through an iterator or index

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
