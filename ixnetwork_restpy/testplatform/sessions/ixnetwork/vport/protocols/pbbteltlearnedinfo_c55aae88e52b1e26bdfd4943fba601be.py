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


class PbbTeLtLearnedInfo(Base):
    """The pbbTeLtLearnedInfo object holds the PBB-TE link trace learned information.
    The PbbTeLtLearnedInfo class encapsulates a list of pbbTeLtLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PbbTeLtLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = "pbbTeLtLearnedInfo"
    _SDM_ATT_MAP = {
        "BVlan": "bVlan",
        "DstMacAddress": "dstMacAddress",
        "HopCount": "hopCount",
        "Hops": "hops",
        "MdLevel": "mdLevel",
        "ReplyStatus": "replyStatus",
        "SrcMacAddress": "srcMacAddress",
        "TransactionId": "transactionId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(PbbTeLtLearnedInfo, self).__init__(parent, list_op)

    @property
    def LtLearnedHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_ec35fa3d1715c9c0cad316ab904f4886.LtLearnedHop): An instance of the LtLearnedHop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_ec35fa3d1715c9c0cad316ab904f4886 import (
            LtLearnedHop,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LtLearnedHop", None) is not None:
                return self._properties.get("LtLearnedHop")
        return LtLearnedHop(self)

    @property
    def BVlan(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned B-VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlan"])

    @property
    def DstMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned destination MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DstMacAddress"])

    @property
    def HopCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned number of hops in the link.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HopCount"])

    @property
    def Hops(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned list of hops to reach the particular MEP (MAC address).
        """
        return self._get_attribute(self._SDM_ATT_MAP["Hops"])

    @property
    def MdLevel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned MD level for the periodic OAM.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel"])

    @property
    def ReplyStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned current reply status.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReplyStatus"])

    @property
    def SrcMacAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: (read only) The learned source MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SrcMacAddress"])

    @property
    def TransactionId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: (read only) The learned identifier sent with the LTM.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransactionId"])

    def add(self):
        """Adds a new pbbTeLtLearnedInfo resource on the json, only valid with batch add utility

        Returns
        -------
        - self: This instance with all currently retrieved pbbTeLtLearnedInfo resources using find and the newly added pbbTeLtLearnedInfo resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        BVlan=None,
        DstMacAddress=None,
        HopCount=None,
        Hops=None,
        MdLevel=None,
        ReplyStatus=None,
        SrcMacAddress=None,
        TransactionId=None,
    ):
        # type: (str, str, int, str, int, str, str, int) -> PbbTeLtLearnedInfo
        """Finds and retrieves pbbTeLtLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pbbTeLtLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pbbTeLtLearnedInfo resources from the server.

        Args
        ----
        - BVlan (str): (read only) The learned B-VLAN identifier.
        - DstMacAddress (str): (read only) The learned destination MAC address.
        - HopCount (number): (read only) The learned number of hops in the link.
        - Hops (str): (read only) The learned list of hops to reach the particular MEP (MAC address).
        - MdLevel (number): (read only) The learned MD level for the periodic OAM.
        - ReplyStatus (str): (read only) The learned current reply status.
        - SrcMacAddress (str): (read only) The learned source MAC address.
        - TransactionId (number): (read only) The learned identifier sent with the LTM.

        Returns
        -------
        - self: This instance with matching pbbTeLtLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pbbTeLtLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pbbTeLtLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
