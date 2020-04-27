# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class TenFortyHundredGigLan(Base):
    """10GE/40GE/100GE LAN
    The TenFortyHundredGigLan class encapsulates a required tenFortyHundredGigLan resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'tenFortyHundredGigLan'

    def __init__(self, parent):
        super(TenFortyHundredGigLan, self).__init__(parent)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.fcoe.fcoe import Fcoe
        return Fcoe(self)._select()

    @property
    def TxLane(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.txlane.txlane.TxLane): An instance of the TxLane class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.tenfortyhundredgiglan.txlane.txlane import TxLane
        return TxLane(self)._select()

    @property
    def AutoInstrumentation(self):
        """
        Returns
        -------
        - str(endOfFrame | floating): The auto instrumentation mode.
        """
        return self._get_attribute('autoInstrumentation')
    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        self._set_attribute('autoInstrumentation', value)

    @property
    def BadBlocksNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('badBlocksNumber')
    @BadBlocksNumber.setter
    def BadBlocksNumber(self, value):
        self._set_attribute('badBlocksNumber', value)

    @property
    def EnableAutoNegotiation(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableAutoNegotiation')
    @EnableAutoNegotiation.setter
    def EnableAutoNegotiation(self, value):
        self._set_attribute('enableAutoNegotiation', value)

    @property
    def EnablePPM(self):
        """
        Returns
        -------
        - bool: If true, enables the portsppm.
        """
        return self._get_attribute('enablePPM')
    @EnablePPM.setter
    def EnablePPM(self, value):
        self._set_attribute('enablePPM', value)

    @property
    def EnableRsFec(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableRsFec')
    @EnableRsFec.setter
    def EnableRsFec(self, value):
        self._set_attribute('enableRsFec', value)

    @property
    def EnableRsFecStats(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('enableRsFecStats')
    @EnableRsFecStats.setter
    def EnableRsFecStats(self, value):
        self._set_attribute('enableRsFecStats', value)

    @property
    def EnabledFlowControl(self):
        """
        Returns
        -------
        - bool: If true, enables the port's MAC flow control and mechanisms to listen for a directed address pause message.
        """
        return self._get_attribute('enabledFlowControl')
    @EnabledFlowControl.setter
    def EnabledFlowControl(self, value):
        self._set_attribute('enabledFlowControl', value)

    @property
    def FlowControlDirectedAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('flowControlDirectedAddress')
    @FlowControlDirectedAddress.setter
    def FlowControlDirectedAddress(self, value):
        self._set_attribute('flowControlDirectedAddress', value)

    @property
    def GoodBlocksNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('goodBlocksNumber')
    @GoodBlocksNumber.setter
    def GoodBlocksNumber(self, value):
        self._set_attribute('goodBlocksNumber', value)

    @property
    def IeeeL1Defaults(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('ieeeL1Defaults')
    @IeeeL1Defaults.setter
    def IeeeL1Defaults(self, value):
        self._set_attribute('ieeeL1Defaults', value)

    @property
    def LaserOn(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('laserOn')
    @LaserOn.setter
    def LaserOn(self, value):
        self._set_attribute('laserOn', value)

    @property
    def LinkTraining(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('linkTraining')
    @LinkTraining.setter
    def LinkTraining(self, value):
        self._set_attribute('linkTraining', value)

    @property
    def LoopContinuously(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('loopContinuously')
    @LoopContinuously.setter
    def LoopContinuously(self, value):
        self._set_attribute('loopContinuously', value)

    @property
    def LoopCountNumber(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('loopCountNumber')
    @LoopCountNumber.setter
    def LoopCountNumber(self, value):
        self._set_attribute('loopCountNumber', value)

    @property
    def Loopback(self):
        """
        Returns
        -------
        - bool: If enabled, the port is set to internally loopback from transmit to receive.
        """
        return self._get_attribute('loopback')
    @Loopback.setter
    def Loopback(self, value):
        self._set_attribute('loopback', value)

    @property
    def LoopbackMode(self):
        """
        Returns
        -------
        - str(internalLoopback | lineLoopback | none): NOT DEFINED
        """
        return self._get_attribute('loopbackMode')
    @LoopbackMode.setter
    def LoopbackMode(self, value):
        self._set_attribute('loopbackMode', value)

    @property
    def Ppm(self):
        """
        Returns
        -------
        - number: Indicates the value that needs to be adjusted for the line transmit frequency
        """
        return self._get_attribute('ppm')
    @Ppm.setter
    def Ppm(self, value):
        self._set_attribute('ppm', value)

    @property
    def SendSetsMode(self):
        """
        Returns
        -------
        - str(alternate | typeAOnly | typeBOnly): NOT DEFINED
        """
        return self._get_attribute('sendSetsMode')
    @SendSetsMode.setter
    def SendSetsMode(self, value):
        self._set_attribute('sendSetsMode', value)

    @property
    def Speed(self):
        """
        Returns
        -------
        - str(speed100g | speed10g | speed25g | speed40g | speed50g): The speed of the lan
        """
        return self._get_attribute('speed')
    @Speed.setter
    def Speed(self, value):
        self._set_attribute('speed', value)

    @property
    def StartErrorInsertion(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute('startErrorInsertion')
    @StartErrorInsertion.setter
    def StartErrorInsertion(self, value):
        self._set_attribute('startErrorInsertion', value)

    @property
    def TxIgnoreRxLinkFaults(self):
        """
        Returns
        -------
        - bool: If enabled, will allow transmission of packets even if the receive link is down.
        """
        return self._get_attribute('txIgnoreRxLinkFaults')
    @TxIgnoreRxLinkFaults.setter
    def TxIgnoreRxLinkFaults(self, value):
        self._set_attribute('txIgnoreRxLinkFaults', value)

    @property
    def TypeAOrderedSets(self):
        """
        Returns
        -------
        - str(localFault | remoteFault): NOT DEFINED
        """
        return self._get_attribute('typeAOrderedSets')
    @TypeAOrderedSets.setter
    def TypeAOrderedSets(self, value):
        self._set_attribute('typeAOrderedSets', value)

    @property
    def TypeBOrderedSets(self):
        """
        Returns
        -------
        - str(localFault | remoteFault): NOT DEFINED
        """
        return self._get_attribute('typeBOrderedSets')
    @TypeBOrderedSets.setter
    def TypeBOrderedSets(self, value):
        self._set_attribute('typeBOrderedSets', value)

    def update(self, AutoInstrumentation=None, BadBlocksNumber=None, EnableAutoNegotiation=None, EnablePPM=None, EnableRsFec=None, EnableRsFecStats=None, EnabledFlowControl=None, FlowControlDirectedAddress=None, GoodBlocksNumber=None, IeeeL1Defaults=None, LaserOn=None, LinkTraining=None, LoopContinuously=None, LoopCountNumber=None, Loopback=None, LoopbackMode=None, Ppm=None, SendSetsMode=None, Speed=None, StartErrorInsertion=None, TxIgnoreRxLinkFaults=None, TypeAOrderedSets=None, TypeBOrderedSets=None):
        """Updates tenFortyHundredGigLan resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)): The auto instrumentation mode.
        - BadBlocksNumber (number): NOT DEFINED
        - EnableAutoNegotiation (bool): NOT DEFINED
        - EnablePPM (bool): If true, enables the portsppm.
        - EnableRsFec (bool): NOT DEFINED
        - EnableRsFecStats (bool): NOT DEFINED
        - EnabledFlowControl (bool): If true, enables the port's MAC flow control and mechanisms to listen for a directed address pause message.
        - FlowControlDirectedAddress (str): NOT DEFINED
        - GoodBlocksNumber (number): NOT DEFINED
        - IeeeL1Defaults (bool): NOT DEFINED
        - LaserOn (bool): NOT DEFINED
        - LinkTraining (bool): NOT DEFINED
        - LoopContinuously (bool): NOT DEFINED
        - LoopCountNumber (number): NOT DEFINED
        - Loopback (bool): If enabled, the port is set to internally loopback from transmit to receive.
        - LoopbackMode (str(internalLoopback | lineLoopback | none)): NOT DEFINED
        - Ppm (number): Indicates the value that needs to be adjusted for the line transmit frequency
        - SendSetsMode (str(alternate | typeAOnly | typeBOnly)): NOT DEFINED
        - Speed (str(speed100g | speed10g | speed25g | speed40g | speed50g)): The speed of the lan
        - StartErrorInsertion (bool): NOT DEFINED
        - TxIgnoreRxLinkFaults (bool): If enabled, will allow transmission of packets even if the receive link is down.
        - TypeAOrderedSets (str(localFault | remoteFault)): NOT DEFINED
        - TypeBOrderedSets (str(localFault | remoteFault)): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())
