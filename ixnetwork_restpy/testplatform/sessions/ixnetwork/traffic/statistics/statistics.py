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
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.advancedsequencechecking.advancedsequencechecking.AdvancedSequenceChecking): An instance of the AdvancedSequenceChecking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.advancedsequencechecking.advancedsequencechecking import AdvancedSequenceChecking
        if self._properties.get('AdvancedSequenceChecking', None) is not None:
            return self._properties.get('AdvancedSequenceChecking')
        else:
            return AdvancedSequenceChecking(self)._select()

    @property
    def CpdpConvergence(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.cpdpconvergence.cpdpconvergence.CpdpConvergence): An instance of the CpdpConvergence class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.cpdpconvergence.cpdpconvergence import CpdpConvergence
        if self._properties.get('CpdpConvergence', None) is not None:
            return self._properties.get('CpdpConvergence')
        else:
            return CpdpConvergence(self)._select()

    @property
    def DataIntegrity(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.dataintegrity.dataintegrity.DataIntegrity): An instance of the DataIntegrity class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.dataintegrity.dataintegrity import DataIntegrity
        if self._properties.get('DataIntegrity', None) is not None:
            return self._properties.get('DataIntegrity')
        else:
            return DataIntegrity(self)._select()

    @property
    def DelayVariation(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.delayvariation.delayvariation.DelayVariation): An instance of the DelayVariation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.delayvariation.delayvariation import DelayVariation
        if self._properties.get('DelayVariation', None) is not None:
            return self._properties.get('DelayVariation')
        else:
            return DelayVariation(self)._select()

    @property
    def ErrorStats(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.errorstats.errorstats.ErrorStats): An instance of the ErrorStats class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.errorstats.errorstats import ErrorStats
        if self._properties.get('ErrorStats', None) is not None:
            return self._properties.get('ErrorStats')
        else:
            return ErrorStats(self)._select()

    @property
    def InterArrivalTimeRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.interarrivaltimerate.interarrivaltimerate.InterArrivalTimeRate): An instance of the InterArrivalTimeRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.interarrivaltimerate.interarrivaltimerate import InterArrivalTimeRate
        if self._properties.get('InterArrivalTimeRate', None) is not None:
            return self._properties.get('InterArrivalTimeRate')
        else:
            return InterArrivalTimeRate(self)._select()

    @property
    def Iptv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.iptv.iptv.Iptv): An instance of the Iptv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.iptv.iptv import Iptv
        if self._properties.get('Iptv', None) is not None:
            return self._properties.get('Iptv')
        else:
            return Iptv(self)._select()

    @property
    def L1Rates(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.l1rates.l1rates.L1Rates): An instance of the L1Rates class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.l1rates.l1rates import L1Rates
        if self._properties.get('L1Rates', None) is not None:
            return self._properties.get('L1Rates')
        else:
            return L1Rates(self)._select()

    @property
    def Latency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.latency.latency.Latency): An instance of the Latency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.latency.latency import Latency
        if self._properties.get('Latency', None) is not None:
            return self._properties.get('Latency')
        else:
            return Latency(self)._select()

    @property
    def MisdirectedPerFlow(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.misdirectedperflow.misdirectedperflow.MisdirectedPerFlow): An instance of the MisdirectedPerFlow class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.misdirectedperflow.misdirectedperflow import MisdirectedPerFlow
        if self._properties.get('MisdirectedPerFlow', None) is not None:
            return self._properties.get('MisdirectedPerFlow')
        else:
            return MisdirectedPerFlow(self)._select()

    @property
    def MultipleJoinLeaveLatency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.multiplejoinleavelatency.multiplejoinleavelatency.MultipleJoinLeaveLatency): An instance of the MultipleJoinLeaveLatency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.multiplejoinleavelatency.multiplejoinleavelatency import MultipleJoinLeaveLatency
        if self._properties.get('MultipleJoinLeaveLatency', None) is not None:
            return self._properties.get('MultipleJoinLeaveLatency')
        else:
            return MultipleJoinLeaveLatency(self)._select()

    @property
    def OneTimeJoinLeaveLatency(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.onetimejoinleavelatency.onetimejoinleavelatency.OneTimeJoinLeaveLatency): An instance of the OneTimeJoinLeaveLatency class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.onetimejoinleavelatency.onetimejoinleavelatency import OneTimeJoinLeaveLatency
        if self._properties.get('OneTimeJoinLeaveLatency', None) is not None:
            return self._properties.get('OneTimeJoinLeaveLatency')
        else:
            return OneTimeJoinLeaveLatency(self)._select()

    @property
    def PacketLossDuration(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.packetlossduration.packetlossduration.PacketLossDuration): An instance of the PacketLossDuration class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.packetlossduration.packetlossduration import PacketLossDuration
        if self._properties.get('PacketLossDuration', None) is not None:
            return self._properties.get('PacketLossDuration')
        else:
            return PacketLossDuration(self)._select()

    @property
    def Prbs(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.prbs.prbs.Prbs): An instance of the Prbs class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.prbs.prbs import Prbs
        if self._properties.get('Prbs', None) is not None:
            return self._properties.get('Prbs')
        else:
            return Prbs(self)._select()

    @property
    def SequenceChecking(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.sequencechecking.sequencechecking.SequenceChecking): An instance of the SequenceChecking class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.traffic.statistics.sequencechecking.sequencechecking import SequenceChecking
        if self._properties.get('SequenceChecking', None) is not None:
            return self._properties.get('SequenceChecking')
        else:
            return SequenceChecking(self)._select()
