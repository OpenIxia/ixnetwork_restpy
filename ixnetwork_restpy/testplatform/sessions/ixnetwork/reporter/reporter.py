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


class Reporter(Base):
    """IxReporter helps to customize a test result report using different
options, commands and wizards.
    The Reporter class encapsulates a required reporter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'reporter'
    _SDM_ATT_MAP = {
        'State': 'state',
    }
    _SDM_ENUM_MAP = {
        'state': ['none', 'started', 'stopped'],
    }

    def __init__(self, parent, list_op=False):
        super(Reporter, self).__init__(parent, list_op)

    @property
    def Generate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.generate.generate.Generate): An instance of the Generate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.generate.generate import Generate
        if self._properties.get('Generate', None) is not None:
            return self._properties.get('Generate')
        else:
            return Generate(self)._select()

    @property
    def SaveResults(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.saveresults.saveresults.SaveResults): An instance of the SaveResults class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.saveresults.saveresults import SaveResults
        if self._properties.get('SaveResults', None) is not None:
            return self._properties.get('SaveResults')
        else:
            return SaveResults(self)._select()

    @property
    def TestParameters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.testparameters.testparameters.TestParameters): An instance of the TestParameters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.reporter.testparameters.testparameters import TestParameters
        if self._properties.get('TestParameters', None) is not None:
            return self._properties.get('TestParameters')
        else:
            return TestParameters(self)._select()

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | started | stopped): The state of the generated report.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])
