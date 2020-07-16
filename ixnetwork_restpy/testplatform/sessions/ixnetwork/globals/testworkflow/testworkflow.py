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


class Testworkflow(Base):
    """
    The Testworkflow class encapsulates a required testworkflow resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'testworkflow'
    _SDM_ATT_MAP = {
        'CurrentDescription': 'currentDescription',
        'CurrentState': 'currentState',
    }

    def __init__(self, parent):
        super(Testworkflow, self).__init__(parent)

    @property
    def CurrentDescription(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentDescription'])

    @property
    def CurrentState(self):
        """
        Returns
        -------
        - str(kApplyTraffic | kConnectPorts | kError | kGenerateTraffic | kIdle | kReleaseCrashedPorts | kStartLAG | kStartProtocols | kStartTopology | kStartTraffic | kStopLAG | kStopProtocols | kStopTraffic | kWaitForChassisUp | kWaitForLicenseBroadcast | kWaitForPortsUp | kWaitForProtocolsUp): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentState'])

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        connect ports, start protocols and generate/apply/start traffic

        start(Arg2=bool)
        ----------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Startlag(self, *args, **kwargs):
        """Executes the startlag operation on the server.

        connect ports and start LAG

        startlag(Arg2=bool)
        -------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startlag', payload=payload, response_object=None)

    def Startprotocols(self, *args, **kwargs):
        """Executes the startprotocols operation on the server.

        connect ports and start protocols

        startprotocols(Arg2=bool)
        -------------------------
        - Arg2 (bool): a boolean indicating if ownership should be taken forcefully

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startprotocols', payload=payload, response_object=None)

    def Startselected(self, *args, **kwargs):
        """Executes the startselected operation on the server.

        connect ports and start the selected item

        startselected(Arg2=href, Arg3=bool)
        -----------------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork/topology | /api/v1/sessions/1/ixnetwork/topology | /api/v1/sessions/1/ixnetwork/topology/.../deviceGroup)): objref to /topology or device group
        - Arg3 (bool): a boolean indicating if ownership should be taken forcefully

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startselected', payload=payload, response_object=None)

    def Starttraffic(self):
        """Executes the starttraffic operation on the server.

        generates (if required), applies and starts traffic

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('starttraffic', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        stop protocols and traffic

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def Stoplag(self):
        """Executes the stoplag operation on the server.

        stop LAG

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stoplag', payload=payload, response_object=None)

    def Stopprotocols(self):
        """Executes the stopprotocols operation on the server.

        stop protocols

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stopprotocols', payload=payload, response_object=None)

    def Stoptraffic(self):
        """Executes the stoptraffic operation on the server.

        stop protocols and traffic

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stoptraffic', payload=payload, response_object=None)
