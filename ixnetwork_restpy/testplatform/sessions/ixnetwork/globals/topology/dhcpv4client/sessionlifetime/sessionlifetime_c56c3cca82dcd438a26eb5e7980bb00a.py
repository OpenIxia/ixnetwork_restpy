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


class SessionLifetime(Base):
    """Parameters used for controlling the lifetime and restart capabilities of sessions
    The SessionLifetime class encapsulates a required sessionLifetime resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "sessionLifetime"
    _SDM_ATT_MAP = {
        "Count": "count",
        "EnableLifetime": "enableLifetime",
        "EnableRestart": "enableRestart",
        "MaxLifetime": "maxLifetime",
        "MaxRestarts": "maxRestarts",
        "MinLifetime": "minLifetime",
        "RowNames": "rowNames",
        "ScaleMode": "scaleMode",
        "UnlimitedRestarts": "unlimitedRestarts",
    }
    _SDM_ENUM_MAP = {
        "scaleMode": ["port", "deviceGroup"],
    }

    def __init__(self, parent, list_op=False):
        super(SessionLifetime, self).__init__(parent, list_op)

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
    def EnableLifetime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables session for lifetime.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableLifetime"])
        )

    @property
    def EnableRestart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables automatic session restart after the stop at lifetime expiry.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EnableRestart"]))

    @property
    def MaxLifetime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum session lifetime (in seconds).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxLifetime"]))

    @property
    def MaxRestarts(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of times each session is automatically restarted.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxRestarts"]))

    @property
    def MinLifetime(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Minimum session lifetime (in seconds).
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MinLifetime"]))

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Names of rows.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowNames"])

    @property
    def ScaleMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(port | deviceGroup): Indicates whether the control is specified per port or per device group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ScaleMode"])

    @ScaleMode.setter
    def ScaleMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ScaleMode"], value)

    @property
    def UnlimitedRestarts(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Allows each session to always be automatically restarted.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UnlimitedRestarts"])
        )

    def update(self, ScaleMode=None):
        # type: (str) -> SessionLifetime
        """Updates sessionLifetime resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ScaleMode (str(port | deviceGroup)): Indicates whether the control is specified per port or per device group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, RowNames=None, ScaleMode=None):
        # type: (int, List[str], str) -> SessionLifetime
        """Finds and retrieves sessionLifetime resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve sessionLifetime resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all sessionLifetime resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - RowNames (list(str)): Names of rows.
        - ScaleMode (str(port | deviceGroup)): Indicates whether the control is specified per port or per device group.

        Returns
        -------
        - self: This instance with matching sessionLifetime resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of sessionLifetime data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the sessionLifetime resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self,
        PortNames=None,
        EnableLifetime=None,
        EnableRestart=None,
        MaxLifetime=None,
        MaxRestarts=None,
        MinLifetime=None,
        UnlimitedRestarts=None,
    ):
        """Base class infrastructure that gets a list of sessionLifetime device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - EnableLifetime (str): optional regex of enableLifetime
        - EnableRestart (str): optional regex of enableRestart
        - MaxLifetime (str): optional regex of maxLifetime
        - MaxRestarts (str): optional regex of maxRestarts
        - MinLifetime (str): optional regex of minLifetime
        - UnlimitedRestarts (str): optional regex of unlimitedRestarts

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
