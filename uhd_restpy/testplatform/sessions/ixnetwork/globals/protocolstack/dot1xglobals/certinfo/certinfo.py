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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


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

    def __init__(self, parent):
        super(CertInfo, self).__init__(parent)

    @property
    def AltName(self):
        """
        Returns
        -------
        - str: Other Options - Alternative Subject Name
        """
        return self._get_attribute(self._SDM_ATT_MAP['AltName'])
    @AltName.setter
    def AltName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AltName'], value)

    @property
    def CertFormat(self):
        """
        Returns
        -------
        - str: Required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CertFormat'])
    @CertFormat.setter
    def CertFormat(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CertFormat'], value)

    @property
    def CertPath(self):
        """
        Returns
        -------
        - str: The path to certificate files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CertPath'])
    @CertPath.setter
    def CertPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CertPath'], value)

    @property
    def City(self):
        """
        Returns
        -------
        - str: Identification Info - City
        """
        return self._get_attribute(self._SDM_ATT_MAP['City'])
    @City.setter
    def City(self, value):
        self._set_attribute(self._SDM_ATT_MAP['City'], value)

    @property
    def Company(self):
        """
        Returns
        -------
        - str: Identification Info - Company
        """
        return self._get_attribute(self._SDM_ATT_MAP['Company'])
    @Company.setter
    def Company(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Company'], value)

    @property
    def Country(self):
        """
        Returns
        -------
        - str: Identification Info - Country
        """
        return self._get_attribute(self._SDM_ATT_MAP['Country'])
    @Country.setter
    def Country(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Country'], value)

    @property
    def Department(self):
        """
        Returns
        -------
        - str: Identification Info - Department
        """
        return self._get_attribute(self._SDM_ATT_MAP['Department'])
    @Department.setter
    def Department(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Department'], value)

    @property
    def GetCACertOnly(self):
        """
        Returns
        -------
        - bool: Obtain only the CA certificate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GetCACertOnly'])
    @GetCACertOnly.setter
    def GetCACertOnly(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GetCACertOnly'], value)

    @property
    def KeyPath(self):
        """
        Returns
        -------
        - str: The path to key files.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyPath'])
    @KeyPath.setter
    def KeyPath(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeyPath'], value)

    @property
    def KeySize(self):
        """
        Returns
        -------
        - number: Key Options - Key Size
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeySize'])
    @KeySize.setter
    def KeySize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeySize'], value)

    @property
    def KeyUsage(self):
        """
        Returns
        -------
        - str: Key Options - Key Usage
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyUsage'])
    @KeyUsage.setter
    def KeyUsage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['KeyUsage'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def SameKeyFile(self):
        """
        Returns
        -------
        - bool: Required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SameKeyFile'])
    @SameKeyFile.setter
    def SameKeyFile(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SameKeyFile'], value)

    @property
    def SendCACertOnly(self):
        """
        Returns
        -------
        - bool: Send only the CA certificate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendCACertOnly'])
    @SendCACertOnly.setter
    def SendCACertOnly(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendCACertOnly'], value)

    @property
    def ServerUrl(self):
        """
        Returns
        -------
        - str: Cerficate Server URL
        """
        return self._get_attribute(self._SDM_ATT_MAP['ServerUrl'])
    @ServerUrl.setter
    def ServerUrl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ServerUrl'], value)

    @property
    def State(self):
        """
        Returns
        -------
        - str: Identification Info - State
        """
        return self._get_attribute(self._SDM_ATT_MAP['State'])
    @State.setter
    def State(self, value):
        self._set_attribute(self._SDM_ATT_MAP['State'], value)

    @property
    def UseCertServer(self):
        """
        Returns
        -------
        - bool: This value is true if the certificates are obtained from a certificate server.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseCertServer'])
    @UseCertServer.setter
    def UseCertServer(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseCertServer'], value)

    def update(self, AltName=None, CertFormat=None, CertPath=None, City=None, Company=None, Country=None, Department=None, GetCACertOnly=None, KeyPath=None, KeySize=None, KeyUsage=None, SameKeyFile=None, SendCACertOnly=None, ServerUrl=None, State=None, UseCertServer=None):
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
