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


class PbbTeCcmLearnedInfo(Base):
    """This object contains the PBB-TE CCM learned information.
    The PbbTeCcmLearnedInfo class encapsulates a list of pbbTeCcmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PbbTeCcmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'pbbTeCcmLearnedInfo'
    _SDM_ATT_MAP = {
        'BVlan': 'bVlan',
        'CciInterval': 'cciInterval',
        'ErrCcmDefect': 'errCcmDefect',
        'ErrCcmDefectCount': 'errCcmDefectCount',
        'IfaceTlvDefectCount': 'ifaceTlvDefectCount',
        'MdLevel': 'mdLevel',
        'MdName': 'mdName',
        'MdNameFormat': 'mdNameFormat',
        'OutOfSequenceCcmCount': 'outOfSequenceCcmCount',
        'PortTlvDefectCount': 'portTlvDefectCount',
        'RdiRxCount': 'rdiRxCount',
        'RdiRxState': 'rdiRxState',
        'RdiTxCount': 'rdiTxCount',
        'RdiTxState': 'rdiTxState',
        'ReceivedIfaceTlvDefect': 'receivedIfaceTlvDefect',
        'ReceivedPortTlvDefect': 'receivedPortTlvDefect',
        'ReceivedRdi': 'receivedRdi',
        'RemoteMacAddress': 'remoteMacAddress',
        'RemoteMepDefectCount': 'remoteMepDefectCount',
        'RemoteMepId': 'remoteMepId',
        'RmepCcmDefect': 'rmepCcmDefect',
        'ShortMaName': 'shortMaName',
        'ShortMaNameFormat': 'shortMaNameFormat',
        'SrcMacAddress': 'srcMacAddress',
        'SrcMepId': 'srcMepId',
    }

    def __init__(self, parent):
        super(PbbTeCcmLearnedInfo, self).__init__(parent)

    @property
    def BVlan(self):
        """
        Returns
        -------
        - str: (read only) The VLAN identifier for the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlan'])

    @property
    def CciInterval(self):
        """
        Returns
        -------
        - str: (read only) The continuity check message interval, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CciInterval'])

    @property
    def ErrCcmDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, CCM defect errors have been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrCcmDefect'])

    @property
    def ErrCcmDefectCount(self):
        """
        Returns
        -------
        - number: (read only) The number of CCM defect errors received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrCcmDefectCount'])

    @property
    def IfaceTlvDefectCount(self):
        """
        Returns
        -------
        - number: (read only) The number of interface TLV defects received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IfaceTlvDefectCount'])

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - number: (read only) The MD level for the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdLevel'])

    @property
    def MdName(self):
        """
        Returns
        -------
        - str: (read only) The MD name for the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdName'])

    @property
    def MdNameFormat(self):
        """
        Returns
        -------
        - number: (read only) The MD name format for the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdNameFormat'])

    @property
    def OutOfSequenceCcmCount(self):
        """
        Returns
        -------
        - number: (read only) The number of out of sequence CCM messages received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutOfSequenceCcmCount'])

    @property
    def PortTlvDefectCount(self):
        """
        Returns
        -------
        - number: (read only) The number of port TLV defect errors received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortTlvDefectCount'])

    @property
    def RdiRxCount(self):
        """
        Returns
        -------
        - number: (read only) The rdi rx count.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RdiRxCount'])

    @property
    def RdiRxState(self):
        """
        Returns
        -------
        - str: (read only) The rdi rx state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RdiRxState'])

    @property
    def RdiTxCount(self):
        """
        Returns
        -------
        - number: (read only) The rdi tx count.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RdiTxCount'])

    @property
    def RdiTxState(self):
        """
        Returns
        -------
        - str: (read only) The rdi tx state.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RdiTxState'])

    @property
    def ReceivedIfaceTlvDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, interface TLV defect errors have been received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedIfaceTlvDefect'])

    @property
    def ReceivedPortTlvDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, port TLV defect errors have been received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPortTlvDefect'])

    @property
    def ReceivedRdi(self):
        """
        Returns
        -------
        - bool: (read only) If true, RDI defect error messages have been receved.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedRdi'])

    @property
    def RemoteMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The remote MAC address for the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMacAddress'])

    @property
    def RemoteMepDefectCount(self):
        """
        Returns
        -------
        - number: (read only) The number of RMEP defect errors received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMepDefectCount'])

    @property
    def RemoteMepId(self):
        """
        Returns
        -------
        - str: (read only) The RMEP identifier for the CCM.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMepId'])

    @property
    def RmepCcmDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, RMEP CCM defect errors have been received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RmepCcmDefect'])

    @property
    def ShortMaName(self):
        """
        Returns
        -------
        - str: (read only) The Short MA name for the CCM.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMaName'])

    @property
    def ShortMaNameFormat(self):
        """
        Returns
        -------
        - number: (read only) The Short MA name format for the CCM.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMaNameFormat'])

    @property
    def SrcMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The source MAC address for the CCM.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcMacAddress'])

    @property
    def SrcMepId(self):
        """
        Returns
        -------
        - number: (read only) The source MEP identifier for the CCM.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrcMepId'])

    def find(self, BVlan=None, CciInterval=None, ErrCcmDefect=None, ErrCcmDefectCount=None, IfaceTlvDefectCount=None, MdLevel=None, MdName=None, MdNameFormat=None, OutOfSequenceCcmCount=None, PortTlvDefectCount=None, RdiRxCount=None, RdiRxState=None, RdiTxCount=None, RdiTxState=None, ReceivedIfaceTlvDefect=None, ReceivedPortTlvDefect=None, ReceivedRdi=None, RemoteMacAddress=None, RemoteMepDefectCount=None, RemoteMepId=None, RmepCcmDefect=None, ShortMaName=None, ShortMaNameFormat=None, SrcMacAddress=None, SrcMepId=None):
        """Finds and retrieves pbbTeCcmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pbbTeCcmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pbbTeCcmLearnedInfo resources from the server.

        Args
        ----
        - BVlan (str): (read only) The VLAN identifier for the CCM message.
        - CciInterval (str): (read only) The continuity check message interval, in seconds.
        - ErrCcmDefect (bool): (read only) If true, CCM defect errors have been detected.
        - ErrCcmDefectCount (number): (read only) The number of CCM defect errors received.
        - IfaceTlvDefectCount (number): (read only) The number of interface TLV defects received.
        - MdLevel (number): (read only) The MD level for the CCM message.
        - MdName (str): (read only) The MD name for the CCM message.
        - MdNameFormat (number): (read only) The MD name format for the CCM message.
        - OutOfSequenceCcmCount (number): (read only) The number of out of sequence CCM messages received.
        - PortTlvDefectCount (number): (read only) The number of port TLV defect errors received.
        - RdiRxCount (number): (read only) The rdi rx count.
        - RdiRxState (str): (read only) The rdi rx state.
        - RdiTxCount (number): (read only) The rdi tx count.
        - RdiTxState (str): (read only) The rdi tx state.
        - ReceivedIfaceTlvDefect (bool): (read only) If true, interface TLV defect errors have been received.
        - ReceivedPortTlvDefect (bool): (read only) If true, port TLV defect errors have been received.
        - ReceivedRdi (bool): (read only) If true, RDI defect error messages have been receved.
        - RemoteMacAddress (str): (read only) The remote MAC address for the CCM message.
        - RemoteMepDefectCount (number): (read only) The number of RMEP defect errors received.
        - RemoteMepId (str): (read only) The RMEP identifier for the CCM.
        - RmepCcmDefect (bool): (read only) If true, RMEP CCM defect errors have been received.
        - ShortMaName (str): (read only) The Short MA name for the CCM.
        - ShortMaNameFormat (number): (read only) The Short MA name format for the CCM.
        - SrcMacAddress (str): (read only) The source MAC address for the CCM.
        - SrcMepId (number): (read only) The source MEP identifier for the CCM.

        Returns
        -------
        - self: This instance with matching pbbTeCcmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pbbTeCcmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pbbTeCcmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
