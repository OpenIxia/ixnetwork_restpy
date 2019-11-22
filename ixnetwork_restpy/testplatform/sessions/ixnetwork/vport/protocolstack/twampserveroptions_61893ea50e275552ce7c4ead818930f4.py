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


class TwampServerOptions(Base):
    """Portgroup options for the Twamp Server extension plug-in.
    The TwampServerOptions class encapsulates a list of twampServerOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the TwampServerOptions.find() method.
    The list can be managed by the user by using the TwampServerOptions.add() and TwampServerOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'twampServerOptions'

    def __init__(self, parent):
        super(TwampServerOptions, self).__init__(parent)

    @property
    def ErrorEstimateMultiplier(self):
        """Twamp error estimate scale multiplier - used for the Error estimation computation

        Returns:
            number
        """
        return self._get_attribute('errorEstimateMultiplier')
    @ErrorEstimateMultiplier.setter
    def ErrorEstimateMultiplier(self, value):
        self._set_attribute('errorEstimateMultiplier', value)

    @property
    def ErrorEstimateScale(self):
        """Twamp error estimate scale factor - used for the Error estimation computation

        Returns:
            number
        """
        return self._get_attribute('errorEstimateScale')
    @ErrorEstimateScale.setter
    def ErrorEstimateScale(self, value):
        self._set_attribute('errorEstimateScale', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, ErrorEstimateMultiplier=None, ErrorEstimateScale=None):
        """Updates a child instance of twampServerOptions on the server.

        Args:
            ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
            ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ErrorEstimateMultiplier=None, ErrorEstimateScale=None):
        """Adds a new twampServerOptions node on the server and retrieves it in this instance.

        Args:
            ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
            ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation

        Returns:
            self: This instance with all currently retrieved twampServerOptions data using find and the newly added twampServerOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the twampServerOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ErrorEstimateMultiplier=None, ErrorEstimateScale=None, ObjectId=None):
        """Finds and retrieves twampServerOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve twampServerOptions data from the server.
        By default the find method takes no parameters and will retrieve all twampServerOptions data from the server.

        Args:
            ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
            ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching twampServerOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of twampServerOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the twampServerOptions data from the server available through an iterator or index

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
