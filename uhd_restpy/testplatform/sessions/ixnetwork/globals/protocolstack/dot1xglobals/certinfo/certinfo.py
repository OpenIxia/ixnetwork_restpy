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


class CertInfo(Base):
    """Certificate Options
    The CertInfo class encapsulates a required certInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'certInfo'
    _SDM_ATT_MAP = {
        'AltName': 'altName',
        'CertFormat': 'certFormat',
        'CertPath': 'certPath',
        'City': 'city',
        'Company': 'company',
        'Country': 'country',
        'Department': 'department',
        'GetCACertOnly': 'getCACertOnly',
        'KeyPath': 'keyPath',
        'KeySize': 'keySize',
        'KeyUsage': 'keyUsage',
        'ObjectId': 'objectId',
        'SameKeyFile': 'sameKeyFile',
        'SendCACertOnly': 'sendCACertOnly',
        'ServerUrl': 'serverUrl',
        'State': 'state',
        'UseCertServer': 'useCertServer',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(CertInfo, self).__init__(parent, list_op)

    @property
    def AltName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Other Options - Alternative Subject Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['AltName'])
    @AltName.setter
    def AltName(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AltName'], value)

    @property
    def CertFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CertFormat'])
    @CertFormat.setter
    def CertFormat(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CertFormat'], value)

    @property
    def CertPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The path to certificate files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CertPath'])
    @CertPath.setter
    def CertPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CertPath'], value)

    @property
    def City(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identification Info - City
        """
        return self._get_attribute(self._SDM_ATT_MAP['City'])
    @City.setter
    def City(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['City'], value)

    @property
    def Company(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identification Info - Company
        """
        return self._get_attribute(self._SDM_ATT_MAP['Company'])
    @Company.setter
    def Company(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Company'], value)

    @property
    def Country(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identification Info - Country
        """
        return self._get_attribute(self._SDM_ATT_MAP['Country'])
    @Country.setter
    def Country(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Country'], value)

    @property
    def Department(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identification Info - Department
        """
        return self._get_attribute(self._SDM_ATT_MAP['Department'])
    @Department.setter
    def Department(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Department'], value)

    @property
    def GetCACertOnly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Obtain only the CA certificate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GetCACertOnly'])
    @GetCACertOnly.setter
    def GetCACertOnly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['GetCACertOnly'], value)

    @property
    def KeyPath(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The path to key files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyPath'])
    @KeyPath.setter
    def KeyPath(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['KeyPath'], value)

    @property
    def KeySize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Key Options - Key Size
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeySize'])
    @KeySize.setter
    def KeySize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['KeySize'], value)

    @property
    def KeyUsage(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Key Options - Key Usage
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyUsage'])
    @KeyUsage.setter
    def KeyUsage(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['KeyUsage'], value)

    @property
    def ObjectId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SameKeyFile(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SameKeyFile'])
    @SameKeyFile.setter
    def SameKeyFile(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SameKeyFile'], value)

    @property
    def SendCACertOnly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Send only the CA certificate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendCACertOnly'])
    @SendCACertOnly.setter
    def SendCACertOnly(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['SendCACertOnly'], value)

    @property
    def ServerUrl(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Cerficate Server URL
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerUrl'])
    @ServerUrl.setter
    def ServerUrl(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ServerUrl'], value)

    @property
    def State(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Identification Info - State
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])
    @State.setter
    def State(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['State'], value)

    @property
    def UseCertServer(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: This value is true if the certificates are obtained from a certificate server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseCertServer'])
    @UseCertServer.setter
    def UseCertServer(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UseCertServer'], value)

    def update(self, AltName=None, CertFormat=None, CertPath=None, City=None, Company=None, Country=None, Department=None, GetCACertOnly=None, KeyPath=None, KeySize=None, KeyUsage=None, SameKeyFile=None, SendCACertOnly=None, ServerUrl=None, State=None, UseCertServer=None):
        # type: (str, str, str, str, str, str, str, bool, str, int, str, bool, bool, str, str, bool) -> CertInfo
        """Updates certInfo resource on the server.

        Args
        ----
        - AltName (str): Other Options - Alternative Subject Name
        - CertFormat (str): Required.
        - CertPath (str): The path to certificate files.
        - City (str): Identification Info - City
        - Company (str): Identification Info - Company
        - Country (str): Identification Info - Country
        - Department (str): Identification Info - Department
        - GetCACertOnly (bool): Obtain only the CA certificate.
        - KeyPath (str): The path to key files.
        - KeySize (number): Key Options - Key Size
        - KeyUsage (str): Key Options - Key Usage
        - SameKeyFile (bool): Required.
        - SendCACertOnly (bool): Send only the CA certificate.
        - ServerUrl (str): Cerficate Server URL
        - State (str): Identification Info - State
        - UseCertServer (bool): This value is true if the certificates are obtained from a certificate server.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AltName=None, CertFormat=None, CertPath=None, City=None, Company=None, Country=None, Department=None, GetCACertOnly=None, KeyPath=None, KeySize=None, KeyUsage=None, ObjectId=None, SameKeyFile=None, SendCACertOnly=None, ServerUrl=None, State=None, UseCertServer=None):
        # type: (str, str, str, str, str, str, str, bool, str, int, str, str, bool, bool, str, str, bool) -> CertInfo
        """Finds and retrieves certInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve certInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all certInfo resources from the server.

        Args
        ----
        - AltName (str): Other Options - Alternative Subject Name
        - CertFormat (str): Required.
        - CertPath (str): The path to certificate files.
        - City (str): Identification Info - City
        - Company (str): Identification Info - Company
        - Country (str): Identification Info - Country
        - Department (str): Identification Info - Department
        - GetCACertOnly (bool): Obtain only the CA certificate.
        - KeyPath (str): The path to key files.
        - KeySize (number): Key Options - Key Size
        - KeyUsage (str): Key Options - Key Usage
        - ObjectId (str): Unique identifier for this object
        - SameKeyFile (bool): Required.
        - SendCACertOnly (bool): Send only the CA certificate.
        - ServerUrl (str): Cerficate Server URL
        - State (str): Identification Info - State
        - UseCertServer (bool): This value is true if the certificates are obtained from a certificate server.

        Returns
        -------
        - self: This instance with matching certInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of certInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the certInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
