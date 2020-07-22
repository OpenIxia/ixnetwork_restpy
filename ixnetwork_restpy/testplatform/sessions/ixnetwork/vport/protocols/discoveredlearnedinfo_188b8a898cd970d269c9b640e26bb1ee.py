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


class DiscoveredLearnedInfo(Base):
    """
    The DiscoveredLearnedInfo class encapsulates a list of discoveredLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the DiscoveredLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'discoveredLearnedInfo'
    _SDM_ATT_MAP = {
        'LocalDiscoveryStatus': 'localDiscoveryStatus',
        'LocalEvaluating': 'localEvaluating',
        'LocalMuxAction': 'localMuxAction',
        'LocalParserAction': 'localParserAction',
        'LocalRevision': 'localRevision',
        'LocalStable': 'localStable',
        'RemoteCriticalEvent': 'remoteCriticalEvent',
        'RemoteDyingGasp': 'remoteDyingGasp',
        'RemoteEvaluating': 'remoteEvaluating',
        'RemoteHeaderRefreshed': 'remoteHeaderRefreshed',
        'RemoteLinkEvent': 'remoteLinkEvent',
        'RemoteLinkFault': 'remoteLinkFault',
        'RemoteLoopbackSupport': 'remoteLoopbackSupport',
        'RemoteMacAddress': 'remoteMacAddress',
        'RemoteMaxPduSize': 'remoteMaxPduSize',
        'RemoteMode': 'remoteMode',
        'RemoteMuxAction': 'remoteMuxAction',
        'RemoteOamVersion': 'remoteOamVersion',
        'RemoteOui': 'remoteOui',
        'RemoteParserAction': 'remoteParserAction',
        'RemoteRevision': 'remoteRevision',
        'RemoteStable': 'remoteStable',
        'RemoteTlvRefreshed': 'remoteTlvRefreshed',
        'RemoteUnidirectionalSupport': 'remoteUnidirectionalSupport',
        'RemoteVariableRetrieval': 'remoteVariableRetrieval',
        'RemoteVendorSpecificInfo': 'remoteVendorSpecificInfo',
    }

    def __init__(self, parent):
        super(DiscoveredLearnedInfo, self).__init__(parent)

    @property
    def LocalDiscoveryStatus(self):
        """
        Returns
        -------
        - str(fault | activeSendLocal | passiveWait | sendLocalRemote | sendLocalRemoteOk | sendAny): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalDiscoveryStatus'])

    @property
    def LocalEvaluating(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalEvaluating'])

    @property
    def LocalMuxAction(self):
        """
        Returns
        -------
        - str(fwd | discard): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalMuxAction'])

    @property
    def LocalParserAction(self):
        """
        Returns
        -------
        - str(fwd | lb | discard): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalParserAction'])

    @property
    def LocalRevision(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalRevision'])

    @property
    def LocalStable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalStable'])

    @property
    def RemoteCriticalEvent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteCriticalEvent'])

    @property
    def RemoteDyingGasp(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteDyingGasp'])

    @property
    def RemoteEvaluating(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteEvaluating'])

    @property
    def RemoteHeaderRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteHeaderRefreshed'])

    @property
    def RemoteLinkEvent(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteLinkEvent'])

    @property
    def RemoteLinkFault(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteLinkFault'])

    @property
    def RemoteLoopbackSupport(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteLoopbackSupport'])

    @property
    def RemoteMacAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMacAddress'])

    @property
    def RemoteMaxPduSize(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMaxPduSize'])

    @property
    def RemoteMode(self):
        """
        Returns
        -------
        - str(active | passive): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMode'])

    @property
    def RemoteMuxAction(self):
        """
        Returns
        -------
        - str(fwd | discard): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMuxAction'])

    @property
    def RemoteOamVersion(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteOamVersion'])

    @property
    def RemoteOui(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteOui'])

    @property
    def RemoteParserAction(self):
        """
        Returns
        -------
        - str(fwd | lb | discard): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteParserAction'])

    @property
    def RemoteRevision(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteRevision'])

    @property
    def RemoteStable(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteStable'])

    @property
    def RemoteTlvRefreshed(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteTlvRefreshed'])

    @property
    def RemoteUnidirectionalSupport(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteUnidirectionalSupport'])

    @property
    def RemoteVariableRetrieval(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteVariableRetrieval'])

    @property
    def RemoteVendorSpecificInfo(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteVendorSpecificInfo'])

    def find(self, LocalDiscoveryStatus=None, LocalEvaluating=None, LocalMuxAction=None, LocalParserAction=None, LocalRevision=None, LocalStable=None, RemoteCriticalEvent=None, RemoteDyingGasp=None, RemoteEvaluating=None, RemoteHeaderRefreshed=None, RemoteLinkEvent=None, RemoteLinkFault=None, RemoteLoopbackSupport=None, RemoteMacAddress=None, RemoteMaxPduSize=None, RemoteMode=None, RemoteMuxAction=None, RemoteOamVersion=None, RemoteOui=None, RemoteParserAction=None, RemoteRevision=None, RemoteStable=None, RemoteTlvRefreshed=None, RemoteUnidirectionalSupport=None, RemoteVariableRetrieval=None, RemoteVendorSpecificInfo=None):
        """Finds and retrieves discoveredLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve discoveredLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all discoveredLearnedInfo resources from the server.

        Args
        ----
        - LocalDiscoveryStatus (str(fault | activeSendLocal | passiveWait | sendLocalRemote | sendLocalRemoteOk | sendAny)): 
        - LocalEvaluating (bool): 
        - LocalMuxAction (str(fwd | discard)): 
        - LocalParserAction (str(fwd | lb | discard)): 
        - LocalRevision (number): 
        - LocalStable (bool): 
        - RemoteCriticalEvent (bool): 
        - RemoteDyingGasp (bool): 
        - RemoteEvaluating (bool): 
        - RemoteHeaderRefreshed (bool): 
        - RemoteLinkEvent (bool): 
        - RemoteLinkFault (bool): 
        - RemoteLoopbackSupport (bool): 
        - RemoteMacAddress (str): 
        - RemoteMaxPduSize (number): 
        - RemoteMode (str(active | passive)): 
        - RemoteMuxAction (str(fwd | discard)): 
        - RemoteOamVersion (number): 
        - RemoteOui (str): 
        - RemoteParserAction (str(fwd | lb | discard)): 
        - RemoteRevision (number): 
        - RemoteStable (bool): 
        - RemoteTlvRefreshed (bool): 
        - RemoteUnidirectionalSupport (bool): 
        - RemoteVariableRetrieval (bool): 
        - RemoteVendorSpecificInfo (str): 

        Returns
        -------
        - self: This instance with matching discoveredLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of discoveredLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the discoveredLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
