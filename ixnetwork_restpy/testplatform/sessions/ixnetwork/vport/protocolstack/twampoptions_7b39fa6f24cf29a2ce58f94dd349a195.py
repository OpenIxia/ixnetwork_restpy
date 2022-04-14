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


class TwampOptions(Base):
    """Portgroup options for the Twamp extension plug-in.
    The TwampOptions class encapsulates a list of twampOptions resources that are managed by the user.
    A list of resources can be retrieved from the server using the TwampOptions.find() method.
    The list can be managed by using the TwampOptions.add() and TwampOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "twampOptions"
    _SDM_ATT_MAP = {
        "ErrorEstimateMultiplier": "errorEstimateMultiplier",
        "ErrorEstimateScale": "errorEstimateScale",
        "MaxOutstanding": "maxOutstanding",
        "ObjectId": "objectId",
        "OverrideGlobalRateOptions": "overrideGlobalRateOptions",
        "SessionTimeout": "sessionTimeout",
        "SetupRate": "setupRate",
        "TeardownRate": "teardownRate",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TwampOptions, self).__init__(parent, list_op)

    @property
    def ErrorEstimateMultiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Twamp error estimate scale multiplier - used for the Error estimation computation
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorEstimateMultiplier"])

    @ErrorEstimateMultiplier.setter
    def ErrorEstimateMultiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorEstimateMultiplier"], value)

    @property
    def ErrorEstimateScale(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Twamp error estimate scale factor - used for the Error estimation computation
        """
        return self._get_attribute(self._SDM_ATT_MAP["ErrorEstimateScale"])

    @ErrorEstimateScale.setter
    def ErrorEstimateScale(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ErrorEstimateScale"], value)

    @property
    def MaxOutstanding(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Twamp-control connections to be in initiation or terminating state at any time.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MaxOutstanding"])

    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MaxOutstanding"], value)

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
    def OverrideGlobalRateOptions(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OverrideGlobalRateOptions"])

    @OverrideGlobalRateOptions.setter
    def OverrideGlobalRateOptions(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OverrideGlobalRateOptions"], value)

    @property
    def SessionTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Maximum duration for establishment of a control-session, test-session, and the start-sessions command
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionTimeout"])

    @SessionTimeout.setter
    def SessionTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SessionTimeout"], value)

    @property
    def SetupRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Twamp-Control connections initiated in a second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetupRate"])

    @SetupRate.setter
    def SetupRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetupRate"], value)

    @property
    def TeardownRate(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of Twamp-Control connections torn down in a second.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TeardownRate"])

    @TeardownRate.setter
    def TeardownRate(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TeardownRate"], value)

    def update(
        self,
        ErrorEstimateMultiplier=None,
        ErrorEstimateScale=None,
        MaxOutstanding=None,
        OverrideGlobalRateOptions=None,
        SessionTimeout=None,
        SetupRate=None,
        TeardownRate=None,
    ):
        # type: (int, int, int, bool, int, int, int) -> TwampOptions
        """Updates twampOptions resource on the server.

        Args
        ----
        - ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
        - ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
        - MaxOutstanding (number): The number of Twamp-control connections to be in initiation or terminating state at any time.
        - OverrideGlobalRateOptions (bool): If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
        - SessionTimeout (number): Maximum duration for establishment of a control-session, test-session, and the start-sessions command
        - SetupRate (number): The number of Twamp-Control connections initiated in a second.
        - TeardownRate (number): The number of Twamp-Control connections torn down in a second.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ErrorEstimateMultiplier=None,
        ErrorEstimateScale=None,
        MaxOutstanding=None,
        OverrideGlobalRateOptions=None,
        SessionTimeout=None,
        SetupRate=None,
        TeardownRate=None,
    ):
        # type: (int, int, int, bool, int, int, int) -> TwampOptions
        """Adds a new twampOptions resource on the server and adds it to the container.

        Args
        ----
        - ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
        - ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
        - MaxOutstanding (number): The number of Twamp-control connections to be in initiation or terminating state at any time.
        - OverrideGlobalRateOptions (bool): If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
        - SessionTimeout (number): Maximum duration for establishment of a control-session, test-session, and the start-sessions command
        - SetupRate (number): The number of Twamp-Control connections initiated in a second.
        - TeardownRate (number): The number of Twamp-Control connections torn down in a second.

        Returns
        -------
        - self: This instance with all currently retrieved twampOptions resources using find and the newly added twampOptions resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained twampOptions resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ErrorEstimateMultiplier=None,
        ErrorEstimateScale=None,
        MaxOutstanding=None,
        ObjectId=None,
        OverrideGlobalRateOptions=None,
        SessionTimeout=None,
        SetupRate=None,
        TeardownRate=None,
    ):
        # type: (int, int, int, str, bool, int, int, int) -> TwampOptions
        """Finds and retrieves twampOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve twampOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all twampOptions resources from the server.

        Args
        ----
        - ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
        - ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
        - MaxOutstanding (number): The number of Twamp-control connections to be in initiation or terminating state at any time.
        - ObjectId (str): Unique identifier for this object
        - OverrideGlobalRateOptions (bool): If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
        - SessionTimeout (number): Maximum duration for establishment of a control-session, test-session, and the start-sessions command
        - SetupRate (number): The number of Twamp-Control connections initiated in a second.
        - TeardownRate (number): The number of Twamp-Control connections torn down in a second.

        Returns
        -------
        - self: This instance with matching twampOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of twampOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the twampOptions resources from the server available through an iterator or index

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
