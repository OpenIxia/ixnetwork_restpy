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


class TestParameters(Base):
    """This node specifies the test parameters.
    The TestParameters class encapsulates a required testParameters resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "testParameters"
    _SDM_ATT_MAP = {
        "TestCategory": "testCategory",
        "TestDUTName": "testDUTName",
        "TestHighlights": "testHighlights",
        "TestId": "testId",
        "TestName": "testName",
        "TestObjectives": "testObjectives",
        "TesterName": "testerName",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TestParameters, self).__init__(parent, list_op)

    @property
    def TestCategory(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The category of the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestCategory"])

    @TestCategory.setter
    def TestCategory(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestCategory"], value)

    @property
    def TestDUTName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestDUTName"])

    @TestDUTName.setter
    def TestDUTName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestDUTName"], value)

    @property
    def TestHighlights(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The test highlights that are relevant.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestHighlights"])

    @TestHighlights.setter
    def TestHighlights(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestHighlights"], value)

    @property
    def TestId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The unique identifier of the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestId"])

    @property
    def TestName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the test for which the report is generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestName"])

    @TestName.setter
    def TestName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestName"], value)

    @property
    def TestObjectives(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The objective of running the test.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestObjectives"])

    @TestObjectives.setter
    def TestObjectives(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestObjectives"], value)

    @property
    def TesterName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The name of the tester.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TesterName"])

    @TesterName.setter
    def TesterName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TesterName"], value)

    def update(
        self,
        TestCategory=None,
        TestDUTName=None,
        TestHighlights=None,
        TestName=None,
        TestObjectives=None,
        TesterName=None,
    ):
        # type: (str, str, str, str, str, str) -> TestParameters
        """Updates testParameters resource on the server.

        Args
        ----
        - TestCategory (str): The category of the test.
        - TestDUTName (str): The name of the DUT.
        - TestHighlights (str): The test highlights that are relevant.
        - TestName (str): The name of the test for which the report is generated.
        - TestObjectives (str): The objective of running the test.
        - TesterName (str): The name of the tester.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        TestCategory=None,
        TestDUTName=None,
        TestHighlights=None,
        TestId=None,
        TestName=None,
        TestObjectives=None,
        TesterName=None,
    ):
        # type: (str, str, str, int, str, str, str) -> TestParameters
        """Finds and retrieves testParameters resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve testParameters resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all testParameters resources from the server.

        Args
        ----
        - TestCategory (str): The category of the test.
        - TestDUTName (str): The name of the DUT.
        - TestHighlights (str): The test highlights that are relevant.
        - TestId (number): The unique identifier of the test.
        - TestName (str): The name of the test for which the report is generated.
        - TestObjectives (str): The objective of running the test.
        - TesterName (str): The name of the tester.

        Returns
        -------
        - self: This instance with matching testParameters resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of testParameters data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the testParameters resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
