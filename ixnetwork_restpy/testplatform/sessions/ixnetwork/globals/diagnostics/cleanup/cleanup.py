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


class Cleanup(Base):
    """
    The Cleanup class encapsulates a required cleanup resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cleanup'
    _SDM_ATT_MAP = {
        'ChassisDaysOld': 'chassisDaysOld',
        'CleanupChassis': 'cleanupChassis',
        'CleanupClient': 'cleanupClient',
        'ClientDaysOld': 'clientDaysOld',
        'ProfileAes': 'profileAes',
        'ProfileAllprofiles': 'profileAllprofiles',
        'ProfileAnalyzer': 'profileAnalyzer',
        'ProfileHlapi': 'profileHlapi',
        'ProfileImpairment': 'profileImpairment',
        'ProfileIxloadlite': 'profileIxloadlite',
        'ProfileMiddleware': 'profileMiddleware',
        'ProfileQuicktests': 'profileQuicktests',
        'ProfileStackmanager': 'profileStackmanager',
        'ProfileStatviewerreporter': 'profileStatviewerreporter',
    }

    def __init__(self, parent):
        super(Cleanup, self).__init__(parent)

    @property
    def ChassisDaysOld(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChassisDaysOld'])
    @ChassisDaysOld.setter
    def ChassisDaysOld(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChassisDaysOld'], value)

    @property
    def CleanupChassis(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CleanupChassis'])
    @CleanupChassis.setter
    def CleanupChassis(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CleanupChassis'], value)

    @property
    def CleanupClient(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CleanupClient'])
    @CleanupClient.setter
    def CleanupClient(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CleanupClient'], value)

    @property
    def ClientDaysOld(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientDaysOld'])
    @ClientDaysOld.setter
    def ClientDaysOld(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientDaysOld'], value)

    @property
    def ProfileAes(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup AES logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileAes'])
    @ProfileAes.setter
    def ProfileAes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileAes'], value)

    @property
    def ProfileAllprofiles(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup All-Profiles logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileAllprofiles'])
    @ProfileAllprofiles.setter
    def ProfileAllprofiles(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileAllprofiles'], value)

    @property
    def ProfileAnalyzer(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup Analyzer logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileAnalyzer'])
    @ProfileAnalyzer.setter
    def ProfileAnalyzer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileAnalyzer'], value)

    @property
    def ProfileHlapi(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup HLAPI logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileHlapi'])
    @ProfileHlapi.setter
    def ProfileHlapi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileHlapi'], value)

    @property
    def ProfileImpairment(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup Impairment logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileImpairment'])
    @ProfileImpairment.setter
    def ProfileImpairment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileImpairment'], value)

    @property
    def ProfileIxloadlite(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup IxLoad Lite logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileIxloadlite'])
    @ProfileIxloadlite.setter
    def ProfileIxloadlite(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileIxloadlite'], value)

    @property
    def ProfileMiddleware(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup MiddleWare logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileMiddleware'])
    @ProfileMiddleware.setter
    def ProfileMiddleware(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileMiddleware'], value)

    @property
    def ProfileQuicktests(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup QuickTests logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileQuicktests'])
    @ProfileQuicktests.setter
    def ProfileQuicktests(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileQuicktests'], value)

    @property
    def ProfileStackmanager(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup StackManager logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileStackmanager'])
    @ProfileStackmanager.setter
    def ProfileStackmanager(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileStackmanager'], value)

    @property
    def ProfileStatviewerreporter(self):
        """
        Returns
        -------
        - bool: Set this flag to cleanup StatViewer-Reporter logs/artifacts
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileStatviewerreporter'])
    @ProfileStatviewerreporter.setter
    def ProfileStatviewerreporter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProfileStatviewerreporter'], value)

    def update(self, ChassisDaysOld=None, CleanupChassis=None, CleanupClient=None, ClientDaysOld=None, ProfileAes=None, ProfileAllprofiles=None, ProfileAnalyzer=None, ProfileHlapi=None, ProfileImpairment=None, ProfileIxloadlite=None, ProfileMiddleware=None, ProfileQuicktests=None, ProfileStackmanager=None, ProfileStatviewerreporter=None):
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

    def CleanupLogs(self):
        """Executes the cleanupLogs operation on the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('cleanupLogs', payload=payload, response_object=None)
