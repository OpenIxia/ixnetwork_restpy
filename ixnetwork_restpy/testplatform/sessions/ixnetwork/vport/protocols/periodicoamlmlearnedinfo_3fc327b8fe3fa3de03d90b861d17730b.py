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


class PeriodicOamLmLearnedInfo(Base):
    """NOT DEFINED
    The PeriodicOamLmLearnedInfo class encapsulates a list of periodicOamLmLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the PeriodicOamLmLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'periodicOamLmLearnedInfo'

    def __init__(self, parent):
        super(PeriodicOamLmLearnedInfo, self).__init__(parent)

    @property
    def AvgFarEndLoss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('avgFarEndLoss')

    @property
    def AvgNearEndLoss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('avgNearEndLoss')

    @property
    def BVlan(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('bVlan')

    @property
    def CVlan(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('cVlan')

    @property
    def CcmReceivedCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('ccmReceivedCount')

    @property
    def CcmSentCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('ccmSentCount')

    @property
    def CurrentFarEndLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('currentFarEndLoss')

    @property
    def CurrentFarEndLossRatio(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('currentFarEndLossRatio')

    @property
    def CurrentNearEndLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('currentNearEndLoss')

    @property
    def CurrentNearEndLossRatio(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('currentNearEndLossRatio')

    @property
    def DestinationMacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('destinationMacAddress')

    @property
    def LmmSentCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('lmmSentCount')

    @property
    def MaxFarEndLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('maxFarEndLoss')

    @property
    def MaxFarEndLossRatio(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('maxFarEndLossRatio')

    @property
    def MaxNearEndLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('maxNearEndLoss')

    @property
    def MaxNearEndLossRatio(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('maxNearEndLossRatio')

    @property
    def MdLevel(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('mdLevel')

    @property
    def MinFarEndLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('minFarEndLoss')

    @property
    def MinFarEndLossRatio(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('minFarEndLossRatio')

    @property
    def MinNearEndLoss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('minNearEndLoss')

    @property
    def MinNearEndLossRatio(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('minNearEndLossRatio')

    @property
    def NoReplyCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('noReplyCount')

    @property
    def SVlan(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('sVlan')

    @property
    def SourceMacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute('sourceMacAddress')

    @property
    def SourceMepId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute('sourceMepId')

    def find(self, AvgFarEndLoss=None, AvgNearEndLoss=None, BVlan=None, CVlan=None, CcmReceivedCount=None, CcmSentCount=None, CurrentFarEndLoss=None, CurrentFarEndLossRatio=None, CurrentNearEndLoss=None, CurrentNearEndLossRatio=None, DestinationMacAddress=None, LmmSentCount=None, MaxFarEndLoss=None, MaxFarEndLossRatio=None, MaxNearEndLoss=None, MaxNearEndLossRatio=None, MdLevel=None, MinFarEndLoss=None, MinFarEndLossRatio=None, MinNearEndLoss=None, MinNearEndLossRatio=None, NoReplyCount=None, SVlan=None, SourceMacAddress=None, SourceMepId=None):
        """Finds and retrieves periodicOamLmLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve periodicOamLmLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all periodicOamLmLearnedInfo resources from the server.

        Args
        ----
        - AvgFarEndLoss (str): NOT DEFINED
        - AvgNearEndLoss (str): NOT DEFINED
        - BVlan (str): NOT DEFINED
        - CVlan (str): NOT DEFINED
        - CcmReceivedCount (number): NOT DEFINED
        - CcmSentCount (number): NOT DEFINED
        - CurrentFarEndLoss (number): NOT DEFINED
        - CurrentFarEndLossRatio (str): NOT DEFINED
        - CurrentNearEndLoss (number): NOT DEFINED
        - CurrentNearEndLossRatio (str): NOT DEFINED
        - DestinationMacAddress (str): NOT DEFINED
        - LmmSentCount (number): NOT DEFINED
        - MaxFarEndLoss (number): NOT DEFINED
        - MaxFarEndLossRatio (str): NOT DEFINED
        - MaxNearEndLoss (number): NOT DEFINED
        - MaxNearEndLossRatio (str): NOT DEFINED
        - MdLevel (number): NOT DEFINED
        - MinFarEndLoss (number): NOT DEFINED
        - MinFarEndLossRatio (str): NOT DEFINED
        - MinNearEndLoss (number): NOT DEFINED
        - MinNearEndLossRatio (str): NOT DEFINED
        - NoReplyCount (number): NOT DEFINED
        - SVlan (str): NOT DEFINED
        - SourceMacAddress (str): NOT DEFINED
        - SourceMepId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching periodicOamLmLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of periodicOamLmLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the periodicOamLmLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
