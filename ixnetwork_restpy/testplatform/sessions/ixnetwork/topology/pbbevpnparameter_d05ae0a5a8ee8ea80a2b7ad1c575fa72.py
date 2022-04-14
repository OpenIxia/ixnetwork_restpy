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


class PbbEVpnParameter(Base):
    """PBB-EVPN
    The PbbEVpnParameter class encapsulates a list of pbbEVpnParameter resources that are managed by the user.
    A list of resources can be retrieved from the server using the PbbEVpnParameter.find() method.
    The list can be managed by using the PbbEVpnParameter.add() and PbbEVpnParameter.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "pbbEVpnParameter"
    _SDM_ATT_MAP = {
        "BMac": "bMac",
        "Count": "count",
        "UsePbbEVpnParameters": "usePbbEVpnParameters",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PbbEVpnParameter, self).__init__(parent, list_op)

    @property
    def BMac(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Broadcast MAC addresses of the devices
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BMac"]))

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
    def UsePbbEVpnParameters(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Flag to determine whether optional PBB EVPN parameters are provided.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsePbbEVpnParameters"])

    @UsePbbEVpnParameters.setter
    def UsePbbEVpnParameters(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsePbbEVpnParameters"], value)

    def update(self, UsePbbEVpnParameters=None):
        # type: (bool) -> PbbEVpnParameter
        """Updates pbbEVpnParameter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - UsePbbEVpnParameters (bool): Flag to determine whether optional PBB EVPN parameters are provided.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, UsePbbEVpnParameters=None):
        # type: (bool) -> PbbEVpnParameter
        """Adds a new pbbEVpnParameter resource on the server and adds it to the container.

        Args
        ----
        - UsePbbEVpnParameters (bool): Flag to determine whether optional PBB EVPN parameters are provided.

        Returns
        -------
        - self: This instance with all currently retrieved pbbEVpnParameter resources using find and the newly added pbbEVpnParameter resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained pbbEVpnParameter resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, UsePbbEVpnParameters=None):
        # type: (int, bool) -> PbbEVpnParameter
        """Finds and retrieves pbbEVpnParameter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pbbEVpnParameter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pbbEVpnParameter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - UsePbbEVpnParameters (bool): Flag to determine whether optional PBB EVPN parameters are provided.

        Returns
        -------
        - self: This instance with matching pbbEVpnParameter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pbbEVpnParameter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pbbEVpnParameter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, BMac=None):
        """Base class infrastructure that gets a list of pbbEVpnParameter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - BMac (str): optional regex of bMac

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
