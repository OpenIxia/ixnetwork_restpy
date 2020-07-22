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


class DiscoveredAppliance(Base):
    """Retrieves the list of appliances that were discovered with Discovery Server
    The DiscoveredAppliance class encapsulates a list of discoveredAppliance resources that are managed by the system.
    A list of resources can be retrieved from the server using the DiscoveredAppliance.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'discoveredAppliance'
    _SDM_ATT_MAP = {
        'ApplianceName': 'applianceName',
        'ApplianceType': 'applianceType',
        'InterfacesNumber': 'interfacesNumber',
        'ManagementIp': 'managementIp',
    }

    def __init__(self, parent):
        super(DiscoveredAppliance, self).__init__(parent)

    @property
    def DiscoveredInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.discoveredappliance.discoveredinterface.discoveredinterface.DiscoveredInterface): An instance of the DiscoveredInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.discoveredappliance.discoveredinterface.discoveredinterface import DiscoveredInterface
        return DiscoveredInterface(self)

    @property
    def ApplianceName(self):
        """
        Returns
        -------
        - str: Represents the appliance Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplianceName'])

    @property
    def ApplianceType(self):
        """
        Returns
        -------
        - str(qemu | vCenter | vmware): Represents the appliance host type
        """
        return self._get_attribute(self._SDM_ATT_MAP['ApplianceType'])

    @property
    def InterfacesNumber(self):
        """
        Returns
        -------
        - number: Represents the number of test interfaces
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfacesNumber'])

    @property
    def ManagementIp(self):
        """
        Returns
        -------
        - str: Represents the management Ip
        """
        return self._get_attribute(self._SDM_ATT_MAP['ManagementIp'])

    def find(self, ApplianceName=None, ApplianceType=None, InterfacesNumber=None, ManagementIp=None):
        """Finds and retrieves discoveredAppliance resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve discoveredAppliance resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all discoveredAppliance resources from the server.

        Args
        ----
        - ApplianceName (str): Represents the appliance Name
        - ApplianceType (str(qemu | vCenter | vmware)): Represents the appliance host type
        - InterfacesNumber (number): Represents the number of test interfaces
        - ManagementIp (str): Represents the management Ip

        Returns
        -------
        - self: This instance with matching discoveredAppliance resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of discoveredAppliance data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the discoveredAppliance resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
