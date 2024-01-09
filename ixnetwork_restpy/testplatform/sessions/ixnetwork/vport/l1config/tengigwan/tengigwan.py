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


class TenGigWan(Base):
    """Layer 1 (physical) parameters for a 10 Gigabit Ethernet WAN port.
    The TenGigWan class encapsulates a required tenGigWan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "tenGigWan"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AvailableSpeeds": "availableSpeeds",
        "C2Expected": "c2Expected",
        "C2Tx": "c2Tx",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "EnablePPM": "enablePPM",
        "EnabledFlowControl": "enabledFlowControl",
        "FlowControlDirectedAddress": "flowControlDirectedAddress",
        "IfsStretch": "ifsStretch",
        "InterfaceType": "interfaceType",
        "Loopback": "loopback",
        "Ppm": "ppm",
        "SelectedSpeeds": "selectedSpeeds",
        "TransmitClocking": "transmitClocking",
        "TxIgnoreRxLinkFaults": "txIgnoreRxLinkFaults",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "interfaceType": ["wanSdh", "wanSonet"],
        "transmitClocking": ["internal", "external", "recovered"],
    }

    def __init__(self, parent, list_op=False):
        super(TenGigWan, self).__init__(parent, list_op)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.fcoe.fcoe import (
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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.txlane.txlane.TxLane): An instance of the TxLane class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.txlane.txlane import (
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
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def C2Expected(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The expected value of the link partner's C2 byte. Typically, this will match the value in the Transmit field. (Hex). The default value is 0x24 (hex).
        """
        return self._get_attribute(self._SDM_ATT_MAP["C2Expected"])

    @C2Expected.setter
    def C2Expected(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["C2Expected"], value)

    @property
    def C2Tx(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The value of the C2 byte in the transmitted stream. (Hex) The default value is 0x24 (hex).
        """
        return self._get_attribute(self._SDM_ATT_MAP["C2Tx"])

    @C2Tx.setter
    def C2Tx(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["C2Tx"], value)

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
    def IfsStretch(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If checked, indicates the ifsStretch as the desired mode of operation. The IFS Stretch ratio determines the number of bits in a frame that require one octet of Inter Frame Spacing Extension.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IfsStretch"])

    @IfsStretch.setter
    def IfsStretch(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IfsStretch"], value)

    @property
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(wanSdh | wanSonet): The 10G WAN interface type for the port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["InterfaceType"])

    @InterfaceType.setter
    def InterfaceType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["InterfaceType"], value)

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
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def TransmitClocking(self):
        # type: () -> str
        """
        Returns
        -------
        - str(internal | external | recovered): The transmit clocking type for this 10G WAN port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitClocking"])

    @TransmitClocking.setter
    def TransmitClocking(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitClocking"], value)

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
        C2Expected=None,
        C2Tx=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        IfsStretch=None,
        InterfaceType=None,
        Loopback=None,
        Ppm=None,
        SelectedSpeeds=None,
        TransmitClocking=None,
        TxIgnoreRxLinkFaults=None,
    ):
        # type: (str, int, int, bool, bool, str, bool, str, bool, int, List[str], str, bool) -> TenGigWan
        """Updates tenGigWan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - C2Expected (number): The expected value of the link partner's C2 byte. Typically, this will match the value in the Transmit field. (Hex). The default value is 0x24 (hex).
        - C2Tx (number): The value of the C2 byte in the transmitted stream. (Hex) The default value is 0x24 (hex).
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - IfsStretch (bool): If checked, indicates the ifsStretch as the desired mode of operation. The IFS Stretch ratio determines the number of bits in a frame that require one octet of Inter Frame Spacing Extension.
        - InterfaceType (str(wanSdh | wanSonet)): The 10G WAN interface type for the port.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TransmitClocking (str(internal | external | recovered)): The transmit clocking type for this 10G WAN port.
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AvailableSpeeds=None,
        C2Expected=None,
        C2Tx=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        EnablePPM=None,
        EnabledFlowControl=None,
        FlowControlDirectedAddress=None,
        IfsStretch=None,
        InterfaceType=None,
        Loopback=None,
        Ppm=None,
        SelectedSpeeds=None,
        TransmitClocking=None,
        TxIgnoreRxLinkFaults=None,
    ):
        # type: (str, List[str], int, int, bool, bool, bool, bool, str, bool, str, bool, int, List[str], str, bool) -> TenGigWan
        """Finds and retrieves tenGigWan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve tenGigWan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all tenGigWan resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AvailableSpeeds (list(str[])): Which speeds are available for the current media and AN settings.
        - C2Expected (number): The expected value of the link partner's C2 byte. Typically, this will match the value in the Transmit field. (Hex). The default value is 0x24 (hex).
        - C2Tx (number): The value of the C2 byte in the transmitted stream. (Hex) The default value is 0x24 (hex).
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - EnablePPM (bool): If true, enables the portsppm.
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - IfsStretch (bool): If checked, indicates the ifsStretch as the desired mode of operation. The IFS Stretch ratio determines the number of bits in a frame that require one octet of Inter Frame Spacing Extension.
        - InterfaceType (str(wanSdh | wanSonet)): The 10G WAN interface type for the port.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TransmitClocking (str(internal | external | recovered)): The transmit clocking type for this 10G WAN port.
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.

        Returns
        -------
        - self: This instance with matching tenGigWan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of tenGigWan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the tenGigWan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
