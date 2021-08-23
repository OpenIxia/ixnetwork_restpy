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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
from typing import List, Any, Union


class Statistics(Base):
    """This object fetches all the traffic statistics.
    The Statistics class encapsulates a required statistics resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'statistics'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(Statistics, self).__init__(parent, list_op)

    @property
    def AdvancedSequenceChecking(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.advancedsequencechecking.advancedsequencechecking.AdvancedSequenceChecking): An instance of the AdvancedSequenceChecking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.advancedsequencechecking.advancedsequencechecking import AdvancedSequenceChecking
        if self._properties.get('AdvancedSequenceChecking', None) is not None:
            return self._properties.get('AdvancedSequenceChecking')
        else:
            return AdvancedSequenceChecking(self)._select()

    @property
    def CpdpConvergence(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.cpdpconvergence.cpdpconvergence.CpdpConvergence): An instance of the CpdpConvergence class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.cpdpconvergence.cpdpconvergence import CpdpConvergence
        if self._properties.get('CpdpConvergence', None) is not None:
            return self._properties.get('CpdpConvergence')
        else:
            return CpdpConvergence(self)._select()

    @property
    def DataIntegrity(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.dataintegrity.dataintegrity.DataIntegrity): An instance of the DataIntegrity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.dataintegrity.dataintegrity import DataIntegrity
        if self._properties.get('DataIntegrity', None) is not None:
            return self._properties.get('DataIntegrity')
        else:
            return DataIntegrity(self)._select()

    @property
    def DelayVariation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.delayvariation.delayvariation.DelayVariation): An instance of the DelayVariation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.delayvariation.delayvariation import DelayVariation
        if self._properties.get('DelayVariation', None) is not None:
            return self._properties.get('DelayVariation')
        else:
            return DelayVariation(self)._select()

    @property
    def ErrorStats(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.errorstats.errorstats.ErrorStats): An instance of the ErrorStats class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.errorstats.errorstats import ErrorStats
        if self._properties.get('ErrorStats', None) is not None:
            return self._properties.get('ErrorStats')
        else:
            return ErrorStats(self)._select()

    @property
    def InterArrivalTimeRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.interarrivaltimerate.interarrivaltimerate.InterArrivalTimeRate): An instance of the InterArrivalTimeRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.interarrivaltimerate.interarrivaltimerate import InterArrivalTimeRate
        if self._properties.get('InterArrivalTimeRate', None) is not None:
            return self._properties.get('InterArrivalTimeRate')
        else:
            return InterArrivalTimeRate(self)._select()

    @property
    def L1Rates(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.l1rates.l1rates.L1Rates): An instance of the L1Rates class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.l1rates.l1rates import L1Rates
        if self._properties.get('L1Rates', None) is not None:
            return self._properties.get('L1Rates')
        else:
            return L1Rates(self)._select()

    @property
    def Latency(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.latency.latency.Latency): An instance of the Latency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.latency.latency import Latency
        if self._properties.get('Latency', None) is not None:
            return self._properties.get('Latency')
        else:
            return Latency(self)._select()

    @property
    def PacketLossDuration(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.packetlossduration.packetlossduration.PacketLossDuration): An instance of the PacketLossDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.traffic.statistics.packetlossduration.packetlossduration import PacketLossDuration
        if self._properties.get('PacketLossDuration', None) is not None:
            return self._properties.get('PacketLossDuration')
        else:
            return PacketLossDuration(self)._select()
