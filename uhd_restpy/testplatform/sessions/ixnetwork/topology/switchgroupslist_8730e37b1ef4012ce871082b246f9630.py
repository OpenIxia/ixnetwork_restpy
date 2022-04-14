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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class SwitchGroupsList(Base):
    """Openflow Switch Groups level Configuration
    The SwitchGroupsList class encapsulates a list of switchGroupsList resources that are managed by the system.
    A list of resources can be retrieved from the server using the SwitchGroupsList.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'switchGroupsList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'ApplyGroup': 'applyGroup',
        'CopyTtlIn': 'copyTtlIn',
        'CopyTtlOut': 'copyTtlOut',
        'Count': 'count',
        'DecrementMplsTtl': 'decrementMplsTtl',
        'DecrementNetwork': 'decrementNetwork',
        'DescriptiveName': 'descriptiveName',
        'GroupType': 'groupType',
        'MaxNumberOfGroups': 'maxNumberOfGroups',
        'Name': 'name',
        'Output': 'output',
        'ParentSwitch': 'parentSwitch',
        'PopMpls': 'popMpls',
        'PopPbb': 'popPbb',
        'PopVlan': 'popVlan',
        'PushMpls': 'pushMpls',
        'PushPbb': 'pushPbb',
        'PushVlan': 'pushVlan',
        'SetField': 'setField',
        'SetMplsTtl': 'setMplsTtl',
        'SetNetwork': 'setNetwork',
        'SetQueue': 'setQueue',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(SwitchGroupsList, self).__init__(parent, list_op)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Checked or Unchecked based on the Group Type selections in Groups tab under OF Switch tab-page.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def ApplyGroup(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Apply Group.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ApplyGroup']))

    @property
    def CopyTtlIn(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Copy TTL inwards from outermost to next-to-outermost.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CopyTtlIn']))

    @property
    def CopyTtlOut(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Copy TTL outwards from next-to-outermost to outermost.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CopyTtlOut']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DecrementMplsTtl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Decrement MPLS TTL.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DecrementMplsTtl']))

    @property
    def DecrementNetwork(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Decrement IP TTL.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DecrementNetwork']))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def GroupType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Can be of the following types per switch: 1)All: Execute all buckets in the group. 2)Select:Execute one bucket in the group. 3)Indirect:Execute the one defined bucket in this group. 4)Fast Failover:Execute the first live bucket.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupType']))

    @property
    def MaxNumberOfGroups(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Maximum number of groups for each group type.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxNumberOfGroups']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def Output(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Output to switch port.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Output']))

    @property
    def ParentSwitch(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Parent Switch Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentSwitch'])

    @property
    def PopMpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Pop the outer MPLS tag.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PopMpls']))

    @property
    def PopPbb(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Pop the outer PBB service tag (I-TAG).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PopPbb']))

    @property
    def PopVlan(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Pop the outer VLAN tag.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PopVlan']))

    @property
    def PushMpls(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Push a new MPLS tag.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PushMpls']))

    @property
    def PushPbb(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Push a new PBB service tag (I-TAG).
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PushPbb']))

    @property
    def PushVlan(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Push a new VLAN tag.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PushVlan']))

    @property
    def SetField(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Set a header field using OXM TLV format.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetField']))

    @property
    def SetMplsTtl(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Set MPLS TTL.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetMplsTtl']))

    @property
    def SetNetwork(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Set IP TTL.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetNetwork']))

    @property
    def SetQueue(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Action:Set queue id when outputting to a port.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SetQueue']))

    def update(self, Name=None):
        # type: (str) -> SwitchGroupsList
        """Updates switchGroupsList resource on the server.

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

    def add(self, Name=None):
        # type: (str) -> SwitchGroupsList
        """Adds a new switchGroupsList resource on the json, only valid with batch add utility

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved switchGroupsList resources using find and the newly added switchGroupsList resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None, ParentSwitch=None):
        # type: (int, str, str, str) -> SwitchGroupsList
        """Finds and retrieves switchGroupsList resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switchGroupsList resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switchGroupsList resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - ParentSwitch (str): Parent Switch Name.

        Returns
        -------
        - self: This instance with matching switchGroupsList resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switchGroupsList data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switchGroupsList resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, ApplyGroup=None, CopyTtlIn=None, CopyTtlOut=None, DecrementMplsTtl=None, DecrementNetwork=None, GroupType=None, MaxNumberOfGroups=None, Output=None, PopMpls=None, PopPbb=None, PopVlan=None, PushMpls=None, PushPbb=None, PushVlan=None, SetField=None, SetMplsTtl=None, SetNetwork=None, SetQueue=None):
        """Base class infrastructure that gets a list of switchGroupsList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - ApplyGroup (str): optional regex of applyGroup
        - CopyTtlIn (str): optional regex of copyTtlIn
        - CopyTtlOut (str): optional regex of copyTtlOut
        - DecrementMplsTtl (str): optional regex of decrementMplsTtl
        - DecrementNetwork (str): optional regex of decrementNetwork
        - GroupType (str): optional regex of groupType
        - MaxNumberOfGroups (str): optional regex of maxNumberOfGroups
        - Output (str): optional regex of output
        - PopMpls (str): optional regex of popMpls
        - PopPbb (str): optional regex of popPbb
        - PopVlan (str): optional regex of popVlan
        - PushMpls (str): optional regex of pushMpls
        - PushPbb (str): optional regex of pushPbb
        - PushVlan (str): optional regex of pushVlan
        - SetField (str): optional regex of setField
        - SetMplsTtl (str): optional regex of setMplsTtl
        - SetNetwork (str): optional regex of setNetwork
        - SetQueue (str): optional regex of setQueue

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
