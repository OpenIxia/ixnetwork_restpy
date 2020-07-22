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


class RemoteLocators(Base):
    """It gives details about the remote locators
    The RemoteLocators class encapsulates a list of remoteLocators resources that are managed by the system.
    A list of resources can be retrieved from the server using the RemoteLocators.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'remoteLocators'
    _SDM_ATT_MAP = {
        'MPriority': 'mPriority',
        'MWeight': 'mWeight',
        'Priority': 'priority',
        'RemoteLocator': 'remoteLocator',
        'RemoteLocatorAfi': 'remoteLocatorAfi',
        'RlocFlagL': 'rlocFlagL',
        'RlocFlagP': 'rlocFlagP',
        'RlocFlagR': 'rlocFlagR',
        'Weight': 'weight',
    }

    def __init__(self, parent):
        super(RemoteLocators, self).__init__(parent)

    @property
    def MPriority(self):
        """
        Returns
        -------
        - number: It gives details about the m priority (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MPriority'])

    @property
    def MWeight(self):
        """
        Returns
        -------
        - number: It gives details about the m weight (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MWeight'])

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: It gives details about the priority (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])

    @property
    def RemoteLocator(self):
        """
        Returns
        -------
        - str: It gives details about the remote locators (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteLocator'])

    @property
    def RemoteLocatorAfi(self):
        """
        Returns
        -------
        - str: It gives details about the remote locators Afi (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteLocatorAfi'])

    @property
    def RlocFlagL(self):
        """
        Returns
        -------
        - bool: It gives details about the rLoc Flag L (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RlocFlagL'])

    @property
    def RlocFlagP(self):
        """
        Returns
        -------
        - bool: It gives details about the rLoc FlagP (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RlocFlagP'])

    @property
    def RlocFlagR(self):
        """
        Returns
        -------
        - bool: If True, It gives details about the rLoc Flag R (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RlocFlagR'])

    @property
    def Weight(self):
        """
        Returns
        -------
        - number: It gives details about the weight (Read-Only)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Weight'])

    def find(self, MPriority=None, MWeight=None, Priority=None, RemoteLocator=None, RemoteLocatorAfi=None, RlocFlagL=None, RlocFlagP=None, RlocFlagR=None, Weight=None):
        """Finds and retrieves remoteLocators resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve remoteLocators resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all remoteLocators resources from the server.

        Args
        ----
        - MPriority (number): It gives details about the m priority (Read-Only)
        - MWeight (number): It gives details about the m weight (Read-Only)
        - Priority (number): It gives details about the priority (Read-Only)
        - RemoteLocator (str): It gives details about the remote locators (Read-Only)
        - RemoteLocatorAfi (str): It gives details about the remote locators Afi (Read-Only)
        - RlocFlagL (bool): It gives details about the rLoc Flag L (Read-Only)
        - RlocFlagP (bool): It gives details about the rLoc FlagP (Read-Only)
        - RlocFlagR (bool): If True, It gives details about the rLoc Flag R (Read-Only)
        - Weight (number): It gives details about the weight (Read-Only)

        Returns
        -------
        - self: This instance with matching remoteLocators resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of remoteLocators data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the remoteLocators resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
