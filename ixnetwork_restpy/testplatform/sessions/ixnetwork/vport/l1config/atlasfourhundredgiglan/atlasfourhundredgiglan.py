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


class AtlasFourHundredGigLan(Base):
    """DEPRECATED 
    The AtlasFourHundredGigLan class encapsulates a required atlasFourHundredGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'atlasFourHundredGigLan'
    _SDM_ATT_MAP = {
        'AutoInstrumentation': 'autoInstrumentation',
        'BadBlocksNumber': 'badBlocksNumber',
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
        'SendSetsMode': 'sendSetsMode',
        'Speed': 'speed',
        'StartErrorInsertion': 'startErrorInsertion',
        'TxIgnoreRxLinkFaults': 'txIgnoreRxLinkFaults',
        'TypeAOrderedSets': 'typeAOrderedSets',
        'TypeBOrderedSets': 'typeBOrderedSets',
        'UseANResults': 'useANResults',
    }

    def __init__(self, parent):
        super(AtlasFourHundredGigLan, self).__init__(parent)

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
    def AutoInstrumentation(self):
        """
        Returns
        -------
        - str(endOfFrame | floating): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoInstrumentation'])
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoInstrumentation'], value)

    @property
    def BadBlocksNumber(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['BadBlocksNumber'])
    @BadBlocksNumber.setter
    def BadBlocksNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BadBlocksNumber'], value)

    @property
    def EnableAutoNegotiation(self):
        """
        Returns
        -------
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
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
        - str: 
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
        - bool: 
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
        - number: 
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
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['IeeeL1Defaults'])

    @property
    def LaserOn(self):
        """
        Returns
        -------
        - bool: 
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
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkTraining'])
    @LinkTraining.setter
    def LinkTraining(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkTraining'], value)

    @property
    def LoopContinuously(self):
        """
        Returns
        -------
        - bool: 
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
        - number: 
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
        - bool: 
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
        - str(internalLoopback | lineLoopback | none): 
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
        - number: 
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
        - bool: 
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
        - bool: 
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
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RsFecRequest'])
    @RsFecRequest.setter
    def RsFecRequest(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RsFecRequest'], value)

    @property
    def SendSetsMode(self):
        """
        Returns
        -------
        - str(alternate | typeAOnly | typeBOnly): 
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
        - str(speed100g | speed200g | speed400g | speed50g): 
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
        - bool: 
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
        - bool: 
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
        - str(localFault | remoteFault): 
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
        - str(localFault | remoteFault): 
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
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseANResults'])
    @UseANResults.setter
    def UseANResults(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UseANResults'], value)

    def update(self, AutoInstrumentation=None, BadBlocksNumber=None, EnableAutoNegotiation=None, EnablePPM=None, EnableRsFec=None, EnableRsFecStats=None, EnabledFlowControl=None, FirecodeAdvertise=None, FirecodeForceOff=None, FirecodeForceOn=None, FirecodeRequest=None, FlowControlDirectedAddress=None, ForceDisableFEC=None, GoodBlocksNumber=None, LaserOn=None, LinkTraining=None, LoopContinuously=None, LoopCountNumber=None, Loopback=None, LoopbackMode=None, Ppm=None, RsFecAdvertise=None, RsFecForceOn=None, RsFecRequest=None, SendSetsMode=None, Speed=None, StartErrorInsertion=None, TxIgnoreRxLinkFaults=None, TypeAOrderedSets=None, TypeBOrderedSets=None, UseANResults=None):
        """Updates atlasFourHundredGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): 
        - BadBlocksNumber (number): 
        - EnableAutoNegotiation (bool): 
        - EnablePPM (bool): 
        - EnableRsFec (bool): 
        - EnableRsFecStats (bool): 
        - EnabledFlowControl (bool): 
        - FirecodeAdvertise (bool): 
        - FirecodeForceOff (bool): 
        - FirecodeForceOn (bool): 
        - FirecodeRequest (bool): 
        - FlowControlDirectedAddress (str): 
        - ForceDisableFEC (bool): 
        - GoodBlocksNumber (number): 
        - LaserOn (bool): 
        - LinkTraining (bool): 
        - LoopContinuously (bool): 
        - LoopCountNumber (number): 
        - Loopback (bool): 
        - LoopbackMode (str(internalLoopback | lineLoopback | none)): 
        - Ppm (number): 
        - RsFecAdvertise (bool): 
        - RsFecForceOn (bool): 
        - RsFecRequest (bool): 
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)): 
        - Speed (str(speed100g | speed200g | speed400g | speed50g)): 
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
