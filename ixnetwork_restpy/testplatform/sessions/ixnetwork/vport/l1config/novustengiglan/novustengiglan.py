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
from typing import List, Any, Union


class NovusTenGigLan(Base):
    """Novus 10GE LAN Port
    The NovusTenGigLan class encapsulates a required novusTenGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'novusTenGigLan'
    _SDM_ATT_MAP = {
        'AutoInstrumentation': 'autoInstrumentation',
        'AutoNegotiate': 'autoNegotiate',
        'AvailableSpeeds': 'availableSpeeds',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'EnablePPM': 'enablePPM',
        'EnabledFlowControl': 'enabledFlowControl',
        'FlowControlDirectedAddress': 'flowControlDirectedAddress',
        'Loopback': 'loopback',
        'LoopbackMode': 'loopbackMode',
        'MasterSlaveMode': 'masterSlaveMode',
        'Media': 'media',
        'NegotiateMasterSlave': 'negotiateMasterSlave',
        'Ppm': 'ppm',
        'SelectedSpeeds': 'selectedSpeeds',
        'Speed': 'speed',
        'SpeedAuto': 'speedAuto',
        'TxIgnoreRxLinkFaults': 'txIgnoreRxLinkFaults',
    }
    _SDM_ENUM_MAP = {
        'autoInstrumentation': ['endOfFrame', 'floating'],
        'loopbackMode': ['internalLoopback', 'lineLoopback', 'none'],
        'masterSlaveMode': ['master', 'slave'],
        'media': ['copper', 'fiber', 'sgmii'],
        'speed': ['speed1000', 'speed100fd', 'speed10g', 'speed2.5g', 'speed5g'],
    }

    def __init__(self, parent, list_op=False):
        super(NovusTenGigLan, self).__init__(parent, list_op)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.fcoe.fcoe import Fcoe
        if self._properties.get('Fcoe', None) is not None:
            return self._properties.get('Fcoe')
        else:
            return Fcoe(self)._select()

    @property
    def TxLane(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.txlane.txlane.TxLane): An instance of the TxLane class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.txlane.txlane import TxLane
        if self._properties.get('TxLane', None) is not None:
            return self._properties.get('TxLane')
        else:
            return TxLane(self)._select()

    @property
    def AutoInstrumentation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoInstrumentation'])
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['AutoInstrumentation'], value)

    @property
    def AutoNegotiate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, allows autonegotiation between ports for speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoNegotiate'])
    @AutoNegotiate.setter
    def AutoNegotiate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['AutoNegotiate'], value)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100fd | speed1000 | speed2.5g | speed5g | speed10g]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableSpeeds'])

    @property
    def CanModifySpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanModifySpeed'])

    @property
    def CanSetMultipleSpeeds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanSetMultipleSpeeds'])

    @property
    def EnablePPM(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])
    @EnablePPM.setter
    def EnablePPM(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnablePPM'], value)

    @property
    def EnabledFlowControl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the port's MAC flow control and mechanisms to listen for a directed address pause message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledFlowControl'])
    @EnabledFlowControl.setter
    def EnabledFlowControl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnabledFlowControl'], value)

    @property
    def FlowControlDirectedAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 48-bit MAC address that the port listens on for a directed pause.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowControlDirectedAddress'])
    @FlowControlDirectedAddress.setter
    def FlowControlDirectedAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowControlDirectedAddress'], value)

    @property
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def LoopbackMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(internalLoopback | lineLoopback | none): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopbackMode'])
    @LoopbackMode.setter
    def LoopbackMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['LoopbackMode'], value)

    @property
    def MasterSlaveMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(master | slave): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MasterSlaveMode'])
    @MasterSlaveMode.setter
    def MasterSlaveMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MasterSlaveMode'], value)

    @property
    def Media(self):
        # type: () -> str
        """
        Returns
        -------
        - str(copper | fiber | sgmii): Available only for cards that support this dual-PHY capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Media'])
    @Media.setter
    def Media(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Media'], value)

    @property
    def NegotiateMasterSlave(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['NegotiateMasterSlave'])
    @NegotiateMasterSlave.setter
    def NegotiateMasterSlave(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['NegotiateMasterSlave'], value)

    @property
    def Ppm(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ppm'])
    @Ppm.setter
    def Ppm(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['Ppm'], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100fd | speed1000 | speed2.5g | speed5g | speed10g]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectedSpeeds'])
    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['SelectedSpeeds'], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed1000 | speed100fd | speed10g | speed2.5g | speed5g): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Speed'])
    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Speed'], value)

    @property
    def SpeedAuto(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed1000 | speed100fd | speed10g | speed2.5g | speed5g]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SpeedAuto'])
    @SpeedAuto.setter
    def SpeedAuto(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['SpeedAuto'], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, will allow transmission of packets even if the receive link is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxIgnoreRxLinkFaults'])
    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['TxIgnoreRxLinkFaults'], value)

    def update(self, AutoInstrumentation=None, AutoNegotiate=None, EnablePPM=None, EnabledFlowControl=None, FlowControlDirectedAddress=None, Loopback=None, LoopbackMode=None, MasterSlaveMode=None, Media=None, NegotiateMasterSlave=None, Ppm=None, SelectedSpeeds=None, Speed=None, SpeedAuto=None, TxIgnoreRxLinkFaults=None):
        # type: (str, bool, bool, bool, str, bool, str, str, str, bool, int, List[str], str, List[str], bool) -> NovusTenGigLan
        """Updates novusTenGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiate (bool): If enabled, allows autonegotiation between ports for speed.
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control and mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(internalLoopback | lineLoopback | none)): NOT DEFINED
        - MasterSlaveMode (str(master | slave)): 
        - Media (str(copper | fiber | sgmii)): Available only for cards that support this dual-PHY capability.
        - NegotiateMasterSlave (bool): 
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[speed100fd | speed1000 | speed2.5g | speed5g | speed10g])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed1000 | speed100fd | speed10g | speed2.5g | speed5g)): NOT DEFINED
        - SpeedAuto (list(str[speed1000 | speed100fd | speed10g | speed2.5g | speed5g])): 
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
