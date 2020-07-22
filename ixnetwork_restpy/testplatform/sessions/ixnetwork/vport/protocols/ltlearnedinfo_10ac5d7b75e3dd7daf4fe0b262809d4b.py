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


class LtLearnedInfo(Base):
    """This object contains the link trace learned information.
    The LtLearnedInfo class encapsulates a list of ltLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LtLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ltLearnedInfo'
    _SDM_ATT_MAP = {
        'CVlan': 'cVlan',
        'DstMacAddress': 'dstMacAddress',
        'HopCount': 'hopCount',
        'Hops': 'hops',
        'MdLevel': 'mdLevel',
        'ReplyStatus': 'replyStatus',
        'SVlan': 'sVlan',
        'SrcMacAddress': 'srcMacAddress',
        'TransactionId': 'transactionId',
    }

    def __init__(self, parent):
        super(LtLearnedInfo, self).__init__(parent)

    @property
    def LtLearnedHop(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_57462a3f529f62632b3fd3cbe879b821.LtLearnedHop): An instance of the LtLearnedHop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.ltlearnedhop_57462a3f529f62632b3fd3cbe879b821 import LtLearnedHop
        return LtLearnedHop(self)

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: (read only) The stacked VLAN identifier for the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])

    @property
    def DstMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The destination MAC address associated with the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DstMacAddress'])

    @property
    def HopCount(self):
        """
        Returns
        -------
        - number: (read only) The hop count for the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HopCount'])

    @property
    def Hops(self):
        """
        Returns
        -------
        - str: (read only) The number of hops for the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Hops'])

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - number: (read only) The MD level associated with the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdLevel'])

    @property
    def ReplyStatus(self):
        """
        Returns
        -------
        - str: (read only) Indicates the status of the reply for the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReplyStatus'])

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: (read only) The single VLAN identifier associated with the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])

    @property
    def SrcMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The source MAC address associated with the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcMacAddress'])

    @property
    def TransactionId(self):
        """
        Returns
        -------
        - number: (read only) The transaction identifier sent with the link trace message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransactionId'])

    def find(self, CVlan=None, DstMacAddress=None, HopCount=None, Hops=None, MdLevel=None, ReplyStatus=None, SVlan=None, SrcMacAddress=None, TransactionId=None):
        """Finds and retrieves ltLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ltLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ltLearnedInfo resources from the server.

        Args
        ----
        - CVlan (str): (read only) The stacked VLAN identifier for the link trace message.
        - DstMacAddress (str): (read only) The destination MAC address associated with the link trace message.
        - HopCount (number): (read only) The hop count for the link trace message.
        - Hops (str): (read only) The number of hops for the link trace message.
        - MdLevel (number): (read only) The MD level associated with the link trace message.
        - ReplyStatus (str): (read only) Indicates the status of the reply for the link trace message.
        - SVlan (str): (read only) The single VLAN identifier associated with the link trace message.
        - SrcMacAddress (str): (read only) The source MAC address associated with the link trace message.
        - TransactionId (number): (read only) The transaction identifier sent with the link trace message.

        Returns
        -------
        - self: This instance with matching ltLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ltLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ltLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
