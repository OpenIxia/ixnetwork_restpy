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


class TwampOptions(Base):
    """Portgroup options for the Twamp extension plug-in.
    The TwampOptions class encapsulates a list of twampOptions resources that is be managed by the user.
    A list of resources can be retrieved from the server using the TwampOptions.find() method.
    The list can be managed by the user by using the TwampOptions.add() and TwampOptions.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'twampOptions'

    def __init__(self, parent):
        super(TwampOptions, self).__init__(parent)

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
    def MaxOutstanding(self):
        """The number of Twamp-control connections to be in initiation or terminating state at any time.

        Returns:
            number
        """
        return self._get_attribute('maxOutstanding')
    @MaxOutstanding.setter
    def MaxOutstanding(self, value):
        self._set_attribute('maxOutstanding', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def OverrideGlobalRateOptions(self):
        """If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.

        Returns:
            bool
        """
        return self._get_attribute('overrideGlobalRateOptions')
    @OverrideGlobalRateOptions.setter
    def OverrideGlobalRateOptions(self, value):
        self._set_attribute('overrideGlobalRateOptions', value)

    @property
    def SessionTimeout(self):
        """Maximum duration for establishment of a control-session, test-session, and the start-sessions command

        Returns:
            number
        """
        return self._get_attribute('sessionTimeout')
    @SessionTimeout.setter
    def SessionTimeout(self, value):
        self._set_attribute('sessionTimeout', value)

    @property
    def SetupRate(self):
        """The number of Twamp-Control connections initiated in a second.

        Returns:
            number
        """
        return self._get_attribute('setupRate')
    @SetupRate.setter
    def SetupRate(self, value):
        self._set_attribute('setupRate', value)

    @property
    def TeardownRate(self):
        """The number of Twamp-Control connections torn down in a second.

        Returns:
            number
        """
        return self._get_attribute('teardownRate')
    @TeardownRate.setter
    def TeardownRate(self, value):
        self._set_attribute('teardownRate', value)

    def update(self, ErrorEstimateMultiplier=None, ErrorEstimateScale=None, MaxOutstanding=None, OverrideGlobalRateOptions=None, SessionTimeout=None, SetupRate=None, TeardownRate=None):
        """Updates a child instance of twampOptions on the server.

        Args:
            ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
            ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
            MaxOutstanding (number): The number of Twamp-control connections to be in initiation or terminating state at any time.
            OverrideGlobalRateOptions (bool): If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
            SessionTimeout (number): Maximum duration for establishment of a control-session, test-session, and the start-sessions command
            SetupRate (number): The number of Twamp-Control connections initiated in a second.
            TeardownRate (number): The number of Twamp-Control connections torn down in a second.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ErrorEstimateMultiplier=None, ErrorEstimateScale=None, MaxOutstanding=None, OverrideGlobalRateOptions=None, SessionTimeout=None, SetupRate=None, TeardownRate=None):
        """Adds a new twampOptions node on the server and retrieves it in this instance.

        Args:
            ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
            ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
            MaxOutstanding (number): The number of Twamp-control connections to be in initiation or terminating state at any time.
            OverrideGlobalRateOptions (bool): If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
            SessionTimeout (number): Maximum duration for establishment of a control-session, test-session, and the start-sessions command
            SetupRate (number): The number of Twamp-Control connections initiated in a second.
            TeardownRate (number): The number of Twamp-Control connections torn down in a second.

        Returns:
            self: This instance with all currently retrieved twampOptions data using find and the newly added twampOptions data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the twampOptions data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ErrorEstimateMultiplier=None, ErrorEstimateScale=None, MaxOutstanding=None, ObjectId=None, OverrideGlobalRateOptions=None, SessionTimeout=None, SetupRate=None, TeardownRate=None):
        """Finds and retrieves twampOptions data from the server.

        All named parameters support regex and can be used to selectively retrieve twampOptions data from the server.
        By default the find method takes no parameters and will retrieve all twampOptions data from the server.

        Args:
            ErrorEstimateMultiplier (number): Twamp error estimate scale multiplier - used for the Error estimation computation
            ErrorEstimateScale (number): Twamp error estimate scale factor - used for the Error estimation computation
            MaxOutstanding (number): The number of Twamp-control connections to be in initiation or terminating state at any time.
            ObjectId (str): Unique identifier for this object
            OverrideGlobalRateOptions (bool): If true then all the rate settings defined at Session level will be overriden byrate settings defined on this PortGroup.
            SessionTimeout (number): Maximum duration for establishment of a control-session, test-session, and the start-sessions command
            SetupRate (number): The number of Twamp-Control connections initiated in a second.
            TeardownRate (number): The number of Twamp-Control connections torn down in a second.

        Returns:
            self: This instance with matching twampOptions data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of twampOptions data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the twampOptions data from the server available through an iterator or index

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
