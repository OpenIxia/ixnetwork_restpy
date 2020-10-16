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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class PimV4JoinPruneList(Base):
    """PIM V4 Join Prune Data
    The PimV4JoinPruneList class encapsulates a required pimV4JoinPruneList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pimV4JoinPruneList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableFlapInfo': 'enableFlapInfo',
        'EnablePack': 'enablePack',
        'FlapInterval': 'flapInterval',
        'GroupAddressCount': 'groupAddressCount',
        'GroupV4Address': 'groupV4Address',
        'GroupV4MaskWidth': 'groupV4MaskWidth',
        'LocalRouterId': 'localRouterId',
        'Name': 'name',
        'PruneSourceAddressCount': 'pruneSourceAddressCount',
        'PruneSourceV4Address': 'pruneSourceV4Address',
        'PruneSourceV4MaskWidth': 'pruneSourceV4MaskWidth',
        'RangeType': 'rangeType',
        'RegisterStopTriggerCount': 'registerStopTriggerCount',
        'RpV4Address': 'rpV4Address',
        'SourceAddressCount': 'sourceAddressCount',
        'SourceGroupMappingType': 'sourceGroupMappingType',
        'SourceV4Address': 'sourceV4Address',
        'SourceV4MaskWidth': 'sourceV4MaskWidth',
        'Status': 'status',
        'SwitchOverInterval': 'switchOverInterval',
    }

    def __init__(self, parent):
        super(PimV4JoinPruneList, self).__init__(parent)

    @property
    def Tag(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d.Tag): An instance of the Tag class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tag_e30f24de79247381d4dfd423b2f6986d import Tag
        return Tag(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from uhd_restpy.multivalue import Multivalue
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
    def EnableFlapInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If selected, enables this Source entry for use in PIM-SM Register messages.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableFlapInfo']))

    @property
    def EnablePack(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, Multiple Groups can be included within a single packet.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePack']))

    @property
    def FlapInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): (in seconds) Specifies the amount of time between emulated flap events. The default is 60 seconds.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlapInterval']))

    @property
    def GroupAddressCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The number of multicast group addresses to be included in the multicast group range. The maximum number of valid possible addresses depends on the values for the Group Address and the Group Mask Width. The default value is 1.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddressCount']))

    @property
    def GroupV4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupV4Address']))

    @property
    def GroupV4MaskWidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Group Mask width
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupV4MaskWidth']))

    @property
    def LocalRouterId(self):
        """
        Returns
        -------
        - list(str): The PIM-SM Router ID value, in IPv4 format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

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
    def PruneSourceAddressCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The number of Prune Source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. The default value is 0. ONLY used for (*,G) Type to send (S,G,rpt) Prune Messages.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PruneSourceAddressCount']))

    @property
    def PruneSourceV4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Prune Source Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PruneSourceV4Address']))

    @property
    def PruneSourceV4MaskWidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Prune Source Mask width
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PruneSourceV4MaskWidth']))

    @property
    def RangeType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The Multicast Range Type. Choose one of: (*, *, RP)-Wildcard Group Set. For (*,*, RP) Join/Prune messages. Refers to all Groups associated with this specific RP. (*, G)-Group Specific type. For (*,G) Join/Prune messages. Refers to all sources associated with a specific Group G on the RP tree. (S, G)-Source specific type. For (S,G) Join/Prune messages. Refers only to specific combination of Source S and Group G. (*, G) -> (S, G)-Switchover type. (For switchover from non-source specific group state to source-specific group state.) Register Triggered (S,G)-These are the ranges of multicast group address and unicast source address to which a PIM-SM Router emulating an RP (for those source-group combinations) will send Triggered (S,G) joins and Register-Stop messages after receiving Register messages.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RangeType']))

    @property
    def RegisterStopTriggerCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Available ONLY for use with Register Triggered (S,G) Range Type. (Default = 10)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RegisterStopTriggerCount']))

    @property
    def RpV4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): RP Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RpV4Address']))

    @property
    def SourceAddressCount(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The number of multicast source addresses to be included. The maximum number of valid possible addresses depends on the values for the Source Address and the Source Mask Width. The default value is 0.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceAddressCount']))

    @property
    def SourceGroupMappingType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Choose one of: Fully-meshed, One-to-One
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceGroupMappingType']))

    @property
    def SourceV4Address(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source Address
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceV4Address']))

    @property
    def SourceV4MaskWidth(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Source Mask width
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SourceV4MaskWidth']))

    @property
    def Status(self):
        """
        Returns
        -------
        - list(str[join | leave | none | notStarted]): Status
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def SwitchOverInterval(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): (in seconds) The time interval allowed for the switch from using the RP tree to using a Source-specific tree-from (*,G) to (S,G). The default value is 0.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SwitchOverInterval']))

    def update(self, Name=None):
        """Updates pimV4JoinPruneList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, EnableFlapInfo=None, EnablePack=None, FlapInterval=None, GroupAddressCount=None, GroupV4Address=None, GroupV4MaskWidth=None, PruneSourceAddressCount=None, PruneSourceV4Address=None, PruneSourceV4MaskWidth=None, RangeType=None, RegisterStopTriggerCount=None, RpV4Address=None, SourceAddressCount=None, SourceGroupMappingType=None, SourceV4Address=None, SourceV4MaskWidth=None, SwitchOverInterval=None):
        """Base class infrastructure that gets a list of pimV4JoinPruneList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - EnableFlapInfo (str): optional regex of enableFlapInfo
        - EnablePack (str): optional regex of enablePack
        - FlapInterval (str): optional regex of flapInterval
        - GroupAddressCount (str): optional regex of groupAddressCount
        - GroupV4Address (str): optional regex of groupV4Address
        - GroupV4MaskWidth (str): optional regex of groupV4MaskWidth
        - PruneSourceAddressCount (str): optional regex of pruneSourceAddressCount
        - PruneSourceV4Address (str): optional regex of pruneSourceV4Address
        - PruneSourceV4MaskWidth (str): optional regex of pruneSourceV4MaskWidth
        - RangeType (str): optional regex of rangeType
        - RegisterStopTriggerCount (str): optional regex of registerStopTriggerCount
        - RpV4Address (str): optional regex of rpV4Address
        - SourceAddressCount (str): optional regex of sourceAddressCount
        - SourceGroupMappingType (str): optional regex of sourceGroupMappingType
        - SourceV4Address (str): optional regex of sourceV4Address
        - SourceV4MaskWidth (str): optional regex of sourceV4MaskWidth
        - SwitchOverInterval (str): optional regex of switchOverInterval

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Join(self, *args, **kwargs):
        """Executes the join operation on the server.

        Join

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        join(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        join(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        join(Arg2=list)list
        -------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        """Executes the leave operation on the server.

        Leave

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        leave(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        leave(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        leave(Arg2=list)list
        --------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        """Executes the resumePeriodicJoin operation on the server.

        Resume Periodic Join

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        resumePeriodicJoin(SessionIndices=list)
        ---------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        resumePeriodicJoin(SessionIndices=string)
        -----------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        resumePeriodicJoin(Arg2=list)list
        ---------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        """Executes the stopPeriodicJoin operation on the server.

        Stop Periodic Join

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopPeriodicJoin(SessionIndices=list)
        -------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopPeriodicJoin(SessionIndices=string)
        ---------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stopPeriodicJoin(Arg2=list)list
        -------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
