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


class Mld(Base):
    """This object sends and responds to MLD messages.
    The Mld class encapsulates a required mld resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "mld"
    _SDM_ATT_MAP = {
        "EnableDoneOnStop": "enableDoneOnStop",
        "EnableUnicastMode": "enableUnicastMode",
        "Enabled": "enabled",
        "Mldv2Report": "mldv2Report",
        "NumberOfGroups": "numberOfGroups",
        "NumberOfQueries": "numberOfQueries",
        "QueryTimePeriod": "queryTimePeriod",
        "RunningState": "runningState",
        "TimePeriod": "timePeriod",
    }
    _SDM_ENUM_MAP = {
        "mldv2Report": ["type143", "type206"],
        "runningState": ["unknown", "stopped", "stopping", "starting", "started"],
    }

    def __init__(self, parent, list_op=False):
        super(Mld, self).__init__(parent, list_op)

    @property
    def Host(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_fa1da007d58124057dd278c45c2d38ab.Host): An instance of the Host class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.host_fa1da007d58124057dd278c45c2d38ab import (
            Host,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Host", None) is not None:
                return self._properties.get("Host")
        return Host(self)

    @property
    def Querier(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_dac8ed773affc99eb47c41c6e99f71c1.Querier): An instance of the Querier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.querier_dac8ed773affc99eb47c41c6e99f71c1 import (
            Querier,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Querier", None) is not None:
                return self._properties.get("Querier")
        return Querier(self)

    @property
    def EnableDoneOnStop(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Controls the behavior of MLD messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableDoneOnStop"])

    @EnableDoneOnStop.setter
    def EnableDoneOnStop(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableDoneOnStop"], value)

    @property
    def EnableUnicastMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableUnicastMode"])

    @EnableUnicastMode.setter
    def EnableUnicastMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableUnicastMode"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables or disables simulation of the router.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def Mldv2Report(self):
        # type: () -> str
        """
        Returns
        -------
        - str(type143 | type206): The version of the MLD report to be generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mldv2Report"])

    @Mldv2Report.setter
    def Mldv2Report(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mldv2Report"], value)

    @property
    def NumberOfGroups(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Provides a means of throttling the amount of MLD traffic generated by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfGroups"])

    @NumberOfGroups.setter
    def NumberOfGroups(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfGroups"], value)

    @property
    def NumberOfQueries(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Provides a means of throttling the amount of MLD queries generated by the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfQueries"])

    @NumberOfQueries.setter
    def NumberOfQueries(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfQueries"], value)

    @property
    def QueryTimePeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The time, in milliseconds, between queries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["QueryTimePeriod"])

    @QueryTimePeriod.setter
    def QueryTimePeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["QueryTimePeriod"], value)

    @property
    def RunningState(self):
        # type: () -> str
        """
        Returns
        -------
        - str(unknown | stopped | stopping | starting | started): The current running state of the MLD server.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RunningState"])

    @property
    def TimePeriod(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specify the length of each time period during which the specified number of MLD Groups will be advertised.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimePeriod"])

    @TimePeriod.setter
    def TimePeriod(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimePeriod"], value)

    def update(
        self,
        EnableDoneOnStop=None,
        EnableUnicastMode=None,
        Enabled=None,
        Mldv2Report=None,
        NumberOfGroups=None,
        NumberOfQueries=None,
        QueryTimePeriod=None,
        TimePeriod=None,
    ):
        # type: (bool, bool, bool, str, int, int, int, int) -> Mld
        """Updates mld resource on the server.

        Args
        ----
        - EnableDoneOnStop (bool): Controls the behavior of MLD messages.
        - EnableUnicastMode (bool):
        - Enabled (bool): Enables or disables simulation of the router.
        - Mldv2Report (str(type143 | type206)): The version of the MLD report to be generated.
        - NumberOfGroups (number): Provides a means of throttling the amount of MLD traffic generated by the port.
        - NumberOfQueries (number): Provides a means of throttling the amount of MLD queries generated by the port.
        - QueryTimePeriod (number): The time, in milliseconds, between queries.
        - TimePeriod (number): Specify the length of each time period during which the specified number of MLD Groups will be advertised.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnableDoneOnStop=None,
        EnableUnicastMode=None,
        Enabled=None,
        Mldv2Report=None,
        NumberOfGroups=None,
        NumberOfQueries=None,
        QueryTimePeriod=None,
        RunningState=None,
        TimePeriod=None,
    ):
        # type: (bool, bool, bool, str, int, int, int, str, int) -> Mld
        """Finds and retrieves mld resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mld resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mld resources from the server.

        Args
        ----
        - EnableDoneOnStop (bool): Controls the behavior of MLD messages.
        - EnableUnicastMode (bool):
        - Enabled (bool): Enables or disables simulation of the router.
        - Mldv2Report (str(type143 | type206)): The version of the MLD report to be generated.
        - NumberOfGroups (number): Provides a means of throttling the amount of MLD traffic generated by the port.
        - NumberOfQueries (number): Provides a means of throttling the amount of MLD queries generated by the port.
        - QueryTimePeriod (number): The time, in milliseconds, between queries.
        - RunningState (str(unknown | stopped | stopping | starting | started)): The current running state of the MLD server.
        - TimePeriod (number): Specify the length of each time period during which the specified number of MLD Groups will be advertised.

        Returns
        -------
        - self: This instance with matching mld resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mld data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mld resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the MLD protocol on a port or group of ports simultaneously.

        start(async_operation=bool)
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
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the MLD protocol on a port or group of ports simultaneously.

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
