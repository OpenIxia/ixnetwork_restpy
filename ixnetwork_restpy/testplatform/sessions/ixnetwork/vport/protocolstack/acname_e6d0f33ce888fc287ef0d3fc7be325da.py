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


class AcName(Base):
    """PPPoX Name schema for multi range support
    The AcName class encapsulates a list of acName resources that is be managed by the user.
    A list of resources can be retrieved from the server using the AcName.find() method.
    The list can be managed by the user by using the AcName.add() and AcName.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'acName'

    def __init__(self, parent):
        super(AcName, self).__init__(parent)

    @property
    def AcName(self):
        """Access Concentrator Name

        Returns:
            str
        """
        return self._get_attribute('acName')
    @AcName.setter
    def AcName(self, value):
        self._set_attribute('acName', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def Percentage(self):
        """Percentage of PPPoE sessions for this AC Name

        Returns:
            number
        """
        return self._get_attribute('percentage')
    @Percentage.setter
    def Percentage(self, value):
        self._set_attribute('percentage', value)

    @property
    def Select(self):
        """Enable/disable AC Name entry

        Returns:
            bool
        """
        return self._get_attribute('select')
    @Select.setter
    def Select(self, value):
        self._set_attribute('select', value)

    def update(self, AcName=None, Percentage=None, Select=None):
        """Updates a child instance of acName on the server.

        Args:
            AcName (str): Access Concentrator Name
            Percentage (number): Percentage of PPPoE sessions for this AC Name
            Select (bool): Enable/disable AC Name entry

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, AcName=None, Percentage=None, Select=None):
        """Adds a new acName node on the server and retrieves it in this instance.

        Args:
            AcName (str): Access Concentrator Name
            Percentage (number): Percentage of PPPoE sessions for this AC Name
            Select (bool): Enable/disable AC Name entry

        Returns:
            self: This instance with all currently retrieved acName data using find and the newly added acName data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the acName data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AcName=None, ObjectId=None, Percentage=None, Select=None):
        """Finds and retrieves acName data from the server.

        All named parameters support regex and can be used to selectively retrieve acName data from the server.
        By default the find method takes no parameters and will retrieve all acName data from the server.

        Args:
            AcName (str): Access Concentrator Name
            ObjectId (str): Unique identifier for this object
            Percentage (number): Percentage of PPPoE sessions for this AC Name
            Select (bool): Enable/disable AC Name entry

        Returns:
            self: This instance with matching acName data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of acName data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the acName data from the server available through an iterator or index

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
