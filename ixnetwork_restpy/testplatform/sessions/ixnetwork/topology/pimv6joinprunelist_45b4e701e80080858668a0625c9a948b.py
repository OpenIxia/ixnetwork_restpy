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
from typing import List, Any, Union


class PimV6JoinPruneList(Base):
    """PIM V6 Join Prune Data
    The PimV6JoinPruneList class encapsulates a required pimV6JoinPruneList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pimV6JoinPruneList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableFlapInfo': 'enableFlapInfo',
        'EnablePack': 'enablePack',
        'FlapInterval': 'flapInterval',
        'GroupAddressCount': 'groupAddressCount',
        'GroupV6Address': 'groupV6Address',
        'GroupV6MaskWidth': 'groupV6MaskWidth',
        'LocalRouterId': 'localRouterId',
        'Name': 'name',
        'PruneSourceAddressCount': 'pruneSourceAddressCount',
        'PruneSourceV6Address': 'pruneSourceV6Address',
        'PruneSourceV6MaskWidth': 'pruneSourceV6MaskWidth',
        'RangeType': 'rangeType',
        'RegisterStopTriggerCount': 'registerStopTriggerCount',
        'RpV6Address': 'rpV6Address',
        'SourceAddressCount': 'sourceAddressCount',
        'SourceGroupMappingType': 'sourceGroupMappingType',
        'SourceV6Address': 'sourceV6Address',
        'SourceV6MaskWidth': 'sourceV6MaskWidth',
        'Status': 'status',
        'SwitchOverInterval': 'switchOverInterval',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(PimV6JoinPruneList, self).__init__(parent, list_op)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        if self._properties.get('Tag', None) is not None:
            return self._properties.get('Tag')
        else:
            return Tag(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

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
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EnableFlapInfo(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, enables this Source entry for use in PIM-SM Register messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFlapInfo']))

    @property
    def EnablePack(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, Multiple Groups can be included within a single packet.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePack']))

    @property
    def FlapInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (in seconds) Specifies the amount of time between emulated flap events. The default is 60 seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapInterval']))

    @property
    def GroupAddressCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of multicast group addresses to be included in the multicast group range. The maximum number of valid possible addresses depends on the values for the Group Address and the Group Mask Width. The default value is 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddressCount']))

    @property
    def GroupV6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): An IPv6 address-used with the Group Mask to create a range of multicast addresses.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupV6Address']))

    @property
    def GroupV6MaskWidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of bits in the mask applied to the Group Address. (The masked bits in the Group Address form the address prefix.) The default value is 32. The valid range is 1 to 128, depending on address family type.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupV6MaskWidth']))

    @property
    def LocalRouterId(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): The PIM-SM Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

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
    def PruneSourceAddressCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of Prune Source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. The default value is 0. ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PruneSourceAddressCount']))

    @property
    def PruneSourceV6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages. (Multicast addresses are invalid.)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PruneSourceV6Address']))

    @property
    def PruneSourceV6MaskWidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of bits in the mask applied to the Prune Source Address. (The masked bits in the Prune Source Address form the address prefix.) The default value is 32. The valid range is 1 to 128, depending on address family type. ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PruneSourceV6MaskWidth']))

    @property
    def RangeType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Multicast Range Type. Choose one of: (*, *, RP)-Wildcard Group Set. For (*,*, RP) Join/Prune messages. Refers to all Groups associated with this specific RP. (*, G)-Group Specific type. For (*,G) Join/Prune messages. Refers to all sources associated with a specific Group G on the RP tree. (S, G)-Source specific type. For (S,G) Join/Prune messages. Refers only to specific combination of Source S and Group G. (*, G) -> (S, G)-Switchover type. (For switchover from non-source specific group state to source-specific group state.) Register Triggered (S,G)-These are the ranges of multicast group address and unicast source address to which a PIM-SM Router emulating an RP (for those source-group combinations) will send Triggered (S,G) joins and Register-Stop messages after receiving Register messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RangeType']))

    @property
    def RegisterStopTriggerCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Available ONLY for use with Register Triggered (S,G) Range Type. (Default = 10)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RegisterStopTriggerCount']))

    @property
    def RpV6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The IP address of the Rendezvous Point (RP) router-the root of the RP shared multicast distribution tree (RPT).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RpV6Address']))

    @property
    def SourceAddressCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. The default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddressCount']))

    @property
    def SourceGroupMappingType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Choose one of: Fully-meshed, One-to-One
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceGroupMappingType']))

    @property
    def SourceV6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Multicast Source Address. Used for (S,G) Type and (S,G, rpt) only. (Multicast addresses are invalid.)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceV6Address']))

    @property
    def SourceV6MaskWidth(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of bits in the mask applied to the Source Address. (The masked bits in the Source Address form the address prefix.) The default value is 32. The valid range is 1 to 128, depending on address family type. Used for (S,G) Type and (S,G, rpt) only.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceV6MaskWidth']))

    @property
    def Status(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[join | leave | none | notStarted]): Status
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def SwitchOverInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): (in seconds) The time interval allowed for the switch from using the RP tree to using a Source-specific tree-from (*,G) to (S,G). The default value is 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SwitchOverInterval']))

    def update(self, Name=None):
        # type: (str) -> PimV6JoinPruneList
        """Updates pimV6JoinPruneList resource on the server.

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

    def Join(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the join operation on the server.

        Join

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        join(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        join(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        join(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        join(Arg2=list, async_operation=bool)list
        -----------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('join', payload=payload, response_object=None)

    def Leave(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the leave operation on the server.

        Leave

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        leave(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        leave(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        leave(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        leave(Arg2=list, async_operation=bool)list
        ------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('leave', payload=payload, response_object=None)

    def ResumePeriodicJoin(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the resumePeriodicJoin operation on the server.

        Resume Periodic Join

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumePeriodicJoin(async_operation=bool)
        ----------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumePeriodicJoin(SessionIndices=list, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumePeriodicJoin(SessionIndices=string, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        resumePeriodicJoin(Arg2=list, async_operation=bool)list
        -------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resumePeriodicJoin', payload=payload, response_object=None)

    def StopPeriodicJoin(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopPeriodicJoin operation on the server.

        Stop Periodic Join

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopPeriodicJoin(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopPeriodicJoin(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopPeriodicJoin(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopPeriodicJoin(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopPeriodicJoin', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, EnableFlapInfo=None, EnablePack=None, FlapInterval=None, GroupAddressCount=None, GroupV6Address=None, GroupV6MaskWidth=None, PruneSourceAddressCount=None, PruneSourceV6Address=None, PruneSourceV6MaskWidth=None, RangeType=None, RegisterStopTriggerCount=None, RpV6Address=None, SourceAddressCount=None, SourceGroupMappingType=None, SourceV6Address=None, SourceV6MaskWidth=None, SwitchOverInterval=None):
        """Base class infrastructure that gets a list of pimV6JoinPruneList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableFlapInfo (str): optional regex of enableFlapInfo
        - EnablePack (str): optional regex of enablePack
        - FlapInterval (str): optional regex of flapInterval
        - GroupAddressCount (str): optional regex of groupAddressCount
        - GroupV6Address (str): optional regex of groupV6Address
        - GroupV6MaskWidth (str): optional regex of groupV6MaskWidth
        - PruneSourceAddressCount (str): optional regex of pruneSourceAddressCount
        - PruneSourceV6Address (str): optional regex of pruneSourceV6Address
        - PruneSourceV6MaskWidth (str): optional regex of pruneSourceV6MaskWidth
        - RangeType (str): optional regex of rangeType
        - RegisterStopTriggerCount (str): optional regex of registerStopTriggerCount
        - RpV6Address (str): optional regex of rpV6Address
        - SourceAddressCount (str): optional regex of sourceAddressCount
        - SourceGroupMappingType (str): optional regex of sourceGroupMappingType
        - SourceV6Address (str): optional regex of sourceV6Address
        - SourceV6MaskWidth (str): optional regex of sourceV6MaskWidth
        - SwitchOverInterval (str): optional regex of switchOverInterval

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
