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


class Macsec(Base):
    """MACsec Port Specific Data
    The Macsec class encapsulates a required macsec resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'macsec'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'KeyGenerationMode': 'keyGenerationMode',
        'MacsecValidation': 'macsecValidation',
        'MaxCaCount': 'maxCaCount',
        'MaxDevicePerCa': 'maxDevicePerCa',
        'MaxDutTxScPerCa': 'maxDutTxScPerCa',
        'Name': 'name',
        'ReplayProtection': 'replayProtection',
        'RowNames': 'rowNames',
        'RxScIdentifyingField': 'rxScIdentifyingField',
        'RxScIdentifyingFieldLengthInBytes': 'rxScIdentifyingFieldLengthInBytes',
        'RxScIdentifyingFieldOffset': 'rxScIdentifyingFieldOffset',
        'RxSecTagOffset': 'rxSecTagOffset',
        'SecTagOffsetUnknown': 'secTagOffsetUnknown',
        'TypeOfCa': 'typeOfCa',
    }

    def __init__(self, parent):
        super(Macsec, self).__init__(parent)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        return StopRate(self)._select()

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def KeyGenerationMode(self):
        """
        Returns
        -------
        - str(staticKeyGenerationMode | dynamicKeyGenerationMode): Determines whether the encryption keys will be informed by MKA or configured statically in MACsec.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyGenerationMode'])

    @property
    def MacsecValidation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the secure frame validation behavior set on the receiving port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacsecValidation']))

    @property
    def MaxCaCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the maximum number of CAs configured on the port. The maximum count supported per port is 256 for Pair-wise CA, each CA having one MACsec device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxCaCount']))

    @property
    def MaxDevicePerCa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the maximum number of Keysight MACsec devices that can be supported on each CA. This number is calculated automatically based on the values configured for 'Max CA Count', 'Max DUT Tx SC Per CA'. Number of Keysight MACsec devices should be configured accordingly.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxDevicePerCa']))

    @property
    def MaxDutTxScPerCa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the maximum number of DUT transmit SC that can be supported per CA. The count should be number of Tx SC supported by the DUT per CA, multiplied by number of DUTs in the CA (in case of 'Group CA - Multiple DUT' scenario)
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MaxDutTxScPerCa']))

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ReplayProtection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes Replay protection behavior of the port. Based on this option, out of window packets will either be discarded or passed to the upper layer control plane plugins and corresponding statistics will be incremented.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReplayProtection']))

    @property
    def RowNames(self):
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def RxScIdentifyingField(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes the field of a MACsec frame, using which the frame is mapped to a receive SC by the receiving Keysight MACsec device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxScIdentifyingField']))

    @property
    def RxScIdentifyingFieldLengthInBytes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This denotes the length in bytes of the Rx SC Identifying Field in macsec packets received from the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxScIdentifyingFieldLengthInBytes']))

    @property
    def RxScIdentifyingFieldOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This denotes the position of the Rx SC Identifying Field in macsec packets received from the DUT.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxScIdentifyingFieldOffset']))

    @property
    def RxSecTagOffset(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): This denotes the position of the SecTAG in macsec packets received from the DUT. The default offset is 12, but it may not be always 12 depending on different tunneling scenario.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxSecTagOffset']))

    @property
    def SecTagOffsetUnknown(self):
        """DEPRECATED 
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Denotes that the position of the SecTAG in MACsec packets received from the DUT is unknown. It is known by default, and only in some cases DUT may insert some outer headers due to which position of SecTAG will be moved.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecTagOffsetUnknown']))

    @property
    def TypeOfCa(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Type of CA configured on the port.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeOfCa']))

    def update(self, Name=None):
        """Updates macsec resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, MacsecValidation=None, MaxCaCount=None, MaxDevicePerCa=None, MaxDutTxScPerCa=None, ReplayProtection=None, RxScIdentifyingField=None, RxScIdentifyingFieldLengthInBytes=None, RxScIdentifyingFieldOffset=None, RxSecTagOffset=None, SecTagOffsetUnknown=None, TypeOfCa=None):
        """Base class infrastructure that gets a list of macsec device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - MacsecValidation (str): optional regex of macsecValidation
        - MaxCaCount (str): optional regex of maxCaCount
        - MaxDevicePerCa (str): optional regex of maxDevicePerCa
        - MaxDutTxScPerCa (str): optional regex of maxDutTxScPerCa
        - ReplayProtection (str): optional regex of replayProtection
        - RxScIdentifyingField (str): optional regex of rxScIdentifyingField
        - RxScIdentifyingFieldLengthInBytes (str): optional regex of rxScIdentifyingFieldLengthInBytes
        - RxScIdentifyingFieldOffset (str): optional regex of rxScIdentifyingFieldOffset
        - RxSecTagOffset (str): optional regex of rxSecTagOffset
        - SecTagOffsetUnknown (str): optional regex of secTagOffsetUnknown
        - TypeOfCa (str): optional regex of typeOfCa

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
