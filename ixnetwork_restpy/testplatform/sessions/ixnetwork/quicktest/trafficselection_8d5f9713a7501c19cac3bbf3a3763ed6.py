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


class TrafficSelection(Base):
    """This object configures the traffic that is already specified with the traffic wizard
    The TrafficSelection class encapsulates a list of trafficSelection resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrafficSelection.find() method.
    The list can be managed by using the TrafficSelection.add() and TrafficSelection.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trafficSelection'
    _SDM_ATT_MAP = {
        'Id__': '__id__',
        'IncludeMode': 'includeMode',
        'IsGenerated': 'isGenerated',
        'ItemType': 'itemType',
        'Role': 'role',
        'TrafficItemType': 'trafficItemType',
    }

    def __init__(self, parent):
        super(TrafficSelection, self).__init__(parent)

    @property
    def Id__(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem | /api/v1/sessions/1/ixnetwork/traffic/.../highLevelStream): The unique identification of the traffic selection
        """
        return self._get_attribute(self._SDM_ATT_MAP['Id__'])
    @Id__.setter
    def Id__(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Id__'], value)

    @property
    def IncludeMode(self):
        """
        Returns
        -------
        - str(background | inTest): Traffic type for the frame data
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeMode'])
    @IncludeMode.setter
    def IncludeMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeMode'], value)

    @property
    def IsGenerated(self):
        """
        Returns
        -------
        - bool: If true, the traffic selection is generated automatically
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsGenerated'])
    @IsGenerated.setter
    def IsGenerated(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsGenerated'], value)

    @property
    def ItemType(self):
        """
        Returns
        -------
        - str(flowGroup | trafficItem): Traffic type for the frame data
        """
        return self._get_attribute(self._SDM_ATT_MAP['ItemType'])
    @ItemType.setter
    def ItemType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ItemType'], value)

    @property
    def Role(self):
        """
        Returns
        -------
        - str(burden | multicast): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Role'])
    @Role.setter
    def Role(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Role'], value)

    @property
    def TrafficItemType(self):
        """
        Returns
        -------
        - str(monitor | normal | quick | timing): This signifies the Traffic Item Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficItemType'])
    @TrafficItemType.setter
    def TrafficItemType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficItemType'], value)

    def update(self, Id__=None, IncludeMode=None, IsGenerated=None, ItemType=None, Role=None, TrafficItemType=None):
        """Updates trafficSelection resource on the server.

        Args
        ----
        - Id__ (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem | /api/v1/sessions/1/ixnetwork/traffic/.../highLevelStream)): The unique identification of the traffic selection
        - IncludeMode (str(background | inTest)): Traffic type for the frame data
        - IsGenerated (bool): If true, the traffic selection is generated automatically
        - ItemType (str(flowGroup | trafficItem)): Traffic type for the frame data
        - Role (str(burden | multicast)): NOT DEFINED
        - TrafficItemType (str(monitor | normal | quick | timing)): This signifies the Traffic Item Type.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Id__=None, IncludeMode=None, IsGenerated=None, ItemType=None, Role=None, TrafficItemType=None):
        """Adds a new trafficSelection resource on the server and adds it to the container.

        Args
        ----
        - Id__ (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem | /api/v1/sessions/1/ixnetwork/traffic/.../highLevelStream)): The unique identification of the traffic selection
        - IncludeMode (str(background | inTest)): Traffic type for the frame data
        - IsGenerated (bool): If true, the traffic selection is generated automatically
        - ItemType (str(flowGroup | trafficItem)): Traffic type for the frame data
        - Role (str(burden | multicast)): NOT DEFINED
        - TrafficItemType (str(monitor | normal | quick | timing)): This signifies the Traffic Item Type.

        Returns
        -------
        - self: This instance with all currently retrieved trafficSelection resources using find and the newly added trafficSelection resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trafficSelection resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Id__=None, IncludeMode=None, IsGenerated=None, ItemType=None, Role=None, TrafficItemType=None):
        """Finds and retrieves trafficSelection resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trafficSelection resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trafficSelection resources from the server.

        Args
        ----
        - Id__ (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficItem | /api/v1/sessions/1/ixnetwork/traffic/.../highLevelStream)): The unique identification of the traffic selection
        - IncludeMode (str(background | inTest)): Traffic type for the frame data
        - IsGenerated (bool): If true, the traffic selection is generated automatically
        - ItemType (str(flowGroup | trafficItem)): Traffic type for the frame data
        - Role (str(burden | multicast)): NOT DEFINED
        - TrafficItemType (str(monitor | normal | quick | timing)): This signifies the Traffic Item Type.

        Returns
        -------
        - self: This instance with matching trafficSelection resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trafficSelection data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trafficSelection resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self):
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('apply', payload=payload, response_object=None)

    def ApplyAsync(self):
        """Executes the applyAsync operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsync', payload=payload, response_object=None)

    def ApplyAsyncResult(self):
        """Executes the applyAsyncResult operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyAsyncResult', payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self):
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('applyITWizardConfiguration', payload=payload, response_object=None)

    def GenerateReport(self):
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('generateReport', payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(InputParameters=string)list
        -------------------------------
        - InputParameters (str): The input arguments of the test.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('run', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(InputParameters=string)
        -----------------------------
        - InputParameters (str): The input arguments of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('stop', payload=payload, response_object=None)

    def WaitForTest(self):
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('waitForTest', payload=payload, response_object=None)
