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


class BgpEvpnJoinSynchMld(Base):
    """
    The BgpEvpnJoinSynchMld class encapsulates a required bgpEvpnJoinSynchMld resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'bgpEvpnJoinSynchMld'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'GroupAddressCountJoinSynch': 'groupAddressCountJoinSynch',
        'GroupType': 'groupType',
        'MldVersionV1JoinSynch': 'mldVersionV1JoinSynch',
        'MldVersionV2JoinSynch': 'mldVersionV2JoinSynch',
        'Mode': 'mode',
        'Name': 'name',
        'SourceAddressCountJoinSynch': 'sourceAddressCountJoinSynch',
        'SourceGroupMappingJoinSynch': 'sourceGroupMappingJoinSynch',
        'StartGroupAddressJoinSynch': 'startGroupAddressJoinSynch',
        'StartSourceAddressJoinSynch': 'startSourceAddressJoinSynch',
    }

    def __init__(self, parent):
        super(BgpEvpnJoinSynchMld, self).__init__(parent)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def GroupAddressCountJoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddressCountJoinSynch']))

    @property
    def GroupType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupType']))

    @property
    def MldVersionV1JoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MLD V1
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MldVersionV1JoinSynch']))

    @property
    def MldVersionV2JoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): MLD V2
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MldVersionV2JoinSynch']))

    @property
    def Mode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Mode']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def SourceAddressCountJoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Address Count
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddressCountJoinSynch']))

    @property
    def SourceGroupMappingJoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Source Group Mapping
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceGroupMappingJoinSynch']))

    @property
    def StartGroupAddressJoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartGroupAddressJoinSynch']))

    @property
    def StartSourceAddressJoinSynch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start Source Address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartSourceAddressJoinSynch']))

    def update(self, Name=None):
        """Updates bgpEvpnJoinSynchMld resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, GroupAddressCountJoinSynch=None, GroupType=None, MldVersionV1JoinSynch=None, MldVersionV2JoinSynch=None, Mode=None, SourceAddressCountJoinSynch=None, SourceGroupMappingJoinSynch=None, StartGroupAddressJoinSynch=None, StartSourceAddressJoinSynch=None):
        """Base class infrastructure that gets a list of bgpEvpnJoinSynchMld device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - GroupAddressCountJoinSynch (str): optional regex of groupAddressCountJoinSynch
        - GroupType (str): optional regex of groupType
        - MldVersionV1JoinSynch (str): optional regex of mldVersionV1JoinSynch
        - MldVersionV2JoinSynch (str): optional regex of mldVersionV2JoinSynch
        - Mode (str): optional regex of mode
        - SourceAddressCountJoinSynch (str): optional regex of sourceAddressCountJoinSynch
        - SourceGroupMappingJoinSynch (str): optional regex of sourceGroupMappingJoinSynch
        - StartGroupAddressJoinSynch (str): optional regex of startGroupAddressJoinSynch
        - StartSourceAddressJoinSynch (str): optional regex of startSourceAddressJoinSynch

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
