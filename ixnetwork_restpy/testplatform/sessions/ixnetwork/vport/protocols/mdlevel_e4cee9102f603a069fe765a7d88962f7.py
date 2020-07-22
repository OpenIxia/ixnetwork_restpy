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


class MdLevel(Base):
    """This object holds the Maintenance Domain (MD) level configuration.
    The MdLevel class encapsulates a list of mdLevel resources that are managed by the user.
    A list of resources can be retrieved from the server using the MdLevel.find() method.
    The list can be managed by using the MdLevel.add() and MdLevel.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'mdLevel'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'MdLevelId': 'mdLevelId',
        'MdName': 'mdName',
        'MdNameFormat': 'mdNameFormat',
    }

    def __init__(self, parent):
        super(MdLevel, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the MD levels are enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def MdLevelId(self):
        """
        Returns
        -------
        - number: Sets the MD level identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdLevelId'])
    @MdLevelId.setter
    def MdLevelId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MdLevelId'], value)

    @property
    def MdName(self):
        """
        Returns
        -------
        - str: Sets the MD name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdName'])
    @MdName.setter
    def MdName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MdName'], value)

    @property
    def MdNameFormat(self):
        """
        Returns
        -------
        - str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString): Sets the MD Name format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdNameFormat'])
    @MdNameFormat.setter
    def MdNameFormat(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MdNameFormat'], value)

    def update(self, Enabled=None, MdLevelId=None, MdName=None, MdNameFormat=None):
        """Updates mdLevel resource on the server.

        Args
        ----
        - Enabled (bool): If true, the MD levels are enabled.
        - MdLevelId (number): Sets the MD level identifier.
        - MdName (str): Sets the MD name.
        - MdNameFormat (str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString)): Sets the MD Name format.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, MdLevelId=None, MdName=None, MdNameFormat=None):
        """Adds a new mdLevel resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, the MD levels are enabled.
        - MdLevelId (number): Sets the MD level identifier.
        - MdName (str): Sets the MD name.
        - MdNameFormat (str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString)): Sets the MD Name format.

        Returns
        -------
        - self: This instance with all currently retrieved mdLevel resources using find and the newly added mdLevel resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained mdLevel resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, MdLevelId=None, MdName=None, MdNameFormat=None):
        """Finds and retrieves mdLevel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve mdLevel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all mdLevel resources from the server.

        Args
        ----
        - Enabled (bool): If true, the MD levels are enabled.
        - MdLevelId (number): Sets the MD level identifier.
        - MdName (str): Sets the MD name.
        - MdNameFormat (str(noDomainName | domainNameBasedString | macAddress2OctetInteger | characterString)): Sets the MD Name format.

        Returns
        -------
        - self: This instance with matching mdLevel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of mdLevel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the mdLevel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
