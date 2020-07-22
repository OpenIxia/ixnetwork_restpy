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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ApplyActionsMiss(Base):
    """Select the type of apply action miss capability that the table miss flow entry will support.
    The ApplyActionsMiss class encapsulates a required applyActionsMiss resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'applyActionsMiss'
    _SDM_ATT_MAP = {
        'CopyTtlIn': 'copyTtlIn',
        'CopyTtlOut': 'copyTtlOut',
        'DecrementMplsTtl': 'decrementMplsTtl',
        'DecrementNetworkTtl': 'decrementNetworkTtl',
        'Group': 'group',
        'Output': 'output',
        'PopMpls': 'popMpls',
        'PopPbb': 'popPbb',
        'PopVlan': 'popVlan',
        'PushMpls': 'pushMpls',
        'PushPbb': 'pushPbb',
        'PushVlan': 'pushVlan',
        'SetField': 'setField',
        'SetMplsTtl': 'setMplsTtl',
        'SetNetworkTtl': 'setNetworkTtl',
        'SetQueue': 'setQueue',
    }

    def __init__(self, parent):
        super(ApplyActionsMiss, self).__init__(parent)

    @property
    def CopyTtlIn(self):
        """
        Returns
        -------
        - bool: If selected, Copy TTL In Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CopyTtlIn'])
    @CopyTtlIn.setter
    def CopyTtlIn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CopyTtlIn'], value)

    @property
    def CopyTtlOut(self):
        """
        Returns
        -------
        - bool: If selected, Copy TTL Out Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CopyTtlOut'])
    @CopyTtlOut.setter
    def CopyTtlOut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CopyTtlOut'], value)

    @property
    def DecrementMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, Decrement MPLS TTL Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DecrementMplsTtl'])
    @DecrementMplsTtl.setter
    def DecrementMplsTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DecrementMplsTtl'], value)

    @property
    def DecrementNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, Decrement Network TTL Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DecrementNetworkTtl'])
    @DecrementNetworkTtl.setter
    def DecrementNetworkTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DecrementNetworkTtl'], value)

    @property
    def Group(self):
        """
        Returns
        -------
        - bool: If selected, Group Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Group'])
    @Group.setter
    def Group(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Group'], value)

    @property
    def Output(self):
        """
        Returns
        -------
        - bool: If selected, Output Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Output'])
    @Output.setter
    def Output(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Output'], value)

    @property
    def PopMpls(self):
        """
        Returns
        -------
        - bool: If selected, Pop MPLS Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PopMpls'])
    @PopMpls.setter
    def PopMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PopMpls'], value)

    @property
    def PopPbb(self):
        """
        Returns
        -------
        - bool: If selected, Pop PBB Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PopPbb'])
    @PopPbb.setter
    def PopPbb(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PopPbb'], value)

    @property
    def PopVlan(self):
        """
        Returns
        -------
        - bool: If selected, Pop VLAN Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PopVlan'])
    @PopVlan.setter
    def PopVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PopVlan'], value)

    @property
    def PushMpls(self):
        """
        Returns
        -------
        - bool: If selected, Push MPLS Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PushMpls'])
    @PushMpls.setter
    def PushMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PushMpls'], value)

    @property
    def PushPbb(self):
        """
        Returns
        -------
        - bool: If selected, Push PBB Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PushPbb'])
    @PushPbb.setter
    def PushPbb(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PushPbb'], value)

    @property
    def PushVlan(self):
        """
        Returns
        -------
        - bool: If selected, Push VLAN Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PushVlan'])
    @PushVlan.setter
    def PushVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PushVlan'], value)

    @property
    def SetField(self):
        """
        Returns
        -------
        - bool: If selected, Set Field Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetField'])
    @SetField.setter
    def SetField(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetField'], value)

    @property
    def SetMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, Set MPLS TTL Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetMplsTtl'])
    @SetMplsTtl.setter
    def SetMplsTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetMplsTtl'], value)

    @property
    def SetNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, Set Network TTL Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetNetworkTtl'])
    @SetNetworkTtl.setter
    def SetNetworkTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetNetworkTtl'], value)

    @property
    def SetQueue(self):
        """
        Returns
        -------
        - bool: If selected, Set Queue Apply Actions is supported for table miss flow entries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetQueue'])
    @SetQueue.setter
    def SetQueue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetQueue'], value)

    def update(self, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, Group=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
        """Updates applyActionsMiss resource on the server.

        Args
        ----
        - CopyTtlIn (bool): If selected, Copy TTL In Apply Actions is supported for table miss flow entries.
        - CopyTtlOut (bool): If selected, Copy TTL Out Apply Actions is supported for table miss flow entries.
        - DecrementMplsTtl (bool): If selected, Decrement MPLS TTL Apply Actions is supported for table miss flow entries.
        - DecrementNetworkTtl (bool): If selected, Decrement Network TTL Apply Actions is supported for table miss flow entries.
        - Group (bool): If selected, Group Apply Actions is supported for table miss flow entries.
        - Output (bool): If selected, Output Apply Actions is supported for table miss flow entries.
        - PopMpls (bool): If selected, Pop MPLS Apply Actions is supported for table miss flow entries.
        - PopPbb (bool): If selected, Pop PBB Apply Actions is supported for table miss flow entries.
        - PopVlan (bool): If selected, Pop VLAN Apply Actions is supported for table miss flow entries.
        - PushMpls (bool): If selected, Push MPLS Apply Actions is supported for table miss flow entries.
        - PushPbb (bool): If selected, Push PBB Apply Actions is supported for table miss flow entries.
        - PushVlan (bool): If selected, Push VLAN Apply Actions is supported for table miss flow entries.
        - SetField (bool): If selected, Set Field Apply Actions is supported for table miss flow entries.
        - SetMplsTtl (bool): If selected, Set MPLS TTL Apply Actions is supported for table miss flow entries.
        - SetNetworkTtl (bool): If selected, Set Network TTL Apply Actions is supported for table miss flow entries.
        - SetQueue (bool): If selected, Set Queue Apply Actions is supported for table miss flow entries.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
