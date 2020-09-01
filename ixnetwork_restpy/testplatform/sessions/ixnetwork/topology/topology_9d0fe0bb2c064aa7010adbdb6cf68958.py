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


class Topology(Base):
    """Topology represents the concept of network devices which are to be configured on a group of ports.
    The Topology class encapsulates a list of topology resources that are managed by the user.
    A list of resources can be retrieved from the server using the Topology.find() method.
    The list can be managed by using the Topology.add() and Topology.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'topology'
    _SDM_ATT_MAP = {
        'DescriptiveName': 'descriptiveName',
        'Errors': 'errors',
        'LagCount': 'lagCount',
        'Name': 'name',
        'Note': 'note',
        'PortCount': 'portCount',
        'Ports': 'ports',
        'PortsStateCount': 'portsStateCount',
        'Status': 'status',
        'Vports': 'vports',
    }

    def __init__(self, parent):
        super(Topology, self).__init__(parent)

    @property
    def DeviceGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09.DeviceGroup): An instance of the DeviceGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09 import DeviceGroup
        return DeviceGroup(self)

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def LagCount(self):
        """
        Returns
        -------
        - number: Number of /lags assigned
        """
        return self._get_attribute(self._SDM_ATT_MAP['LagCount'])

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
    def Note(self):
        """
        Returns
        -------
        - str: Any Note about the Topology
        """
        return self._get_attribute(self._SDM_ATT_MAP['Note'])
    @Note.setter
    def Note(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Note'], value)

    @property
    def PortCount(self):
        """
        Returns
        -------
        - number: Number of /vports assigned (including unmapped ports)
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortCount'])

    @property
    def Ports(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport]): Logical port information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ports'])
    @Ports.setter
    def Ports(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ports'], value)

    @property
    def PortsStateCount(self):
        """
        Returns
        -------
        - dict(arg1:number,arg2:number,arg3:number,arg4:number): State of ports on this topology, arg1:total, arg2:up, arg3:down, arg4:other, arg5:busy, arg6:unassigned, arg7:lag
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortsStateCount'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def Vports(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/vport]): Virtual port information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vports'])
    @Vports.setter
    def Vports(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vports'], value)

    def update(self, Name=None, Note=None, Ports=None, Vports=None):
        """Updates topology resource on the server.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Note (str): Any Note about the Topology
        - Ports (list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport])): Logical port information.
        - Vports (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): Virtual port information.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, Note=None, Ports=None, Vports=None):
        """Adds a new topology resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Note (str): Any Note about the Topology
        - Ports (list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport])): Logical port information.
        - Vports (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): Virtual port information.

        Returns
        -------
        - self: This instance with all currently retrieved topology resources using find and the newly added topology resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained topology resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, DescriptiveName=None, Errors=None, LagCount=None, Name=None, Note=None, PortCount=None, Ports=None, PortsStateCount=None, Status=None, Vports=None):
        """Finds and retrieves topology resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve topology resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all topology resources from the server.

        Args
        ----
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - LagCount (number): Number of /lags assigned
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Note (str): Any Note about the Topology
        - PortCount (number): Number of /vports assigned (including unmapped ports)
        - Ports (list(str[None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport])): Logical port information.
        - PortsStateCount (dict(arg1:number,arg2:number,arg3:number,arg4:number)): State of ports on this topology, arg1:total, arg2:up, arg3:down, arg4:other, arg5:busy, arg6:unassigned, arg7:lag
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - Vports (list(str[None | /api/v1/sessions/1/ixnetwork/vport])): Virtual port information.

        Returns
        -------
        - self: This instance with matching topology resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of topology data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the topology resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def AdjustPortCount(self, *args, **kwargs):
        """Executes the adjustPortCount operation on the server.

        Adjusts the number of /vport objects in the -vports attribute by creating or deleting /vport objects and modifying the -vports attribute

        adjustPortCount(Arg2=number)
        ----------------------------
        - Arg2 (number): The target number of /vport objects references in the /topology -vports attribute

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('adjustPortCount', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string)
        ------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

    def RestartDown(self):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions in Topology that are in 'Down' state.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)
