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


class CertInfo(Base):
    """Certificate Options
    The CertInfo class encapsulates a required certInfo resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'certInfo'

    def __init__(self, parent):
        super(CertInfo, self).__init__(parent)

    @property
    def AltName(self):
        """Other Options - Alternative Subject Name

        Returns:
            str
        """
        return self._get_attribute('altName')
    @AltName.setter
    def AltName(self, value):
        self._set_attribute('altName', value)

    @property
    def CertFormat(self):
        """Required.

        Returns:
            str
        """
        return self._get_attribute('certFormat')
    @CertFormat.setter
    def CertFormat(self, value):
        self._set_attribute('certFormat', value)

    @property
    def CertPath(self):
        """The path to certificate files.

        Returns:
            str
        """
        return self._get_attribute('certPath')
    @CertPath.setter
    def CertPath(self, value):
        self._set_attribute('certPath', value)

    @property
    def City(self):
        """Identification Info - City

        Returns:
            str
        """
        return self._get_attribute('city')
    @City.setter
    def City(self, value):
        self._set_attribute('city', value)

    @property
    def Company(self):
        """Identification Info - Company

        Returns:
            str
        """
        return self._get_attribute('company')
    @Company.setter
    def Company(self, value):
        self._set_attribute('company', value)

    @property
    def Country(self):
        """Identification Info - Country

        Returns:
            str
        """
        return self._get_attribute('country')
    @Country.setter
    def Country(self, value):
        self._set_attribute('country', value)

    @property
    def Department(self):
        """Identification Info - Department

        Returns:
            str
        """
        return self._get_attribute('department')
    @Department.setter
    def Department(self, value):
        self._set_attribute('department', value)

    @property
    def GetCACertOnly(self):
        """Obtain only the CA certificate.

        Returns:
            bool
        """
        return self._get_attribute('getCACertOnly')
    @GetCACertOnly.setter
    def GetCACertOnly(self, value):
        self._set_attribute('getCACertOnly', value)

    @property
    def KeyPath(self):
        """The path to key files.

        Returns:
            str
        """
        return self._get_attribute('keyPath')
    @KeyPath.setter
    def KeyPath(self, value):
        self._set_attribute('keyPath', value)

    @property
    def KeySize(self):
        """Key Options - Key Size

        Returns:
            number
        """
        return self._get_attribute('keySize')
    @KeySize.setter
    def KeySize(self, value):
        self._set_attribute('keySize', value)

    @property
    def KeyUsage(self):
        """Key Options - Key Usage

        Returns:
            str
        """
        return self._get_attribute('keyUsage')
    @KeyUsage.setter
    def KeyUsage(self, value):
        self._set_attribute('keyUsage', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    @property
    def SameKeyFile(self):
        """Required.

        Returns:
            bool
        """
        return self._get_attribute('sameKeyFile')
    @SameKeyFile.setter
    def SameKeyFile(self, value):
        self._set_attribute('sameKeyFile', value)

    @property
    def SendCACertOnly(self):
        """Send only the CA certificate.

        Returns:
            bool
        """
        return self._get_attribute('sendCACertOnly')
    @SendCACertOnly.setter
    def SendCACertOnly(self, value):
        self._set_attribute('sendCACertOnly', value)

    @property
    def ServerUrl(self):
        """Cerficate Server URL

        Returns:
            str
        """
        return self._get_attribute('serverUrl')
    @ServerUrl.setter
    def ServerUrl(self, value):
        self._set_attribute('serverUrl', value)

    @property
    def State(self):
        """Identification Info - State

        Returns:
            str
        """
        return self._get_attribute('state')
    @State.setter
    def State(self, value):
        self._set_attribute('state', value)

    @property
    def UseCertServer(self):
        """This value is true if the certificates are obtained from a certificate server.

        Returns:
            bool
        """
        return self._get_attribute('useCertServer')
    @UseCertServer.setter
    def UseCertServer(self, value):
        self._set_attribute('useCertServer', value)

    def update(self, AltName=None, CertFormat=None, CertPath=None, City=None, Company=None, Country=None, Department=None, GetCACertOnly=None, KeyPath=None, KeySize=None, KeyUsage=None, SameKeyFile=None, SendCACertOnly=None, ServerUrl=None, State=None, UseCertServer=None):
        """Updates a child instance of certInfo on the server.

        Args:
            AltName (str): Other Options - Alternative Subject Name
            CertFormat (str): Required.
            CertPath (str): The path to certificate files.
            City (str): Identification Info - City
            Company (str): Identification Info - Company
            Country (str): Identification Info - Country
            Department (str): Identification Info - Department
            GetCACertOnly (bool): Obtain only the CA certificate.
            KeyPath (str): The path to key files.
            KeySize (number): Key Options - Key Size
            KeyUsage (str): Key Options - Key Usage
            SameKeyFile (bool): Required.
            SendCACertOnly (bool): Send only the CA certificate.
            ServerUrl (str): Cerficate Server URL
            State (str): Identification Info - State
            UseCertServer (bool): This value is true if the certificates are obtained from a certificate server.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
