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


class CfmSlm(Base):
    """Synthetic Loss Measurement configuration for Emulated MEP
    The CfmSlm class encapsulates a required cfmSlm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cfmSlm"
    _SDM_ATT_MAP = {
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "Name": "name",
        "SlmAutoTestId": "slmAutoTestId",
        "SlmBurstCount": "slmBurstCount",
        "SlmBurstGap": "slmBurstGap",
        "SlmContinuousBurst": "slmContinuousBurst",
        "SlmDestinationType": "slmDestinationType",
        "SlmFlags": "slmFlags",
        "SlmFrameSize": "slmFrameSize",
        "SlmFrameTxCount": "slmFrameTxCount",
        "SlmFramesPerBurst": "slmFramesPerBurst",
        "SlmInitialTxfcf": "slmInitialTxfcf",
        "SlmMode": "slmMode",
        "SlmOverridePriority": "slmOverridePriority",
        "SlmPriority": "slmPriority",
        "SlmProactiveStart": "slmProactiveStart",
        "SlmSimulatedLossInTx": "slmSimulatedLossInTx",
        "SlmStateInfo": "slmStateInfo",
        "SlmTestId": "slmTestId",
        "SlmTestIdInfo": "slmTestIdInfo",
        "SlmTxFCfInfo": "slmTxFCfInfo",
        "SlmUnicastMac": "slmUnicastMac",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CfmSlm, self).__init__(parent, list_op)

    @property
    def StopSlmParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.stopslmparams_2117fd9e6d0ad885042f04f4604813e9.StopSlmParams): An instance of the StopSlmParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.stopslmparams_2117fd9e6d0ad885042f04f4604813e9 import (
            StopSlmParams,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StopSlmParams", None) is not None:
                return self._properties.get("StopSlmParams")
        return StopSlmParams(self)._select()

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def SlmAutoTestId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Generate SLM Test ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmAutoTestId"]))

    @property
    def SlmBurstCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Bursts.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmBurstCount"]))

    @property
    def SlmBurstGap(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time Gap between bursts in miliseconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmBurstGap"]))

    @property
    def SlmContinuousBurst(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, will send continuous bursts.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmContinuousBurst"])
        )

    @property
    def SlmDestinationType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast/All Remote MEP/Unicast. Multicast will send SLM to class 1 multicast address, All Remote MEP option will send unicast SLM to individual Remote MEPs, Unicast option will send SLM to configured unicast MAC.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmDestinationType"])
        )

    @property
    def SlmFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flags values to be sent in SLM PDU. Default 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmFlags"]))

    @property
    def SlmFrameSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SLM Frame Size.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmFrameSize"]))

    @property
    def SlmFrameTxCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SLM Frame Tx Count.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmFrameTxCount"])
        )

    @property
    def SlmFramesPerBurst(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Frames Per Burst.Default Value: 1, represent periodic transmission.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmFramesPerBurst"])
        )

    @property
    def SlmInitialTxfcf(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 4-octet field which contains the initial value of the local counter TxFCl for SLM frames.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmInitialTxfcf"])
        )

    @property
    def SlmMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Synthetic Loss Measurement Method - One way or Two way
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmMode"]))

    @property
    def SlmOverridePriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, it overrides MEP VLAN priority in SLM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmOverridePriority"])
        )

    @property
    def SlmPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN priority in SLM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmPriority"]))

    @property
    def SlmProactiveStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, MEP will Start sending SLM at startup.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmProactiveStart"])
        )

    @property
    def SlmSimulatedLossInTx(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage loss simulation in SLM Tx side.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SlmSimulatedLossInTx"])
        )

    @property
    def SlmStateInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[expired | none | notStarted | running | stopped]): Displays the current SLM State. Valid states are Running, Stopped, Expired and Not Started.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SlmStateInfo"])

    @property
    def SlmTestId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configurable, Non-negative integer value. Minimum Value: 1, Maximum Value: 4294967296, Default Value: 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmTestId"]))

    @property
    def SlmTestIdInfo(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Displays SLM Test ID Information.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SlmTestIdInfo"])

    @property
    def SlmTxFCfInfo(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Displays SLM Last TxFCf.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SlmTxFCfInfo"])

    @property
    def SlmUnicastMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Unicast MAC destination address.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SlmUnicastMac"]))

    def update(self, Name=None):
        # type: (str) -> CfmSlm
        """Updates cfmSlm resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        SlmStateInfo=None,
        SlmTestIdInfo=None,
        SlmTxFCfInfo=None,
    ):
        # type: (int, str, str, List[str], List[int], List[int]) -> CfmSlm
        """Finds and retrieves cfmSlm resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cfmSlm resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cfmSlm resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SlmStateInfo (list(str[expired | none | notStarted | running | stopped])): Displays the current SLM State. Valid states are Running, Stopped, Expired and Not Started.
        - SlmTestIdInfo (list(number)): Displays SLM Test ID Information.
        - SlmTxFCfInfo (list(number)): Displays SLM Last TxFCf.

        Returns
        -------
        - self: This instance with matching cfmSlm resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cfmSlm data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cfmSlm resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def StartSlm(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the startSlm operation on the server.

        Start SLM

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startSlm(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startSlm(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startSlm(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startSlm(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("startSlm", payload=payload, response_object=None)

    def StopSlm(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopSlm operation on the server.

        Stop SLM

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopSlm(async_operation=bool)
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopSlm(SessionIndices=list, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopSlm(SessionIndices=string, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        DEPRECATED stopSlm(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stopSlm", payload=payload, response_object=None)

    def get_device_ids(
        self,
        PortNames=None,
        SlmAutoTestId=None,
        SlmBurstCount=None,
        SlmBurstGap=None,
        SlmContinuousBurst=None,
        SlmDestinationType=None,
        SlmFlags=None,
        SlmFrameSize=None,
        SlmFrameTxCount=None,
        SlmFramesPerBurst=None,
        SlmInitialTxfcf=None,
        SlmMode=None,
        SlmOverridePriority=None,
        SlmPriority=None,
        SlmProactiveStart=None,
        SlmSimulatedLossInTx=None,
        SlmTestId=None,
        SlmUnicastMac=None,
    ):
        """Base class infrastructure that gets a list of cfmSlm device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - SlmAutoTestId (str): optional regex of slmAutoTestId
        - SlmBurstCount (str): optional regex of slmBurstCount
        - SlmBurstGap (str): optional regex of slmBurstGap
        - SlmContinuousBurst (str): optional regex of slmContinuousBurst
        - SlmDestinationType (str): optional regex of slmDestinationType
        - SlmFlags (str): optional regex of slmFlags
        - SlmFrameSize (str): optional regex of slmFrameSize
        - SlmFrameTxCount (str): optional regex of slmFrameTxCount
        - SlmFramesPerBurst (str): optional regex of slmFramesPerBurst
        - SlmInitialTxfcf (str): optional regex of slmInitialTxfcf
        - SlmMode (str): optional regex of slmMode
        - SlmOverridePriority (str): optional regex of slmOverridePriority
        - SlmPriority (str): optional regex of slmPriority
        - SlmProactiveStart (str): optional regex of slmProactiveStart
        - SlmSimulatedLossInTx (str): optional regex of slmSimulatedLossInTx
        - SlmTestId (str): optional regex of slmTestId
        - SlmUnicastMac (str): optional regex of slmUnicastMac

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
