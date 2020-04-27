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


class DomainGroup(Base):
    """Domain Group
    The DomainGroup class encapsulates a list of domainGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the DomainGroup.find() method.
    The list can be managed by using the DomainGroup.add() and DomainGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'domainGroup'

    def __init__(self, parent):
        super(DomainGroup, self).__init__(parent)

    @property
    def AutoIncrement(self):
        """
        Returns
        -------
        - bool: If enabled, ID is incremented
        """
        return self._get_attribute('autoIncrement')
    @AutoIncrement.setter
    def AutoIncrement(self, value):
        self._set_attribute('autoIncrement', value)

    @property
    def BaseName(self):
        """
        Returns
        -------
        - str: Base name of the domain group
        """
        return self._get_attribute('baseName')
    @BaseName.setter
    def BaseName(self, value):
        self._set_attribute('baseName', value)

    @property
    def FullName(self):
        """
        Returns
        -------
        - str: Full name of the domain group
        """
        return self._get_attribute('fullName')
    @FullName.setter
    def FullName(self, value):
        self._set_attribute('fullName', value)

    @property
    def IncrementCount(self):
        """
        Returns
        -------
        - number: Number of iterations of numerical field
        """
        return self._get_attribute('incrementCount')
    @IncrementCount.setter
    def IncrementCount(self, value):
        self._set_attribute('incrementCount', value)

    @property
    def IncrementRepeat(self):
        """
        Returns
        -------
        - number: Number of times the ID is repeated before passing to the next value
        """
        return self._get_attribute('incrementRepeat')
    @IncrementRepeat.setter
    def IncrementRepeat(self, value):
        self._set_attribute('incrementRepeat', value)

    @property
    def IpAddresses(self):
        """
        Returns
        -------
        - list(str): List of ipAddresses
        """
        return self._get_attribute('ipAddresses')
    @IpAddresses.setter
    def IpAddresses(self, value):
        self._set_attribute('ipAddresses', value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

    @property
    def StartWidth(self):
        """
        Returns
        -------
        - str: Initial increment pattern including trailing characters e.g. 0001
        """
        return self._get_attribute('startWidth')
    @StartWidth.setter
    def StartWidth(self, value):
        self._set_attribute('startWidth', value)

    @property
    def TrailingName(self):
        """
        Returns
        -------
        - str: String appended after the numeric expression in the name
        """
        return self._get_attribute('trailingName')
    @TrailingName.setter
    def TrailingName(self, value):
        self._set_attribute('trailingName', value)

    def update(self, AutoIncrement=None, BaseName=None, FullName=None, IncrementCount=None, IncrementRepeat=None, IpAddresses=None, StartWidth=None, TrailingName=None):
        """Updates domainGroup resource on the server.

        Args
        ----
        - AutoIncrement (bool): If enabled, ID is incremented
        - BaseName (str): Base name of the domain group
        - FullName (str): Full name of the domain group
        - IncrementCount (number): Number of iterations of numerical field
        - IncrementRepeat (number): Number of times the ID is repeated before passing to the next value
        - IpAddresses (list(str)): List of ipAddresses
        - StartWidth (str): Initial increment pattern including trailing characters e.g. 0001
        - TrailingName (str): String appended after the numeric expression in the name

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, AutoIncrement=None, BaseName=None, FullName=None, IncrementCount=None, IncrementRepeat=None, IpAddresses=None, StartWidth=None, TrailingName=None):
        """Adds a new domainGroup resource on the server and adds it to the container.

        Args
        ----
        - AutoIncrement (bool): If enabled, ID is incremented
        - BaseName (str): Base name of the domain group
        - FullName (str): Full name of the domain group
        - IncrementCount (number): Number of iterations of numerical field
        - IncrementRepeat (number): Number of times the ID is repeated before passing to the next value
        - IpAddresses (list(str)): List of ipAddresses
        - StartWidth (str): Initial increment pattern including trailing characters e.g. 0001
        - TrailingName (str): String appended after the numeric expression in the name

        Returns
        -------
        - self: This instance with all currently retrieved domainGroup resources using find and the newly added domainGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained domainGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoIncrement=None, BaseName=None, FullName=None, IncrementCount=None, IncrementRepeat=None, IpAddresses=None, ObjectId=None, StartWidth=None, TrailingName=None):
        """Finds and retrieves domainGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve domainGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all domainGroup resources from the server.

        Args
        ----
        - AutoIncrement (bool): If enabled, ID is incremented
        - BaseName (str): Base name of the domain group
        - FullName (str): Full name of the domain group
        - IncrementCount (number): Number of iterations of numerical field
        - IncrementRepeat (number): Number of times the ID is repeated before passing to the next value
        - IpAddresses (list(str)): List of ipAddresses
        - ObjectId (str): Unique identifier for this object
        - StartWidth (str): Initial increment pattern including trailing characters e.g. 0001
        - TrailingName (str): String appended after the numeric expression in the name

        Returns
        -------
        - self: This instance with matching domainGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of domainGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the domainGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
