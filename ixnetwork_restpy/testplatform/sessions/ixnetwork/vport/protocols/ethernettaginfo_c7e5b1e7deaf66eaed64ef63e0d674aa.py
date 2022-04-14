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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class EthernetTagInfo(Base):
    """(Read Only) List of ethernet tags for an EVI.
    The EthernetTagInfo class encapsulates a list of ethernetTagInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the EthernetTagInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "ethernetTagInfo"
    _SDM_ATT_MAP = {
        "EsiLabel": "esiLabel",
        "EthernetTag": "ethernetTag",
        "Labels": "labels",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(EthernetTagInfo, self).__init__(parent, list_op)

    @property
    def EsiLabel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) ESI label learned.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EsiLabel"])

    @property
    def EthernetTag(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) Ethernet Tag id in hex format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EthernetTag"])

    @property
    def Labels(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (Read Only) Per EVI/EthernetTag A-D label learned for an EVI or an Ethernet Tag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Labels"])

    def add(self):
        """Adds a new ethernetTagInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved ethernetTagInfo resources using find and the newly added ethernetTagInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, EsiLabel=None, EthernetTag=None, Labels=None):
        # type: (str, str, str) -> EthernetTagInfo
        """Finds and retrieves ethernetTagInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernetTagInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernetTagInfo resources from the server.

        Args
        ----
        - EsiLabel (str): (Read Only) ESI label learned.
        - EthernetTag (str): (Read Only) Ethernet Tag id in hex format.
        - Labels (str): (Read Only) Per EVI/EthernetTag A-D label learned for an EVI or an Ethernet Tag.

        Returns
        -------
        - self: This instance with matching ethernetTagInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernetTagInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernetTagInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
