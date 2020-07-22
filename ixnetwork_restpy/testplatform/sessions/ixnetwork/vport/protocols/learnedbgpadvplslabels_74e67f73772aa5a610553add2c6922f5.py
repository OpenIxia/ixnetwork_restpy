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


class LearnedBgpAdVplsLabels(Base):
    """This objects dispalys the learned BGP AD VPLS Labels.
    The LearnedBgpAdVplsLabels class encapsulates a list of learnedBgpAdVplsLabels resources that are managed by the system.
    A list of resources can be retrieved from the server using the LearnedBgpAdVplsLabels.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'learnedBgpAdVplsLabels'
    _SDM_ATT_MAP = {
        'CBit': 'cBit',
        'GroupId': 'groupId',
        'Label': 'label',
        'LocalPwSubState': 'localPwSubState',
        'Mtu': 'mtu',
        'PeerAddress': 'peerAddress',
        'PwState': 'pwState',
        'RemotePwSubState': 'remotePwSubState',
        'SourceAii': 'sourceAii',
        'TargetAii': 'targetAii',
        'VplsId': 'vplsId',
    }

    def __init__(self, parent):
        super(LearnedBgpAdVplsLabels, self).__init__(parent)

    @property
    def CBit(self):
        """
        Returns
        -------
        - bool: (Read Only) The boolean value for c Bit.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CBit'])

    @property
    def GroupId(self):
        """
        Returns
        -------
        - number: (Read Only) The 4-byte unsigned number indicating the Group Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GroupId'])

    @property
    def Label(self):
        """
        Returns
        -------
        - number: (Read Only) The 4-byte unsigned number indicating the Label.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Label'])

    @property
    def LocalPwSubState(self):
        """
        Returns
        -------
        - number: (Read Only) The 4-byte unsigned number indicating the Local PW Sub State.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalPwSubState'])

    @property
    def Mtu(self):
        """
        Returns
        -------
        - number: (Read Only) The 2 byte value for the maximum Transmission Unit (MTU).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mtu'])

    @property
    def PeerAddress(self):
        """
        Returns
        -------
        - str: (Read Only) The Peer Address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PeerAddress'])

    @property
    def PwState(self):
        """
        Returns
        -------
        - bool: (Read Only) The boolean value for PW State.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PwState'])

    @property
    def RemotePwSubState(self):
        """
        Returns
        -------
        - number: (Read Only)The 4-byte unsigned number indicating the PE Sub State.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemotePwSubState'])

    @property
    def SourceAii(self):
        """
        Returns
        -------
        - number: (Read Only) The 4 byte unsigned number indicationg the Source AII.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceAii'])

    @property
    def TargetAii(self):
        """
        Returns
        -------
        - number: (Read Only) The 4 byte unsigned number indicationg the Target AII.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TargetAii'])

    @property
    def VplsId(self):
        """
        Returns
        -------
        - str: (Read Only) The VPLS ID indicated by an IP or AS.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VplsId'])

    def find(self, CBit=None, GroupId=None, Label=None, LocalPwSubState=None, Mtu=None, PeerAddress=None, PwState=None, RemotePwSubState=None, SourceAii=None, TargetAii=None, VplsId=None):
        """Finds and retrieves learnedBgpAdVplsLabels resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedBgpAdVplsLabels resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedBgpAdVplsLabels resources from the server.

        Args
        ----
        - CBit (bool): (Read Only) The boolean value for c Bit.
        - GroupId (number): (Read Only) The 4-byte unsigned number indicating the Group Id.
        - Label (number): (Read Only) The 4-byte unsigned number indicating the Label.
        - LocalPwSubState (number): (Read Only) The 4-byte unsigned number indicating the Local PW Sub State.
        - Mtu (number): (Read Only) The 2 byte value for the maximum Transmission Unit (MTU).
        - PeerAddress (str): (Read Only) The Peer Address.
        - PwState (bool): (Read Only) The boolean value for PW State.
        - RemotePwSubState (number): (Read Only)The 4-byte unsigned number indicating the PE Sub State.
        - SourceAii (number): (Read Only) The 4 byte unsigned number indicationg the Source AII.
        - TargetAii (number): (Read Only) The 4 byte unsigned number indicationg the Target AII.
        - VplsId (str): (Read Only) The VPLS ID indicated by an IP or AS.

        Returns
        -------
        - self: This instance with matching learnedBgpAdVplsLabels resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedBgpAdVplsLabels data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedBgpAdVplsLabels resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
