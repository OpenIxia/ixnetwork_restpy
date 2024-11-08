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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class NovusTenGigLan(Base):
    """Novus 10GE LAN Port
    The NovusTenGigLan class encapsulates a required novusTenGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "novusTenGigLan"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AutoNegotiate": "autoNegotiate",
        "AutoNegotiatePauseAdvertisement": "autoNegotiatePauseAdvertisement",
        "AvailableSpeeds": "availableSpeeds",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "EnableIntrinsicLatencyAdjustment": "enableIntrinsicLatencyAdjustment",
        "EnablePPM": "enablePPM",
        "EnabledFlowControl": "enabledFlowControl",
        "FlowControlDirectedAddress": "flowControlDirectedAddress",
        "Loopback": "loopback",
        "LoopbackMode": "loopbackMode",
        "MasterSlaveMode": "masterSlaveMode",
        "Media": "media",
        "NegotiateMasterSlave": "negotiateMasterSlave",
        "NegotiatePrimarySecondary": "negotiatePrimarySecondary",
        "Ppm": "ppm",
        "PrimarySecondaryMode": "primarySecondaryMode",
        "RxExtraIntrinsicLatency": "rxExtraIntrinsicLatency",
        "SelectedSpeeds": "selectedSpeeds",
        "Speed": "speed",
        "SpeedAuto": "speedAuto",
        "TxExtraIntrinsicLatency": "txExtraIntrinsicLatency",
        "TxIgnoreRxLinkFaults": "txIgnoreRxLinkFaults",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "autoNegotiatePauseAdvertisement": ["none", "both", "asymmetric", "fullDuplex"],
        "loopbackMode": ["none", "lineLoopback", "internalLoopback"],
        "masterSlaveMode": ["master", "slave"],
        "media": ["copper", "fiber", "sgmii"],
        "primarySecondaryMode": ["primary", "secondary"],
        "speed": [
            "speed1000",
            "speed100fd",
            "speed100hd",
            "speed10fd",
            "speed10g",
            "speed10hd",
            "speed2.5g",
            "speed5g",
        ],
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.fcoe.fcoe import (
            Fcoe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fcoe", None) is not None:
                return self._properties.get("Fcoe")
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.txlane.txlane import (
            TxLane,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TxLane", None) is not None:
                return self._properties.get("TxLane")
        return TxLane(self)._select()

    @property
    def AutoInstrumentation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoInstrumentation"])

    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoInstrumentation"], value)

    @property
    def AutoNegotiate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, allows autonegotiation between ports for speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoNegotiate"])

    @AutoNegotiate.setter
    def AutoNegotiate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoNegotiate"], value)

    @property
    def AutoNegotiatePauseAdvertisement(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | both | asymmetric | fullDuplex): Auto Negotiate Pause Advertisement.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoNegotiatePauseAdvertisement"])

    @AutoNegotiatePauseAdvertisement.setter
    def AutoNegotiatePauseAdvertisement(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoNegotiatePauseAdvertisement"], value)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000 | speed2.5g | speed5g | speed10g]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def CanModifySpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanModifySpeed"])

    @property
    def CanSetMultipleSpeeds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanSetMultipleSpeeds"])

    @property
    def EnableIntrinsicLatencyAdjustment(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables intrinsic latency adjustmnet on the port.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["EnableIntrinsicLatencyAdjustment"]
        )

    @EnableIntrinsicLatencyAdjustment.setter
    def EnableIntrinsicLatencyAdjustment(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["EnableIntrinsicLatencyAdjustment"], value
        )

    @property
    def EnablePPM(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePPM"])

    @EnablePPM.setter
    def EnablePPM(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnablePPM"], value)

    @property
    def EnabledFlowControl(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnabledFlowControl"])

    @EnabledFlowControl.setter
    def EnabledFlowControl(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnabledFlowControl"], value)

    @property
    def FlowControlDirectedAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The 48-bit MAC address that the port listens on for a directed pause.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FlowControlDirectedAddress"])

    @FlowControlDirectedAddress.setter
    def FlowControlDirectedAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FlowControlDirectedAddress"], value)

    @property
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopback"])

    @Loopback.setter
    def Loopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Loopback"], value)

    @property
    def LoopbackMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(none | lineLoopback | internalLoopback): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackMode"])

    @LoopbackMode.setter
    def LoopbackMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackMode"], value)

    @property
    def MasterSlaveMode(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(master | slave):
        """
        return self._get_attribute(self._SDM_ATT_MAP["MasterSlaveMode"])

    @MasterSlaveMode.setter
    def MasterSlaveMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MasterSlaveMode"], value)

    @property
    def Media(self):
        # type: () -> str
        """
        Returns
        -------
        - str(copper | fiber | sgmii): Available only for cards that support this dual-PHY capability.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Media"])

    @Media.setter
    def Media(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Media"], value)

    @property
    def NegotiateMasterSlave(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiateMasterSlave"])

    @NegotiateMasterSlave.setter
    def NegotiateMasterSlave(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NegotiateMasterSlave"], value)

    @property
    def NegotiatePrimarySecondary(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["NegotiatePrimarySecondary"])

    @NegotiatePrimarySecondary.setter
    def NegotiatePrimarySecondary(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["NegotiatePrimarySecondary"], value)

    @property
    def Ppm(self):
        # type: () -> int
        """DEPRECATED
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ppm"])

    @Ppm.setter
    def Ppm(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Ppm"], value)

    @property
    def PrimarySecondaryMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(primary | secondary):
        """
        return self._get_attribute(self._SDM_ATT_MAP["PrimarySecondaryMode"])

    @PrimarySecondaryMode.setter
    def PrimarySecondaryMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PrimarySecondaryMode"], value)

    @property
    def RxExtraIntrinsicLatency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Rx Extra Intrinsic Latency value in nano seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxExtraIntrinsicLatency"])

    @RxExtraIntrinsicLatency.setter
    def RxExtraIntrinsicLatency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RxExtraIntrinsicLatency"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000 | speed2.5g | speed5g | speed10g]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed1000 | speed100fd | speed100hd | speed10fd | speed10g | speed10hd | speed2.5g | speed5g): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["Speed"])

    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Speed"], value)

    @property
    def SpeedAuto(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed1000 | speed100fd | speed100hd | speed10fd | speed10g | speed10hd | speed2.5g | speed5g]):
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpeedAuto"])

    @SpeedAuto.setter
    def SpeedAuto(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpeedAuto"], value)

    @property
    def TxExtraIntrinsicLatency(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Tx Extra Intrinsic Latency value in nano seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxExtraIntrinsicLatency"])

    @TxExtraIntrinsicLatency.setter
    def TxExtraIntrinsicLatency(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxExtraIntrinsicLatency"], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If enabled, will allow transmission of packets even if the receive link is down.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"])

    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"], value)

    def update(
        self,
        AutoInstrumentation=None,
        AutoNegotiate=None,
        AutoNegotiatePauseAdvertisement=None,
        EnableIntrinsicLatencyAdjustment=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        Loopback=None,
        LoopbackMode=None,
        MasterSlaveMode=None,
        Media=None,
        NegotiateMasterSlave=None,
        NegotiatePrimarySecondary=None,
        Ppm=None,
        PrimarySecondaryMode=None,
        RxExtraIntrinsicLatency=None,
        SelectedSpeeds=None,
        Speed=None,
        SpeedAuto=None,
        TxExtraIntrinsicLatency=None,
        TxIgnoreRxLinkFaults=None,
    ):
        # type: (str, bool, str, bool, bool, bool, str, bool, str, str, str, bool, bool, int, str, int, List[str], str, List[str], int, bool) -> NovusTenGigLan
        """Updates novusTenGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiate (bool): If enabled, allows autonegotiation between ports for speed.
        - AutoNegotiatePauseAdvertisement (str(none | both | asymmetric | fullDuplex)): Auto Negotiate Pause Advertisement.
        - EnableIntrinsicLatencyAdjustment (bool): If true, enables intrinsic latency adjustmnet on the port.
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(none | lineLoopback | internalLoopback)): NOT DEFINED
        - MasterSlaveMode (str(master | slave)):
        - Media (str(copper | fiber | sgmii)): Available only for cards that support this dual-PHY capability.
        - NegotiateMasterSlave (bool):
        - NegotiatePrimarySecondary (bool):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - PrimarySecondaryMode (str(primary | secondary)):
        - RxExtraIntrinsicLatency (number): Rx Extra Intrinsic Latency value in nano seconds.
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000 | speed2.5g | speed5g | speed10g])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed1000 | speed100fd | speed100hd | speed10fd | speed10g | speed10hd | speed2.5g | speed5g)): NOT DEFINED
        - SpeedAuto (list(str[speed1000 | speed100fd | speed100hd | speed10fd | speed10g | speed10hd | speed2.5g | speed5g])):
        - TxExtraIntrinsicLatency (number): Tx Extra Intrinsic Latency value in nano seconds.
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AutoNegotiate=None,
        AutoNegotiatePauseAdvertisement=None,
        AvailableSpeeds=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        EnableIntrinsicLatencyAdjustment=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        Loopback=None,
        LoopbackMode=None,
        MasterSlaveMode=None,
        Media=None,
        NegotiateMasterSlave=None,
        NegotiatePrimarySecondary=None,
        Ppm=None,
        PrimarySecondaryMode=None,
        RxExtraIntrinsicLatency=None,
        SelectedSpeeds=None,
        Speed=None,
        SpeedAuto=None,
        TxExtraIntrinsicLatency=None,
        TxIgnoreRxLinkFaults=None,
    ):
        # type: (str, bool, str, List[str], bool, bool, bool, bool, bool, str, bool, str, str, str, bool, bool, int, str, int, List[str], str, List[str], int, bool) -> NovusTenGigLan
        """Finds and retrieves novusTenGigLan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve novusTenGigLan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all novusTenGigLan resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiate (bool): If enabled, allows autonegotiation between ports for speed.
        - AutoNegotiatePauseAdvertisement (str(none | both | asymmetric | fullDuplex)): Auto Negotiate Pause Advertisement.
        - AvailableSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000 | speed2.5g | speed5g | speed10g])): Which speeds are available for the current media and AN settings.
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - EnableIntrinsicLatencyAdjustment (bool): If true, enables intrinsic latency adjustmnet on the port.
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(none | lineLoopback | internalLoopback)): NOT DEFINED
        - MasterSlaveMode (str(master | slave)):
        - Media (str(copper | fiber | sgmii)): Available only for cards that support this dual-PHY capability.
        - NegotiateMasterSlave (bool):
        - NegotiatePrimarySecondary (bool):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - PrimarySecondaryMode (str(primary | secondary)):
        - RxExtraIntrinsicLatency (number): Rx Extra Intrinsic Latency value in nano seconds.
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000 | speed2.5g | speed5g | speed10g])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed1000 | speed100fd | speed100hd | speed10fd | speed10g | speed10hd | speed2.5g | speed5g)): NOT DEFINED
        - SpeedAuto (list(str[speed1000 | speed100fd | speed100hd | speed10fd | speed10g | speed10hd | speed2.5g | speed5g])):
        - TxExtraIntrinsicLatency (number): Tx Extra Intrinsic Latency value in nano seconds.
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.

        Returns
        -------
        - self: This instance with matching novusTenGigLan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of novusTenGigLan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the novusTenGigLan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
