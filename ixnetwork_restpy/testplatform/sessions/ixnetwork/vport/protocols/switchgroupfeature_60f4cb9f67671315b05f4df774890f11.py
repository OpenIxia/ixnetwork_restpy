# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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

    def __init__(self, parent):
        super(SwitchGroupFeature, self).__init__(parent)

    @property
    def ApplyGroup(self):
        """
        Returns
        -------
        - bool: If selected, table supports Apply Group capability.
        """
        return self._get_attribute('applyGroup')
    @ApplyGroup.setter
    def ApplyGroup(self, value):
        self._set_attribute('applyGroup', value)

    @property
    def CopyTtlIn(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL In capability.
        """
        return self._get_attribute('copyTtlIn')
    @CopyTtlIn.setter
    def CopyTtlIn(self, value):
        self._set_attribute('copyTtlIn', value)

    @property
    def CopyTtlOut(self):
        """
        Returns
        -------
        - bool: If selected, table supports Copy TTL capability.
        """
        return self._get_attribute('copyTtlOut')
    @CopyTtlOut.setter
    def CopyTtlOut(self, value):
        self._set_attribute('copyTtlOut', value)

    @property
    def DecrementMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Decrement MPLS TTL capability.
        """
        return self._get_attribute('decrementMplsTtl')
    @DecrementMplsTtl.setter
    def DecrementMplsTtl(self, value):
        self._set_attribute('decrementMplsTtl', value)

    @property
    def DecrementNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Decrement Network TTL capability.
        """
        return self._get_attribute('decrementNetworkTtl')
    @DecrementNetworkTtl.setter
    def DecrementNetworkTtl(self, value):
        self._set_attribute('decrementNetworkTtl', value)

    @property
    def GroupType(self):
        """
        Returns
        -------
        - str(allGroup | selectGroup | indirectGroup | fastFailoverGroup): The type of group. (This type is selected in the Switches window.)
        """
        return self._get_attribute('groupType')

    @property
    def MaxNoOfGroups(self):
        """
        Returns
        -------
        - number: Specify the maximum number of groups supported per switch group type.
        """
        return self._get_attribute('maxNoOfGroups')
    @MaxNoOfGroups.setter
    def MaxNoOfGroups(self, value):
        self._set_attribute('maxNoOfGroups', value)

    @property
    def Output(self):
        """
        Returns
        -------
        - bool: If selected, table supports Output capability.
        """
        return self._get_attribute('output')
    @Output.setter
    def Output(self, value):
        self._set_attribute('output', value)

    @property
    def PopMpls(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop MPLS capability.
        """
        return self._get_attribute('popMpls')
    @PopMpls.setter
    def PopMpls(self, value):
        self._set_attribute('popMpls', value)

    @property
    def PopPbb(self):
        """
        Returns
        -------
        - bool: If selected, table supports Experimenter capability.
        """
        return self._get_attribute('popPbb')
    @PopPbb.setter
    def PopPbb(self, value):
        self._set_attribute('popPbb', value)

    @property
    def PopVlan(self):
        """
        Returns
        -------
        - bool: If selected, table supports Pop VLAN capability.
        """
        return self._get_attribute('popVlan')
    @PopVlan.setter
    def PopVlan(self, value):
        self._set_attribute('popVlan', value)

    @property
    def PushMpls(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push MPLS capability.
        """
        return self._get_attribute('pushMpls')
    @PushMpls.setter
    def PushMpls(self, value):
        self._set_attribute('pushMpls', value)

    @property
    def PushPbb(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push PBB capability.
        """
        return self._get_attribute('pushPbb')
    @PushPbb.setter
    def PushPbb(self, value):
        self._set_attribute('pushPbb', value)

    @property
    def PushVlan(self):
        """
        Returns
        -------
        - bool: If selected, table supports Push VLAN capability.
        """
        return self._get_attribute('pushVlan')
    @PushVlan.setter
    def PushVlan(self, value):
        self._set_attribute('pushVlan', value)

    @property
    def SetField(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Field capability.
        """
        return self._get_attribute('setField')
    @SetField.setter
    def SetField(self, value):
        self._set_attribute('setField', value)

    @property
    def SetMplsTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set MPLS TTL capability.
        """
        return self._get_attribute('setMplsTtl')
    @SetMplsTtl.setter
    def SetMplsTtl(self, value):
        self._set_attribute('setMplsTtl', value)

    @property
    def SetNetworkTtl(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Network TTL capability.
        """
        return self._get_attribute('setNetworkTtl')
    @SetNetworkTtl.setter
    def SetNetworkTtl(self, value):
        self._set_attribute('setNetworkTtl', value)

    @property
    def SetQueue(self):
        """
        Returns
        -------
        - bool: If selected, table supports Set Queue capability.
        """
        return self._get_attribute('setQueue')
    @SetQueue.setter
    def SetQueue(self, value):
        self._set_attribute('setQueue', value)

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
        return self._update(locals())

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
        return self._select(locals())

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
