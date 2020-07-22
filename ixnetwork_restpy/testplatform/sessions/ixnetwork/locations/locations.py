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


class Locations(Base):
    """
    The Locations class encapsulates a list of locations resources that are managed by the user.
    A list of resources can be retrieved from the server using the Locations.find() method.
    The list can be managed by using the Locations.add() and Locations.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'locations'
    _SDM_ATT_MAP = {
        'CableLength': 'cableLength',
        'ChainTopology': 'chainTopology',
        'ConnectRetries': 'connectRetries',
        'DeviceType': 'deviceType',
        'ErrorDescription': 'errorDescription',
        'ErrorState': 'errorState',
        'Hostname': 'hostname',
        'Ip': 'ip',
        'IsMaster': 'isMaster',
        'IxnBuildNumber': 'ixnBuildNumber',
        'IxosBuildNumber': 'ixosBuildNumber',
        'LicenseErrors': 'licenseErrors',
        'MasterDevice': 'masterDevice',
        'OsType': 'osType',
        'ProtocolBuildNumber': 'protocolBuildNumber',
        'SequenceId': 'sequenceId',
        'State': 'state',
    }

    def __init__(self, parent):
        super(Locations, self).__init__(parent)

    @property
    def Ports(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.ports.ports.Ports): An instance of the Ports class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.ports.ports import Ports
        return Ports(self)

    @property
    def ResourceGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.resourcegroups.resourcegroups.ResourceGroups): An instance of the ResourceGroups class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.locations.resourcegroups.resourcegroups import ResourceGroups
        return ResourceGroups(self)

    @property
    def CableLength(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CableLength'])
    @CableLength.setter
    def CableLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CableLength'], value)

    @property
    def ChainTopology(self):
        """
        Returns
        -------
        - str(daisy | none | star): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ChainTopology'])
    @ChainTopology.setter
    def ChainTopology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ChainTopology'], value)

    @property
    def ConnectRetries(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectRetries'])

    @property
    def DeviceType(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeviceType'])

    @property
    def ErrorDescription(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorDescription'])

    @property
    def ErrorState(self):
        """
        Returns
        -------
        - str(ConnectError | DuplicateChassis | IncompatibleIxOS | MultipleNics | NoCardsFound | NoError | NoLicenseFound | NonAppliance | NonLinuxChassis): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrorState'])

    @property
    def Hostname(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Hostname'])
    @Hostname.setter
    def Hostname(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Hostname'], value)

    @property
    def Ip(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ip'])

    @property
    def IsMaster(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsMaster'])

    @property
    def IxnBuildNumber(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IxnBuildNumber'])

    @property
    def IxosBuildNumber(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IxosBuildNumber'])

    @property
    def LicenseErrors(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LicenseErrors'])

    @property
    def MasterDevice(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterDevice'])
    @MasterDevice.setter
    def MasterDevice(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MasterDevice'], value)

    @property
    def OsType(self):
        """
        Returns
        -------
        - str(linux | unknown | windows): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OsType'])

    @property
    def ProtocolBuildNumber(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolBuildNumber'])

    @property
    def SequenceId(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SequenceId'])
    @SequenceId.setter
    def SequenceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SequenceId'], value)

    @property
    def State(self):
        """
        Returns
        -------
        - str(down | down | polling | polling | polling | ready): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])

    def update(self, CableLength=None, ChainTopology=None, Hostname=None, MasterDevice=None, SequenceId=None):
        """Updates locations resource on the server.

        Args
        ----
        - CableLength (number): 
        - ChainTopology (str(daisy | none | star)): 
        - Hostname (str): 
        - MasterDevice (str): 
        - SequenceId (number): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CableLength=None, ChainTopology=None, Hostname=None, MasterDevice=None, SequenceId=None):
        """Adds a new locations resource on the server and adds it to the container.

        Args
        ----
        - CableLength (number): 
        - ChainTopology (str(daisy | none | star)): 
        - Hostname (str): 
        - MasterDevice (str): 
        - SequenceId (number): 

        Returns
        -------
        - self: This instance with all currently retrieved locations resources using find and the newly added locations resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained locations resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CableLength=None, ChainTopology=None, ConnectRetries=None, DeviceType=None, ErrorDescription=None, ErrorState=None, Hostname=None, Ip=None, IsMaster=None, IxnBuildNumber=None, IxosBuildNumber=None, LicenseErrors=None, MasterDevice=None, OsType=None, ProtocolBuildNumber=None, SequenceId=None, State=None):
        """Finds and retrieves locations resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve locations resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all locations resources from the server.

        Args
        ----
        - CableLength (number): 
        - ChainTopology (str(daisy | none | star)): 
        - ConnectRetries (number): 
        - DeviceType (str): 
        - ErrorDescription (str): 
        - ErrorState (str(ConnectError | DuplicateChassis | IncompatibleIxOS | MultipleNics | NoCardsFound | NoError | NoLicenseFound | NonAppliance | NonLinuxChassis)): 
        - Hostname (str): 
        - Ip (str): 
        - IsMaster (bool): 
        - IxnBuildNumber (str): 
        - IxosBuildNumber (str): 
        - LicenseErrors (list(str)): 
        - MasterDevice (str): 
        - OsType (str(linux | unknown | windows)): 
        - ProtocolBuildNumber (str): 
        - SequenceId (number): 
        - State (str(down | down | polling | polling | polling | ready)): 

        Returns
        -------
        - self: This instance with matching locations resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of locations data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the locations resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
