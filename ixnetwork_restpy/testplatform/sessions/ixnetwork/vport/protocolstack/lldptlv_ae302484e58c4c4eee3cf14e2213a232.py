# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class LldpTlv(Base):
    """LLDP TLV (Type-Length-Value)
    The LldpTlv class encapsulates a list of lldpTlv resources that is be managed by the user.
    A list of resources can be retrieved from the server using the LldpTlv.find() method.
    The list can be managed by the user by using the LldpTlv.add() and LldpTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'lldpTlv'

    def __init__(self, parent):
        super(LldpTlv, self).__init__(parent)

    @property
    def TlvSettings(self):
        """An instance of the TlvSettings class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.tlvsettings_d54852b24984861a085df56ddbd46132.TlvSettings)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.tlvsettings_d54852b24984861a085df56ddbd46132 import TlvSettings
        return TlvSettings(self)._select()

    @property
    def Enabled(self):
        """Specifies if this TLV is used in the configuration.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Name(self):
        """Name of TLV

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def Type(self):
        """Type of LLDP TLV:4 - Port Description TLV5 - System Name TLV6 - System Description TLV8 - Management Address TLV127 - Organizationally Specific TLV

        Returns:
            number
        """
        return self._get_attribute('type')
    @Type.setter
    def Type(self, value):
        self._set_attribute('type', value)

    def update(self, Enabled=None, Name=None, Type=None):
        """Updates a child instance of lldpTlv on the server.

        Args:
            Enabled (bool): Specifies if this TLV is used in the configuration.
            Name (str): Name of TLV
            Type (number): Type of LLDP TLV:4 - Port Description TLV5 - System Name TLV6 - System Description TLV8 - Management Address TLV127 - Organizationally Specific TLV

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, Name=None, Type=None):
        """Adds a new lldpTlv node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Specifies if this TLV is used in the configuration.
            Name (str): Name of TLV
            Type (number): Type of LLDP TLV:4 - Port Description TLV5 - System Name TLV6 - System Description TLV8 - Management Address TLV127 - Organizationally Specific TLV

        Returns:
            self: This instance with all currently retrieved lldpTlv data using find and the newly added lldpTlv data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the lldpTlv data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, Name=None, ObjectId=None, Type=None):
        """Finds and retrieves lldpTlv data from the server.

        All named parameters support regex and can be used to selectively retrieve lldpTlv data from the server.
        By default the find method takes no parameters and will retrieve all lldpTlv data from the server.

        Args:
            Enabled (bool): Specifies if this TLV is used in the configuration.
            Name (str): Name of TLV
            ObjectId (str): Unique identifier for this object
            Type (number): Type of LLDP TLV:4 - Port Description TLV5 - System Name TLV6 - System Description TLV8 - Management Address TLV127 - Organizationally Specific TLV

        Returns:
            self: This instance with matching lldpTlv data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of lldpTlv data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the lldpTlv data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
