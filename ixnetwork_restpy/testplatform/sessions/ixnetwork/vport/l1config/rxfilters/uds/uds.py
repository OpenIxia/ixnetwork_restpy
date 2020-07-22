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


class Uds(Base):
    """A counter that increments each time the capture filter conditions are met, as defined in the Capture Filter window.
    The Uds class encapsulates a list of uds resources that are managed by the system.
    A list of resources can be retrieved from the server using the Uds.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'uds'
    _SDM_ATT_MAP = {
        'CustomFrameSizeFrom': 'customFrameSizeFrom',
        'CustomFrameSizeTo': 'customFrameSizeTo',
        'DestinationAddressSelector': 'destinationAddressSelector',
        'Error': 'error',
        'FrameSizeType': 'frameSizeType',
        'IsEnabled': 'isEnabled',
        'PatternSelector': 'patternSelector',
        'SourceAddressSelector': 'sourceAddressSelector',
    }

    def __init__(self, parent):
        super(Uds, self).__init__(parent)

    @property
    def CustomFrameSizeFrom(self):
        """
        Returns
        -------
        - number: Frame size customized from.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomFrameSizeFrom'])
    @CustomFrameSizeFrom.setter
    def CustomFrameSizeFrom(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomFrameSizeFrom'], value)

    @property
    def CustomFrameSizeTo(self):
        """
        Returns
        -------
        - number: Customized frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CustomFrameSizeTo'])
    @CustomFrameSizeTo.setter
    def CustomFrameSizeTo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CustomFrameSizeTo'], value)

    @property
    def DestinationAddressSelector(self):
        """
        Returns
        -------
        - str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2): Destination address selector.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DestinationAddressSelector'])
    @DestinationAddressSelector.setter
    def DestinationAddressSelector(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DestinationAddressSelector'], value)

    @property
    def Error(self):
        """
        Returns
        -------
        - str(errAnyFrame | errBadCRC | errBadFrame | errGoodFrame): Indicates error.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Error'])
    @Error.setter
    def Error(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Error'], value)

    @property
    def FrameSizeType(self):
        """
        Returns
        -------
        - str(any | custom | jumbo | oversized | undersized): The type of frame size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameSizeType'])
    @FrameSizeType.setter
    def FrameSizeType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameSizeType'], value)

    @property
    def IsEnabled(self):
        """
        Returns
        -------
        - bool: If true, UDS is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsEnabled'])
    @IsEnabled.setter
    def IsEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IsEnabled'], value)

    @property
    def PatternSelector(self):
        """
        Returns
        -------
        - str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern2): Pattern selector.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PatternSelector'])
    @PatternSelector.setter
    def PatternSelector(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PatternSelector'], value)

    @property
    def SourceAddressSelector(self):
        """
        Returns
        -------
        - str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2): Source address selector.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAddressSelector'])
    @SourceAddressSelector.setter
    def SourceAddressSelector(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceAddressSelector'], value)

    def update(self, CustomFrameSizeFrom=None, CustomFrameSizeTo=None, DestinationAddressSelector=None, Error=None, FrameSizeType=None, IsEnabled=None, PatternSelector=None, SourceAddressSelector=None):
        """Updates uds resource on the server.

        Args
        ----
        - CustomFrameSizeFrom (number): Frame size customized from.
        - CustomFrameSizeTo (number): Customized frame size.
        - DestinationAddressSelector (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): Destination address selector.
        - Error (str(errAnyFrame | errBadCRC | errBadFrame | errGoodFrame)): Indicates error.
        - FrameSizeType (str(any | custom | jumbo | oversized | undersized)): The type of frame size.
        - IsEnabled (bool): If true, UDS is enabled.
        - PatternSelector (str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern2)): Pattern selector.
        - SourceAddressSelector (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): Source address selector.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CustomFrameSizeFrom=None, CustomFrameSizeTo=None, DestinationAddressSelector=None, Error=None, FrameSizeType=None, IsEnabled=None, PatternSelector=None, SourceAddressSelector=None):
        """Finds and retrieves uds resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve uds resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all uds resources from the server.

        Args
        ----
        - CustomFrameSizeFrom (number): Frame size customized from.
        - CustomFrameSizeTo (number): Customized frame size.
        - DestinationAddressSelector (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): Destination address selector.
        - Error (str(errAnyFrame | errBadCRC | errBadFrame | errGoodFrame)): Indicates error.
        - FrameSizeType (str(any | custom | jumbo | oversized | undersized)): The type of frame size.
        - IsEnabled (bool): If true, UDS is enabled.
        - PatternSelector (str(anyPattern | notPattern1 | notPattern2 | pattern1 | pattern2)): Pattern selector.
        - SourceAddressSelector (str(addr1 | addr2 | anyAddr | notAddr1 | notAddr2)): Source address selector.

        Returns
        -------
        - self: This instance with matching uds resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of uds data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the uds resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
