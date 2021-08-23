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
from typing import List, Any, Union


class ReportGeneration(Base):
    """DEPRECATED Generates report for IxReporter.
    The ReportGeneration class encapsulates a required reportGeneration resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'reportGeneration'
    _SDM_ATT_MAP = {
        'OutputFile': 'OutputFile',
        'OutputType': 'OutputType',
        'Template': 'Template',
        'TestRunId': 'TestRunId',
    }
    _SDM_ENUM_MAP = {
        'OutputType': ['Html', 'Pdf'],
    }

    def __init__(self, parent, list_op=False):
        super(ReportGeneration, self).__init__(parent, list_op)

    @property
    def OutputFile(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the output file
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputFile'])
    @OutputFile.setter
    def OutputFile(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['OutputFile'], value)

    @property
    def OutputType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(Html | Pdf): Signifies the output type
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputType'])
    @OutputType.setter
    def OutputType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['OutputType'], value)

    @property
    def Template(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Signifies the template for IxReporter
        """
        return self._get_attribute(self._SDM_ATT_MAP['Template'])
    @Template.setter
    def Template(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Template'], value)

    @property
    def TestRunId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Signifies the identifier for the test run
        """
        return self._get_attribute(self._SDM_ATT_MAP['TestRunId'])
    @TestRunId.setter
    def TestRunId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['TestRunId'], value)

    def update(self, OutputFile=None, OutputType=None, Template=None, TestRunId=None):
        # type: (str, str, str, int) -> ReportGeneration
        """Updates reportGeneration resource on the server.

        Args
        ----
        - OutputFile (str): Signifies the output file
        - OutputType (str(Html | Pdf)): Signifies the output type
        - Template (str): Signifies the template for IxReporter
        - TestRunId (number): Signifies the identifier for the test run

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        NOT DEFINED

        DEPRECATED start(async_operation=bool)
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)
