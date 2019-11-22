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


class Dot1xRange(Base):
    """
    The Dot1xRange class encapsulates a list of dot1xRange resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Dot1xRange.find() method.
    The list can be managed by the user by using the Dot1xRange.add() and Dot1xRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dot1xRange'

    def __init__(self, parent):
        super(Dot1xRange, self).__init__(parent)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FastInnerMethod(self):
        """FAST Inner Method.

        Returns:
            str
        """
        return self._get_attribute('fastInnerMethod')
    @FastInnerMethod.setter
    def FastInnerMethod(self, value):
        self._set_attribute('fastInnerMethod', value)

    @property
    def FastProvisionMode(self):
        """FAST Provision Mode.

        Returns:
            str
        """
        return self._get_attribute('fastProvisionMode')
    @FastProvisionMode.setter
    def FastProvisionMode(self, value):
        self._set_attribute('fastProvisionMode', value)

    @property
    def FastStatelessResume(self):
        """FAST Stateless Resume.

        Returns:
            str
        """
        return self._get_attribute('fastStatelessResume')
    @FastStatelessResume.setter
    def FastStatelessResume(self, value):
        self._set_attribute('fastStatelessResume', value)

    @property
    def HostAuthMode(self):
        """Machine Authentification Method.

        Returns:
            str
        """
        return self._get_attribute('hostAuthMode')
    @HostAuthMode.setter
    def HostAuthMode(self, value):
        self._set_attribute('hostAuthMode', value)

    @property
    def HostName(self):
        """The MachineName used to authentificate the port.

        Returns:
            str
        """
        return self._get_attribute('hostName')
    @HostName.setter
    def HostName(self, value):
        self._set_attribute('hostName', value)

    @property
    def HostPassword(self):
        """The MachinePassword used to authentificate the port.

        Returns:
            str
        """
        return self._get_attribute('hostPassword')
    @HostPassword.setter
    def HostPassword(self, value):
        self._set_attribute('hostPassword', value)

    @property
    def NacSequence(self):
        """Nac Sequence used by this range.

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacSequence)
        """
        return self._get_attribute('nacSequence')
    @NacSequence.setter
    def NacSequence(self, value):
        self._set_attribute('nacSequence', value)

    @property
    def Name(self):
        """Name of range

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
    def Protocol(self):
        """Authentification Protocol.

        Returns:
            str
        """
        return self._get_attribute('protocol')
    @Protocol.setter
    def Protocol(self, value):
        self._set_attribute('protocol', value)

    @property
    def UserName(self):
        """The UserName used to authentificate the port.

        Returns:
            str
        """
        return self._get_attribute('userName')
    @UserName.setter
    def UserName(self, value):
        self._set_attribute('userName', value)

    @property
    def UserPassword(self):
        """The UserPassword used to authentificate the port.

        Returns:
            str
        """
        return self._get_attribute('userPassword')
    @UserPassword.setter
    def UserPassword(self, value):
        self._set_attribute('userPassword', value)

    @property
    def WaitId(self):
        """This value is true if supplicant is waiting for RequestId from DUT part.

        Returns:
            bool
        """
        return self._get_attribute('waitId')
    @WaitId.setter
    def WaitId(self, value):
        self._set_attribute('waitId', value)

    def update(self, Enabled=None, FastInnerMethod=None, FastProvisionMode=None, FastStatelessResume=None, HostAuthMode=None, HostName=None, HostPassword=None, NacSequence=None, Name=None, Protocol=None, UserName=None, UserPassword=None, WaitId=None):
        """Updates a child instance of dot1xRange on the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FastInnerMethod (str): FAST Inner Method.
            FastProvisionMode (str): FAST Provision Mode.
            FastStatelessResume (str): FAST Stateless Resume.
            HostAuthMode (str): Machine Authentification Method.
            HostName (str): The MachineName used to authentificate the port.
            HostPassword (str): The MachinePassword used to authentificate the port.
            NacSequence (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacSequence)): Nac Sequence used by this range.
            Name (str): Name of range
            Protocol (str): Authentification Protocol.
            UserName (str): The UserName used to authentificate the port.
            UserPassword (str): The UserPassword used to authentificate the port.
            WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Enabled=None, FastInnerMethod=None, FastProvisionMode=None, FastStatelessResume=None, HostAuthMode=None, HostName=None, HostPassword=None, NacSequence=None, Name=None, Protocol=None, UserName=None, UserPassword=None, WaitId=None):
        """Adds a new dot1xRange node on the server and retrieves it in this instance.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FastInnerMethod (str): FAST Inner Method.
            FastProvisionMode (str): FAST Provision Mode.
            FastStatelessResume (str): FAST Stateless Resume.
            HostAuthMode (str): Machine Authentification Method.
            HostName (str): The MachineName used to authentificate the port.
            HostPassword (str): The MachinePassword used to authentificate the port.
            NacSequence (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacSequence)): Nac Sequence used by this range.
            Name (str): Name of range
            Protocol (str): Authentification Protocol.
            UserName (str): The UserName used to authentificate the port.
            UserPassword (str): The UserPassword used to authentificate the port.
            WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Returns:
            self: This instance with all currently retrieved dot1xRange data using find and the newly added dot1xRange data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the dot1xRange data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, FastInnerMethod=None, FastProvisionMode=None, FastStatelessResume=None, HostAuthMode=None, HostName=None, HostPassword=None, NacSequence=None, Name=None, ObjectId=None, Protocol=None, UserName=None, UserPassword=None, WaitId=None):
        """Finds and retrieves dot1xRange data from the server.

        All named parameters support regex and can be used to selectively retrieve dot1xRange data from the server.
        By default the find method takes no parameters and will retrieve all dot1xRange data from the server.

        Args:
            Enabled (bool): Disabled ranges won't be configured nor validated.
            FastInnerMethod (str): FAST Inner Method.
            FastProvisionMode (str): FAST Provision Mode.
            FastStatelessResume (str): FAST Stateless Resume.
            HostAuthMode (str): Machine Authentification Method.
            HostName (str): The MachineName used to authentificate the port.
            HostPassword (str): The MachinePassword used to authentificate the port.
            NacSequence (str(None|/api/v1/sessions/1/ixnetwork/globals?deepchild=nacSequence)): Nac Sequence used by this range.
            Name (str): Name of range
            ObjectId (str): Unique identifier for this object
            Protocol (str): Authentification Protocol.
            UserName (str): The UserName used to authentificate the port.
            UserPassword (str): The UserPassword used to authentificate the port.
            WaitId (bool): This value is true if supplicant is waiting for RequestId from DUT part.

        Returns:
            self: This instance with matching dot1xRange data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of dot1xRange data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the dot1xRange data from the server available through an iterator or index

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
