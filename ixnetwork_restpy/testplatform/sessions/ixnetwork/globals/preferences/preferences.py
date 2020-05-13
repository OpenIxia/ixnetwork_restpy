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


class Preferences(Base):
    """The preferences node contains user configurable system wide preferences
    The Preferences class encapsulates a required preferences resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'preferences'
    _SDM_ATT_MAP = {
        'ClientTraceLevel': 'clientTraceLevel',
        'ConnectPortsOnLoadConfig': 'connectPortsOnLoadConfig',
        'LatestConfigInDiagEnabled': 'latestConfigInDiagEnabled',
        'RebootPortsOnConnect': 'rebootPortsOnConnect',
        'RecentChassisList': 'recentChassisList',
        'RecentFiles': 'recentFiles',
    }

    def __init__(self, parent):
        super(Preferences, self).__init__(parent)

    @property
    def ClientTraceLevel(self):
        """
        Returns
        -------
        - str(debug | error | fatal | info | warn): Set the IxNetwork Client side Log/Trace level
        """
        return self._get_attribute(self._SDM_ATT_MAP['ClientTraceLevel'])
    @ClientTraceLevel.setter
    def ClientTraceLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ClientTraceLevel'], value)

    @property
    def ConnectPortsOnLoadConfig(self):
        """
        Returns
        -------
        - bool: If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectPortsOnLoadConfig'])
    @ConnectPortsOnLoadConfig.setter
    def ConnectPortsOnLoadConfig(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectPortsOnLoadConfig'], value)

    @property
    def LatestConfigInDiagEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LatestConfigInDiagEnabled'])
    @LatestConfigInDiagEnabled.setter
    def LatestConfigInDiagEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LatestConfigInDiagEnabled'], value)

    @property
    def RebootPortsOnConnect(self):
        """
        Returns
        -------
        - bool: If true the application will reboot any connected virtual ports when the configuration is loaded
        """
        return self._get_attribute(self._SDM_ATT_MAP['RebootPortsOnConnect'])
    @RebootPortsOnConnect.setter
    def RebootPortsOnConnect(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RebootPortsOnConnect'], value)

    @property
    def RecentChassisList(self):
        """
        Returns
        -------
        - list(str): List of recently used chassis
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentChassisList'])
    @RecentChassisList.setter
    def RecentChassisList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RecentChassisList'], value)

    @property
    def RecentFiles(self):
        """
        Returns
        -------
        - list(str): List of recently used files
        """
        return self._get_attribute(self._SDM_ATT_MAP['RecentFiles'])

    def update(self, ClientTraceLevel=None, ConnectPortsOnLoadConfig=None, LatestConfigInDiagEnabled=None, RebootPortsOnConnect=None, RecentChassisList=None):
        """Updates preferences resource on the server.

        Args
        ----
        - ClientTraceLevel (str(debug | error | fatal | info | warn)): Set the IxNetwork Client side Log/Trace level
        - ConnectPortsOnLoadConfig (bool): If true the application will connect the virtual ports to any assigned hardware ports when the configuration is loaded
        - LatestConfigInDiagEnabled (bool): 
        - RebootPortsOnConnect (bool): If true the application will reboot any connected virtual ports when the configuration is loaded
        - RecentChassisList (list(str)): List of recently used chassis

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
