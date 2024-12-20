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


class Cleanup(Base):
    """
    The Cleanup class encapsulates a required cleanup resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "cleanup"
    _SDM_ATT_MAP = {
        "ChassisDaysOld": "chassisDaysOld",
        "CleanupChassis": "cleanupChassis",
        "CleanupClient": "cleanupClient",
        "ClientDaysOld": "clientDaysOld",
        "ProfileAes": "profileAes",
        "ProfileAllprofiles": "profileAllprofiles",
        "ProfileAnalyzer": "profileAnalyzer",
        "ProfileHlapi": "profileHlapi",
        "ProfileImpairment": "profileImpairment",
        "ProfileIxloadlite": "profileIxloadlite",
        "ProfileMiddleware": "profileMiddleware",
        "ProfileQuicktests": "profileQuicktests",
        "ProfileStackmanager": "profileStackmanager",
        "ProfileStatviewerreporter": "profileStatviewerreporter",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Cleanup, self).__init__(parent, list_op)

    @property
    def ChassisDaysOld(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ChassisDaysOld"])

    @ChassisDaysOld.setter
    def ChassisDaysOld(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ChassisDaysOld"], value)

    @property
    def CleanupChassis(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CleanupChassis"])

    @CleanupChassis.setter
    def CleanupChassis(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CleanupChassis"], value)

    @property
    def CleanupClient(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["CleanupClient"])

    @CleanupClient.setter
    def CleanupClient(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CleanupClient"], value)

    @property
    def ClientDaysOld(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ClientDaysOld"])

    @ClientDaysOld.setter
    def ClientDaysOld(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ClientDaysOld"], value)

    @property
    def ProfileAes(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup AES logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileAes"])

    @ProfileAes.setter
    def ProfileAes(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileAes"], value)

    @property
    def ProfileAllprofiles(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup All-Profiles logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileAllprofiles"])

    @ProfileAllprofiles.setter
    def ProfileAllprofiles(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileAllprofiles"], value)

    @property
    def ProfileAnalyzer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup Analyzer logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileAnalyzer"])

    @ProfileAnalyzer.setter
    def ProfileAnalyzer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileAnalyzer"], value)

    @property
    def ProfileHlapi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup HLAPI logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileHlapi"])

    @ProfileHlapi.setter
    def ProfileHlapi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileHlapi"], value)

    @property
    def ProfileImpairment(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup Impairment logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileImpairment"])

    @ProfileImpairment.setter
    def ProfileImpairment(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileImpairment"], value)

    @property
    def ProfileIxloadlite(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup IxLoad Lite logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileIxloadlite"])

    @ProfileIxloadlite.setter
    def ProfileIxloadlite(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileIxloadlite"], value)

    @property
    def ProfileMiddleware(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup MiddleWare logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileMiddleware"])

    @ProfileMiddleware.setter
    def ProfileMiddleware(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileMiddleware"], value)

    @property
    def ProfileQuicktests(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup QuickTests logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileQuicktests"])

    @ProfileQuicktests.setter
    def ProfileQuicktests(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileQuicktests"], value)

    @property
    def ProfileStackmanager(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup StackManager logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileStackmanager"])

    @ProfileStackmanager.setter
    def ProfileStackmanager(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileStackmanager"], value)

    @property
    def ProfileStatviewerreporter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set this flag to cleanup StatViewer-Reporter logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP["ProfileStatviewerreporter"])

    @ProfileStatviewerreporter.setter
    def ProfileStatviewerreporter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ProfileStatviewerreporter"], value)

    def update(
        self,
        ChassisDaysOld=None,
        CleanupChassis=None,
        CleanupClient=None,
        ClientDaysOld=None,
        ProfileAes=None,
        ProfileAllprofiles=None,
        ProfileAnalyzer=None,
        ProfileHlapi=None,
        ProfileImpairment=None,
        ProfileIxloadlite=None,
        ProfileMiddleware=None,
        ProfileQuicktests=None,
        ProfileStackmanager=None,
        ProfileStatviewerreporter=None,
    ):
        # type: (int, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Cleanup
        """Updates cleanup resource on the server.

        Args
        ----
        - ChassisDaysOld (number):
        - CleanupChassis (bool):
        - CleanupClient (bool):
        - ClientDaysOld (number):
        - ProfileAes (bool): Set this flag to cleanup AES logs/artifacts
        - ProfileAllprofiles (bool): Set this flag to cleanup All-Profiles logs/artifacts
        - ProfileAnalyzer (bool): Set this flag to cleanup Analyzer logs/artifacts
        - ProfileHlapi (bool): Set this flag to cleanup HLAPI logs/artifacts
        - ProfileImpairment (bool): Set this flag to cleanup Impairment logs/artifacts
        - ProfileIxloadlite (bool): Set this flag to cleanup IxLoad Lite logs/artifacts
        - ProfileMiddleware (bool): Set this flag to cleanup MiddleWare logs/artifacts
        - ProfileQuicktests (bool): Set this flag to cleanup QuickTests logs/artifacts
        - ProfileStackmanager (bool): Set this flag to cleanup StackManager logs/artifacts
        - ProfileStatviewerreporter (bool): Set this flag to cleanup StatViewer-Reporter logs/artifacts

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ChassisDaysOld=None,
        CleanupChassis=None,
        CleanupClient=None,
        ClientDaysOld=None,
        ProfileAes=None,
        ProfileAllprofiles=None,
        ProfileAnalyzer=None,
        ProfileHlapi=None,
        ProfileImpairment=None,
        ProfileIxloadlite=None,
        ProfileMiddleware=None,
        ProfileQuicktests=None,
        ProfileStackmanager=None,
        ProfileStatviewerreporter=None,
    ):
        # type: (int, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> Cleanup
        """Finds and retrieves cleanup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve cleanup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all cleanup resources from the server.

        Args
        ----
        - ChassisDaysOld (number):
        - CleanupChassis (bool):
        - CleanupClient (bool):
        - ClientDaysOld (number):
        - ProfileAes (bool): Set this flag to cleanup AES logs/artifacts
        - ProfileAllprofiles (bool): Set this flag to cleanup All-Profiles logs/artifacts
        - ProfileAnalyzer (bool): Set this flag to cleanup Analyzer logs/artifacts
        - ProfileHlapi (bool): Set this flag to cleanup HLAPI logs/artifacts
        - ProfileImpairment (bool): Set this flag to cleanup Impairment logs/artifacts
        - ProfileIxloadlite (bool): Set this flag to cleanup IxLoad Lite logs/artifacts
        - ProfileMiddleware (bool): Set this flag to cleanup MiddleWare logs/artifacts
        - ProfileQuicktests (bool): Set this flag to cleanup QuickTests logs/artifacts
        - ProfileStackmanager (bool): Set this flag to cleanup StackManager logs/artifacts
        - ProfileStatviewerreporter (bool): Set this flag to cleanup StatViewer-Reporter logs/artifacts

        Returns
        -------
        - self: This instance with matching cleanup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of cleanup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the cleanup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def CleanupLogs(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the cleanupLogs operation on the server.

        cleanupLogs(async_operation=bool)
        ---------------------------------
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
        return self._execute("cleanupLogs", payload=payload, response_object=None)

    def CleanupOldDiags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the cleanupOldDiags operation on the server.

        cleanupOldDiags(async_operation=bool)
        -------------------------------------
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
        return self._execute("cleanupOldDiags", payload=payload, response_object=None)
