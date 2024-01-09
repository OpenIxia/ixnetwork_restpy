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


class Atm(Base):
    """Layer 1 (Physical) parameters for an Asynchronous Transfer Mode (ATM) port.
    The Atm class encapsulates a required atm resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "atm"
    _SDM_ATT_MAP = {
        "AvailableSpeeds": "availableSpeeds",
        "C2Expected": "c2Expected",
        "C2Tx": "c2Tx",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "CellHeader": "cellHeader",
        "CosetActive": "cosetActive",
        "CrcSize": "crcSize",
        "DataScrambling": "dataScrambling",
        "EnablePPM": "enablePPM",
        "FillerCell": "fillerCell",
        "InterfaceType": "interfaceType",
        "Loopback": "loopback",
        "PatternMatching": "patternMatching",
        "Ppm": "ppm",
        "ReassemblyTimeout": "reassemblyTimeout",
        "SelectedSpeeds": "selectedSpeeds",
        "TransmitClocking": "transmitClocking",
    }
    _SDM_ENUM_MAP = {
        "cellHeader": ["nni", "uni"],
        "crcSize": ["crc32", "crc16"],
        "fillerCell": ["idle", "unassigned"],
        "interfaceType": ["oc3", "oc12", "stm1", "stm4"],
        "transmitClocking": ["internal", "external", "recovered"],
    }

    def __init__(self, parent, list_op=False):
        super(Atm, self).__init__(parent, list_op)

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
        - number: The expected value of the C2 byte in the received path overhead. Typically, this will match the value in the Transmit field. For ATM, the expected value is 0x13 (Hex).
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
        - number: The value of the C2 byte in the transmitted path overhead. For ATM, the transmitted value is 0x13 (Hex).
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
    def CellHeader(self):
        # type: () -> str
        """
        Returns
        -------
        - str(nni | uni): user/network-to-network interface
        """
        return self._get_attribute(self._SDM_ATT_MAP["CellHeader"])

    @CellHeader.setter
    def CellHeader(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CellHeader"], value)

    @property
    def CosetActive(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: CRC + Exclusive OR Operation
        """
        return self._get_attribute(self._SDM_ATT_MAP["CosetActive"])

    @CosetActive.setter
    def CosetActive(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CosetActive"], value)

    @property
    def CrcSize(self):
        # type: () -> str
        """
        Returns
        -------
        - str(crc32 | crc16): Choose the type of Cyclic Redundancy Check to be used.
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
        - bool: If enabled, data is scrambled with the x43 + 1 polynomial. Note: The ATM cell header is not scrambled.
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
    def FillerCell(self):
        # type: () -> str
        """
        Returns
        -------
        - str(idle | unassigned): SONET frame transmission is continuous even when data or control messages are not being transmitted. Choose the ATM cell type to be transmitted during those intervals.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FillerCell"])

    @FillerCell.setter
    def FillerCell(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["FillerCell"], value)

    @property
    def InterfaceType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(oc3 | oc12 | stm1 | stm4): The interface type for ATM.
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
    def PatternMatching(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Used to enable capture/filter values for use with ATM ports. When enabled, the frame data from one or more VPI/VCIs may be used as capture trigger or capture filter option.
        """
        return self._get_attribute(self._SDM_ATT_MAP["PatternMatching"])

    @PatternMatching.setter
    def PatternMatching(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PatternMatching"], value)

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
    def ReassemblyTimeout(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets the value for the Reassembly Timeout. It is the period of time that the receive side will wait for another cell on that channel - for reassembly of cells into a CPCS PDU (packet). If no cell is received within that period, the timer will expire. (in hex)
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReassemblyTimeout"])

    @ReassemblyTimeout.setter
    def ReassemblyTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReassemblyTimeout"], value)

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
        - str(internal | external | recovered): The options for the transmit clock.
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
        CellHeader=None,
        CosetActive=None,
        CrcSize=None,
        DataScrambling=None,
        EnablePPM=None,
        FillerCell=None,
        InterfaceType=None,
        Loopback=None,
        PatternMatching=None,
        Ppm=None,
        ReassemblyTimeout=None,
        SelectedSpeeds=None,
        TransmitClocking=None,
    ):
        # type: (int, int, str, bool, str, bool, bool, str, str, bool, bool, int, int, List[str], str) -> Atm
        """Updates atm resource on the server.

        Args
        ----
        - C2Expected (number): The expected value of the C2 byte in the received path overhead. Typically, this will match the value in the Transmit field. For ATM, the expected value is 0x13 (Hex).
        - C2Tx (number): The value of the C2 byte in the transmitted path overhead. For ATM, the transmitted value is 0x13 (Hex).
        - CellHeader (str(nni | uni)): user/network-to-network interface
        - CosetActive (bool): CRC + Exclusive OR Operation
        - CrcSize (str(crc32 | crc16)): Choose the type of Cyclic Redundancy Check to be used.
        - DataScrambling (bool): If enabled, data is scrambled with the x43 + 1 polynomial. Note: The ATM cell header is not scrambled.
        - EnablePPM (bool): If true, enables the portsppm.
        - FillerCell (str(idle | unassigned)): SONET frame transmission is continuous even when data or control messages are not being transmitted. Choose the ATM cell type to be transmitted during those intervals.
        - InterfaceType (str(oc3 | oc12 | stm1 | stm4)): The interface type for ATM.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - PatternMatching (bool): Used to enable capture/filter values for use with ATM ports. When enabled, the frame data from one or more VPI/VCIs may be used as capture trigger or capture filter option.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - ReassemblyTimeout (number): Sets the value for the Reassembly Timeout. It is the period of time that the receive side will wait for another cell on that channel - for reassembly of cells into a CPCS PDU (packet). If no cell is received within that period, the timer will expire. (in hex)
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TransmitClocking (str(internal | external | recovered)): The options for the transmit clock.

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
        CellHeader=None,
        CosetActive=None,
        CrcSize=None,
        DataScrambling=None,
        EnablePPM=None,
        FillerCell=None,
        InterfaceType=None,
        Loopback=None,
        PatternMatching=None,
        Ppm=None,
        ReassemblyTimeout=None,
        SelectedSpeeds=None,
        TransmitClocking=None,
    ):
        # type: (List[str], int, int, bool, bool, str, bool, str, bool, bool, str, str, bool, bool, int, int, List[str], str) -> Atm
        """Finds and retrieves atm resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve atm resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all atm resources from the server.

        Args
        ----
        - AvailableSpeeds (list(str[])): Which speeds are available for the current media and AN settings.
        - C2Expected (number): The expected value of the C2 byte in the received path overhead. Typically, this will match the value in the Transmit field. For ATM, the expected value is 0x13 (Hex).
        - C2Tx (number): The value of the C2 byte in the transmitted path overhead. For ATM, the transmitted value is 0x13 (Hex).
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - CellHeader (str(nni | uni)): user/network-to-network interface
        - CosetActive (bool): CRC + Exclusive OR Operation
        - CrcSize (str(crc32 | crc16)): Choose the type of Cyclic Redundancy Check to be used.
        - DataScrambling (bool): If enabled, data is scrambled with the x43 + 1 polynomial. Note: The ATM cell header is not scrambled.
        - EnablePPM (bool): If true, enables the portsppm.
        - FillerCell (str(idle | unassigned)): SONET frame transmission is continuous even when data or control messages are not being transmitted. Choose the ATM cell type to be transmitted during those intervals.
        - InterfaceType (str(oc3 | oc12 | stm1 | stm4)): The interface type for ATM.
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - PatternMatching (bool): Used to enable capture/filter values for use with ATM ports. When enabled, the frame data from one or more VPI/VCIs may be used as capture trigger or capture filter option.
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - ReassemblyTimeout (number): Sets the value for the Reassembly Timeout. It is the period of time that the receive side will wait for another cell on that channel - for reassembly of cells into a CPCS PDU (packet). If no cell is received within that period, the timer will expire. (in hex)
        - SelectedSpeeds (list(str[])): Which speeds are selected for the current media and AN settings.
        - TransmitClocking (str(internal | external | recovered)): The options for the transmit clock.

        Returns
        -------
        - self: This instance with matching atm resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of atm data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the atm resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
