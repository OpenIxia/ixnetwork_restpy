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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class MulticastTrafficMapping(Base):
    """This helps to configure the traffic that is already specified with the traffic wizard.
    The MulticastTrafficMapping class encapsulates a list of multicastTrafficMapping resources that are managed by the system.
    A list of resources can be retrieved from the server using the MulticastTrafficMapping.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "multicastTrafficMapping"
    _SDM_ATT_MAP = {
        "Bidirectional": "bidirectional",
        "HasTimingPort": "hasTimingPort",
        "Mesh": "mesh",
        "Name": "name",
        "SelfDestined": "selfDestined",
        "TimingPortId": "timingPortId",
        "UsesLightMaps": "usesLightMaps",
    }
    _SDM_ENUM_MAP = {
        "mesh": [
            "custom",
            "fullMesh",
            "manyToMany",
            "manyToOne",
            "multicastManyToMany",
            "oneToMany",
            "oneToOne",
            "oneToOneWrapped",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(MulticastTrafficMapping, self).__init__(parent, list_op)

    @property
    def LightMap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lightmap_aa3cd3683ef7a0e7e854392bcd4eca1f.LightMap): An instance of the LightMap class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.lightmap_aa3cd3683ef7a0e7e854392bcd4eca1f import (
            LightMap,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LightMap", None) is not None:
                return self._properties.get("LightMap")
        return LightMap(self)

    @property
    def Map(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.map_1f5f79085c997a867a3a92b0b0a7889e.Map): An instance of the Map class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.quicktest.map_1f5f79085c997a867a3a92b0b0a7889e import (
            Map,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Map", None) is not None:
                return self._properties.get("Map")
        return Map(self)

    @property
    def Bidirectional(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it signifies the two way direction of the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP["Bidirectional"])

    @Bidirectional.setter
    def Bidirectional(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Bidirectional"], value)

    @property
    def HasTimingPort(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, it has timing port of the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP["HasTimingPort"])

    @HasTimingPort.setter
    def HasTimingPort(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HasTimingPort"], value)

    @property
    def Mesh(self):
        # type: () -> str
        """
        Returns
        -------
        - str(custom | fullMesh | manyToMany | manyToOne | multicastManyToMany | oneToMany | oneToOne | oneToOneWrapped): It signifies the mesh of the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mesh"])

    @Mesh.setter
    def Mesh(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mesh"], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the name of the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def SelfDestined(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelfDestined"])

    @SelfDestined.setter
    def SelfDestined(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelfDestined"], value)

    @property
    def TimingPortId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It signifies the timing port ID of the protocol
        """
        return self._get_attribute(self._SDM_ATT_MAP["TimingPortId"])

    @TimingPortId.setter
    def TimingPortId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TimingPortId"], value)

    @property
    def UsesLightMaps(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the usage of light maps
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsesLightMaps"])

    @UsesLightMaps.setter
    def UsesLightMaps(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsesLightMaps"], value)

    def update(
        self,
        Bidirectional=None,
        HasTimingPort=None,
        Mesh=None,
        Name=None,
        SelfDestined=None,
        TimingPortId=None,
        UsesLightMaps=None,
    ):
        # type: (bool, bool, str, str, bool, str, bool) -> MulticastTrafficMapping
        """Updates multicastTrafficMapping resource on the server.

        Args
        ----
        - Bidirectional (bool): If enabled, it signifies the two way direction of the protocol
        - HasTimingPort (bool): If enabled, it has timing port of the protocol
        - Mesh (str(custom | fullMesh | manyToMany | manyToOne | multicastManyToMany | oneToMany | oneToOne | oneToOneWrapped)): It signifies the mesh of the protocol
        - Name (str): It signifies the name of the protocol
        - SelfDestined (bool): NOT DEFINED
        - TimingPortId (str): It signifies the timing port ID of the protocol
        - UsesLightMaps (bool): Enables the usage of light maps

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        Bidirectional=None,
        HasTimingPort=None,
        Mesh=None,
        Name=None,
        SelfDestined=None,
        TimingPortId=None,
        UsesLightMaps=None,
    ):
        # type: (bool, bool, str, str, bool, str, bool) -> MulticastTrafficMapping
        """Adds a new multicastTrafficMapping resource on the json, only valid with batch add utility

        Args
        ----
        - Bidirectional (bool): If enabled, it signifies the two way direction of the protocol
        - HasTimingPort (bool): If enabled, it has timing port of the protocol
        - Mesh (str(custom | fullMesh | manyToMany | manyToOne | multicastManyToMany | oneToMany | oneToOne | oneToOneWrapped)): It signifies the mesh of the protocol
        - Name (str): It signifies the name of the protocol
        - SelfDestined (bool): NOT DEFINED
        - TimingPortId (str): It signifies the timing port ID of the protocol
        - UsesLightMaps (bool): Enables the usage of light maps

        Returns
        -------
        - self: This instance with all currently retrieved multicastTrafficMapping resources using find and the newly added multicastTrafficMapping resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Bidirectional=None,
        HasTimingPort=None,
        Mesh=None,
        Name=None,
        SelfDestined=None,
        TimingPortId=None,
        UsesLightMaps=None,
    ):
        # type: (bool, bool, str, str, bool, str, bool) -> MulticastTrafficMapping
        """Finds and retrieves multicastTrafficMapping resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastTrafficMapping resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastTrafficMapping resources from the server.

        Args
        ----
        - Bidirectional (bool): If enabled, it signifies the two way direction of the protocol
        - HasTimingPort (bool): If enabled, it has timing port of the protocol
        - Mesh (str(custom | fullMesh | manyToMany | manyToOne | multicastManyToMany | oneToMany | oneToOne | oneToOneWrapped)): It signifies the mesh of the protocol
        - Name (str): It signifies the name of the protocol
        - SelfDestined (bool): NOT DEFINED
        - TimingPortId (str): It signifies the timing port ID of the protocol
        - UsesLightMaps (bool): Enables the usage of light maps

        Returns
        -------
        - self: This instance with matching multicastTrafficMapping resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastTrafficMapping data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastTrafficMapping resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Apply(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the apply operation on the server.

        Applies the specified Quick Test.

        apply(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("apply", payload=payload, response_object=None)

    def ApplyAsync(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyAsync operation on the server.

        applyAsync(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsync", payload=payload, response_object=None)

    def ApplyAsyncResult(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the applyAsyncResult operation on the server.

        applyAsyncResult(async_operation=bool)bool
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("applyAsyncResult", payload=payload, response_object=None)

    def ApplyITWizardConfiguration(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the applyITWizardConfiguration operation on the server.

        Applies the specified Quick Test.

        applyITWizardConfiguration(async_operation=bool)
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "applyITWizardConfiguration", payload=payload, response_object=None
        )

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateReport operation on the server.

        Generate a PDF report for the last succesfull test run.

        generateReport(async_operation=bool)string
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: This method is asynchronous and has no return value.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("generateReport", payload=payload, response_object=None)

    def Run(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the run operation on the server.

        Starts the specified Quick Test and waits for its execution to finish.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        run(async_operation=bool)list
        -----------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        run(InputParameters=string, async_operation=bool)list
        -----------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("run", payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Starts the specified Quick Test.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(InputParameters=string, async_operation=bool)
        ---------------------------------------------------
        - InputParameters (str): The input arguments of the test.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("start", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stops the currently running Quick Test.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("stop", payload=payload, response_object=None)

    def WaitForTest(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the waitForTest operation on the server.

        Waits for the execution of the specified Quick Test to be completed.

        waitForTest(async_operation=bool)list
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): This method is synchronous and returns the result of the test.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("waitForTest", payload=payload, response_object=None)
