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


class LearnedBsrInfo(Base):
    """The learnedBSRInfo object fetches and describes the learned BSR information for the bootstrap router.
    The LearnedBsrInfo class encapsulates a list of learnedBsrInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedBsrInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedBsrInfo'
    _SDM_ATT_MAP = {
        'BsrAddress': 'bsrAddress',
        'LastBsmSendRecv': 'lastBsmSendRecv',
        'OurBsrState': 'ourBsrState',
        'Priority': 'priority',
    }

    def __init__(self, parent):
        super(LearnedBsrInfo, self).__init__(parent)

    @property
    def BsrAddress(self):
        """
        Returns
        -------
        - str: The address of the elected bootstrap router that is sending periodic bootstrap messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BsrAddress'])

    @property
    def LastBsmSendRecv(self):
        """
        Returns
        -------
        - number: Indicates the elapsed time (in seconds) since last bootstrap message was received or sent.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastBsmSendRecv'])

    @property
    def OurBsrState(self):
        """
        Returns
        -------
        - str(candidate | elected | notStarted | pending): Indicates the state of the configured bootstrap router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OurBsrState'])

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: Priority of the elected bootstrap router as received in Bootstrap messages or configured priority.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])

    def find(self, BsrAddress=None, LastBsmSendRecv=None, OurBsrState=None, Priority=None):
        """Finds and retrieves learnedBsrInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedBsrInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedBsrInfo resources from the server.

        Args
        ----
        - BsrAddress (str): The address of the elected bootstrap router that is sending periodic bootstrap messages.
        - LastBsmSendRecv (number): Indicates the elapsed time (in seconds) since last bootstrap message was received or sent.
        - OurBsrState (str(candidate | elected | notStarted | pending)): Indicates the state of the configured bootstrap router.
        - Priority (number): Priority of the elected bootstrap router as received in Bootstrap messages or configured priority.

        Returns
        -------
        - self: This instance with matching learnedBsrInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedBsrInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedBsrInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
