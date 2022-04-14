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


class Stack(Base):
    """This object helps to specify the field properties of a protocol stack.
    The Stack class encapsulates a list of stack resources that are managed by the system.
    A list of resources can be retrieved from the server using the Stack.find() method.
    """

    __slots__ = '_stack_index'
    _SDM_NAME = 'stack'
    _SDM_ATT_MAP = {
        'DisplayName': 'displayName',
        'StackTypeId': 'stackTypeId',
        'TemplateName': 'templateName',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Stack, self).__init__(parent, list_op)
        self._stack_index = 0

    @property
    def Field(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field.Field): An instance of the Field class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.field.field import Field
        if len(self._object_properties) > 0:
            if self._properties.get('Field', None) is not None:
                return self._properties.get('Field')
        return Field(self)

    @property
    def EthernetARP(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetARP_template.EthernetARP): An instance of the EthernetARP traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetARP_template import EthernetARP
        return EthernetARP(self)

    @property
    def Ethernet(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernet_template.Ethernet): An instance of the Ethernet traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernet_template import Ethernet
        return Ethernet(self)

    @property
    def EthernetNoFCS(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetNoFCS_template.EthernetNoFCS): An instance of the EthernetNoFCS traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ethernetNoFCS_template import EthernetNoFCS
        return EthernetNoFCS(self)

    @property
    def Mpls(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpls_template.Mpls): An instance of the Mpls traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.mpls_template import Mpls
        return Mpls(self)

    @property
    def Vlan(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vlan_template.Vlan): An instance of the Vlan traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vlan_template import Vlan
        return Vlan(self)

    @property
    def PfcPause(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pfcPause_template.PfcPause): An instance of the PfcPause traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.pfcPause_template import PfcPause
        return PfcPause(self)

    @property
    def GlobalPause(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.globalPause_template.GlobalPause): An instance of the GlobalPause traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.globalPause_template import GlobalPause
        return GlobalPause(self)

    @property
    def Ipv4(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv4_template.Ipv4): An instance of the Ipv4 traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv4_template import Ipv4
        return Ipv4(self)

    @property
    def Ipv6(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6_template.Ipv6): An instance of the Ipv6 traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.ipv6_template import Ipv6
        return Ipv6(self)

    @property
    def Gre(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gre_template.Gre): An instance of the Gre traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gre_template import Gre
        return Gre(self)

    @property
    def GTPuOptionalFields(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gTPuOptionalFields_template.GTPuOptionalFields): An instance of the GTPuOptionalFields traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gTPuOptionalFields_template import GTPuOptionalFields
        return GTPuOptionalFields(self)

    @property
    def Gtpu(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gtpu_template.Gtpu): An instance of the Gtpu traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.gtpu_template import Gtpu
        return Gtpu(self)

    @property
    def Vxlan(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlan_template.Vxlan): An instance of the Vxlan traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.vxlan_template import Vxlan
        return Vxlan(self)

    @property
    def Tcp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tcp_template.Tcp): An instance of the Tcp traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.tcp_template import Tcp
        return Tcp(self)

    @property
    def Udp(self):
        """
        valid only with Batch Add
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.udp_template.Udp): An instance of the Udp traffic stack
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.trafficitem.configelement.stack.udp_template import Udp
        return Udp(self)

    @property
    def DisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The display name of the stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayName'])

    @property
    def StackTypeId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackTypeId'])

    @property
    def TemplateName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indiates the protocol template name that is added to a packet in a stack.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TemplateName'])

    def add(self):
        """Adds a new stack resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved stack resources using find and the newly added stack resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, DisplayName=None, StackTypeId=None, TemplateName=None):
        # type: (str, str, str) -> Stack
        """Finds and retrieves stack resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve stack resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all stack resources from the server.

        Args
        ----
        - DisplayName (str): The display name of the stack.
        - StackTypeId (str): 
        - TemplateName (str): Indiates the protocol template name that is added to a packet in a stack.

        Returns
        -------
        - self: This instance with matching stack resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of stack data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the stack resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Append(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the append operation on the server.

        Append a protocol template after the specified stack object reference.

        DEPRECATED append(Arg2=href, async_operation=bool)string
        --------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('append', payload=payload, response_object=None)

    def AppendProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the appendProtocol operation on the server.

        Append a protocol template after the specified stack object reference.

        appendProtocol(Arg2=href, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/.../stack): This exec returns an object reference to the newly appended stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('appendProtocol', payload=payload, response_object=None)

    def GetValidProtocols(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getValidProtocols operation on the server.

        Retrieves the list of recommended protocols that can be added on top of the current protocol.

        getValidProtocols(async_operation=bool)list
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This exec returns an array containing: the name of the protocol, the reference of the protocol and the type of it (successor or ancestor)

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getValidProtocols', payload=payload, response_object=None)

    def Insert(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the insert operation on the server.

        Insert a protocol template before the specified stack object reference.

        DEPRECATED insert(Arg2=href, async_operation=bool)string
        --------------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('insert', payload=payload, response_object=None)

    def InsertProtocol(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the insertProtocol operation on the server.

        Insert a protocol template before the specified stack object reference.

        insertProtocol(Arg2=href, async_operation=bool)href
        ---------------------------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../protocolTemplate)): A valid /traffic/protocolTemplate object reference
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str(None | /api/v1/sessions/1/ixnetwork/traffic/.../stack): This exec returns an object reference to the newly inserted stack item.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('insertProtocol', payload=payload, response_object=None)

    def Remove(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the remove operation on the server.

        Delete the specified stack object reference.

        remove(async_operation=bool)
        ----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('remove', payload=payload, response_object=None)
