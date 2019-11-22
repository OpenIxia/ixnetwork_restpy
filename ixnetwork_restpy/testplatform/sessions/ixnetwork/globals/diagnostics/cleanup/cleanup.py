# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class Cleanup(Base):
    """
    The Cleanup class encapsulates a required cleanup resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cleanup'

    def __init__(self, parent):
        super(Cleanup, self).__init__(parent)

    @property
    def ChassisDaysOld(self):
        """

        Returns:
            number
        """
        return self._get_attribute('chassisDaysOld')
    @ChassisDaysOld.setter
    def ChassisDaysOld(self, value):
        self._set_attribute('chassisDaysOld', value)

    @property
    def CleanupChassis(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('cleanupChassis')
    @CleanupChassis.setter
    def CleanupChassis(self, value):
        self._set_attribute('cleanupChassis', value)

    @property
    def CleanupClient(self):
        """

        Returns:
            bool
        """
        return self._get_attribute('cleanupClient')
    @CleanupClient.setter
    def CleanupClient(self, value):
        self._set_attribute('cleanupClient', value)

    @property
    def ClientDaysOld(self):
        """

        Returns:
            number
        """
        return self._get_attribute('clientDaysOld')
    @ClientDaysOld.setter
    def ClientDaysOld(self, value):
        self._set_attribute('clientDaysOld', value)

    @property
    def ProfileAes(self):
        """Set this flag to cleanup AES logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileAes')
    @ProfileAes.setter
    def ProfileAes(self, value):
        self._set_attribute('profileAes', value)

    @property
    def ProfileAllprofiles(self):
        """Set this flag to cleanup All-Profiles logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileAllprofiles')
    @ProfileAllprofiles.setter
    def ProfileAllprofiles(self, value):
        self._set_attribute('profileAllprofiles', value)

    @property
    def ProfileAnalyzer(self):
        """Set this flag to cleanup Analyzer logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileAnalyzer')
    @ProfileAnalyzer.setter
    def ProfileAnalyzer(self, value):
        self._set_attribute('profileAnalyzer', value)

    @property
    def ProfileHlapi(self):
        """Set this flag to cleanup HLAPI logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileHlapi')
    @ProfileHlapi.setter
    def ProfileHlapi(self, value):
        self._set_attribute('profileHlapi', value)

    @property
    def ProfileImpairment(self):
        """Set this flag to cleanup Impairment logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileImpairment')
    @ProfileImpairment.setter
    def ProfileImpairment(self, value):
        self._set_attribute('profileImpairment', value)

    @property
    def ProfileIxloadlite(self):
        """Set this flag to cleanup IxLoad Lite logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileIxloadlite')
    @ProfileIxloadlite.setter
    def ProfileIxloadlite(self, value):
        self._set_attribute('profileIxloadlite', value)

    @property
    def ProfileMiddleware(self):
        """Set this flag to cleanup MiddleWare logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileMiddleware')
    @ProfileMiddleware.setter
    def ProfileMiddleware(self, value):
        self._set_attribute('profileMiddleware', value)

    @property
    def ProfileQuicktests(self):
        """Set this flag to cleanup QuickTests logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileQuicktests')
    @ProfileQuicktests.setter
    def ProfileQuicktests(self, value):
        self._set_attribute('profileQuicktests', value)

    @property
    def ProfileStackmanager(self):
        """Set this flag to cleanup StackManager logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileStackmanager')
    @ProfileStackmanager.setter
    def ProfileStackmanager(self, value):
        self._set_attribute('profileStackmanager', value)

    @property
    def ProfileStatviewerreporter(self):
        """Set this flag to cleanup StatViewer-Reporter logs/artifacts

        Returns:
            bool
        """
        return self._get_attribute('profileStatviewerreporter')
    @ProfileStatviewerreporter.setter
    def ProfileStatviewerreporter(self, value):
        self._set_attribute('profileStatviewerreporter', value)

    def update(self, ChassisDaysOld=None, CleanupChassis=None, CleanupClient=None, ClientDaysOld=None, ProfileAes=None, ProfileAllprofiles=None, ProfileAnalyzer=None, ProfileHlapi=None, ProfileImpairment=None, ProfileIxloadlite=None, ProfileMiddleware=None, ProfileQuicktests=None, ProfileStackmanager=None, ProfileStatviewerreporter=None):
        """Updates a child instance of cleanup on the server.

        Args:
            ChassisDaysOld (number): 
            CleanupChassis (bool): 
            CleanupClient (bool): 
            ClientDaysOld (number): 
            ProfileAes (bool): Set this flag to cleanup AES logs/artifacts
            ProfileAllprofiles (bool): Set this flag to cleanup All-Profiles logs/artifacts
            ProfileAnalyzer (bool): Set this flag to cleanup Analyzer logs/artifacts
            ProfileHlapi (bool): Set this flag to cleanup HLAPI logs/artifacts
            ProfileImpairment (bool): Set this flag to cleanup Impairment logs/artifacts
            ProfileIxloadlite (bool): Set this flag to cleanup IxLoad Lite logs/artifacts
            ProfileMiddleware (bool): Set this flag to cleanup MiddleWare logs/artifacts
            ProfileQuicktests (bool): Set this flag to cleanup QuickTests logs/artifacts
            ProfileStackmanager (bool): Set this flag to cleanup StackManager logs/artifacts
            ProfileStatviewerreporter (bool): Set this flag to cleanup StatViewer-Reporter logs/artifacts

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CleanupLogs(self):
        """Executes the cleanupLogs operation on the server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('cleanupLogs', payload=payload, response_object=None)
