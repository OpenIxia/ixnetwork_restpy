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


class CcmLearnedInfo(Base):
    """This object contains the CMM learned information.
    The CcmLearnedInfo class encapsulates a list of ccmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the CcmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ccmLearnedInfo'
    _SDM_ATT_MAP = {
        'AllRmepDead': 'allRmepDead',
        'CVlan': 'cVlan',
        'CciInterval': 'cciInterval',
        'ErrCcmDefect': 'errCcmDefect',
        'ErrCcmDefectCount': 'errCcmDefectCount',
        'IfaceTlvDefectCount': 'ifaceTlvDefectCount',
        'MdLevel': 'mdLevel',
        'MdName': 'mdName',
        'MdNameFormat': 'mdNameFormat',
        'MepId': 'mepId',
        'MepMacAddress': 'mepMacAddress',
        'OutOfSequenceCcmCount': 'outOfSequenceCcmCount',
        'PortTlvDefectCount': 'portTlvDefectCount',
        'RdiRxCount': 'rdiRxCount',
        'RdiRxState': 'rdiRxState',
        'ReceivedAis': 'receivedAis',
        'ReceivedIfaceTlvDefect': 'receivedIfaceTlvDefect',
        'ReceivedPortTlvDefect': 'receivedPortTlvDefect',
        'ReceivedRdi': 'receivedRdi',
        'RemoteMepDefectCount': 'remoteMepDefectCount',
        'RmepCcmDefect': 'rmepCcmDefect',
        'SVlan': 'sVlan',
        'ShortMaName': 'shortMaName',
        'ShortMaNameFormat': 'shortMaNameFormat',
        'SomeRmepDefect': 'someRmepDefect',
    }

    def __init__(self, parent):
        super(CcmLearnedInfo, self).__init__(parent)

    @property
    def AllRmepDead(self):
        """
        Returns
        -------
        - bool: (read only) If true, indicates this MEP is receiving none of the remote MEPs' CCMs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllRmepDead'])

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: (read only) The stacked VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CVlan'])

    @property
    def CciInterval(self):
        """
        Returns
        -------
        - str: (read only) The Continuity Check interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CciInterval'])

    @property
    def ErrCcmDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, a CCM defect error has been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrCcmDefect'])

    @property
    def ErrCcmDefectCount(self):
        """
        Returns
        -------
        - number: The total number of CCM defect error that has been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ErrCcmDefectCount'])

    @property
    def IfaceTlvDefectCount(self):
        """
        Returns
        -------
        - number: The total number of iface Tlv defect error that has been detected.
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
        - str: (read only) The MD name associated with the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdName'])

    @property
    def MdNameFormat(self):
        """
        Returns
        -------
        - number: (read only) The MD Name Format of the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MdNameFormat'])

    @property
    def MepId(self):
        """
        Returns
        -------
        - number: (read only) The MEP identifier of the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MepId'])

    @property
    def MepMacAddress(self):
        """
        Returns
        -------
        - str: (read only) The MEP MAC address of the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MepMacAddress'])

    @property
    def OutOfSequenceCcmCount(self):
        """
        Returns
        -------
        - number: (read only) The number of Out of Sequence CCM messages received.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OutOfSequenceCcmCount'])

    @property
    def PortTlvDefectCount(self):
        """
        Returns
        -------
        - number: The total number of Port Tlv defect error that has been detected.
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
    def ReceivedAis(self):
        """
        Returns
        -------
        - bool: (read only) If true, AIS messages have been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedAis'])

    @property
    def ReceivedIfaceTlvDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, interface TLV defect messages have been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedIfaceTlvDefect'])

    @property
    def ReceivedPortTlvDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, port TLV defect messages have been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedPortTlvDefect'])

    @property
    def ReceivedRdi(self):
        """
        Returns
        -------
        - bool: (read only) If true, RDI messages have been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReceivedRdi'])

    @property
    def RemoteMepDefectCount(self):
        """
        Returns
        -------
        - number: The total number of remote Mep defect error that has been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteMepDefectCount'])

    @property
    def RmepCcmDefect(self):
        """
        Returns
        -------
        - bool: (read only) If true, remote MEP CCM defect messages have been detected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RmepCcmDefect'])

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: (read only) The single VLAN associated with the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SVlan'])

    @property
    def ShortMaName(self):
        """
        Returns
        -------
        - str: (read only) The Short MA Name associated with the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMaName'])

    @property
    def ShortMaNameFormat(self):
        """
        Returns
        -------
        - number: (read only) The Short MA Name format associated with the CCM message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ShortMaNameFormat'])

    @property
    def SomeRmepDefect(self):
        """
        Returns
        -------
        - bool: (read only) Indicates the aggregate state of the Remote MEP State Machines. If true, at least one of the Remote MEP State Machines is not receiving valid CCMs from its remote MEPs. If false, all Remote MEP State Machines are receiving valid CCMs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SomeRmepDefect'])

    def find(self, AllRmepDead=None, CVlan=None, CciInterval=None, ErrCcmDefect=None, ErrCcmDefectCount=None, IfaceTlvDefectCount=None, MdLevel=None, MdName=None, MdNameFormat=None, MepId=None, MepMacAddress=None, OutOfSequenceCcmCount=None, PortTlvDefectCount=None, RdiRxCount=None, RdiRxState=None, ReceivedAis=None, ReceivedIfaceTlvDefect=None, ReceivedPortTlvDefect=None, ReceivedRdi=None, RemoteMepDefectCount=None, RmepCcmDefect=None, SVlan=None, ShortMaName=None, ShortMaNameFormat=None, SomeRmepDefect=None):
        """Finds and retrieves ccmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ccmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ccmLearnedInfo resources from the server.

        Args
        ----
        - AllRmepDead (bool): (read only) If true, indicates this MEP is receiving none of the remote MEPs' CCMs.
        - CVlan (str): (read only) The stacked VLAN identifier.
        - CciInterval (str): (read only) The Continuity Check interval.
        - ErrCcmDefect (bool): (read only) If true, a CCM defect error has been detected.
        - ErrCcmDefectCount (number): The total number of CCM defect error that has been detected.
        - IfaceTlvDefectCount (number): The total number of iface Tlv defect error that has been detected.
        - MdLevel (number): (read only) The MD level for the CCM message.
        - MdName (str): (read only) The MD name associated with the CCM message.
        - MdNameFormat (number): (read only) The MD Name Format of the CCM message.
        - MepId (number): (read only) The MEP identifier of the CCM message.
        - MepMacAddress (str): (read only) The MEP MAC address of the CCM message.
        - OutOfSequenceCcmCount (number): (read only) The number of Out of Sequence CCM messages received.
        - PortTlvDefectCount (number): The total number of Port Tlv defect error that has been detected.
        - RdiRxCount (number): (read only) The rdi rx count.
        - RdiRxState (str): (read only) The rdi rx state.
        - ReceivedAis (bool): (read only) If true, AIS messages have been detected.
        - ReceivedIfaceTlvDefect (bool): (read only) If true, interface TLV defect messages have been detected.
        - ReceivedPortTlvDefect (bool): (read only) If true, port TLV defect messages have been detected.
        - ReceivedRdi (bool): (read only) If true, RDI messages have been detected.
        - RemoteMepDefectCount (number): The total number of remote Mep defect error that has been detected.
        - RmepCcmDefect (bool): (read only) If true, remote MEP CCM defect messages have been detected.
        - SVlan (str): (read only) The single VLAN associated with the CCM message.
        - ShortMaName (str): (read only) The Short MA Name associated with the CCM message.
        - ShortMaNameFormat (number): (read only) The Short MA Name format associated with the CCM message.
        - SomeRmepDefect (bool): (read only) Indicates the aggregate state of the Remote MEP State Machines. If true, at least one of the Remote MEP State Machines is not receiving valid CCMs from its remote MEPs. If false, all Remote MEP State Machines are receiving valid CCMs.

        Returns
        -------
        - self: This instance with matching ccmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ccmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ccmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
