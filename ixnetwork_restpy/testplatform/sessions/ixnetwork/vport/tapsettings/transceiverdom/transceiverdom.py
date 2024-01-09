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


class TransceiverDom(Base):
    """
    The TransceiverDom class encapsulates a required transceiverDom resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "transceiverDom"
    _SDM_ATT_MAP = {
        "CableLength": "cableLength",
        "DateCode": "dateCode",
        "FirmwareRevision": "firmwareRevision",
        "HardwareRevision": "hardwareRevision",
        "IdentifierType": "identifierType",
        "Manufacturer": "manufacturer",
        "MediaConnector": "mediaConnector",
        "MediaTech": "mediaTech",
        "MediaType": "mediaType",
        "MfgRevision": "mfgRevision",
        "Model": "model",
        "ModuleSupplyVoltageHighAlarm": "moduleSupplyVoltageHighAlarm",
        "ModuleSupplyVoltageHighWarn": "moduleSupplyVoltageHighWarn",
        "ModuleSupplyVoltageLowAlarm": "moduleSupplyVoltageLowAlarm",
        "ModuleSupplyVoltageLowWarn": "moduleSupplyVoltageLowWarn",
        "ModuleTemperatureHighAlarm": "moduleTemperatureHighAlarm",
        "ModuleTemperatureHighWarn": "moduleTemperatureHighWarn",
        "ModuleTemperatureLowAlarm": "moduleTemperatureLowAlarm",
        "ModuleTemperatureLowWarn": "moduleTemperatureLowWarn",
        "Msa": "msa",
        "ReportedMaxPower": "reportedMaxPower",
        "ReportedPowerClass": "reportedPowerClass",
        "RxOpticalPowerHighAlarm": "rxOpticalPowerHighAlarm",
        "RxOpticalPowerHighWarn": "rxOpticalPowerHighWarn",
        "RxOpticalPowerLowAlarm": "rxOpticalPowerLowAlarm",
        "RxOpticalPowerLowWarn": "rxOpticalPowerLowWarn",
        "SerialNumber": "serialNumber",
        "TxBiasCurrentHighAlarm": "txBiasCurrentHighAlarm",
        "TxBiasCurrentHighWarn": "txBiasCurrentHighWarn",
        "TxBiasCurrentLowAlarm": "txBiasCurrentLowAlarm",
        "TxBiasCurrentLowWarn": "txBiasCurrentLowWarn",
        "TxOpticalPowerHighAlarm": "txOpticalPowerHighAlarm",
        "TxOpticalPowerHighWarn": "txOpticalPowerHighWarn",
        "TxOpticalPowerLowAlarm": "txOpticalPowerLowAlarm",
        "TxOpticalPowerLowWarn": "txOpticalPowerLowWarn",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(TransceiverDom, self).__init__(parent, list_op)

    @property
    def CableLength(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver cable length.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CableLength"])

    @property
    def DateCode(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver date code in YYMMDDLL format.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DateCode"])

    @property
    def FirmwareRevision(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver firmware revision.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirmwareRevision"])

    @property
    def HardwareRevision(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver hardware revision.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HardwareRevision"])

    @property
    def IdentifierType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver identifier type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IdentifierType"])

    @property
    def Manufacturer(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver manufacturer.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Manufacturer"])

    @property
    def MediaConnector(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver media connector type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaConnector"])

    @property
    def MediaTech(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver media tech.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaTech"])

    @property
    def MediaType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver media type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaType"])

    @property
    def MfgRevision(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver mfg. revision.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MfgRevision"])

    @property
    def Model(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver model number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Model"])

    @property
    def ModuleSupplyVoltageHighAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module supply voltage high alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleSupplyVoltageHighAlarm"])

    @property
    def ModuleSupplyVoltageHighWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module supply voltage high warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleSupplyVoltageHighWarn"])

    @property
    def ModuleSupplyVoltageLowAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module supply voltage low alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleSupplyVoltageLowAlarm"])

    @property
    def ModuleSupplyVoltageLowWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module supply voltage low warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleSupplyVoltageLowWarn"])

    @property
    def ModuleTemperatureHighAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module temperature high alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleTemperatureHighAlarm"])

    @property
    def ModuleTemperatureHighWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module temperature high warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleTemperatureHighWarn"])

    @property
    def ModuleTemperatureLowAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module temperature low alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleTemperatureLowAlarm"])

    @property
    def ModuleTemperatureLowWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver module temperature low warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleTemperatureLowWarn"])

    @property
    def Msa(self):
        # type: () -> str
        """
        Returns
        -------
        - str: MSA.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Msa"])

    @property
    def ReportedMaxPower(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver reported max power.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportedMaxPower"])

    @property
    def ReportedPowerClass(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver reported power class.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReportedPowerClass"])

    @property
    def RxOpticalPowerHighAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Rx optical power high alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerHighAlarm"])

    @property
    def RxOpticalPowerHighWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Rx optical power high warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerHighWarn"])

    @property
    def RxOpticalPowerLowAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Rx optical power low alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerLowAlarm"])

    @property
    def RxOpticalPowerLowWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Rx optical power low warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RxOpticalPowerLowWarn"])

    @property
    def SerialNumber(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver serial number.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SerialNumber"])

    @property
    def TxBiasCurrentHighAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx bias current high alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentHighAlarm"])

    @property
    def TxBiasCurrentHighWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx bias current high warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentHighWarn"])

    @property
    def TxBiasCurrentLowAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx bias current low alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentLowAlarm"])

    @property
    def TxBiasCurrentLowWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx bias current low warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxBiasCurrentLowWarn"])

    @property
    def TxOpticalPowerHighAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx optical power high alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerHighAlarm"])

    @property
    def TxOpticalPowerHighWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx optical power high warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerHighWarn"])

    @property
    def TxOpticalPowerLowAlarm(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx optical power low alarm.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerLowAlarm"])

    @property
    def TxOpticalPowerLowWarn(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Tx optical power low warning.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxOpticalPowerLowWarn"])

    def find(
        self,
        CableLength=None,
        DateCode=None,
        FirmwareRevision=None,
        HardwareRevision=None,
        IdentifierType=None,
        Manufacturer=None,
        MediaConnector=None,
        MediaTech=None,
        MediaType=None,
        MfgRevision=None,
        Model=None,
        ModuleSupplyVoltageHighAlarm=None,
        ModuleSupplyVoltageHighWarn=None,
        ModuleSupplyVoltageLowAlarm=None,
        ModuleSupplyVoltageLowWarn=None,
        ModuleTemperatureHighAlarm=None,
        ModuleTemperatureHighWarn=None,
        ModuleTemperatureLowAlarm=None,
        ModuleTemperatureLowWarn=None,
        Msa=None,
        ReportedMaxPower=None,
        ReportedPowerClass=None,
        RxOpticalPowerHighAlarm=None,
        RxOpticalPowerHighWarn=None,
        RxOpticalPowerLowAlarm=None,
        RxOpticalPowerLowWarn=None,
        SerialNumber=None,
        TxBiasCurrentHighAlarm=None,
        TxBiasCurrentHighWarn=None,
        TxBiasCurrentLowAlarm=None,
        TxBiasCurrentLowWarn=None,
        TxOpticalPowerHighAlarm=None,
        TxOpticalPowerHighWarn=None,
        TxOpticalPowerLowAlarm=None,
        TxOpticalPowerLowWarn=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str) -> TransceiverDom
        """Finds and retrieves transceiverDom resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve transceiverDom resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all transceiverDom resources from the server.

        Args
        ----
        - CableLength (str): Transceiver cable length.
        - DateCode (str): Transceiver date code in YYMMDDLL format.
        - FirmwareRevision (str): Transceiver firmware revision.
        - HardwareRevision (str): Transceiver hardware revision.
        - IdentifierType (str): Transceiver identifier type.
        - Manufacturer (str): Transceiver manufacturer.
        - MediaConnector (str): Transceiver media connector type.
        - MediaTech (str): Transceiver media tech.
        - MediaType (str): Transceiver media type.
        - MfgRevision (str): Transceiver mfg. revision.
        - Model (str): Transceiver model number.
        - ModuleSupplyVoltageHighAlarm (str): Transceiver module supply voltage high alarm.
        - ModuleSupplyVoltageHighWarn (str): Transceiver module supply voltage high warning.
        - ModuleSupplyVoltageLowAlarm (str): Transceiver module supply voltage low alarm.
        - ModuleSupplyVoltageLowWarn (str): Transceiver module supply voltage low warning.
        - ModuleTemperatureHighAlarm (str): Transceiver module temperature high alarm.
        - ModuleTemperatureHighWarn (str): Transceiver module temperature high warning.
        - ModuleTemperatureLowAlarm (str): Transceiver module temperature low alarm.
        - ModuleTemperatureLowWarn (str): Transceiver module temperature low warning.
        - Msa (str): MSA.
        - ReportedMaxPower (str): Transceiver reported max power.
        - ReportedPowerClass (str): Transceiver reported power class.
        - RxOpticalPowerHighAlarm (str): Rx optical power high alarm.
        - RxOpticalPowerHighWarn (str): Rx optical power high warning.
        - RxOpticalPowerLowAlarm (str): Rx optical power low alarm.
        - RxOpticalPowerLowWarn (str): Rx optical power low warning.
        - SerialNumber (str): Transceiver serial number.
        - TxBiasCurrentHighAlarm (str): Tx bias current high alarm.
        - TxBiasCurrentHighWarn (str): Tx bias current high warning.
        - TxBiasCurrentLowAlarm (str): Tx bias current low alarm.
        - TxBiasCurrentLowWarn (str): Tx bias current low warning.
        - TxOpticalPowerHighAlarm (str): Tx optical power high alarm.
        - TxOpticalPowerHighWarn (str): Tx optical power high warning.
        - TxOpticalPowerLowAlarm (str): Tx optical power low alarm.
        - TxOpticalPowerLowWarn (str): Tx optical power low warning.

        Returns
        -------
        - self: This instance with matching transceiverDom resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of transceiverDom data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the transceiverDom resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
