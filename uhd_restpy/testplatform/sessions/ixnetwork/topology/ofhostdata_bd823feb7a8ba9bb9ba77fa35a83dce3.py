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


class OfHostData(Base):
    """Contains number of host ports per switch and number of hosts per host port
    The OfHostData class encapsulates a list of ofHostData resources that are managed by the user.
    A list of resources can be retrieved from the server using the OfHostData.find() method.
    The list can be managed by using the OfHostData.add() and OfHostData.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ofHostData'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'NumberOfHostPorts': 'numberOfHostPorts',
        'NumberOfHostsPerPort': 'numberOfHostsPerPort',
        'ParentSwitchPortName': 'parentSwitchPortName',
    }

    def __init__(self, parent):
        super(OfHostData, self).__init__(parent)

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
    def NumberOfHostPorts(self):
        """
        Returns
        -------
        - number: number of Host Ports per OF Switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfHostPorts'])
    @NumberOfHostPorts.setter
    def NumberOfHostPorts(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfHostPorts'], value)

    @property
    def NumberOfHostsPerPort(self):
        """
        Returns
        -------
        - number: Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfHostsPerPort'])
    @NumberOfHostsPerPort.setter
    def NumberOfHostsPerPort(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfHostsPerPort'], value)

    @property
    def ParentSwitchPortName(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Description of the parent Switch Port.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ParentSwitchPortName']))

    def update(self, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None):
        """Updates ofHostData resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfHostPorts (number): number of Host Ports per OF Switch.
        - NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None):
        """Adds a new ofHostData resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfHostPorts (number): number of Host Ports per OF Switch.
        - NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

        Returns
        -------
        - self: This instance with all currently retrieved ofHostData resources using find and the newly added ofHostData resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ofHostData resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Name=None, NumberOfHostPorts=None, NumberOfHostsPerPort=None):
        """Finds and retrieves ofHostData resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofHostData resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofHostData resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfHostPorts (number): number of Host Ports per OF Switch.
        - NumberOfHostsPerPort (number): Number of Host Groups for each Host Port. Configure Number of Hosts Per Host Group using the Count field in Encapsulations Tab

        Returns
        -------
        - self: This instance with matching ofHostData resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofHostData data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofHostData resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ParentSwitchPortName=None):
        """Base class infrastructure that gets a list of ofHostData device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ParentSwitchPortName (str): optional regex of parentSwitchPortName

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def SendPacketWithTraverseLI(self, *args, **kwargs):
        """Executes the sendPacketWithTraverseLI operation on the server.

        Send an Host Packet (ARP/PING/CUSTOM) from the given device instance to the given destination instance.

        sendPacketWithTraverseLI(Arg2=list, Arg3=number, Arg4=enum, Arg5=number, Arg6=number, Arg7=bool, Arg8=number, Arg9=number)list
        ------------------------------------------------------------------------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the device group for the corresponding device instances whose IP addresses are used as the source of the request messages.
        - Arg3 (number): Destination Host index.
        - Arg4 (str(aRP | pING | custom)): Packet Type.
        - Arg5 (number): Encapsulation index.
        - Arg6 (number): Response Timeout.
        - Arg7 (bool): Periodic.
        - Arg8 (number): Periodic Interval.
        - Arg9 (number): Number of Iteration.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('sendPacketWithTraverseLI', payload=payload, response_object=None)
