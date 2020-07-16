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


class L1Config(Base):
    """Layer 1 (physical) configuration.
    The L1Config class encapsulates a required l1Config resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'l1Config'
    _SDM_ATT_MAP = {
        'CurrentType': 'currentType',
    }

    def __init__(self, parent):
        super(L1Config, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.oam.oam import OAM
        return OAM(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.aresonefourhundredgiglan.aresonefourhundredgiglan import AresOneFourHundredGigLan
        return AresOneFourHundredGigLan(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.atlasfourhundredgiglan.atlasfourhundredgiglan import AtlasFourHundredGigLan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.atm.atm import Atm
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.ethernet import Ethernet
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetimpairment.ethernetimpairment import EthernetImpairment
        return EthernetImpairment(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetvm.ethernetvm import Ethernetvm
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fc.fc import Fc
        return Fc(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.fortygiglan.fortygiglan import FortyGigLan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.framepreemption.framepreemption import FramePreemption
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.hundredgiglan.hundredgiglan import HundredGigLan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.krakenfourhundredgiglan.krakenfourhundredgiglan import KrakenFourHundredGigLan
        return KrakenFourHundredGigLan(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novushundredgiglan.novushundredgiglan import NovusHundredGigLan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.novustengiglan.novustengiglan import NovusTenGigLan
        return NovusTenGigLan(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.pos.pos import Pos
        return Pos(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.rxfilters.rxfilters import RxFilters
        return RxFilters(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.tenfortyhundredgiglan import TenFortyHundredGigLan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengiglan.tengiglan import TenGigLan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tengigwan.tengigwan import TenGigWan
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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.uhdonehundredgiglan.uhdonehundredgiglan import UhdOneHundredGigLan
        return UhdOneHundredGigLan(self)._select()

    @property
    def CurrentType(self):
        """
        Returns
        -------
        - str(ethernet | ethernetvm | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan): Indicates the five types of ports for configuration to choose from.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CurrentType'])
    @CurrentType.setter
    def CurrentType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CurrentType'], value)

    def update(self, CurrentType=None):
        """Updates l1Config resource on the server.

        Args
        ----
        - CurrentType (str(ethernet | ethernetvm | ethernetFcoe | atm | pos | tenGigLan | tenGigLanFcoe | fortyGigLan | fortyGigLanFcoe | tenGigWan | tenGigWanFcoe | hundredGigLan | hundredGigLanFcoe | tenFortyHundredGigLan | tenFortyHundredGigLanFcoe | fc | ethernetImpairment | novusHundredGigLan | novusHundredGigLanFcoe | novusTenGigLan | novusTenGigLanFcoe | krakenFourHundredGigLan | krakenFourHundredGigLanFcoe | aresOneFourHundredGigLan | aresOneFourHundredGigLanFcoe | uhdOneHundredGigLan)): Indicates the five types of ports for configuration to choose from.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
