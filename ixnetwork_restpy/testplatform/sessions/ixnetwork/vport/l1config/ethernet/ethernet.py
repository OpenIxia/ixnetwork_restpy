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


class Ethernet(Base):
    """Ethernet Layer 1 configuration settings.
    The Ethernet class encapsulates a required ethernet resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ethernet"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AutoNegotiate": "autoNegotiate",
        "AvailableSpeeds": "availableSpeeds",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "EnablePPM": "enablePPM",
        "EnabledFlowControl": "enabledFlowControl",
        "FlowControlDirectedAddress": "flowControlDirectedAddress",
        "Loopback": "loopback",
        "MasterSlaveMode": "masterSlaveMode",
        "Media": "media",
        "NegotiateMasterSlave": "negotiateMasterSlave",
        "NegotiatePrimarySecondary": "negotiatePrimarySecondary",
        "Ppm": "ppm",
        "PrimarySecondaryMode": "primarySecondaryMode",
        "SelectedSpeeds": "selectedSpeeds",
        "Speed": "speed",
        "SpeedAuto": "speedAuto",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "masterSlaveMode": ["master", "slave"],
        "media": ["copper", "fiber", "sgmii"],
        "primarySecondaryMode": ["primary", "secondary"],
        "speed": [
            "auto",
            "speed1000",
            "speed100fd",
            "speed100hd",
            "speed10fd",
            "speed10hd",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Ethernet, self).__init__(parent, list_op)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe import (
            Fcoe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fcoe", None) is not None:
                return self._properties.get("Fcoe")
        return Fcoe(self)._select()

    @property
    def Oam(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.oam.oam.Oam): An instance of the Oam class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.oam.oam import (
            Oam,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Oam", None) is not None:
                return self._properties.get("Oam")
        return Oam(self)._select()

    @property
    def TxLane(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane.TxLane): An instance of the TxLane class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane import (
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
        - bool: If enabled, allows autonegotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoNegotiate"])

    @AutoNegotiate.setter
    def AutoNegotiate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoNegotiate"], value)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000]): Which speeds are available for the current media and AN settings.
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
    def MasterSlaveMode(self):
        # type: () -> str
        """DEPRECATED
        Returns
        -------
        - str(master | slave): NOT DEFINED
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
        - str(copper | fiber | sgmii): Available only for Ethernet cards that support this dual-PHY capability.
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
        - bool: NOT DEFINED
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
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000]): Which speeds are selected for the current media and AN settings.
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
        - str(auto | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd): The speed and duplex operation options.
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
        - list(str[all | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd]): If selected, allows auto negotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SpeedAuto"])

    @SpeedAuto.setter
    def SpeedAuto(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SpeedAuto"], value)

    def update(
        self,
        AutoInstrumentation=None,
        AutoNegotiate=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        Loopback=None,
        MasterSlaveMode=None,
        Media=None,
        NegotiateMasterSlave=None,
        NegotiatePrimarySecondary=None,
        Ppm=None,
        PrimarySecondaryMode=None,
        SelectedSpeeds=None,
        Speed=None,
        SpeedAuto=None,
    ):
        # type: (str, bool, bool, bool, str, bool, str, str, bool, bool, int, str, List[str], str, List[str]) -> Ethernet
        """Updates ethernet resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiate (bool): If enabled, allows autonegotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - MasterSlaveMode (str(master | slave)): NOT DEFINED
        - Media (str(copper | fiber | sgmii)): Available only for Ethernet cards that support this dual-PHY capability.
        - NegotiateMasterSlave (bool): NOT DEFINED
        - NegotiatePrimarySecondary (bool):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - PrimarySecondaryMode (str(primary | secondary)):
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000])): Which speeds are selected for the current media and AN settings.
        - Speed (str(auto | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd)): The speed and duplex operation options.
        - SpeedAuto (list(str[all | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd])): If selected, allows auto negotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AutoNegotiate=None,
        AvailableSpeeds=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        Loopback=None,
        MasterSlaveMode=None,
        Media=None,
        NegotiateMasterSlave=None,
        NegotiatePrimarySecondary=None,
        Ppm=None,
        PrimarySecondaryMode=None,
        SelectedSpeeds=None,
        Speed=None,
        SpeedAuto=None,
    ):
        # type: (str, bool, List[str], bool, bool, bool, bool, str, bool, str, str, bool, bool, int, str, List[str], str, List[str]) -> Ethernet
        """Finds and retrieves ethernet resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernet resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernet resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AutoNegotiate (bool): If enabled, allows autonegotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation
        - AvailableSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000])): Which speeds are available for the current media and AN settings.
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - MasterSlaveMode (str(master | slave)): NOT DEFINED
        - Media (str(copper | fiber | sgmii)): Available only for Ethernet cards that support this dual-PHY capability.
        - NegotiateMasterSlave (bool): NOT DEFINED
        - NegotiatePrimarySecondary (bool):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - PrimarySecondaryMode (str(primary | secondary)):
        - SelectedSpeeds (list(str[speed10fd | speed10hd | speed100fd | speed100hd | speed1000])): Which speeds are selected for the current media and AN settings.
        - Speed (str(auto | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd)): The speed and duplex operation options.
        - SpeedAuto (list(str[all | speed1000 | speed100fd | speed100hd | speed10fd | speed10hd])): If selected, allows auto negotiation between ports for speed and duplex operation based on the various choices. The selected capabilities are advertised during AutoNegotiation.

        Returns
        -------
        - self: This instance with matching ethernet resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernet data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernet resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
