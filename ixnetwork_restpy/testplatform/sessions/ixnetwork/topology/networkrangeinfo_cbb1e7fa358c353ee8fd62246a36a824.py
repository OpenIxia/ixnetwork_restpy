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


class NetworkRangeInfo(Base):
    """RBRangeInfo help : TODO.
    The NetworkRangeInfo class encapsulates a list of networkRangeInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkRangeInfo.find() method.
    The list can be managed by using the NetworkRangeInfo.add() and NetworkRangeInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkRangeInfo'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'NetworkRangeIPByMask': 'networkRangeIPByMask',
        'NetworkRangeInterfaceIp': 'networkRangeInterfaceIp',
        'NetworkRangeInterfaceIpMask': 'networkRangeInterfaceIpMask',
        'NetworkRangeIp': 'networkRangeIp',
        'NetworkRangeIpIncrementBy': 'networkRangeIpIncrementBy',
        'NetworkRangeIpMask': 'networkRangeIpMask',
        'NetworkRangeLinkType': 'networkRangeLinkType',
        'NetworkRangeRID': 'networkRangeRID',
        'NetworkRangeRIDIncrement': 'networkRangeRIDIncrement',
        'NumColumns': 'numColumns',
        'NumRows': 'numRows',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(NetworkRangeInfo, self).__init__(parent, list_op)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        if self._properties.get('CMacProperties', None) is not None:
            return self._properties.get('CMacProperties')
        else:
            return CMacProperties(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        if self._properties.get('EvpnIPv4PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv4PrefixRange')
        else:
            return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        if self._properties.get('EvpnIPv6PrefixRange', None) is not None:
            return self._properties.get('EvpnIPv6PrefixRange')
        else:
            return EvpnIPv6PrefixRange(self)

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
    def NetworkRangeIPByMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use mask to generate range of addresses
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIPByMask']))

    @property
    def NetworkRangeInterfaceIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface IP address for a non-connected interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeInterfaceIp']))

    @property
    def NetworkRangeInterfaceIpMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interface IP mask for a non-connected interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeInterfaceIpMask']))

    @property
    def NetworkRangeIp(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Range IP
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIp']))

    @property
    def NetworkRangeIpIncrementBy(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Range IP Increment By
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpIncrementBy']))

    @property
    def NetworkRangeIpMask(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Range IP Mask
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeIpMask']))

    @property
    def NetworkRangeLinkType(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Link Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeLinkType']))

    @property
    def NetworkRangeRID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Range RID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeRID']))

    @property
    def NetworkRangeRIDIncrement(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Range RID Increment
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NetworkRangeRIDIncrement']))

    @property
    def NumColumns(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 4 Byte Integer.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumColumns']))

    @property
    def NumRows(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): 4 Byte Integer.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NumRows']))

    def update(self, Name=None):
        # type: (str) -> NetworkRangeInfo
        """Updates networkRangeInfo resource on the server.

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
        # type: (str) -> NetworkRangeInfo
        """Adds a new networkRangeInfo resource on the server and adds it to the container.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved networkRangeInfo resources using find and the newly added networkRangeInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained networkRangeInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Name=None):
        # type: (int, str, str) -> NetworkRangeInfo
        """Finds and retrieves networkRangeInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkRangeInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkRangeInfo resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching networkRangeInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of networkRangeInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkRangeInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

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
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, NetworkRangeIPByMask=None, NetworkRangeInterfaceIp=None, NetworkRangeInterfaceIpMask=None, NetworkRangeIp=None, NetworkRangeIpIncrementBy=None, NetworkRangeIpMask=None, NetworkRangeLinkType=None, NetworkRangeRID=None, NetworkRangeRIDIncrement=None, NumColumns=None, NumRows=None):
        """Base class infrastructure that gets a list of networkRangeInfo device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - NetworkRangeIPByMask (str): optional regex of networkRangeIPByMask
        - NetworkRangeInterfaceIp (str): optional regex of networkRangeInterfaceIp
        - NetworkRangeInterfaceIpMask (str): optional regex of networkRangeInterfaceIpMask
        - NetworkRangeIp (str): optional regex of networkRangeIp
        - NetworkRangeIpIncrementBy (str): optional regex of networkRangeIpIncrementBy
        - NetworkRangeIpMask (str): optional regex of networkRangeIpMask
        - NetworkRangeLinkType (str): optional regex of networkRangeLinkType
        - NetworkRangeRID (str): optional regex of networkRangeRID
        - NetworkRangeRIDIncrement (str): optional regex of networkRangeRIDIncrement
        - NumColumns (str): optional regex of numColumns
        - NumRows (str): optional regex of numRows

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
