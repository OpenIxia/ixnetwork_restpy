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


class DefaultTlv(Base):
    """Default Tlv container created by protocols
    The DefaultTlv class encapsulates a list of defaultTlv resources that are managed by the system.
    A list of resources can be retrieved from the server using the DefaultTlv.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'defaultTlv'
    _SDM_ATT_MAP = {
        'AvailableIncludeInMessages': 'availableIncludeInMessages',
        'Description': 'description',
        'EnablePerSession': 'enablePerSession',
        'IncludeInMessages': 'includeInMessages',
        'IsEnabled': 'isEnabled',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(DefaultTlv, self).__init__(parent)

    @property
    def Value(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.value_ac1d7b13584a86b9cf1c28dca3390bca.Value): An instance of the Value class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.tlvprofile.value_ac1d7b13584a86b9cf1c28dca3390bca import Value
        return Value(self)._select()

    @property
    def AvailableIncludeInMessages(self):
        """
        Returns
        -------
        - list(str): A list of available messages which are used in the includeInMessages attribute
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableIncludeInMessages'])

    @property
    def Description(self):
        """
        Returns
        -------
        - str: Description of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def EnablePerSession(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enable TLV per session
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EnablePerSession']))

    @property
    def IncludeInMessages(self):
        """
        Returns
        -------
        - list(str): Include the TLV in these protocol messages
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInMessages'])
    @IncludeInMessages.setter
    def IncludeInMessages(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInMessages'], value)

    @property
    def IsEnabled(self):
        """
        Returns
        -------
        - bool: Enables/disables this tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEnabled'])
    @IsEnabled.setter
    def IsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEnabled'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of the tlv
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Description=None, IncludeInMessages=None, IsEnabled=None, Name=None):
        """Updates defaultTlv resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Description (str): Description of the tlv
        - IncludeInMessages (list(str)): Include the TLV in these protocol messages
        - IsEnabled (bool): Enables/disables this tlv
        - Name (str): Name of the tlv

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, AvailableIncludeInMessages=None, Description=None, IncludeInMessages=None, IsEnabled=None, Name=None):
        """Finds and retrieves defaultTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve defaultTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all defaultTlv resources from the server.

        Args
        ----
        - AvailableIncludeInMessages (list(str)): A list of available messages which are used in the includeInMessages attribute
        - Description (str): Description of the tlv
        - IncludeInMessages (list(str)): Include the TLV in these protocol messages
        - IsEnabled (bool): Enables/disables this tlv
        - Name (str): Name of the tlv

        Returns
        -------
        - self: This instance with matching defaultTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of defaultTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the defaultTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, EnablePerSession=None):
        """Base class infrastructure that gets a list of defaultTlv device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - EnablePerSession (str): optional regex of enablePerSession

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
