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


class ReportGenerator(Base):
    """This node contains Stats Report Generator Options and APIs.
    The ReportGenerator class encapsulates a required reportGenerator resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "reportGenerator"
    _SDM_ATT_MAP = {
        "CompanyName": "companyName",
        "CustomCompanyLogoFileName": "customCompanyLogoFileName",
        "CustomCoverPicFileName": "customCoverPicFileName",
        "DutHwVersion": "dutHwVersion",
        "DutName": "dutName",
        "DutSerialNo": "dutSerialNo",
        "DutSwVersion": "dutSwVersion",
        "ImageUploadPath": "imageUploadPath",
        "IncludeCustomViews": "includeCustomViews",
        "IncludePortProtocolSummary": "includePortProtocolSummary",
        "IncludeProtocolStats": "includeProtocolStats",
        "IncludeProtocolSummary": "includeProtocolSummary",
        "IncludeTrafficBestFlows": "includeTrafficBestFlows",
        "IncludeTrafficFlowStats": "includeTrafficFlowStats",
        "IncludeTrafficItemStats": "includeTrafficItemStats",
        "IncludeTrafficL23Summary": "includeTrafficL23Summary",
        "IncludeTrafficWorstFlows": "includeTrafficWorstFlows",
        "IxNetworkVersion": "ixNetworkVersion",
        "ProtocolsToInclude": "protocolsToInclude",
        "ReportType": "reportType",
        "ShowCustomViewOption": "showCustomViewOption",
        "TestCategory": "testCategory",
        "TestHighlights": "testHighlights",
        "TestName": "testName",
        "TestObjectives": "testObjectives",
        "TesterName": "testerName",
    }
    _SDM_ENUM_MAP = {
        "reportType": ["kNGPF", "kNone", "kTraffic", "kTrafficAndNGPF"],
    }

    def __init__(self, parent, list_op=False):
        super(ReportGenerator, self).__init__(parent, list_op)

    @property
    def CompanyName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This is used in the report header
        """
        return self._get_attribute(self._SDM_ATT_MAP["CompanyName"])

    @CompanyName.setter
    def CompanyName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CompanyName"], value)

    @property
    def CustomCompanyLogoFileName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This is used in the report
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomCompanyLogoFileName"])

    @CustomCompanyLogoFileName.setter
    def CustomCompanyLogoFileName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomCompanyLogoFileName"], value)

    @property
    def CustomCoverPicFileName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: This is used in the report
        """
        return self._get_attribute(self._SDM_ATT_MAP["CustomCoverPicFileName"])

    @CustomCoverPicFileName.setter
    def CustomCoverPicFileName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CustomCoverPicFileName"], value)

    @property
    def DutHwVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutHwVersion"])

    @DutHwVersion.setter
    def DutHwVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DutHwVersion"], value)

    @property
    def DutName(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutName"])

    @DutName.setter
    def DutName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DutName"], value)

    @property
    def DutSerialNo(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutSerialNo"])

    @DutSerialNo.setter
    def DutSerialNo(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DutSerialNo"], value)

    @property
    def DutSwVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["DutSwVersion"])

    @DutSwVersion.setter
    def DutSwVersion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["DutSwVersion"], value)

    @property
    def ImageUploadPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Path where the report images are kept
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImageUploadPath"])

    @property
    def IncludeCustomViews(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeCustomViews"])

    @IncludeCustomViews.setter
    def IncludeCustomViews(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeCustomViews"], value)

    @property
    def IncludePortProtocolSummary(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludePortProtocolSummary"])

    @IncludePortProtocolSummary.setter
    def IncludePortProtocolSummary(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludePortProtocolSummary"], value)

    @property
    def IncludeProtocolStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeProtocolStats"])

    @IncludeProtocolStats.setter
    def IncludeProtocolStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeProtocolStats"], value)

    @property
    def IncludeProtocolSummary(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeProtocolSummary"])

    @IncludeProtocolSummary.setter
    def IncludeProtocolSummary(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeProtocolSummary"], value)

    @property
    def IncludeTrafficBestFlows(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficBestFlows"])

    @IncludeTrafficBestFlows.setter
    def IncludeTrafficBestFlows(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficBestFlows"], value)

    @property
    def IncludeTrafficFlowStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficFlowStats"])

    @IncludeTrafficFlowStats.setter
    def IncludeTrafficFlowStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficFlowStats"], value)

    @property
    def IncludeTrafficItemStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficItemStats"])

    @IncludeTrafficItemStats.setter
    def IncludeTrafficItemStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficItemStats"], value)

    @property
    def IncludeTrafficL23Summary(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficL23Summary"])

    @IncludeTrafficL23Summary.setter
    def IncludeTrafficL23Summary(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficL23Summary"], value)

    @property
    def IncludeTrafficWorstFlows(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludeTrafficWorstFlows"])

    @IncludeTrafficWorstFlows.setter
    def IncludeTrafficWorstFlows(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludeTrafficWorstFlows"], value)

    @property
    def IxNetworkVersion(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IxNetworkVersion"])

    @property
    def ProtocolsToInclude(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Comma separate names of Protocols to be included in Report. Empty means everything is included
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProtocolsToInclude"])

    @ProtocolsToInclude.setter
    def ProtocolsToInclude(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProtocolsToInclude"], value)

    @property
    def ReportType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(kNGPF | kNone | kTraffic | kTrafficAndNGPF):
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportType"])

    @ReportType.setter
    def ReportType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReportType"], value)

    @property
    def ShowCustomViewOption(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowCustomViewOption"])

    @property
    def TestCategory(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestCategory"])

    @TestCategory.setter
    def TestCategory(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestCategory"], value)

    @property
    def TestHighlights(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TestHighlights"])

    @TestHighlights.setter
    def TestHighlights(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TestHighlights"], value)

    @property
    def TestName(self):
        # type: () -> str
        """
        Returns
        -------
        - str:
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
        - str:
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
        - str:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TesterName"])

    @TesterName.setter
    def TesterName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TesterName"], value)

    def update(
        self,
        CompanyName=None,
        CustomCompanyLogoFileName=None,
        CustomCoverPicFileName=None,
        DutHwVersion=None,
        DutName=None,
        DutSerialNo=None,
        DutSwVersion=None,
        IncludeCustomViews=None,
        IncludePortProtocolSummary=None,
        IncludeProtocolStats=None,
        IncludeProtocolSummary=None,
        IncludeTrafficBestFlows=None,
        IncludeTrafficFlowStats=None,
        IncludeTrafficItemStats=None,
        IncludeTrafficL23Summary=None,
        IncludeTrafficWorstFlows=None,
        ProtocolsToInclude=None,
        ReportType=None,
        TestCategory=None,
        TestHighlights=None,
        TestName=None,
        TestObjectives=None,
        TesterName=None,
    ):
        # type: (str, str, str, str, str, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, str, str, str, str, str) -> ReportGenerator
        """Updates reportGenerator resource on the server.

        Args
        ----
        - CompanyName (str): This is used in the report header
        - CustomCompanyLogoFileName (str): This is used in the report
        - CustomCoverPicFileName (str): This is used in the report
        - DutHwVersion (str):
        - DutName (str):
        - DutSerialNo (str):
        - DutSwVersion (str):
        - IncludeCustomViews (bool):
        - IncludePortProtocolSummary (bool):
        - IncludeProtocolStats (bool):
        - IncludeProtocolSummary (bool):
        - IncludeTrafficBestFlows (bool):
        - IncludeTrafficFlowStats (bool):
        - IncludeTrafficItemStats (bool):
        - IncludeTrafficL23Summary (bool):
        - IncludeTrafficWorstFlows (bool):
        - ProtocolsToInclude (str): Comma separate names of Protocols to be included in Report. Empty means everything is included
        - ReportType (str(kNGPF | kNone | kTraffic | kTrafficAndNGPF)):
        - TestCategory (str):
        - TestHighlights (str):
        - TestName (str):
        - TestObjectives (str):
        - TesterName (str):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        CompanyName=None,
        CustomCompanyLogoFileName=None,
        CustomCoverPicFileName=None,
        DutHwVersion=None,
        DutName=None,
        DutSerialNo=None,
        DutSwVersion=None,
        ImageUploadPath=None,
        IncludeCustomViews=None,
        IncludePortProtocolSummary=None,
        IncludeProtocolStats=None,
        IncludeProtocolSummary=None,
        IncludeTrafficBestFlows=None,
        IncludeTrafficFlowStats=None,
        IncludeTrafficItemStats=None,
        IncludeTrafficL23Summary=None,
        IncludeTrafficWorstFlows=None,
        IxNetworkVersion=None,
        ProtocolsToInclude=None,
        ReportType=None,
        ShowCustomViewOption=None,
        TestCategory=None,
        TestHighlights=None,
        TestName=None,
        TestObjectives=None,
        TesterName=None,
    ):
        # type: (str, str, str, str, str, str, str, str, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, str, str, bool, str, str, str, str, str) -> ReportGenerator
        """Finds and retrieves reportGenerator resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve reportGenerator resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all reportGenerator resources from the server.

        Args
        ----
        - CompanyName (str): This is used in the report header
        - CustomCompanyLogoFileName (str): This is used in the report
        - CustomCoverPicFileName (str): This is used in the report
        - DutHwVersion (str):
        - DutName (str):
        - DutSerialNo (str):
        - DutSwVersion (str):
        - ImageUploadPath (str): Path where the report images are kept
        - IncludeCustomViews (bool):
        - IncludePortProtocolSummary (bool):
        - IncludeProtocolStats (bool):
        - IncludeProtocolSummary (bool):
        - IncludeTrafficBestFlows (bool):
        - IncludeTrafficFlowStats (bool):
        - IncludeTrafficItemStats (bool):
        - IncludeTrafficL23Summary (bool):
        - IncludeTrafficWorstFlows (bool):
        - IxNetworkVersion (str):
        - ProtocolsToInclude (str): Comma separate names of Protocols to be included in Report. Empty means everything is included
        - ReportType (str(kNGPF | kNone | kTraffic | kTrafficAndNGPF)):
        - ShowCustomViewOption (bool):
        - TestCategory (str):
        - TestHighlights (str):
        - TestName (str):
        - TestObjectives (str):
        - TesterName (str):

        Returns
        -------
        - self: This instance with matching reportGenerator resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of reportGenerator data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the reportGenerator resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GenerateStatReportV2(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the generateStatReportV2 operation on the server.

        Generates Stat Report

        generateStatReportV2(async_operation=bool)string
        ------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Either the location of the generated report file or error string in case of error

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
            "generateStatReportV2", payload=payload, response_object=None
        )

    def GetCustomGraphData(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the getCustomGraphData operation on the server.

        Get custom graph data plotted over time

        getCustomGraphData(Arg2=string, async_operation=bool)string
        -----------------------------------------------------------
        - Arg2 (str): view caption
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: Graph Data with column names and time stamp

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
            "getCustomGraphData", payload=payload, response_object=None
        )

    def ProcessUploadedCustomImage(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the processUploadedCustomImage operation on the server.

        processs the uploaded customer image for Cover Pic/Company Logo

        processUploadedCustomImage(Arg2=string, Arg3=string, async_operation=bool)
        --------------------------------------------------------------------------
        - Arg2 (str): CoverPic/CompanyLogo
        - Arg3 (str): name of the file
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
            "processUploadedCustomImage", payload=payload, response_object=None
        )
