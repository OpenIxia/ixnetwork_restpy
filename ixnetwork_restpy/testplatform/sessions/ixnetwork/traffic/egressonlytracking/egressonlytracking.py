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


class EgressOnlyTracking(Base):
    """
    The EgressOnlyTracking class encapsulates a list of egressOnlyTracking resources that are managed by the user.
    A list of resources can be retrieved from the server using the EgressOnlyTracking.find() method.
    The list can be managed by using the EgressOnlyTracking.add() and EgressOnlyTracking.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'egressOnlyTracking'
    _SDM_ATT_MAP = {
        'Egress': 'egress',
        'Enabled': 'enabled',
        'Port': 'port',
        'SignatureLengthType': 'signatureLengthType',
        'SignatureMask': 'signatureMask',
        'SignatureOffset': 'signatureOffset',
        'SignatureValue': 'signatureValue',
    }

    def __init__(self, parent):
        super(EgressOnlyTracking, self).__init__(parent)

    @property
    def Egress(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:str)): Struct contains: egress offset and egress mask
        """
        return self._get_attribute(self._SDM_ATT_MAP['Egress'])
    @Egress.setter
    def Egress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Egress'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the egress only tracking for the given port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Port(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Port'])
    @Port.setter
    def Port(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Port'], value)

    @property
    def SignatureLengthType(self):
        """
        Returns
        -------
        - str(fourByte | twelveByte): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignatureLengthType'])
    @SignatureLengthType.setter
    def SignatureLengthType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SignatureLengthType'], value)

    @property
    def SignatureMask(self):
        """
        Returns
        -------
        - str: Signature maks to be placed inside the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignatureMask'])
    @SignatureMask.setter
    def SignatureMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SignatureMask'], value)

    @property
    def SignatureOffset(self):
        """
        Returns
        -------
        - number: Offset where the signature value will be placed in the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignatureOffset'])
    @SignatureOffset.setter
    def SignatureOffset(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SignatureOffset'], value)

    @property
    def SignatureValue(self):
        """
        Returns
        -------
        - str: Signature value to be placed inside the packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SignatureValue'])
    @SignatureValue.setter
    def SignatureValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SignatureValue'], value)

    def update(self, Egress=None, Enabled=None, Port=None, SignatureLengthType=None, SignatureMask=None, SignatureOffset=None, SignatureValue=None):
        """Updates egressOnlyTracking resource on the server.

        Args
        ----
        - Egress (list(dict(arg1:number,arg2:str))): Struct contains: egress offset and egress mask
        - Enabled (bool): Enables the egress only tracking for the given port.
        - Port (str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport)): 
        - SignatureLengthType (str(fourByte | twelveByte)): 
        - SignatureMask (str): Signature maks to be placed inside the packet.
        - SignatureOffset (number): Offset where the signature value will be placed in the packet.
        - SignatureValue (str): Signature value to be placed inside the packet.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Egress=None, Enabled=None, Port=None, SignatureLengthType=None, SignatureMask=None, SignatureOffset=None, SignatureValue=None):
        """Adds a new egressOnlyTracking resource on the server and adds it to the container.

        Args
        ----
        - Egress (list(dict(arg1:number,arg2:str))): Struct contains: egress offset and egress mask
        - Enabled (bool): Enables the egress only tracking for the given port.
        - Port (str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport)): 
        - SignatureLengthType (str(fourByte | twelveByte)): 
        - SignatureMask (str): Signature maks to be placed inside the packet.
        - SignatureOffset (number): Offset where the signature value will be placed in the packet.
        - SignatureValue (str): Signature value to be placed inside the packet.

        Returns
        -------
        - self: This instance with all currently retrieved egressOnlyTracking resources using find and the newly added egressOnlyTracking resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained egressOnlyTracking resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Egress=None, Enabled=None, Port=None, SignatureLengthType=None, SignatureMask=None, SignatureOffset=None, SignatureValue=None):
        """Finds and retrieves egressOnlyTracking resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve egressOnlyTracking resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all egressOnlyTracking resources from the server.

        Args
        ----
        - Egress (list(dict(arg1:number,arg2:str))): Struct contains: egress offset and egress mask
        - Enabled (bool): Enables the egress only tracking for the given port.
        - Port (str(None | /api/v1/sessions/1/ixnetwork/lag | /api/v1/sessions/1/ixnetwork/vport)): 
        - SignatureLengthType (str(fourByte | twelveByte)): 
        - SignatureMask (str): Signature maks to be placed inside the packet.
        - SignatureOffset (number): Offset where the signature value will be placed in the packet.
        - SignatureValue (str): Signature value to be placed inside the packet.

        Returns
        -------
        - self: This instance with matching egressOnlyTracking resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of egressOnlyTracking data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the egressOnlyTracking resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
