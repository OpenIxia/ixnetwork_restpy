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


class SwitchGroupFeature(Base):
    """This window allows you to configure the capabilities of groups on a switch. The fields and controls in the Switch Group Features window are described in this section. This window is available for Switch configuration only.
    The SwitchGroupFeature class encapsulates a list of switchGroupFeature resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupFeature.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchGroupFeature'
    _SDM_ATT_MAP = {
        'ApplyGroup': 'applyGroup',
        'CopyTtlIn': 'copyTtlIn',
        'CopyTtlOut': 'copyTtlOut',
        'DecrementMplsTtl': 'decrementMplsTtl',
        'DecrementNetworkTtl': 'decrementNetworkTtl',
        'GroupType': 'groupType',
        'MaxNoOfGroups': 'maxNoOfGroups',
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
        super(SwitchGroupFeature, self).__init__(parent)

    @property
    def ApplyGroup(self):
        """
        Returns
        -------
        - bool: If selected, table supports Apply Group capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplyGroup'])
    @ApplyGroup.setter
    def ApplyGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ApplyGroup'], value)

    @property
    def CopyTtlIn(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL In capability.
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
        - bool: If selected, table supports Copy TTL capability.
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
        - bool: If selected, table supports Decrement MPLS TTL capability.
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
        - bool: If selected, table supports Decrement Network TTL capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DecrementNetworkTtl'])
    @DecrementNetworkTtl.setter
    def DecrementNetworkTtl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DecrementNetworkTtl'], value)

    @property
    def GroupType(self):
        """
        Returns
        -------
        - str(allGroup | selectGroup | indirectGroup | fastFailoverGroup): The type of group. (This type is selected in the Switches window.)
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupType'])

    @property
    def MaxNoOfGroups(self):
        """
        Returns
        -------
        - number: Specify the maximum number of groups supported per switch group type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxNoOfGroups'])
    @MaxNoOfGroups.setter
    def MaxNoOfGroups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxNoOfGroups'], value)

    @property
    def Output(self):
        """
        Returns
        -------
        - bool: If selected, table supports Output capability.
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
        - bool: If selected, table supports Pop MPLS capability.
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
        - bool: If selected, table supports Experimenter capability.
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
        - bool: If selected, table supports Pop VLAN capability.
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
        - bool: If selected, table supports Push MPLS capability.
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
        - bool: If selected, table supports Push PBB capability.
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
        - bool: If selected, table supports Push VLAN capability.
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
        - bool: If selected, table supports Set Field capability.
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
        - bool: If selected, table supports Set MPLS TTL capability.
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
        - bool: If selected, table supports Set Network TTL capability.
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
        - bool: If selected, table supports Set Queue capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SetQueue'])
    @SetQueue.setter
    def SetQueue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SetQueue'], value)

    def update(self, ApplyGroup=None, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, MaxNoOfGroups=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
        """Updates switchGroupFeature resource on the server.

        Args
        ----
        - ApplyGroup (bool): If selected, table supports Apply Group capability.
        - CopyTtlIn (bool): If selected, table supports Copy TTL In capability.
        - CopyTtlOut (bool): If selected, table supports Copy TTL capability.
        - DecrementMplsTtl (bool): If selected, table supports Decrement MPLS TTL capability.
        - DecrementNetworkTtl (bool): If selected, table supports Decrement Network TTL capability.
        - MaxNoOfGroups (number): Specify the maximum number of groups supported per switch group type.
        - Output (bool): If selected, table supports Output capability.
        - PopMpls (bool): If selected, table supports Pop MPLS capability.
        - PopPbb (bool): If selected, table supports Experimenter capability.
        - PopVlan (bool): If selected, table supports Pop VLAN capability.
        - PushMpls (bool): If selected, table supports Push MPLS capability.
        - PushPbb (bool): If selected, table supports Push PBB capability.
        - PushVlan (bool): If selected, table supports Push VLAN capability.
        - SetField (bool): If selected, table supports Set Field capability.
        - SetMplsTtl (bool): If selected, table supports Set MPLS TTL capability.
        - SetNetworkTtl (bool): If selected, table supports Set Network TTL capability.
        - SetQueue (bool): If selected, table supports Set Queue capability.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, ApplyGroup=None, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetworkTtl=None, GroupType=None, MaxNoOfGroups=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetworkTtl=None, SetQueue=None):
        """Finds and retrieves switchGroupFeature resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchGroupFeature resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchGroupFeature resources from the server.

        Args
        ----
        - ApplyGroup (bool): If selected, table supports Apply Group capability.
        - CopyTtlIn (bool): If selected, table supports Copy TTL In capability.
        - CopyTtlOut (bool): If selected, table supports Copy TTL capability.
        - DecrementMplsTtl (bool): If selected, table supports Decrement MPLS TTL capability.
        - DecrementNetworkTtl (bool): If selected, table supports Decrement Network TTL capability.
        - GroupType (str(allGroup | selectGroup | indirectGroup | fastFailoverGroup)): The type of group. (This type is selected in the Switches window.)
        - MaxNoOfGroups (number): Specify the maximum number of groups supported per switch group type.
        - Output (bool): If selected, table supports Output capability.
        - PopMpls (bool): If selected, table supports Pop MPLS capability.
        - PopPbb (bool): If selected, table supports Experimenter capability.
        - PopVlan (bool): If selected, table supports Pop VLAN capability.
        - PushMpls (bool): If selected, table supports Push MPLS capability.
        - PushPbb (bool): If selected, table supports Push PBB capability.
        - PushVlan (bool): If selected, table supports Push VLAN capability.
        - SetField (bool): If selected, table supports Set Field capability.
        - SetMplsTtl (bool): If selected, table supports Set MPLS TTL capability.
        - SetNetworkTtl (bool): If selected, table supports Set Network TTL capability.
        - SetQueue (bool): If selected, table supports Set Queue capability.

        Returns
        -------
        - self: This instance with matching switchGroupFeature resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchGroupFeature data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchGroupFeature resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
