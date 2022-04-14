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


class AncpPvcRange(Base):
    """Range of multiple PVCs for fine grained configuration
    The AncpPvcRange class encapsulates a required ancpPvcRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ancpPvcRange"
    _SDM_ATT_MAP = {
        "Enabled": "enabled",
        "IncrementMode": "incrementMode",
        "Name": "name",
        "ObjectId": "objectId",
        "VciFirstId": "vciFirstId",
        "VciIncrement": "vciIncrement",
        "VciIncrementStep": "vciIncrementStep",
        "VciUniqueCount": "vciUniqueCount",
        "VpiFirstId": "vpiFirstId",
        "VpiIncrement": "vpiIncrement",
        "VpiIncrementStep": "vpiIncrementStep",
        "VpiUniqueCount": "vpiUniqueCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(AncpPvcRange, self).__init__(parent, list_op)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def IncrementMode(self):
        # type: () -> int
        """
        Returns
        -------
        - number: May take the following values: 0 (VCI first), 1 (VPI first), 2 (Both)
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncrementMode"])

    @IncrementMode.setter
    def IncrementMode(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncrementMode"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP["ObjectId"])

    @property
    def VciFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: First ATM VCI value to use
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciFirstId"])

    @VciFirstId.setter
    def VciFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciFirstId"], value)

    @property
    def VciIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Step size for VCI increment
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciIncrement"])

    @VciIncrement.setter
    def VciIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciIncrement"], value)

    @property
    def VciIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increment VCI every 'vciIncrementStep' addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciIncrementStep"])

    @VciIncrementStep.setter
    def VciIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciIncrementStep"], value)

    @property
    def VciUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of VCIs
        """
        return self._get_attribute(self._SDM_ATT_MAP["VciUniqueCount"])

    @VciUniqueCount.setter
    def VciUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VciUniqueCount"], value)

    @property
    def VpiFirstId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: First ATM VPI value to use.
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiFirstId"])

    @VpiFirstId.setter
    def VpiFirstId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiFirstId"], value)

    @property
    def VpiIncrement(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Step size for VPI increment
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiIncrement"])

    @VpiIncrement.setter
    def VpiIncrement(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiIncrement"], value)

    @property
    def VpiIncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Increment VPI every 'vpiIncrementStep' addresses
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiIncrementStep"])

    @VpiIncrementStep.setter
    def VpiIncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiIncrementStep"], value)

    @property
    def VpiUniqueCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of VPIs
        """
        return self._get_attribute(self._SDM_ATT_MAP["VpiUniqueCount"])

    @VpiUniqueCount.setter
    def VpiUniqueCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["VpiUniqueCount"], value)

    def update(
        self,
        Enabled=None,
        IncrementMode=None,
        Name=None,
        VciFirstId=None,
        VciIncrement=None,
        VciIncrementStep=None,
        VciUniqueCount=None,
        VpiFirstId=None,
        VpiIncrement=None,
        VpiIncrementStep=None,
        VpiUniqueCount=None,
    ):
        # type: (bool, int, str, int, int, int, int, int, int, int, int) -> AncpPvcRange
        """Updates ancpPvcRange resource on the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IncrementMode (number): May take the following values: 0 (VCI first), 1 (VPI first), 2 (Both)
        - Name (str): Name of range
        - VciFirstId (number): First ATM VCI value to use
        - VciIncrement (number): Step size for VCI increment
        - VciIncrementStep (number): Increment VCI every 'vciIncrementStep' addresses
        - VciUniqueCount (number): Number of VCIs
        - VpiFirstId (number): First ATM VPI value to use.
        - VpiIncrement (number): Step size for VPI increment
        - VpiIncrementStep (number): Increment VPI every 'vpiIncrementStep' addresses
        - VpiUniqueCount (number): Number of VPIs

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Enabled=None,
        IncrementMode=None,
        Name=None,
        ObjectId=None,
        VciFirstId=None,
        VciIncrement=None,
        VciIncrementStep=None,
        VciUniqueCount=None,
        VpiFirstId=None,
        VpiIncrement=None,
        VpiIncrementStep=None,
        VpiUniqueCount=None,
    ):
        # type: (bool, int, str, str, int, int, int, int, int, int, int, int) -> AncpPvcRange
        """Finds and retrieves ancpPvcRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ancpPvcRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ancpPvcRange resources from the server.

        Args
        ----
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - IncrementMode (number): May take the following values: 0 (VCI first), 1 (VPI first), 2 (Both)
        - Name (str): Name of range
        - ObjectId (str): Unique identifier for this object
        - VciFirstId (number): First ATM VCI value to use
        - VciIncrement (number): Step size for VCI increment
        - VciIncrementStep (number): Increment VCI every 'vciIncrementStep' addresses
        - VciUniqueCount (number): Number of VCIs
        - VpiFirstId (number): First ATM VPI value to use.
        - VpiIncrement (number): Step size for VPI increment
        - VpiIncrementStep (number): Increment VPI every 'vpiIncrementStep' addresses
        - VpiUniqueCount (number): Number of VPIs

        Returns
        -------
        - self: This instance with matching ancpPvcRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ancpPvcRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ancpPvcRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum, async_operation=bool)
        ---------------------------------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        return self._execute(
            "customProtocolStack", payload=payload, response_object=None
        )

    def DisableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string, async_operation=bool)string
        -------------------------------------------------------------
        - Arg2 (str): Protocol class name to disable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
            "disableProtocolStack", payload=payload, response_object=None
        )

    def EnableProtocolStack(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------
        - Arg2 (str): Protocol class name to enable
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Status of the exec

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
            "enableProtocolStack", payload=payload, response_object=None
        )
