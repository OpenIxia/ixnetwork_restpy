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


class CfmSlm(Base):
    """Synthetic Loss Measurement configuration for Emulated MEP
    The CfmSlm class encapsulates a required cfmSlm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'cfmSlm'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'SlmAutoTestId': 'slmAutoTestId',
        'SlmBurstCount': 'slmBurstCount',
        'SlmBurstGap': 'slmBurstGap',
        'SlmContinuousBurst': 'slmContinuousBurst',
        'SlmDestinationType': 'slmDestinationType',
        'SlmFlags': 'slmFlags',
        'SlmFrameSize': 'slmFrameSize',
        'SlmFrameTxCount': 'slmFrameTxCount',
        'SlmFramesPerBurst': 'slmFramesPerBurst',
        'SlmInitialTxfcf': 'slmInitialTxfcf',
        'SlmMode': 'slmMode',
        'SlmOverridePriority': 'slmOverridePriority',
        'SlmPriority': 'slmPriority',
        'SlmProactiveStart': 'slmProactiveStart',
        'SlmSimulatedLossInTx': 'slmSimulatedLossInTx',
        'SlmStateInfo': 'slmStateInfo',
        'SlmTestId': 'slmTestId',
        'SlmTestIdInfo': 'slmTestIdInfo',
        'SlmTxFCfInfo': 'slmTxFCfInfo',
        'SlmUnicastMac': 'slmUnicastMac',
    }

    def __init__(self, parent):
        super(CfmSlm, self).__init__(parent)

    @property
    def StopSlmParams(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.stopslmparams_2117fd9e6d0ad885042f04f4604813e9.StopSlmParams): An instance of the StopSlmParams class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.stopslmparams_2117fd9e6d0ad885042f04f4604813e9 import StopSlmParams
        return StopSlmParams(self)._select()

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
    def SlmAutoTestId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Auto Generate SLM Test ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmAutoTestId']))

    @property
    def SlmBurstCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Bursts.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmBurstCount']))

    @property
    def SlmBurstGap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time Gap between bursts in miliseconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmBurstGap']))

    @property
    def SlmContinuousBurst(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, will send continous bursts.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmContinuousBurst']))

    @property
    def SlmDestinationType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Multicast/All Remote MEP/Unicast. Multicast will send SLM to class 1 multicast address, All Remote MEP option will send unicast SLM to individual Remote MEPs, Unicast option will send SLM to configured unicast MAC.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmDestinationType']))

    @property
    def SlmFlags(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Flags values to be sent in SLM PDU. Default 0.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmFlags']))

    @property
    def SlmFrameSize(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SLM Frame Size.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmFrameSize']))

    @property
    def SlmFrameTxCount(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SLM Frame Tx Count.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmFrameTxCount']))

    @property
    def SlmFramesPerBurst(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of Frames Per Burst.Default Value: 1, represent periodic transmission.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmFramesPerBurst']))

    @property
    def SlmInitialTxfcf(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 4-octet field which contains the initial value of the local counter TxFCl for SLM frames.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmInitialTxfcf']))

    @property
    def SlmMode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mode
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmMode']))

    @property
    def SlmOverridePriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, it overrides MEP VLAN priority in SLM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmOverridePriority']))

    @property
    def SlmPriority(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VLAN priority in SLM PDU.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmPriority']))

    @property
    def SlmProactiveStart(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If enabled, MEP will Start sending SLM at startup.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmProactiveStart']))

    @property
    def SlmSimulatedLossInTx(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Percentage loss simulation in SLM Tx side.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmSimulatedLossInTx']))

    @property
    def SlmStateInfo(self):
        """
        Returns
        -------
        - list(str[expired | none | notStarted | running | stopped]): Displays the current SLM State. Valid states are Running, Stopped, Expired and Not Started.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlmStateInfo'])

    @property
    def SlmTestId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configurable, Non-negative integer value. Minimum Value: 1, Maximum Value: 4294967296, Default Value: 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmTestId']))

    @property
    def SlmTestIdInfo(self):
        """
        Returns
        -------
        - list(number): Displays SLM Test ID Information.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlmTestIdInfo'])

    @property
    def SlmTxFCfInfo(self):
        """
        Returns
        -------
        - list(number): Displays SLM Last TxFCf.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SlmTxFCfInfo'])

    @property
    def SlmUnicastMac(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Unicast MAC destination address.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SlmUnicastMac']))

    def update(self, Name=None):
        """Updates cfmSlm resource on the server.

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

    def get_device_ids(self, PortNames=None, SlmAutoTestId=None, SlmBurstCount=None, SlmBurstGap=None, SlmContinuousBurst=None, SlmDestinationType=None, SlmFlags=None, SlmFrameSize=None, SlmFrameTxCount=None, SlmFramesPerBurst=None, SlmInitialTxfcf=None, SlmMode=None, SlmOverridePriority=None, SlmPriority=None, SlmProactiveStart=None, SlmSimulatedLossInTx=None, SlmTestId=None, SlmUnicastMac=None):
        """Base class infrastructure that gets a list of cfmSlm device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - SlmAutoTestId (str): optional regex of slmAutoTestId
        - SlmBurstCount (str): optional regex of slmBurstCount
        - SlmBurstGap (str): optional regex of slmBurstGap
        - SlmContinuousBurst (str): optional regex of slmContinuousBurst
        - SlmDestinationType (str): optional regex of slmDestinationType
        - SlmFlags (str): optional regex of slmFlags
        - SlmFrameSize (str): optional regex of slmFrameSize
        - SlmFrameTxCount (str): optional regex of slmFrameTxCount
        - SlmFramesPerBurst (str): optional regex of slmFramesPerBurst
        - SlmInitialTxfcf (str): optional regex of slmInitialTxfcf
        - SlmMode (str): optional regex of slmMode
        - SlmOverridePriority (str): optional regex of slmOverridePriority
        - SlmPriority (str): optional regex of slmPriority
        - SlmProactiveStart (str): optional regex of slmProactiveStart
        - SlmSimulatedLossInTx (str): optional regex of slmSimulatedLossInTx
        - SlmTestId (str): optional regex of slmTestId
        - SlmUnicastMac (str): optional regex of slmUnicastMac

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
