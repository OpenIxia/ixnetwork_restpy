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
from typing import List, Any, Union


class Iptv(Base):
    """IGMP/MLD IPTV Configuration
    The Iptv class encapsulates a required iptv resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'iptv'
    _SDM_ATT_MAP = {
        'CombinedLeaveJoin': 'combinedLeaveJoin',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EnableGeneralQueryResponse': 'enableGeneralQueryResponse',
        'EnableGroupSpecificQueryResponse': 'enableGroupSpecificQueryResponse',
        'JoinLatencyThreshold': 'joinLatencyThreshold',
        'LeaveLatencyThreshold': 'leaveLatencyThreshold',
        'LogAllTimestamps': 'logAllTimestamps',
        'LogFailureTimestamps': 'logFailureTimestamps',
        'Name': 'name',
        'NumChannelChangesBeforeView': 'numChannelChangesBeforeView',
        'State': 'state',
        'StbLeaveJoinDelay': 'stbLeaveJoinDelay',
        'ViewDuration': 'viewDuration',
        'ZapBehavior': 'zapBehavior',
        'ZapDirection': 'zapDirection',
        'ZapInterval': 'zapInterval',
        'ZapIntervalType': 'zapIntervalType',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Iptv, self).__init__(parent, list_op)

    @property
    def CombinedLeaveJoin(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, Leave for current group and join for next group gets merged in a single multicast packet
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CombinedLeaveJoin']))

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
    def EnableGeneralQueryResponse(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, General Query Response is send.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGeneralQueryResponse']))

    @property
    def EnableGroupSpecificQueryResponse(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, Group Specific Response is sent
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnableGroupSpecificQueryResponse']))

    @property
    def JoinLatencyThreshold(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The maximum time that is allowed for a multicast stream to arrive for channel for which a Join has been sent.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['JoinLatencyThreshold']))

    @property
    def LeaveLatencyThreshold(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): The maximum time allowed for a multicast stream to stop for a channel for which a Leave has been sent.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LeaveLatencyThreshold']))

    @property
    def LogAllTimestamps(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, all the captured timestamps for Join and Leave are saved to a log file.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogAllTimestamps']))

    @property
    def LogFailureTimestamps(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If enabled, the timestamps for Join and Leave failures are saved to a log file.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LogFailureTimestamps']))

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
    def NumChannelChangesBeforeView(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Number of channels to change before stopping on a channel and watching it for View Duration.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumChannelChangesBeforeView']))

    @property
    def State(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[notStarted | started]): Indicates the state IPTV
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def StbLeaveJoinDelay(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Time in milliseconds between sending a Leave for the current channel and Join for the next channel.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StbLeaveJoinDelay']))

    @property
    def ViewDuration(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies the time in milliseconds to view the last channel.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ViewDuration']))

    @property
    def ZapBehavior(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Use Zap Only to change channels without viewing the channel or Zap and View to change traffic and receive traffic for the last channel.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ZapBehavior']))

    @property
    def ZapDirection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies the direction of changing channels.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ZapDirection']))

    @property
    def ZapInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Interval in milliseconds between channel changes based on the selected type.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ZapInterval']))

    @property
    def ZapIntervalType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Specifies the wait interval type before changing the channels.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ZapIntervalType']))

    def update(self, Name=None):
        # type: (str) -> Iptv
        """Updates iptv resource on the server.

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

    def ImportFailureTimestampFile(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the importFailureTimestampFile operation on the server.

        Fetch IPTV Failure Timestamp File from PCPU to Client

        importFailureTimestampFile(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the IPTV grid An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('importFailureTimestampFile', payload=payload, response_object=None)

    def StartIptv(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the startIptv operation on the server.

        Start IPTV

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startIptv(async_operation=bool)
        -------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startIptv(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startIptv(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        startIptv(Arg2=list, async_operation=bool)list
        ----------------------------------------------
        - Arg2 (list(number)): List of indices into the IPTV grid An empty list indicates all instances in the plugin.
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
        return self._execute('startIptv', payload=payload, response_object=None)

    def StopIptv(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopIptv operation on the server.

        Stop IPTV

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopIptv(async_operation=bool)
        ------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopIptv(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopIptv(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stopIptv(Arg2=list, async_operation=bool)list
        ---------------------------------------------
        - Arg2 (list(number)): List of indices into the IPTV grid An empty list indicates all instances in the plugin.
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
        return self._execute('stopIptv', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, CombinedLeaveJoin=None, EnableGeneralQueryResponse=None, EnableGroupSpecificQueryResponse=None, JoinLatencyThreshold=None, LeaveLatencyThreshold=None, LogAllTimestamps=None, LogFailureTimestamps=None, NumChannelChangesBeforeView=None, StbLeaveJoinDelay=None, ViewDuration=None, ZapBehavior=None, ZapDirection=None, ZapInterval=None, ZapIntervalType=None):
        """Base class infrastructure that gets a list of iptv device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - CombinedLeaveJoin (str): optional regex of combinedLeaveJoin
        - EnableGeneralQueryResponse (str): optional regex of enableGeneralQueryResponse
        - EnableGroupSpecificQueryResponse (str): optional regex of enableGroupSpecificQueryResponse
        - JoinLatencyThreshold (str): optional regex of joinLatencyThreshold
        - LeaveLatencyThreshold (str): optional regex of leaveLatencyThreshold
        - LogAllTimestamps (str): optional regex of logAllTimestamps
        - LogFailureTimestamps (str): optional regex of logFailureTimestamps
        - NumChannelChangesBeforeView (str): optional regex of numChannelChangesBeforeView
        - StbLeaveJoinDelay (str): optional regex of stbLeaveJoinDelay
        - ViewDuration (str): optional regex of viewDuration
        - ZapBehavior (str): optional regex of zapBehavior
        - ZapDirection (str): optional regex of zapDirection
        - ZapInterval (str): optional regex of zapInterval
        - ZapIntervalType (str): optional regex of zapIntervalType

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
