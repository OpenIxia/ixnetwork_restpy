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


class WriteActionsMiss(Base):
    """Select the type of write action miss capability that the table miss flow entry will support.
    The WriteActionsMiss class encapsulates a required writeActionsMiss resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "writeActionsMiss"
    _SDM_ATT_MAP = {
        "CopyTtlIn": "copyTtlIn",
        "CopyTtlOut": "copyTtlOut",
        "DecrementMplsTtl": "decrementMplsTtl",
        "DecrementNetworkTtl": "decrementNetworkTtl",
        "Group": "group",
        "Output": "output",
        "PopMpls": "popMpls",
        "PopPbb": "popPbb",
        "PopVlan": "popVlan",
        "PushMpls": "pushMpls",
        "PushPbb": "pushPbb",
        "PushVlan": "pushVlan",
        "SetField": "setField",
        "SetMplsTtl": "setMplsTtl",
        "SetNetworkTtl": "setNetworkTtl",
        "SetQueue": "setQueue",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(WriteActionsMiss, self).__init__(parent, list_op)

    @property
    def CopyTtlIn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Copy TTL In Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CopyTtlIn"])

    @CopyTtlIn.setter
    def CopyTtlIn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CopyTtlIn"], value)

    @property
    def CopyTtlOut(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Copy TTL Out Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CopyTtlOut"])

    @CopyTtlOut.setter
    def CopyTtlOut(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CopyTtlOut"], value)

    @property
    def DecrementMplsTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Decrement MPLS TTL Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DecrementMplsTtl"])

    @DecrementMplsTtl.setter
    def DecrementMplsTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DecrementMplsTtl"], value)

    @property
    def DecrementNetworkTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Decrement Network TTL Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DecrementNetworkTtl"])

    @DecrementNetworkTtl.setter
    def DecrementNetworkTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DecrementNetworkTtl"], value)

    @property
    def Group(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Group Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Group"])

    @Group.setter
    def Group(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Group"], value)

    @property
    def Output(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Output Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Output"])

    @Output.setter
    def Output(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Output"], value)

    @property
    def PopMpls(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Pop MPLS Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PopMpls"])

    @PopMpls.setter
    def PopMpls(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PopMpls"], value)

    @property
    def PopPbb(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Pop PBB Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PopPbb"])

    @PopPbb.setter
    def PopPbb(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PopPbb"], value)

    @property
    def PopVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Pop VLAN Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PopVlan"])

    @PopVlan.setter
    def PopVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PopVlan"], value)

    @property
    def PushMpls(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Push MPLS Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PushMpls"])

    @PushMpls.setter
    def PushMpls(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PushMpls"], value)

    @property
    def PushPbb(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Push PBB Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PushPbb"])

    @PushPbb.setter
    def PushPbb(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PushPbb"], value)

    @property
    def PushVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Push VLAN Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PushVlan"])

    @PushVlan.setter
    def PushVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PushVlan"], value)

    @property
    def SetField(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Set Field Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetField"])

    @SetField.setter
    def SetField(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetField"], value)

    @property
    def SetMplsTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Set MPLS TTL Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetMplsTtl"])

    @SetMplsTtl.setter
    def SetMplsTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetMplsTtl"], value)

    @property
    def SetNetworkTtl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Set Network TTL Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetNetworkTtl"])

    @SetNetworkTtl.setter
    def SetNetworkTtl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetNetworkTtl"], value)

    @property
    def SetQueue(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If selected, Set Queue Write Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SetQueue"])

    @SetQueue.setter
    def SetQueue(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SetQueue"], value)

    def update(
        self,
        CopyTtlIn=None,
        CopyTtlOut=None,
        DecrementMplsTtl=None,
        DecrementNetworkTtl=None,
        Group=None,
        Output=None,
        PopMpls=None,
        PopPbb=None,
        PopVlan=None,
        PushMpls=None,
        PushPbb=None,
        PushVlan=None,
        SetField=None,
        SetMplsTtl=None,
        SetNetworkTtl=None,
        SetQueue=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> WriteActionsMiss
        """Updates writeActionsMiss resource on the server.

        Args
        ----
        - CopyTtlIn (bool): If selected, Copy TTL In Write Actions is supported for table miss flow entries.
        - CopyTtlOut (bool): If selected, Copy TTL Out Write Actions is supported for table miss flow entries.
        - DecrementMplsTtl (bool): If selected, Decrement MPLS TTL Write Actions is supported for table miss flow entries.
        - DecrementNetworkTtl (bool): If selected, Decrement Network TTL Write Actions is supported for table miss flow entries.
        - Group (bool): If selected, Group Write Actions is supported for table miss flow entries.
        - Output (bool): If selected, Output Write Actions is supported for table miss flow entries.
        - PopMpls (bool): If selected, Pop MPLS Write Actions is supported for table miss flow entries.
        - PopPbb (bool): If selected, Pop PBB Write Actions is supported for table miss flow entries.
        - PopVlan (bool): If selected, Pop VLAN Write Actions is supported for table miss flow entries.
        - PushMpls (bool): If selected, Push MPLS Write Actions is supported for table miss flow entries.
        - PushPbb (bool): If selected, Push PBB Write Actions is supported for table miss flow entries.
        - PushVlan (bool): If selected, Push VLAN Write Actions is supported for table miss flow entries.
        - SetField (bool): If selected, Set Field Write Actions is supported for table miss flow entries.
        - SetMplsTtl (bool): If selected, Set MPLS TTL Write Actions is supported for table miss flow entries.
        - SetNetworkTtl (bool): If selected, Set Network TTL Write Actions is supported for table miss flow entries.
        - SetQueue (bool): If selected, Set Queue Write Actions is supported for table miss flow entries.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CopyTtlIn=None,
        CopyTtlOut=None,
        DecrementMplsTtl=None,
        DecrementNetworkTtl=None,
        Group=None,
        Output=None,
        PopMpls=None,
        PopPbb=None,
        PopVlan=None,
        PushMpls=None,
        PushPbb=None,
        PushVlan=None,
        SetField=None,
        SetMplsTtl=None,
        SetNetworkTtl=None,
        SetQueue=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> WriteActionsMiss
        """Finds and retrieves writeActionsMiss resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve writeActionsMiss resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all writeActionsMiss resources from the server.

        Args
        ----
        - CopyTtlIn (bool): If selected, Copy TTL In Write Actions is supported for table miss flow entries.
        - CopyTtlOut (bool): If selected, Copy TTL Out Write Actions is supported for table miss flow entries.
        - DecrementMplsTtl (bool): If selected, Decrement MPLS TTL Write Actions is supported for table miss flow entries.
        - DecrementNetworkTtl (bool): If selected, Decrement Network TTL Write Actions is supported for table miss flow entries.
        - Group (bool): If selected, Group Write Actions is supported for table miss flow entries.
        - Output (bool): If selected, Output Write Actions is supported for table miss flow entries.
        - PopMpls (bool): If selected, Pop MPLS Write Actions is supported for table miss flow entries.
        - PopPbb (bool): If selected, Pop PBB Write Actions is supported for table miss flow entries.
        - PopVlan (bool): If selected, Pop VLAN Write Actions is supported for table miss flow entries.
        - PushMpls (bool): If selected, Push MPLS Write Actions is supported for table miss flow entries.
        - PushPbb (bool): If selected, Push PBB Write Actions is supported for table miss flow entries.
        - PushVlan (bool): If selected, Push VLAN Write Actions is supported for table miss flow entries.
        - SetField (bool): If selected, Set Field Write Actions is supported for table miss flow entries.
        - SetMplsTtl (bool): If selected, Set MPLS TTL Write Actions is supported for table miss flow entries.
        - SetNetworkTtl (bool): If selected, Set Network TTL Write Actions is supported for table miss flow entries.
        - SetQueue (bool): If selected, Set Queue Write Actions is supported for table miss flow entries.

        Returns
        -------
        - self: This instance with matching writeActionsMiss resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of writeActionsMiss data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the writeActionsMiss resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
