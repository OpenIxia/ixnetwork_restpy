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


class FcVnportRight(Base):
    """This object configures the options for FC Target topology.
    The FcVnportRight class encapsulates a list of fcVnportRight resources that are managed by the system.
    A list of resources can be retrieved from the server using the FcVnportRight.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "fcVnportRight"
    _SDM_ATT_MAP = {
        "EnodeCount": "enodeCount",
        "EnodeNodeWwnIncrement": "enodeNodeWwnIncrement",
        "EnodeNodeWwnStart": "enodeNodeWwnStart",
        "EnodeSourceOuiIncrement": "enodeSourceOuiIncrement",
        "EnodeSourceOuiStart": "enodeSourceOuiStart",
        "FdiscCount": "fdiscCount",
        "FdiscPortWwnIncrement": "fdiscPortWwnIncrement",
        "FdiscPortWwnStart": "fdiscPortWwnStart",
        "FlogiCount": "flogiCount",
        "FlogiPortWwnIncrement": "flogiPortWwnIncrement",
        "FlogiPortWwnStart": "flogiPortWwnStart",
        "SameAsLeftSide": "sameAsLeftSide",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(FcVnportRight, self).__init__(parent, list_op)

    @property
    def EnodeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of emulated ENodes to create on the selected Ixia port. IxNetwork creates a range for each ENode. The maximum value is 32.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnodeCount"])

    @EnodeCount.setter
    def EnodeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnodeCount"], value)

    @property
    def EnodeNodeWwnIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which the Node WWN is incremented for each new emulated ENode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnodeNodeWwnIncrement"])

    @EnodeNodeWwnIncrement.setter
    def EnodeNodeWwnIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnodeNodeWwnIncrement"], value)

    @property
    def EnodeNodeWwnStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Node WWN (World Wide Name) for the first emulated ENode in the range. A Node WWN is a burned-in eight-byte identifier that is shared by all ports on an HBA.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnodeNodeWwnStart"])

    @EnodeNodeWwnStart.setter
    def EnodeNodeWwnStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnodeNodeWwnStart"], value)

    @property
    def EnodeSourceOuiIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which the Source OUI is incremented for each generated range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnodeSourceOuiIncrement"])

    @EnodeSourceOuiIncrement.setter
    def EnodeSourceOuiIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnodeSourceOuiIncrement"], value)

    @property
    def EnodeSourceOuiStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The three-byte Organizationally Unique Identifier (OUI) associated with all emulated ENodes in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnodeSourceOuiStart"])

    @EnodeSourceOuiStart.setter
    def EnodeSourceOuiStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnodeSourceOuiStart"], value)

    @property
    def FdiscCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of fdiscs to create on the selected Ixia port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FdiscCount"])

    @FdiscCount.setter
    def FdiscCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FdiscCount"], value)

    @property
    def FdiscPortWwnIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which the fdisc WWN is incremented for each new emulated ENode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FdiscPortWwnIncrement"])

    @FdiscPortWwnIncrement.setter
    def FdiscPortWwnIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FdiscPortWwnIncrement"], value)

    @property
    def FdiscPortWwnStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The fdisc WWN (World Wide Name) for the first emulated ENode in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FdiscPortWwnStart"])

    @FdiscPortWwnStart.setter
    def FdiscPortWwnStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FdiscPortWwnStart"], value)

    @property
    def FlogiCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The number of FLOGI ports.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogiCount"])

    @FlogiCount.setter
    def FlogiCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogiCount"], value)

    @property
    def FlogiPortWwnIncrement(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The value by which the Port WWN is incremented for each new emulated FDISC VN_Port configured on the FLOGI VN_Port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogiPortWwnIncrement"])

    @FlogiPortWwnIncrement.setter
    def FlogiPortWwnIncrement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogiPortWwnIncrement"], value)

    @property
    def FlogiPortWwnStart(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The Port WWN (World Wide Name) for the first emulated ENode in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlogiPortWwnStart"])

    @FlogiPortWwnStart.setter
    def FlogiPortWwnStart(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlogiPortWwnStart"], value)

    @property
    def SameAsLeftSide(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: When selected, the target-side topology is a duplicate of the initiator-side topology, with the exception of the Node and Port WWN values (as these must be unique).
        """
        return self._get_attribute(self._SDM_ATT_MAP["SameAsLeftSide"])

    @SameAsLeftSide.setter
    def SameAsLeftSide(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["SameAsLeftSide"], value)

    def update(
        self,
        EnodeCount=None,
        EnodeNodeWwnIncrement=None,
        EnodeNodeWwnStart=None,
        EnodeSourceOuiIncrement=None,
        EnodeSourceOuiStart=None,
        FdiscCount=None,
        FdiscPortWwnIncrement=None,
        FdiscPortWwnStart=None,
        FlogiCount=None,
        FlogiPortWwnIncrement=None,
        FlogiPortWwnStart=None,
        SameAsLeftSide=None,
    ):
        # type: (int, str, str, str, str, int, str, str, int, str, str, bool) -> FcVnportRight
        """Updates fcVnportRight resource on the server.

        Args
        ----
        - EnodeCount (number): The number of emulated ENodes to create on the selected Ixia port. IxNetwork creates a range for each ENode. The maximum value is 32.
        - EnodeNodeWwnIncrement (str): The value by which the Node WWN is incremented for each new emulated ENode.
        - EnodeNodeWwnStart (str): The Node WWN (World Wide Name) for the first emulated ENode in the range. A Node WWN is a burned-in eight-byte identifier that is shared by all ports on an HBA.
        - EnodeSourceOuiIncrement (str): The value by which the Source OUI is incremented for each generated range.
        - EnodeSourceOuiStart (str): The three-byte Organizationally Unique Identifier (OUI) associated with all emulated ENodes in the range.
        - FdiscCount (number): The number of fdiscs to create on the selected Ixia port.
        - FdiscPortWwnIncrement (str): The value by which the fdisc WWN is incremented for each new emulated ENode.
        - FdiscPortWwnStart (str): The fdisc WWN (World Wide Name) for the first emulated ENode in the range.
        - FlogiCount (number): The number of FLOGI ports.
        - FlogiPortWwnIncrement (str): The value by which the Port WWN is incremented for each new emulated FDISC VN_Port configured on the FLOGI VN_Port.
        - FlogiPortWwnStart (str): The Port WWN (World Wide Name) for the first emulated ENode in the range.
        - SameAsLeftSide (bool): When selected, the target-side topology is a duplicate of the initiator-side topology, with the exception of the Node and Port WWN values (as these must be unique).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        EnodeCount=None,
        EnodeNodeWwnIncrement=None,
        EnodeNodeWwnStart=None,
        EnodeSourceOuiIncrement=None,
        EnodeSourceOuiStart=None,
        FdiscCount=None,
        FdiscPortWwnIncrement=None,
        FdiscPortWwnStart=None,
        FlogiCount=None,
        FlogiPortWwnIncrement=None,
        FlogiPortWwnStart=None,
        SameAsLeftSide=None,
    ):
        # type: (int, str, str, str, str, int, str, str, int, str, str, bool) -> FcVnportRight
        """Adds a new fcVnportRight resource on the json, only valid with batch add utility

        Args
        ----
        - EnodeCount (number): The number of emulated ENodes to create on the selected Ixia port. IxNetwork creates a range for each ENode. The maximum value is 32.
        - EnodeNodeWwnIncrement (str): The value by which the Node WWN is incremented for each new emulated ENode.
        - EnodeNodeWwnStart (str): The Node WWN (World Wide Name) for the first emulated ENode in the range. A Node WWN is a burned-in eight-byte identifier that is shared by all ports on an HBA.
        - EnodeSourceOuiIncrement (str): The value by which the Source OUI is incremented for each generated range.
        - EnodeSourceOuiStart (str): The three-byte Organizationally Unique Identifier (OUI) associated with all emulated ENodes in the range.
        - FdiscCount (number): The number of fdiscs to create on the selected Ixia port.
        - FdiscPortWwnIncrement (str): The value by which the fdisc WWN is incremented for each new emulated ENode.
        - FdiscPortWwnStart (str): The fdisc WWN (World Wide Name) for the first emulated ENode in the range.
        - FlogiCount (number): The number of FLOGI ports.
        - FlogiPortWwnIncrement (str): The value by which the Port WWN is incremented for each new emulated FDISC VN_Port configured on the FLOGI VN_Port.
        - FlogiPortWwnStart (str): The Port WWN (World Wide Name) for the first emulated ENode in the range.
        - SameAsLeftSide (bool): When selected, the target-side topology is a duplicate of the initiator-side topology, with the exception of the Node and Port WWN values (as these must be unique).

        Returns
        -------
        - self: This instance with all currently retrieved fcVnportRight resources using find and the newly added fcVnportRight resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        EnodeCount=None,
        EnodeNodeWwnIncrement=None,
        EnodeNodeWwnStart=None,
        EnodeSourceOuiIncrement=None,
        EnodeSourceOuiStart=None,
        FdiscCount=None,
        FdiscPortWwnIncrement=None,
        FdiscPortWwnStart=None,
        FlogiCount=None,
        FlogiPortWwnIncrement=None,
        FlogiPortWwnStart=None,
        SameAsLeftSide=None,
    ):
        # type: (int, str, str, str, str, int, str, str, int, str, str, bool) -> FcVnportRight
        """Finds and retrieves fcVnportRight resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fcVnportRight resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fcVnportRight resources from the server.

        Args
        ----
        - EnodeCount (number): The number of emulated ENodes to create on the selected Ixia port. IxNetwork creates a range for each ENode. The maximum value is 32.
        - EnodeNodeWwnIncrement (str): The value by which the Node WWN is incremented for each new emulated ENode.
        - EnodeNodeWwnStart (str): The Node WWN (World Wide Name) for the first emulated ENode in the range. A Node WWN is a burned-in eight-byte identifier that is shared by all ports on an HBA.
        - EnodeSourceOuiIncrement (str): The value by which the Source OUI is incremented for each generated range.
        - EnodeSourceOuiStart (str): The three-byte Organizationally Unique Identifier (OUI) associated with all emulated ENodes in the range.
        - FdiscCount (number): The number of fdiscs to create on the selected Ixia port.
        - FdiscPortWwnIncrement (str): The value by which the fdisc WWN is incremented for each new emulated ENode.
        - FdiscPortWwnStart (str): The fdisc WWN (World Wide Name) for the first emulated ENode in the range.
        - FlogiCount (number): The number of FLOGI ports.
        - FlogiPortWwnIncrement (str): The value by which the Port WWN is incremented for each new emulated FDISC VN_Port configured on the FLOGI VN_Port.
        - FlogiPortWwnStart (str): The Port WWN (World Wide Name) for the first emulated ENode in the range.
        - SameAsLeftSide (bool): When selected, the target-side topology is a duplicate of the initiator-side topology, with the exception of the Node and Port WWN values (as these must be unique).

        Returns
        -------
        - self: This instance with matching fcVnportRight resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fcVnportRight data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fcVnportRight resources from the server available through an iterator or index

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
