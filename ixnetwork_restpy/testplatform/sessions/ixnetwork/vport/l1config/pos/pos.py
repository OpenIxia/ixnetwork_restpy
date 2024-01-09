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


class Pos(Base):
    """Layer 1 (physical) parameters for a POS (Packet over SONET) port.
    The Pos class encapsulates a required pos resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "pos"
    _SDM_ATT_MAP = {
        "AvailableSpeeds": "availableSpeeds",
        "C2Expected": "c2Expected",
        "C2Tx": "c2Tx",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "CrcSize": "crcSize",
        "DataScrambling": "dataScrambling",
        "EnablePPM": "enablePPM",
        "InterfaceType": "interfaceType",
        "Loopback": "loopback",
        "PayloadType": "payloadType",
        "Ppm": "ppm",
        "SelectedSpeeds": "selectedSpeeds",
        "TrafficMapType": "trafficMapType",
        "TransmitClocking": "transmitClocking",
    }
    _SDM_ENUM_MAP = {
        "crcSize": ["crc32", "crc16"],
        "interfaceType": [
            "oc3",
            "oc12",
            "oc48",
            "oc192",
            "stm1",
            "stm4",
            "stm16",
            "stm64",
        ],
        "payloadType": ["ciscoFrameRelay", "ciscoHdlc", "frameRelay", "ppp"],
        "trafficMapType": ["dcc", "spe"],
        "transmitClocking": ["internal", "external", "recovered"],
    }

    def __init__(self, parent, list_op=False):
        super(Pos, self).__init__(parent, list_op)

    @property
    def Dcc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.dcc.dcc.Dcc): An instance of the Dcc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.dcc.dcc import (
            Dcc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Dcc", None) is not None:
                return self._properties.get("Dcc")
        return Dcc(self)._select()

    @property
    def Ppp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.ppp.ppp.Ppp): An instance of the Ppp class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.ppp.ppp import (
            Ppp,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ppp", None) is not None:
                return self._properties.get("Ppp")
        return Ppp(self)._select()

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
        - number: C2 Byte
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
        - number: C2 Byte
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
    def CrcSize(self):
        # type: () -> str
        """
        Returns
        -------
        - str(crc32 | crc16): The type of cyclic redundancy check (CRC) to be used.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CrcSize"])

    @CrcSize.setter
    def CrcSize(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CrcSize"], value)

    @property
    def DataScrambling(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Data scrambling is enabled on this POS port.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DataScrambling"])

    @DataScrambling.setter
    def DataScrambling(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["DataScrambling"], value)

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
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oc3 | oc12 | oc48 | oc192 | stm1 | stm4 | stm16 | stm64): The POS interface type for the port.
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
    def PayloadType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ciscoFrameRelay | ciscoHdlc | frameRelay | ppp): The POS payload type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PayloadType"])

    @PayloadType.setter
    def PayloadType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["PayloadType"], value)

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
    def TrafficMapType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(dcc | spe): The POS traffic map type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TrafficMapType"])

    @TrafficMapType.setter
    def TrafficMapType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TrafficMapType"], value)

    @property
    def TransmitClocking(self):
        # type: () -> str
        """
        Returns
        -------
        - str(internal | external | recovered): The POS transmit clocking type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransmitClocking"])

    @TransmitClocking.setter
    def TransmitClocking(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TransmitClocking"], value)

    def update(
        self,
        C2Expected=None,
        C2Tx=None,
        CrcSize=None,
        DataScrambling=None,
        EnablePPM=None,
        InterfaceType=None,
        Loopback=None,
        PayloadType=None,
        Ppm=None,
        SelectedSpeeds=None,
        TrafficMapType=None,
        TransmitClocking=None,
    ):
        # type: (int, int, str, bool, bool, str, bool, str, int, List[str], str, str) -> Pos
        """Updates pos resource on the server.

        Args
        ----
        - C2Expected (number): C2 Byte
        - C2Tx (number): C2 Byte
        - CrcSize (str(crc32 | crc16)): The type of cyclic redundancy check (CRC) to be used.
        - DataScrambling (bool): Data scrambling is enabled on this POS port.
        - EnablePPM (bool): If true, enables the portsppm.
        - InterfaceType (str(oc3 | oc12 | oc48 | oc192 | stm1 | stm4 | stm16 | stm64)): The POS interface type for the port.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - PayloadType (str(ciscoFrameRelay | ciscoHdlc | frameRelay | ppp)): The POS payload type.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TrafficMapType (str(dcc | spe)): The POS traffic map type.
        - TransmitClocking (str(internal | external | recovered)): The POS transmit clocking type.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AvailableSpeeds=None,
        C2Expected=None,
        C2Tx=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        CrcSize=None,
        DataScrambling=None,
        EnablePPM=None,
        InterfaceType=None,
        Loopback=None,
        PayloadType=None,
        Ppm=None,
        SelectedSpeeds=None,
        TrafficMapType=None,
        TransmitClocking=None,
    ):
        # type: (List[str], int, int, bool, bool, str, bool, bool, str, bool, str, int, List[str], str, str) -> Pos
        """Finds and retrieves pos resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve pos resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all pos resources from the server.

        Args
        ----
        - AvailableSpeeds (list(str[])): Which speeds are available for the current media and AN settings.
        - C2Expected (number): C2 Byte
        - C2Tx (number): C2 Byte
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - CrcSize (str(crc32 | crc16)): The type of cyclic redundancy check (CRC) to be used.
        - DataScrambling (bool): Data scrambling is enabled on this POS port.
        - EnablePPM (bool): If true, enables the portsppm.
        - InterfaceType (str(oc3 | oc12 | oc48 | oc192 | stm1 | stm4 | stm16 | stm64)): The POS interface type for the port.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - PayloadType (str(ciscoFrameRelay | ciscoHdlc | frameRelay | ppp)): The POS payload type.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TrafficMapType (str(dcc | spe)): The POS traffic map type.
        - TransmitClocking (str(internal | external | recovered)): The POS transmit clocking type.

        Returns
        -------
        - self: This instance with matching pos resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of pos data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the pos resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
