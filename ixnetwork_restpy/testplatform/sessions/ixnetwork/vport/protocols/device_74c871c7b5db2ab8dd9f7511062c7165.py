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


class Device(Base):
    """Indicates that the device is used to configure the protocol.
    The Device class encapsulates a list of device resources that are managed by the user.
    A list of resources can be retrieved from the server using the Device.find() method.
    The list can be managed by using the Device.add() and Device.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'device'
    _SDM_ATT_MAP = {
        'CaCertificateFile': 'caCertificateFile',
        'CertificateFile': 'certificateFile',
        'Description': 'description',
        'DeviceRole': 'deviceRole',
        'EnableVersion100': 'enableVersion100',
        'EnableVersion131': 'enableVersion131',
        'Enabled': 'enabled',
        'PrivateFile': 'privateFile',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(Device, self).__init__(parent)

    @property
    def Interface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_396a1eb75d29065157fb9b891b905216.Interface): An instance of the Interface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.interface_396a1eb75d29065157fb9b891b905216 import Interface
        return Interface(self)

    @property
    def CaCertificateFile(self):
        """
        Returns
        -------
        - str: Indicates the Trusted Root certificate file for the device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CaCertificateFile'])

    @property
    def CertificateFile(self):
        """
        Returns
        -------
        - str: Indicates the certificate file for the device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CertificateFile'])

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description of the device used to configure this protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def DeviceRole(self):
        """
        Returns
        -------
        - str(controller | switch): Indicates the device role of the OpenFlow device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DeviceRole'])
    @DeviceRole.setter
    def DeviceRole(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DeviceRole'], value)

    @property
    def EnableVersion100(self):
        """
        Returns
        -------
        - bool: Enables protocol version 1.0
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVersion100'])
    @EnableVersion100.setter
    def EnableVersion100(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVersion100'], value)

    @property
    def EnableVersion131(self):
        """
        Returns
        -------
        - bool: Enables protocol version 1.3
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVersion131'])
    @EnableVersion131.setter
    def EnableVersion131(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVersion131'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If set enables the open-flow device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def PrivateFile(self):
        """
        Returns
        -------
        - str: Indicates the private key file for the device.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrivateFile'])

    @property
    def Version(self):
        """DEPRECATED 
        Returns
        -------
        - str(1.0.0): Indicates the current version of the Openflow protocol implemented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Version'])
    @Version.setter
    def Version(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Version'], value)

    def update(self, Description=None, DeviceRole=None, EnableVersion100=None, EnableVersion131=None, Enabled=None, Version=None):
        """Updates device resource on the server.

        Args
        ----
        - Description (str): A description of the device used to configure this protocol.
        - DeviceRole (str(controller | switch)): Indicates the device role of the OpenFlow device.
        - EnableVersion100 (bool): Enables protocol version 1.0
        - EnableVersion131 (bool): Enables protocol version 1.3
        - Enabled (bool): If set enables the open-flow device.
        - Version (str(1.0.0)): Indicates the current version of the Openflow protocol implemented.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Description=None, DeviceRole=None, EnableVersion100=None, EnableVersion131=None, Enabled=None, Version=None):
        """Adds a new device resource on the server and adds it to the container.

        Args
        ----
        - Description (str): A description of the device used to configure this protocol.
        - DeviceRole (str(controller | switch)): Indicates the device role of the OpenFlow device.
        - EnableVersion100 (bool): Enables protocol version 1.0
        - EnableVersion131 (bool): Enables protocol version 1.3
        - Enabled (bool): If set enables the open-flow device.
        - Version (str(1.0.0)): Indicates the current version of the Openflow protocol implemented.

        Returns
        -------
        - self: This instance with all currently retrieved device resources using find and the newly added device resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained device resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CaCertificateFile=None, CertificateFile=None, Description=None, DeviceRole=None, EnableVersion100=None, EnableVersion131=None, Enabled=None, PrivateFile=None, Version=None):
        """Finds and retrieves device resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve device resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all device resources from the server.

        Args
        ----
        - CaCertificateFile (str): Indicates the Trusted Root certificate file for the device.
        - CertificateFile (str): Indicates the certificate file for the device.
        - Description (str): A description of the device used to configure this protocol.
        - DeviceRole (str(controller | switch)): Indicates the device role of the OpenFlow device.
        - EnableVersion100 (bool): Enables protocol version 1.0
        - EnableVersion131 (bool): Enables protocol version 1.3
        - Enabled (bool): If set enables the open-flow device.
        - PrivateFile (str): Indicates the private key file for the device.
        - Version (str(1.0.0)): Indicates the current version of the Openflow protocol implemented.

        Returns
        -------
        - self: This instance with matching device resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of device data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the device resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddTlsCertificates(self, *args, **kwargs):
        """Executes the addTlsCertificates operation on the server.

        Exec to add TLS certificates.

        addTlsCertificates(Arg2=href, Arg3=href, Arg4=href)number
        ---------------------------------------------------------
        - Arg2 (obj(ixnetwork_restpy.files.Files)): NOT DEFINED
        - Arg3 (obj(ixnetwork_restpy.files.Files)): NOT DEFINED
        - Arg4 (obj(ixnetwork_restpy.files.Files)): NOT DEFINED
        - Returns number: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addTlsCertificates', payload=payload, response_object=None)
