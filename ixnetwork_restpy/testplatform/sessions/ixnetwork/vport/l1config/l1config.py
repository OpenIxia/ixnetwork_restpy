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


class L1Config(Base):
    """Layer 1 (physical) configuration.
    The L1Config class encapsulates a required l1Config resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "l1Config"
    _SDM_ATT_MAP = {
        "CurrentType": "currentType",
    }
    _SDM_ENUM_MAP = {
        "currentType": [
            "ethernet",
            "ethernetvm",
            "ethernetcm",
            "novusmini",
            "novusminipro",
            "ethernetFcoe",
            "atm",
            "pos",
            "tenGigLan",
            "tenGigLanFcoe",
            "fortyGigLan",
            "fortyGigLanFcoe",
            "tenGigWan",
            "tenGigWanFcoe",
            "hundredGigLan",
            "hundredGigLanFcoe",
            "tenFortyHundredGigLan",
            "tenFortyHundredGigLanFcoe",
            "fc",
            "ethernetImpairment",
            "novusHundredGigLan",
            "novusHundredGigLanFcoe",
            "novusTenGigLan",
            "novusTenGigLanFcoe",
            "krakenFourHundredGigLan",
            "krakenFourHundredGigLanFcoe",
            "aresOneFourHundredGigLan",
            "aresOneFourHundredGigLanFcoe",
            "uhdOneHundredGigLan",
            "novus5GTenTwentyFiveGigLan",
            "novus5GTenTwentyFiveGigLanFcoe",
            "starFourHundredGigLan",
            "starFourHundredGigLanFcoe",
            "ravenEightHundredGigLan",
            "ravenEightHundredGigLanFcoe",
            "aresOneEightHundredGigLanQddC",
            "aresOneEightHundredGigLanQddCFcoe",
            "sertHundredGigLan",
            "aresOneEightHundredGigLanOsfpC",
            "aresOneEightHundredGigLanOsfpCFcoe",
            "aresOneM",
            "aresOneMFcoe",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(L1Config, self).__init__(parent, list_op)

    @property
    def OAM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.oam.oam.OAM): An instance of the OAM class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.oam.oam import (
            OAM,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OAM", None) is not None:
                return self._properties.get("OAM")
        return OAM(self)._select()

    @property
    def AresOneEightHundredGigLanOsfpC(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresoneeighthundredgiglanosfpc.aresoneeighthundredgiglanosfpc.AresOneEightHundredGigLanOsfpC): An instance of the AresOneEightHundredGigLanOsfpC class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresoneeighthundredgiglanosfpc.aresoneeighthundredgiglanosfpc import (
            AresOneEightHundredGigLanOsfpC,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AresOneEightHundredGigLanOsfpC", None) is not None:
                return self._properties.get("AresOneEightHundredGigLanOsfpC")
        return AresOneEightHundredGigLanOsfpC(self)._select()

    @property
    def AresOneEightHundredGigLanQddC(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresoneeighthundredgiglanqddc.aresoneeighthundredgiglanqddc.AresOneEightHundredGigLanQddC): An instance of the AresOneEightHundredGigLanQddC class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresoneeighthundredgiglanqddc.aresoneeighthundredgiglanqddc import (
            AresOneEightHundredGigLanQddC,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AresOneEightHundredGigLanQddC", None) is not None:
                return self._properties.get("AresOneEightHundredGigLanQddC")
        return AresOneEightHundredGigLanQddC(self)._select()

    @property
    def AresOneFourHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresonefourhundredgiglan.aresonefourhundredgiglan.AresOneFourHundredGigLan): An instance of the AresOneFourHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresonefourhundredgiglan.aresonefourhundredgiglan import (
            AresOneFourHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AresOneFourHundredGigLan", None) is not None:
                return self._properties.get("AresOneFourHundredGigLan")
        return AresOneFourHundredGigLan(self)._select()

    @property
    def AresOneM(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresonem.aresonem.AresOneM): An instance of the AresOneM class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresonem.aresonem import (
            AresOneM,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AresOneM", None) is not None:
                return self._properties.get("AresOneM")
        return AresOneM(self)._select()

    @property
    def AtlasFourHundredGigLan(self):
        """DEPRECATED
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.atlasfourhundredgiglan.atlasfourhundredgiglan.AtlasFourHundredGigLan): An instance of the AtlasFourHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.atlasfourhundredgiglan.atlasfourhundredgiglan import (
            AtlasFourHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AtlasFourHundredGigLan", None) is not None:
                return self._properties.get("AtlasFourHundredGigLan")
        return AtlasFourHundredGigLan(self)._select()

    @property
    def Atm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.atm.atm.Atm): An instance of the Atm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.atm.atm import (
            Atm,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Atm", None) is not None:
                return self._properties.get("Atm")
        return Atm(self)._select()

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.ethernet.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.ethernet import (
            Ethernet,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ethernet", None) is not None:
                return self._properties.get("Ethernet")
        return Ethernet(self)._select()

    @property
    def EthernetImpairment(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetimpairment.ethernetimpairment.EthernetImpairment): An instance of the EthernetImpairment class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetimpairment.ethernetimpairment import (
            EthernetImpairment,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EthernetImpairment", None) is not None:
                return self._properties.get("EthernetImpairment")
        return EthernetImpairment(self)._select()

    @property
    def Ethernetcm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetcm.ethernetcm.Ethernetcm): An instance of the Ethernetcm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetcm.ethernetcm import (
            Ethernetcm,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ethernetcm", None) is not None:
                return self._properties.get("Ethernetcm")
        return Ethernetcm(self)._select()

    @property
    def Ethernetvm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetvm.ethernetvm.Ethernetvm): An instance of the Ethernetvm class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetvm.ethernetvm import (
            Ethernetvm,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ethernetvm", None) is not None:
                return self._properties.get("Ethernetvm")
        return Ethernetvm(self)._select()

    @property
    def Fc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fc.fc.Fc): An instance of the Fc class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fc.fc import (
            Fc,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fc", None) is not None:
                return self._properties.get("Fc")
        return Fc(self)._select()

    @property
    def FecErrorInsertion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fecerrorinsertion.fecerrorinsertion.FecErrorInsertion): An instance of the FecErrorInsertion class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fecerrorinsertion.fecerrorinsertion import (
            FecErrorInsertion,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FecErrorInsertion", None) is not None:
                return self._properties.get("FecErrorInsertion")
        return FecErrorInsertion(self)._select()

    @property
    def FortyGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fortygiglan.fortygiglan.FortyGigLan): An instance of the FortyGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fortygiglan.fortygiglan import (
            FortyGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FortyGigLan", None) is not None:
                return self._properties.get("FortyGigLan")
        return FortyGigLan(self)._select()

    @property
    def FramePreemption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.framepreemption.framepreemption.FramePreemption): An instance of the FramePreemption class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.framepreemption.framepreemption import (
            FramePreemption,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("FramePreemption", None) is not None:
                return self._properties.get("FramePreemption")
        return FramePreemption(self)._select()

    @property
    def HundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.hundredgiglan.HundredGigLan): An instance of the HundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.hundredgiglan import (
            HundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("HundredGigLan", None) is not None:
                return self._properties.get("HundredGigLan")
        return HundredGigLan(self)._select()

    @property
    def KrakenFourHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.krakenfourhundredgiglan.krakenfourhundredgiglan.KrakenFourHundredGigLan): An instance of the KrakenFourHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.krakenfourhundredgiglan.krakenfourhundredgiglan import (
            KrakenFourHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("KrakenFourHundredGigLan", None) is not None:
                return self._properties.get("KrakenFourHundredGigLan")
        return KrakenFourHundredGigLan(self)._select()

    @property
    def Novus5GTenTwentyFiveGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novus5gtentwentyfivegiglan.novus5gtentwentyfivegiglan.Novus5GTenTwentyFiveGigLan): An instance of the Novus5GTenTwentyFiveGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novus5gtentwentyfivegiglan.novus5gtentwentyfivegiglan import (
            Novus5GTenTwentyFiveGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Novus5GTenTwentyFiveGigLan", None) is not None:
                return self._properties.get("Novus5GTenTwentyFiveGigLan")
        return Novus5GTenTwentyFiveGigLan(self)._select()

    @property
    def NovusHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.novushundredgiglan.NovusHundredGigLan): An instance of the NovusHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.novushundredgiglan import (
            NovusHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NovusHundredGigLan", None) is not None:
                return self._properties.get("NovusHundredGigLan")
        return NovusHundredGigLan(self)._select()

    @property
    def NovusTenGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.novustengiglan.NovusTenGigLan): An instance of the NovusTenGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.novustengiglan import (
            NovusTenGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("NovusTenGigLan", None) is not None:
                return self._properties.get("NovusTenGigLan")
        return NovusTenGigLan(self)._select()

    @property
    def Novusmini(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novusmini.novusmini.Novusmini): An instance of the Novusmini class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novusmini.novusmini import (
            Novusmini,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Novusmini", None) is not None:
                return self._properties.get("Novusmini")
        return Novusmini(self)._select()

    @property
    def Novusminipro(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novusminipro.novusminipro.Novusminipro): An instance of the Novusminipro class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novusminipro.novusminipro import (
            Novusminipro,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Novusminipro", None) is not None:
                return self._properties.get("Novusminipro")
        return Novusminipro(self)._select()

    @property
    def PcsErrorGeneration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pcserrorgeneration.pcserrorgeneration.PcsErrorGeneration): An instance of the PcsErrorGeneration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pcserrorgeneration.pcserrorgeneration import (
            PcsErrorGeneration,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PcsErrorGeneration", None) is not None:
                return self._properties.get("PcsErrorGeneration")
        return PcsErrorGeneration(self)._select()

    @property
    def Plca(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.plca.plca.Plca): An instance of the Plca class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.plca.plca import (
            Plca,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Plca", None) is not None:
                return self._properties.get("Plca")
        return Plca(self)._select()

    @property
    def Pos(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.pos.Pos): An instance of the Pos class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.pos import (
            Pos,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Pos", None) is not None:
                return self._properties.get("Pos")
        return Pos(self)._select()

    @property
    def Qbv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.qbv.qbv.Qbv): An instance of the Qbv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.qbv.qbv import (
            Qbv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Qbv", None) is not None:
                return self._properties.get("Qbv")
        return Qbv(self)._select()

    @property
    def RavenEightHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.raveneighthundredgiglan.raveneighthundredgiglan.RavenEightHundredGigLan): An instance of the RavenEightHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.raveneighthundredgiglan.raveneighthundredgiglan import (
            RavenEightHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RavenEightHundredGigLan", None) is not None:
                return self._properties.get("RavenEightHundredGigLan")
        return RavenEightHundredGigLan(self)._select()

    @property
    def RxFilters(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.rxfilters.rxfilters.RxFilters): An instance of the RxFilters class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.rxfilters.rxfilters import (
            RxFilters,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RxFilters", None) is not None:
                return self._properties.get("RxFilters")
        return RxFilters(self)._select()

    @property
    def SertHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.serthundredgiglan.serthundredgiglan.SertHundredGigLan): An instance of the SertHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.serthundredgiglan.serthundredgiglan import (
            SertHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SertHundredGigLan", None) is not None:
                return self._properties.get("SertHundredGigLan")
        return SertHundredGigLan(self)._select()

    @property
    def StarFourHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.starfourhundredgiglan.starfourhundredgiglan.StarFourHundredGigLan): An instance of the StarFourHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.starfourhundredgiglan.starfourhundredgiglan import (
            StarFourHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StarFourHundredGigLan", None) is not None:
                return self._properties.get("StarFourHundredGigLan")
        return StarFourHundredGigLan(self)._select()

    @property
    def TenFortyHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.tenfortyhundredgiglan.TenFortyHundredGigLan): An instance of the TenFortyHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.tenfortyhundredgiglan import (
            TenFortyHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TenFortyHundredGigLan", None) is not None:
                return self._properties.get("TenFortyHundredGigLan")
        return TenFortyHundredGigLan(self)._select()

    @property
    def TenGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengiglan.tengiglan.TenGigLan): An instance of the TenGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengiglan.tengiglan import (
            TenGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TenGigLan", None) is not None:
                return self._properties.get("TenGigLan")
        return TenGigLan(self)._select()

    @property
    def TenGigWan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.tengigwan.TenGigWan): An instance of the TenGigWan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.tengigwan import (
            TenGigWan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("TenGigWan", None) is not None:
                return self._properties.get("TenGigWan")
        return TenGigWan(self)._select()

    @property
    def UhdOneHundredGigLan(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.uhdonehundredgiglan.uhdonehundredgiglan.UhdOneHundredGigLan): An instance of the UhdOneHundredGigLan class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.uhdonehundredgiglan.uhdonehundredgiglan import (
            UhdOneHundredGigLan,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("UhdOneHundredGigLan", None) is not None:
                return self._properties.get("UhdOneHundredGigLan")
        return UhdOneHundredGigLan(self)._select()

    @property
    def CurrentType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe): Indicates the types of ports for configuration to choose from.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentType"])

    @CurrentType.setter
    def CurrentType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["CurrentType"], value)

    def update(self, CurrentType=None):
        # type: (str) -> L1Config
        """Updates l1Config resource on the server.

        Args
        ----
        - CurrentType (str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe)): Indicates the types of ports for configuration to choose from.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CurrentType=None):
        # type: (str) -> L1Config
        """Finds and retrieves l1Config resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve l1Config resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all l1Config resources from the server.

        Args
        ----
        - CurrentType (str(ethernet | ethernetvm | ethernetcm | novusmini | novusminipro | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan | novus5GTenTwentyFiveGigLan | novus5GTenTwentyFiveGigLanFcoe | starFourHundredGigLan | starFourHundredGigLanFcoe | ravenEightHundredGigLan | ravenEightHundredGigLanFcoe | aresOneEightHundredGigLanQddC | aresOneEightHundredGigLanQddCFcoe | sertHundredGigLan | aresOneEightHundredGigLanOsfpC | aresOneEightHundredGigLanOsfpCFcoe | aresOneM | aresOneMFcoe)): Indicates the types of ports for configuration to choose from.

        Returns
        -------
        - self: This instance with matching l1Config resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of l1Config data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the l1Config resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
