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


class SaveResults(Base):
    """This object specifies the properties of the results. There are two execs - saveSummaryResults
and saveDetailedResults. The execs are used to save the summary and detailed results respectively.
    The SaveResults class encapsulates a required saveResults resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'saveResults'
    _SDM_ATT_MAP = {
        'EnableAllResults': 'enableAllResults',
        'State': 'state',
    }

    def __init__(self, parent):
        super(SaveResults, self).__init__(parent)

    @property
    def EnableAllResults(self):
        """
        Returns
        -------
        - bool: If true, all the results are enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAllResults'])
    @EnableAllResults.setter
    def EnableAllResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAllResults'], value)

    @property
    def State(self):
        """
        Returns
        -------
        - str(done | failed | inProgress | none): The state of the results.
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    def update(self, EnableAllResults=None):
        """Updates saveResults resource on the server.

        Args
        ----
        - EnableAllResults (bool): If true, all the results are enabled.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def SaveDetailedResults(self):
        """Executes the saveDetailedResults operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('saveDetailedResults', payload=payload, response_object=None)

    def SaveFile(self, *args, **kwargs):
        """Executes the saveFile operation on the server.

        NOT DEFINED

        saveFile(Arg2=enum, Arg3=string)
        --------------------------------
        - Arg2 (str(csv | generic)): NOT DEFINED
        - Arg3 (str): NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('saveFile', payload=payload, response_object=None)

    def SaveSummaryResults(self):
        """Executes the saveSummaryResults operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('saveSummaryResults', payload=payload, response_object=None)