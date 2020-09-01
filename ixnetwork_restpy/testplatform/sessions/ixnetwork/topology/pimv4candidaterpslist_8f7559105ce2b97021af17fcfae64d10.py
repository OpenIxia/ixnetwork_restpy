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


class PimV4CandidateRPsList(Base):
    """PIM V4 Candidate RP Ranges
    The PimV4CandidateRPsList class encapsulates a required pimV4CandidateRPsList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'pimV4CandidateRPsList'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertisementHoldTime': 'advertisementHoldTime',
        'BackOffInterval': 'backOffInterval',
        'Count': 'count',
        'CrpAddress': 'crpAddress',
        'CrpAddressCount': 'crpAddressCount',
        'DescriptiveName': 'descriptiveName',
        'GroupAddress': 'groupAddress',
        'GroupCount': 'groupCount',
        'GroupMaskLen': 'groupMaskLen',
        'LocalRouterId': 'localRouterId',
        'MeshingType': 'meshingType',
        'Name': 'name',
        'PeriodicAdvertisementInterval': 'periodicAdvertisementInterval',
        'Priority': 'priority',
        'PriorityChangeInterval': 'priorityChangeInterval',
        'PriorityType': 'priorityType',
        'Status': 'status',
        'TriggeredCrpMessageCount': 'triggeredCrpMessageCount',
    }

    def __init__(self, parent):
        super(PimV4CandidateRPsList, self).__init__(parent)

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
    def AdvertisementHoldTime(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval between two consecutive Candidate RP advertisements
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertisementHoldTime']))

    @property
    def BackOffInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The back-off time interval for the C-RP-Adv messages
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BackOffInterval']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def CrpAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Start address of the set of candidate RPs to be simulated
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CrpAddress']))

    @property
    def CrpAddressCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Total number of Candidate RPs to be simulated starting from C-RP address
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CrpAddressCount']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def GroupAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Starting group address of the group range for which the candidate RP will advertise candidacy
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupAddress']))

    @property
    def GroupCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of groups in the range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupCount']))

    @property
    def GroupMaskLen(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mask width (prefix length in bits) for the group range
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['GroupMaskLen']))

    @property
    def LocalRouterId(self):
        """
        Returns
        -------
        - list(str): Router ID
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRouterId'])

    @property
    def MeshingType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It indicates if the mappings for groups and RP addresses are Fully-Meshed or One-To-One. One-to-one indicates that for each group only one RP shall be sent regardless of the RP count. Full meshed means for each group all RPs shall be advertised for candidacy which is essentially a (group to rp) mapping.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MeshingType']))

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
    def PeriodicAdvertisementInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Rate controlling variable indicating how many C-RP-Adv messages can be sent in the specified time interval
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PeriodicAdvertisementInterval']))

    @property
    def Priority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value of priority to be sent in candidate RP advertisement
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Priority']))

    @property
    def PriorityChangeInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time interval after which priority of all the RPs get changed
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PriorityChangeInterval']))

    @property
    def PriorityType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): It indicates the type of priority to be held by the candidate RPs
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PriorityType']))

    @property
    def Status(self):
        """
        Returns
        -------
        - list(str[none | notStarted | started]): Status
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TriggeredCrpMessageCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of times C-RP advertisements is sent to the newly elected Bootstrap Routers
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TriggeredCrpMessageCount']))

    def update(self, Name=None):
        """Updates pimV4CandidateRPsList resource on the server.

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

    def get_device_ids(self, PortNames=None, Active=None, AdvertisementHoldTime=None, BackOffInterval=None, CrpAddress=None, CrpAddressCount=None, GroupAddress=None, GroupCount=None, GroupMaskLen=None, MeshingType=None, PeriodicAdvertisementInterval=None, Priority=None, PriorityChangeInterval=None, PriorityType=None, TriggeredCrpMessageCount=None):
        """Base class infrastructure that gets a list of pimV4CandidateRPsList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertisementHoldTime (str): optional regex of advertisementHoldTime
        - BackOffInterval (str): optional regex of backOffInterval
        - CrpAddress (str): optional regex of crpAddress
        - CrpAddressCount (str): optional regex of crpAddressCount
        - GroupAddress (str): optional regex of groupAddress
        - GroupCount (str): optional regex of groupCount
        - GroupMaskLen (str): optional regex of groupMaskLen
        - MeshingType (str): optional regex of meshingType
        - PeriodicAdvertisementInterval (str): optional regex of periodicAdvertisementInterval
        - Priority (str): optional regex of priority
        - PriorityChangeInterval (str): optional regex of priorityChangeInterval
        - PriorityType (str): optional regex of priorityType
        - TriggeredCrpMessageCount (str): optional regex of triggeredCrpMessageCount

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Activate Candidate RP

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        start(Arg2=list)list
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
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Deactivate Candidate RP

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stop(Arg2=list)list
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
        return self._execute('stop', payload=payload, response_object=None)
