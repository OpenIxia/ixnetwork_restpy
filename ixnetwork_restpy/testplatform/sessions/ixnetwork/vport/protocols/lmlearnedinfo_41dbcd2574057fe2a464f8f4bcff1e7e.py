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


class LmLearnedInfo(Base):
    """This object holds lists of the lm learned information.
    The LmLearnedInfo class encapsulates a list of lmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'lmLearnedInfo'

    def __init__(self, parent):
        super(LmLearnedInfo, self).__init__(parent)

    @property
    def IncomingLabelOuterInner(self):
        """
        Returns
        -------
        - str: This signifies the incoming label information.
        """
        return self._get_attribute('incomingLabelOuterInner')

    @property
    def LastLmResponseDutRx(self):
        """
        Returns
        -------
        - number: This signifies the value of the DUT Rx counter in the last LM Response received.
        """
        return self._get_attribute('lastLmResponseDutRx')

    @property
    def LastLmResponseDutTx(self):
        """
        Returns
        -------
        - number: This signifies the value of the DUT Tx counter in the last LM Response received.
        """
        return self._get_attribute('lastLmResponseDutTx')

    @property
    def LastLmResponseMyTx(self):
        """
        Returns
        -------
        - number: This signifies the value of the My Tx counter in the last LM Response received.
        """
        return self._get_attribute('lastLmResponseMyTx')

    @property
    def LmQueriesSent(self):
        """
        Returns
        -------
        - number: This signifies the number of LM queries sent.
        """
        return self._get_attribute('lmQueriesSent')

    @property
    def LmRemoteUsing64Bit(self):
        """
        Returns
        -------
        - bool: This specifies whether the remote end is using 64bit counter or not.
        """
        return self._get_attribute('lmRemoteUsing64Bit')

    @property
    def LmResponsesReceived(self):
        """
        Returns
        -------
        - number: This signifies the number of LM responses received.
        """
        return self._get_attribute('lmResponsesReceived')

    @property
    def OutgoingLabelOuterInner(self):
        """
        Returns
        -------
        - str: This signifies the Outgoing Label information.
        """
        return self._get_attribute('outgoingLabelOuterInner')

    @property
    def Type(self):
        """
        Returns
        -------
        - str: This signifies the Selection of this option to filter according to the following types LSP and PW.
        """
        return self._get_attribute('type')

    def find(self, IncomingLabelOuterInner=None, LastLmResponseDutRx=None, LastLmResponseDutTx=None, LastLmResponseMyTx=None, LmQueriesSent=None, LmRemoteUsing64Bit=None, LmResponsesReceived=None, OutgoingLabelOuterInner=None, Type=None):
        """Finds and retrieves lmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve lmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all lmLearnedInfo resources from the server.

        Args
        ----
        - IncomingLabelOuterInner (str): This signifies the incoming label information.
        - LastLmResponseDutRx (number): This signifies the value of the DUT Rx counter in the last LM Response received.
        - LastLmResponseDutTx (number): This signifies the value of the DUT Tx counter in the last LM Response received.
        - LastLmResponseMyTx (number): This signifies the value of the My Tx counter in the last LM Response received.
        - LmQueriesSent (number): This signifies the number of LM queries sent.
        - LmRemoteUsing64Bit (bool): This specifies whether the remote end is using 64bit counter or not.
        - LmResponsesReceived (number): This signifies the number of LM responses received.
        - OutgoingLabelOuterInner (str): This signifies the Outgoing Label information.
        - Type (str): This signifies the Selection of this option to filter according to the following types LSP and PW.

        Returns
        -------
        - self: This instance with matching lmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of lmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the lmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
