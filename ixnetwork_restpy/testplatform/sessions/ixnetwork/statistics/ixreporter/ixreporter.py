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


class Ixreporter(Base):
    """Specifies the statistics for IxReporter.
    The Ixreporter class encapsulates a required ixreporter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ixreporter'
    _SDM_ATT_MAP = {
    }

    def __init__(self, parent):
        super(Ixreporter, self).__init__(parent)

    @property
    def DataCollection(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.datacollection.datacollection.DataCollection): An instance of the DataCollection class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.datacollection.datacollection import DataCollection
        return DataCollection(self)._select()

    @property
    def ReportGeneration(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.reportgeneration.reportgeneration.ReportGeneration): An instance of the ReportGeneration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.statistics.ixreporter.reportgeneration.reportgeneration import ReportGeneration
        return ReportGeneration(self)._select()
