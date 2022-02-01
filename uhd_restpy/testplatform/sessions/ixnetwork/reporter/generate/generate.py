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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Generate(Base):
    """This object specifies the properties of the generated report.
    The Generate class encapsulates a required generate resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'generate'
    _SDM_ATT_MAP = {
        'OutputFormat': 'outputFormat',
        'OutputPath': 'outputPath',
        'State': 'state',
        'TemplatePath': 'templatePath',
    }
    _SDM_ENUM_MAP = {
        'outputFormat': ['html', 'pdf'],
        'state': ['done', 'failed', 'inProgress', 'none'],
    }

    def __init__(self, parent, list_op=False):
        super(Generate, self).__init__(parent, list_op)

    @property
    def OutputFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(html | pdf): The format of the generated report, either PDF or HTML.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputFormat'])
    @OutputFormat.setter
    def OutputFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['OutputFormat'], value)

    @property
    def OutputPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The location where the generated report is saved.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutputPath'])
    @OutputPath.setter
    def OutputPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['OutputPath'], value)

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str(done | failed | inProgress | none): The state of the generated report.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    @property
    def TemplatePath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The location of the template used to generate a report.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TemplatePath'])
    @TemplatePath.setter
    def TemplatePath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['TemplatePath'], value)

    def update(self, OutputFormat=None, OutputPath=None, TemplatePath=None):
        # type: (str, str, str) -> Generate
        """Updates generate resource on the server.

        Args
        ----
        - OutputFormat (str(html | pdf)): The format of the generated report, either PDF or HTML.
        - OutputPath (str): The location where the generated report is saved.
        - TemplatePath (str): The location of the template used to generate a report.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, OutputFormat=None, OutputPath=None, State=None, TemplatePath=None):
        # type: (str, str, str, str) -> Generate
        """Finds and retrieves generate resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve generate resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all generate resources from the server.

        Args
        ----
        - OutputFormat (str(html | pdf)): The format of the generated report, either PDF or HTML.
        - OutputPath (str): The location where the generated report is saved.
        - State (str(done | failed | inProgress | none)): The state of the generated report.
        - TemplatePath (str): The location of the template used to generate a report.

        Returns
        -------
        - self: This instance with matching generate resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of generate data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the generate resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GenerateReport(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the generateReport operation on the server.

        NOT DEFINED

        generateReport(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('generateReport', payload=payload, response_object=None)
