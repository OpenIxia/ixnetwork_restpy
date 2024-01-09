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


class Novus5GTenTwentyFiveGigLan(Base):
    """
    The Novus5GTenTwentyFiveGigLan class encapsulates a required novus5GTenTwentyFiveGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "novus5GTenTwentyFiveGigLan"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AvailableSpeeds": "availableSpeeds",
        "BadBlocksNumber": "badBlocksNumber",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "EnableAutoNegotiation": "enableAutoNegotiation",
        "EnablePPM": "enablePPM",
        "EnableRsFec": "enableRsFec",
        "EnableRsFecStats": "enableRsFecStats",
        "EnabledFlowControl": "enabledFlowControl",
        "FirecodeAdvertise": "firecodeAdvertise",
        "FirecodeForceOff": "firecodeForceOff",
        "FirecodeForceOn": "firecodeForceOn",
        "FirecodeRequest": "firecodeRequest",
        "FlowControlDirectedAddress": "flowControlDirectedAddress",
        "ForceDisableFEC": "forceDisableFEC",
        "GoodBlocksNumber": "goodBlocksNumber",
        "IeeeL1Defaults": "ieeeL1Defaults",
        "LaserOn": "laserOn",
        "LinkTraining": "linkTraining",
        "LoopContinuously": "loopContinuously",
        "LoopCountNumber": "loopCountNumber",
        "Loopback": "loopback",
        "LoopbackMode": "loopbackMode",
        "Ppm": "ppm",
        "RsFecAdvertise": "rsFecAdvertise",
        "RsFecForceOn": "rsFecForceOn",
        "RsFecRequest": "rsFecRequest",
        "SelectedSpeeds": "selectedSpeeds",
        "SendSetsMode": "sendSetsMode",
        "Speed": "speed",
        "StartErrorInsertion": "startErrorInsertion",
        "TxIgnoreRxLinkFaults": "txIgnoreRxLinkFaults",
        "TypeAOrderedSets": "typeAOrderedSets",
        "TypeBOrderedSets": "typeBOrderedSets",
        "UseANResults": "useANResults",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "loopbackMode": ["none", "lineLoopback", "internalLoopback"],
        "sendSetsMode": ["alternate", "typeAOnly", "typeBOnly"],
        "speed": ["speed100g", "speed10g", "speed25g", "speed50g"],
        "typeAOrderedSets": ["localFault", "remoteFault"],
        "typeBOrderedSets": ["localFault", "remoteFault"],
    }

    def __init__(self, parent, list_op=False):
        super(Novus5GTenTwentyFiveGigLan, self).__init__(parent, list_op)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novus5gtentwentyfivegiglan.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novus5gtentwentyfivegiglan.fcoe.fcoe import (
            Fcoe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fcoe", None) is not None:
                return self._properties.get("Fcoe")
        return Fcoe(self)._select()

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
        - list(str[speed100g | speed25g | speed50g | speed10g]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def BadBlocksNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["BadBlocksNumber"])

    @BadBlocksNumber.setter
    def BadBlocksNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BadBlocksNumber"], value)

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
    def EnableAutoNegotiation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAutoNegotiation"])

    @EnableAutoNegotiation.setter
    def EnableAutoNegotiation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAutoNegotiation"], value)

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
    def EnableRsFec(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRsFec"])

    @EnableRsFec.setter
    def EnableRsFec(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRsFec"], value)

    @property
    def EnableRsFecStats(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableRsFecStats"])

    @EnableRsFecStats.setter
    def EnableRsFecStats(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableRsFecStats"], value)

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
    def FirecodeAdvertise(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirecodeAdvertise"])

    @FirecodeAdvertise.setter
    def FirecodeAdvertise(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirecodeAdvertise"], value)

    @property
    def FirecodeForceOff(self):
        # type: () -> bool
        """DEPRECATED
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirecodeForceOff"])

    @FirecodeForceOff.setter
    def FirecodeForceOff(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirecodeForceOff"], value)

    @property
    def FirecodeForceOn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirecodeForceOn"])

    @FirecodeForceOn.setter
    def FirecodeForceOn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirecodeForceOn"], value)

    @property
    def FirecodeRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["FirecodeRequest"])

    @FirecodeRequest.setter
    def FirecodeRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FirecodeRequest"], value)

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
    def ForceDisableFEC(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["ForceDisableFEC"])

    @ForceDisableFEC.setter
    def ForceDisableFEC(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ForceDisableFEC"], value)

    @property
    def GoodBlocksNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["GoodBlocksNumber"])

    @GoodBlocksNumber.setter
    def GoodBlocksNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["GoodBlocksNumber"], value)

    @property
    def IeeeL1Defaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["IeeeL1Defaults"])

    @IeeeL1Defaults.setter
    def IeeeL1Defaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IeeeL1Defaults"], value)

    @property
    def LaserOn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LaserOn"])

    @LaserOn.setter
    def LaserOn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LaserOn"], value)

    @property
    def LinkTraining(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkTraining"])

    @property
    def LoopContinuously(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopContinuously"])

    @LoopContinuously.setter
    def LoopContinuously(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopContinuously"], value)

    @property
    def LoopCountNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopCountNumber"])

    @LoopCountNumber.setter
    def LoopCountNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopCountNumber"], value)

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
        - str(none | lineLoopback | internalLoopback):
        """
        return self._get_attribute(self._SDM_ATT_MAP["LoopbackMode"])

    @LoopbackMode.setter
    def LoopbackMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LoopbackMode"], value)

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
    def RsFecAdvertise(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsFecAdvertise"])

    @RsFecAdvertise.setter
    def RsFecAdvertise(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsFecAdvertise"], value)

    @property
    def RsFecForceOn(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsFecForceOn"])

    @RsFecForceOn.setter
    def RsFecForceOn(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsFecForceOn"], value)

    @property
    def RsFecRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsFecRequest"])

    @RsFecRequest.setter
    def RsFecRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsFecRequest"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed10g]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def SendSetsMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(alternate | typeAOnly | typeBOnly):
        """
        return self._get_attribute(self._SDM_ATT_MAP["SendSetsMode"])

    @SendSetsMode.setter
    def SendSetsMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["SendSetsMode"], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed100g | speed10g | speed25g | speed50g):
        """
        return self._get_attribute(self._SDM_ATT_MAP["Speed"])

    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Speed"], value)

    @property
    def StartErrorInsertion(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["StartErrorInsertion"])

    @StartErrorInsertion.setter
    def StartErrorInsertion(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["StartErrorInsertion"], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"])

    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TxIgnoreRxLinkFaults"], value)

    @property
    def TypeAOrderedSets(self):
        # type: () -> str
        """
        Returns
        -------
        - str(localFault | remoteFault):
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeAOrderedSets"])

    @TypeAOrderedSets.setter
    def TypeAOrderedSets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeAOrderedSets"], value)

    @property
    def TypeBOrderedSets(self):
        # type: () -> str
        """
        Returns
        -------
        - str(localFault | remoteFault):
        """
        return self._get_attribute(self._SDM_ATT_MAP["TypeBOrderedSets"])

    @TypeBOrderedSets.setter
    def TypeBOrderedSets(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["TypeBOrderedSets"], value)

    @property
    def UseANResults(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseANResults"])

    @UseANResults.setter
    def UseANResults(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseANResults"], value)

    def update(
        self,
        AutoInstrumentation=None,
        BadBlocksNumber=None,
        EnableAutoNegotiation=None,
        EnablePPM=None,
        EnableRsFec=None,
        EnableRsFecStats=None,
        EnabledFlowControl=None,
        FirecodeAdvertise=None,
        FirecodeForceOff=None,
        FirecodeForceOn=None,
        FirecodeRequest=None,
        FlowControlDirectedAddress=None,
        ForceDisableFEC=None,
        GoodBlocksNumber=None,
        IeeeL1Defaults=None,
        LaserOn=None,
        LoopContinuously=None,
        LoopCountNumber=None,
        Loopback=None,
        LoopbackMode=None,
        Ppm=None,
        RsFecAdvertise=None,
        RsFecForceOn=None,
        RsFecRequest=None,
        SelectedSpeeds=None,
        SendSetsMode=None,
        Speed=None,
        StartErrorInsertion=None,
        TxIgnoreRxLinkFaults=None,
        TypeAOrderedSets=None,
        TypeBOrderedSets=None,
        UseANResults=None,
    ):
        # type: (str, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, int, bool, bool, bool, int, bool, str, int, bool, bool, bool, List[str], str, str, bool, bool, str, str, bool) -> Novus5GTenTwentyFiveGigLan
        """Updates novus5GTenTwentyFiveGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - BadBlocksNumber (number):
        - EnableAutoNegotiation (bool):
        - EnablePPM (bool): If true, enables the portsppm.
        - EnableRsFec (bool):
        - EnableRsFecStats (bool):
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FirecodeAdvertise (bool):
        - FirecodeForceOff (bool):
        - FirecodeForceOn (bool):
        - FirecodeRequest (bool):
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - ForceDisableFEC (bool):
        - GoodBlocksNumber (number):
        - IeeeL1Defaults (bool):
        - LaserOn (bool):
        - LoopContinuously (bool):
        - LoopCountNumber (number):
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(none | lineLoopback | internalLoopback)):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - RsFecAdvertise (bool):
        - RsFecForceOn (bool):
        - RsFecRequest (bool):
        - SelectedSpeeds (list(str[speed100g | speed25g | speed50g | speed10g])): Which speeds are selected for the current media and AN settings.
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)):
        - Speed (str(speed100g | speed10g | speed25g | speed50g)):
        - StartErrorInsertion (bool):
        - TxIgnoreRxLinkFaults (bool):
        - TypeAOrderedSets (str(localFault | remoteFault)):
        - TypeBOrderedSets (str(localFault | remoteFault)):
        - UseANResults (bool):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AvailableSpeeds=None,
        BadBlocksNumber=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        EnableAutoNegotiation=None,
        EnablePPM=None,
        EnableRsFec=None,
        EnableRsFecStats=None,
        EnabledFlowControl=None,
        FirecodeAdvertise=None,
        FirecodeForceOff=None,
        FirecodeForceOn=None,
        FirecodeRequest=None,
        FlowControlDirectedAddress=None,
        ForceDisableFEC=None,
        GoodBlocksNumber=None,
        IeeeL1Defaults=None,
        LaserOn=None,
        LinkTraining=None,
        LoopContinuously=None,
        LoopCountNumber=None,
        Loopback=None,
        LoopbackMode=None,
        Ppm=None,
        RsFecAdvertise=None,
        RsFecForceOn=None,
        RsFecRequest=None,
        SelectedSpeeds=None,
        SendSetsMode=None,
        Speed=None,
        StartErrorInsertion=None,
        TxIgnoreRxLinkFaults=None,
        TypeAOrderedSets=None,
        TypeBOrderedSets=None,
        UseANResults=None,
    ):
        # type: (str, List[str], int, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, str, bool, int, bool, bool, bool, bool, int, bool, str, int, bool, bool, bool, List[str], str, str, bool, bool, str, str, bool) -> Novus5GTenTwentyFiveGigLan
        """Finds and retrieves novus5GTenTwentyFiveGigLan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve novus5GTenTwentyFiveGigLan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all novus5GTenTwentyFiveGigLan resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - AvailableSpeeds (list(str[speed100g | speed25g | speed50g | speed10g])): Which speeds are available for the current media and AN settings.
        - BadBlocksNumber (number):
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - EnableAutoNegotiation (bool):
        - EnablePPM (bool): If true, enables the portsppm.
        - EnableRsFec (bool):
        - EnableRsFecStats (bool):
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control mechanisms to listen for a directed address pause message.
        - FirecodeAdvertise (bool):
        - FirecodeForceOff (bool):
        - FirecodeForceOn (bool):
        - FirecodeRequest (bool):
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - ForceDisableFEC (bool):
        - GoodBlocksNumber (number):
        - IeeeL1Defaults (bool):
        - LaserOn (bool):
        - LinkTraining (bool):
        - LoopContinuously (bool):
        - LoopCountNumber (number):
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(none | lineLoopback | internalLoopback)):
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - RsFecAdvertise (bool):
        - RsFecForceOn (bool):
        - RsFecRequest (bool):
        - SelectedSpeeds (list(str[speed100g | speed25g | speed50g | speed10g])): Which speeds are selected for the current media and AN settings.
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)):
        - Speed (str(speed100g | speed10g | speed25g | speed50g)):
        - StartErrorInsertion (bool):
        - TxIgnoreRxLinkFaults (bool):
        - TypeAOrderedSets (str(localFault | remoteFault)):
        - TypeBOrderedSets (str(localFault | remoteFault)):
        - UseANResults (bool):

        Returns
        -------
        - self: This instance with matching novus5GTenTwentyFiveGigLan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of novus5GTenTwentyFiveGigLan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the novus5GTenTwentyFiveGigLan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
