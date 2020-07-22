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


class NovusHundredGigLan(Base):
    """Novus 100GE LAN port.
    The NovusHundredGigLan class encapsulates a required novusHundredGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'novusHundredGigLan'
    _SDM_ATT_MAP = {
        'AutoInstrumentation': 'autoInstrumentation',
        'AvailableSpeeds': 'availableSpeeds',
        'BadBlocksNumber': 'badBlocksNumber',
        'CanModifySpeed': 'canModifySpeed',
        'CanSetMultipleSpeeds': 'canSetMultipleSpeeds',
        'EnableAutoNegotiation': 'enableAutoNegotiation',
        'EnablePPM': 'enablePPM',
        'EnableRsFec': 'enableRsFec',
        'EnableRsFecStats': 'enableRsFecStats',
        'EnabledFlowControl': 'enabledFlowControl',
        'FirecodeAdvertise': 'firecodeAdvertise',
        'FirecodeForceOff': 'firecodeForceOff',
        'FirecodeForceOn': 'firecodeForceOn',
        'FirecodeRequest': 'firecodeRequest',
        'FlowControlDirectedAddress': 'flowControlDirectedAddress',
        'ForceDisableFEC': 'forceDisableFEC',
        'GoodBlocksNumber': 'goodBlocksNumber',
        'IeeeL1Defaults': 'ieeeL1Defaults',
        'LaserOn': 'laserOn',
        'LinkTraining': 'linkTraining',
        'LoopContinuously': 'loopContinuously',
        'LoopCountNumber': 'loopCountNumber',
        'Loopback': 'loopback',
        'LoopbackMode': 'loopbackMode',
        'Ppm': 'ppm',
        'RsFecAdvertise': 'rsFecAdvertise',
        'RsFecForceOn': 'rsFecForceOn',
        'RsFecRequest': 'rsFecRequest',
        'SelectedSpeeds': 'selectedSpeeds',
        'SendSetsMode': 'sendSetsMode',
        'Speed': 'speed',
        'StartErrorInsertion': 'startErrorInsertion',
        'TxIgnoreRxLinkFaults': 'txIgnoreRxLinkFaults',
        'TypeAOrderedSets': 'typeAOrderedSets',
        'TypeBOrderedSets': 'typeBOrderedSets',
        'UseANResults': 'useANResults',
    }

    def __init__(self, parent):
        super(NovusHundredGigLan, self).__init__(parent)

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.fcoe.fcoe import Fcoe
        return Fcoe(self)._select()

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
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernet.txlane.txlane import TxLane
        return TxLane(self)._select()

    @property
    def AutoInstrumentation(self):
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoInstrumentation'])
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoInstrumentation'], value)

    @property
    def AvailableSpeeds(self):
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed10g | speed40g]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableSpeeds'])

    @property
    def BadBlocksNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['BadBlocksNumber'])
    @BadBlocksNumber.setter
    def BadBlocksNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BadBlocksNumber'], value)

    @property
    def CanModifySpeed(self):
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanModifySpeed'])

    @property
    def CanSetMultipleSpeeds(self):
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CanSetMultipleSpeeds'])

    @property
    def EnableAutoNegotiation(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoNegotiation'])
    @EnableAutoNegotiation.setter
    def EnableAutoNegotiation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoNegotiation'], value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePPM'])
    @EnablePPM.setter
    def EnablePPM(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePPM'], value)

    @property
    def EnableRsFec(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRsFec'])
    @EnableRsFec.setter
    def EnableRsFec(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRsFec'], value)

    @property
    def EnableRsFecStats(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRsFecStats'])
    @EnableRsFecStats.setter
    def EnableRsFecStats(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRsFecStats'], value)

    @property
    def EnabledFlowControl(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnabledFlowControl'])
    @EnabledFlowControl.setter
    def EnabledFlowControl(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnabledFlowControl'], value)

    @property
    def FirecodeAdvertise(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeAdvertise'])
    @FirecodeAdvertise.setter
    def FirecodeAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeAdvertise'], value)

    @property
    def FirecodeForceOff(self):
        """DEPRECATED 
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeForceOff'])
    @FirecodeForceOff.setter
    def FirecodeForceOff(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeForceOff'], value)

    @property
    def FirecodeForceOn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeForceOn'])
    @FirecodeForceOn.setter
    def FirecodeForceOn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeForceOn'], value)

    @property
    def FirecodeRequest(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirecodeRequest'])
    @FirecodeRequest.setter
    def FirecodeRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirecodeRequest'], value)

    @property
    def FlowControlDirectedAddress(self):
        """
        Returns
        -------
        - str: The 48-bit MAC address that the port listens on for a directed pause.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowControlDirectedAddress'])
    @FlowControlDirectedAddress.setter
    def FlowControlDirectedAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowControlDirectedAddress'], value)

    @property
    def ForceDisableFEC(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ForceDisableFEC'])
    @ForceDisableFEC.setter
    def ForceDisableFEC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ForceDisableFEC'], value)

    @property
    def GoodBlocksNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['GoodBlocksNumber'])
    @GoodBlocksNumber.setter
    def GoodBlocksNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GoodBlocksNumber'], value)

    @property
    def IeeeL1Defaults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IeeeL1Defaults'])
    @IeeeL1Defaults.setter
    def IeeeL1Defaults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IeeeL1Defaults'], value)

    @property
    def LaserOn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LaserOn'])
    @LaserOn.setter
    def LaserOn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LaserOn'], value)

    @property
    def LinkTraining(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkTraining'])

    @property
    def LoopContinuously(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopContinuously'])
    @LoopContinuously.setter
    def LoopContinuously(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoopContinuously'], value)

    @property
    def LoopCountNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopCountNumber'])
    @LoopCountNumber.setter
    def LoopCountNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoopCountNumber'], value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Loopback'])
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Loopback'], value)

    @property
    def LoopbackMode(self):
        """
        Returns
        -------
        - str(internalLoopback | lineLoopback | none): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LoopbackMode'])
    @LoopbackMode.setter
    def LoopbackMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LoopbackMode'], value)

    @property
    def Ppm(self):
        """
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ppm'])
    @Ppm.setter
    def Ppm(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ppm'], value)

    @property
    def RsFecAdvertise(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecAdvertise'])
    @RsFecAdvertise.setter
    def RsFecAdvertise(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecAdvertise'], value)

    @property
    def RsFecForceOn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecForceOn'])
    @RsFecForceOn.setter
    def RsFecForceOn(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecForceOn'], value)

    @property
    def RsFecRequest(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecRequest'])
    @RsFecRequest.setter
    def RsFecRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecRequest'], value)

    @property
    def SelectedSpeeds(self):
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed10g | speed40g]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SelectedSpeeds'])
    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SelectedSpeeds'], value)

    @property
    def SendSetsMode(self):
        """
        Returns
        -------
        - str(alternate | typeAOnly | typeBOnly): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['SendSetsMode'])
    @SendSetsMode.setter
    def SendSetsMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SendSetsMode'], value)

    @property
    def Speed(self):
        """
        Returns
        -------
        - str(speed100g | speed10g | speed25g | speed40g | speed50g): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Speed'])
    @Speed.setter
    def Speed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Speed'], value)

    @property
    def StartErrorInsertion(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartErrorInsertion'])
    @StartErrorInsertion.setter
    def StartErrorInsertion(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartErrorInsertion'], value)

    @property
    def TxIgnoreRxLinkFaults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TxIgnoreRxLinkFaults'])
    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TxIgnoreRxLinkFaults'], value)

    @property
    def TypeAOrderedSets(self):
        """
        Returns
        -------
        - str(localFault | remoteFault): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeAOrderedSets'])
    @TypeAOrderedSets.setter
    def TypeAOrderedSets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeAOrderedSets'], value)

    @property
    def TypeBOrderedSets(self):
        """
        Returns
        -------
        - str(localFault | remoteFault): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TypeBOrderedSets'])
    @TypeBOrderedSets.setter
    def TypeBOrderedSets(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TypeBOrderedSets'], value)

    @property
    def UseANResults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseANResults'])
    @UseANResults.setter
    def UseANResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseANResults'], value)

    def update(self, AutoInstrumentation=None, BadBlocksNumber=None, EnableAutoNegotiation=None, EnablePPM=None, EnableRsFec=None, EnableRsFecStats=None, EnabledFlowControl=None, FirecodeAdvertise=None, FirecodeForceOff=None, FirecodeForceOn=None, FirecodeRequest=None, FlowControlDirectedAddress=None, ForceDisableFEC=None, GoodBlocksNumber=None, IeeeL1Defaults=None, LaserOn=None, LoopContinuously=None, LoopCountNumber=None, Loopback=None, LoopbackMode=None, Ppm=None, RsFecAdvertise=None, RsFecForceOn=None, RsFecRequest=None, SelectedSpeeds=None, SendSetsMode=None, Speed=None, StartErrorInsertion=None, TxIgnoreRxLinkFaults=None, TypeAOrderedSets=None, TypeBOrderedSets=None, UseANResults=None):
        """Updates novusHundredGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - BadBlocksNumber (number): NOT DEFINED
        - EnableAutoNegotiation (bool): NOT DEFINED
        - EnablePPM (bool): If true, enables the portsppm.
        - EnableRsFec (bool): NOT DEFINED
        - EnableRsFecStats (bool): NOT DEFINED
        - EnabledFlowControl (bool): NOT DEFINED
        - FirecodeAdvertise (bool): NOT DEFINED
        - FirecodeForceOff (bool): NOT DEFINED
        - FirecodeForceOn (bool): NOT DEFINED
        - FirecodeRequest (bool): NOT DEFINED
        - FlowControlDirectedAddress (str): The 48-bit MAC address that the port listens on for a directed pause.
        - ForceDisableFEC (bool): NOT DEFINED
        - GoodBlocksNumber (number): NOT DEFINED
        - IeeeL1Defaults (bool): NOT DEFINED
        - LaserOn (bool): NOT DEFINED
        - LoopContinuously (bool): NOT DEFINED
        - LoopCountNumber (number): NOT DEFINED
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(internalLoopback | lineLoopback | none)): NOT DEFINED
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency.
        - RsFecAdvertise (bool): NOT DEFINED
        - RsFecForceOn (bool): NOT DEFINED
        - RsFecRequest (bool): NOT DEFINED
        - SelectedSpeeds (list(str[speed100g | speed25g | speed50g | speed10g | speed40g])): Which speeds are selected for the current media and AN settings.
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)): NOT DEFINED
        - Speed (str(speed100g | speed10g | speed25g | speed40g | speed50g)): NOT DEFINED
        - StartErrorInsertion (bool): NOT DEFINED
        - TxIgnoreRxLinkFaults (bool): NOT DEFINED
        - TypeAOrderedSets (str(localFault | remoteFault)): NOT DEFINED
        - TypeBOrderedSets (str(localFault | remoteFault)): NOT DEFINED
        - UseANResults (bool): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
