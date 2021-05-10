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


class Fcoe(Base):
    """
    The Fcoe class encapsulates a required fcoe resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'fcoe'
    _SDM_ATT_MAP = {
        'EnablePFCPauseDelay': 'enablePFCPauseDelay',
        'FlowControlType': 'flowControlType',
        'PfcPauseDelay': 'pfcPauseDelay',
        'PfcPriorityGroups': 'pfcPriorityGroups',
        'PriorityGroupSize': 'priorityGroupSize',
        'SupportDataCenterMode': 'supportDataCenterMode',
    }

    def __init__(self, parent):
        super(Fcoe, self).__init__(parent)

    @property
    def EnablePFCPauseDelay(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePFCPauseDelay'])
    @EnablePFCPauseDelay.setter
    def EnablePFCPauseDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePFCPauseDelay'], value)

    @property
    def FlowControlType(self):
        """
        Returns
        -------
        - str(ieee802.1Qbb | ieee802.3x): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowControlType'])
    @FlowControlType.setter
    def FlowControlType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FlowControlType'], value)

    @property
    def PfcPauseDelay(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PfcPauseDelay'])
    @PfcPauseDelay.setter
    def PfcPauseDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PfcPauseDelay'], value)

    @property
    def PfcPriorityGroups(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PfcPriorityGroups'])
    @PfcPriorityGroups.setter
    def PfcPriorityGroups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PfcPriorityGroups'], value)

    @property
    def PriorityGroupSize(self):
        """
        Returns
        -------
        - str(priorityGroupSize-4 | priorityGroupSize-8): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityGroupSize'])
    @PriorityGroupSize.setter
    def PriorityGroupSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PriorityGroupSize'], value)

    @property
    def SupportDataCenterMode(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportDataCenterMode'])
    @SupportDataCenterMode.setter
    def SupportDataCenterMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportDataCenterMode'], value)

    def update(self, EnablePFCPauseDelay=None, FlowControlType=None, PfcPauseDelay=None, PfcPriorityGroups=None, PriorityGroupSize=None, SupportDataCenterMode=None):
        """Updates fcoe resource on the server.

        Args
        ----
        - EnablePFCPauseDelay (bool): 
        - FlowControlType (str(ieee802.1Qbb | ieee802.3x)): 
        - PfcPauseDelay (number): 
        - PfcPriorityGroups (list(str)): 
        - PriorityGroupSize (str(priorityGroupSize-4 | priorityGroupSize-8)): 
        - SupportDataCenterMode (bool): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
