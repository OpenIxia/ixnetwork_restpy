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


class CsvSnapshot(Base):
    """NOT DEFINED
    The CsvSnapshot class encapsulates a required csvSnapshot resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'csvSnapshot'
    _SDM_ATT_MAP = {
        'CsvDecimalPrecision': 'csvDecimalPrecision',
        'CsvDumpTxPortLabelMap': 'csvDumpTxPortLabelMap',
        'CsvFormatTimestamp': 'csvFormatTimestamp',
        'CsvLocation': 'csvLocation',
        'CsvName': 'csvName',
        'CsvStringQuotes': 'csvStringQuotes',
        'CsvSupportsCSVSorting': 'csvSupportsCSVSorting',
        'NextGenRefreshBeforeSnapshot': 'nextGenRefreshBeforeSnapshot',
        'OpenViewer': 'openViewer',
        'SnapshotSettingsName': 'snapshotSettingsName',
        'SnapshotViewContents': 'snapshotViewContents',
        'SnapshotViewCsvGenerationMode': 'snapshotViewCsvGenerationMode',
        'Views': 'views',
    }
    _SDM_ENUM_MAP = {
        'snapshotViewContents': ['allPages', 'currentPage'],
        'snapshotViewCsvGenerationMode': ['appendCSVFile', 'newCSVFile', 'overwriteCSVFile'],
    }

    def __init__(self, parent, list_op=False):
        super(CsvSnapshot, self).__init__(parent, list_op)

    @property
    def CsvDecimalPrecision(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvDecimalPrecision'])
    @CsvDecimalPrecision.setter
    def CsvDecimalPrecision(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvDecimalPrecision'], value)

    @property
    def CsvDumpTxPortLabelMap(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvDumpTxPortLabelMap'])
    @CsvDumpTxPortLabelMap.setter
    def CsvDumpTxPortLabelMap(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvDumpTxPortLabelMap'], value)

    @property
    def CsvFormatTimestamp(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvFormatTimestamp'])
    @CsvFormatTimestamp.setter
    def CsvFormatTimestamp(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvFormatTimestamp'], value)

    @property
    def CsvLocation(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvLocation'])
    @CsvLocation.setter
    def CsvLocation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvLocation'], value)

    @property
    def CsvName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvName'])
    @CsvName.setter
    def CsvName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvName'], value)

    @property
    def CsvStringQuotes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvStringQuotes'])
    @CsvStringQuotes.setter
    def CsvStringQuotes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvStringQuotes'], value)

    @property
    def CsvSupportsCSVSorting(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CsvSupportsCSVSorting'])
    @CsvSupportsCSVSorting.setter
    def CsvSupportsCSVSorting(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CsvSupportsCSVSorting'], value)

    @property
    def NextGenRefreshBeforeSnapshot(self):
        # type: () -> bool
        """DEPRECATED 
        Returns
        -------
        - bool: nextGenRefreshBeforeSnapshot is deprecated and has no effect starting from IxNetwork 8.10.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NextGenRefreshBeforeSnapshot'])
    @NextGenRefreshBeforeSnapshot.setter
    def NextGenRefreshBeforeSnapshot(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['NextGenRefreshBeforeSnapshot'], value)

    @property
    def OpenViewer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OpenViewer'])
    @OpenViewer.setter
    def OpenViewer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OpenViewer'], value)

    @property
    def SnapshotSettingsName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SnapshotSettingsName'])

    @property
    def SnapshotViewContents(self):
        # type: () -> str
        """
        Returns
        -------
        - str(allPages | currentPage): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SnapshotViewContents'])
    @SnapshotViewContents.setter
    def SnapshotViewContents(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SnapshotViewContents'], value)

    @property
    def SnapshotViewCsvGenerationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(appendCSVFile | newCSVFile | overwriteCSVFile): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SnapshotViewCsvGenerationMode'])
    @SnapshotViewCsvGenerationMode.setter
    def SnapshotViewCsvGenerationMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SnapshotViewCsvGenerationMode'], value)

    @property
    def Views(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../view]): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Views'])
    @Views.setter
    def Views(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['Views'], value)

    def update(self, CsvDecimalPrecision=None, CsvDumpTxPortLabelMap=None, CsvFormatTimestamp=None, CsvLocation=None, CsvName=None, CsvStringQuotes=None, CsvSupportsCSVSorting=None, NextGenRefreshBeforeSnapshot=None, OpenViewer=None, SnapshotViewContents=None, SnapshotViewCsvGenerationMode=None, Views=None):
        # type: (int, bool, bool, str, str, bool, bool, bool, bool, str, str, List[str]) -> CsvSnapshot
        """Updates csvSnapshot resource on the server.

        Args
        ----
        - CsvDecimalPrecision (number): NOT DEFINED
        - CsvDumpTxPortLabelMap (bool): NOT DEFINED
        - CsvFormatTimestamp (bool): NOT DEFINED
        - CsvLocation (str): NOT DEFINED
        - CsvName (str): 
        - CsvStringQuotes (bool): NOT DEFINED
        - CsvSupportsCSVSorting (bool): NOT DEFINED
        - NextGenRefreshBeforeSnapshot (bool): nextGenRefreshBeforeSnapshot is deprecated and has no effect starting from IxNetwork 8.10.
        - OpenViewer (bool): 
        - SnapshotViewContents (str(allPages | currentPage)): NOT DEFINED
        - SnapshotViewCsvGenerationMode (str(appendCSVFile | newCSVFile | overwriteCSVFile)): NOT DEFINED
        - Views (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../view])): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CsvDecimalPrecision=None, CsvDumpTxPortLabelMap=None, CsvFormatTimestamp=None, CsvLocation=None, CsvName=None, CsvStringQuotes=None, CsvSupportsCSVSorting=None, NextGenRefreshBeforeSnapshot=None, OpenViewer=None, SnapshotSettingsName=None, SnapshotViewContents=None, SnapshotViewCsvGenerationMode=None, Views=None):
        # type: (int, bool, bool, str, str, bool, bool, bool, bool, str, str, str, List[str]) -> CsvSnapshot
        """Finds and retrieves csvSnapshot resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve csvSnapshot resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all csvSnapshot resources from the server.

        Args
        ----
        - CsvDecimalPrecision (number): NOT DEFINED
        - CsvDumpTxPortLabelMap (bool): NOT DEFINED
        - CsvFormatTimestamp (bool): NOT DEFINED
        - CsvLocation (str): NOT DEFINED
        - CsvName (str): 
        - CsvStringQuotes (bool): NOT DEFINED
        - CsvSupportsCSVSorting (bool): NOT DEFINED
        - NextGenRefreshBeforeSnapshot (bool): nextGenRefreshBeforeSnapshot is deprecated and has no effect starting from IxNetwork 8.10.
        - OpenViewer (bool): 
        - SnapshotSettingsName (str): NOT DEFINED
        - SnapshotViewContents (str(allPages | currentPage)): NOT DEFINED
        - SnapshotViewCsvGenerationMode (str(appendCSVFile | newCSVFile | overwriteCSVFile)): NOT DEFINED
        - Views (list(str[None | /api/v1/sessions/1/ixnetwork/statistics/.../view])): NOT DEFINED

        Returns
        -------
        - self: This instance with matching csvSnapshot resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of csvSnapshot data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the csvSnapshot resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ResetToDefaults(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the resetToDefaults operation on the server.

        NOT DEFINED

        resetToDefaults(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('resetToDefaults', payload=payload, response_object=None)

    def TakeCsvSnapshot(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the takeCsvSnapshot operation on the server.

        Takes CSV Snapshot. The views and other settings must be set before the call using the /statistics/csvSnapshot attributes.

        takeCsvSnapshot(async_operation=bool)
        -------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('takeCsvSnapshot', payload=payload, response_object=None)
