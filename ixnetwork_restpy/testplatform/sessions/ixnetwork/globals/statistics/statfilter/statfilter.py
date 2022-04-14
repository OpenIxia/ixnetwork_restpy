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


class StatFilter(Base):
    """
    The StatFilter class encapsulates a required statFilter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "statFilter"
    _SDM_ATT_MAP = {}
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(StatFilter, self).__init__(parent, list_op)

    @property
    def BfdAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.bfdaggregatedstatistics.bfdaggregatedstatistics.BfdAggregatedStatistics): An instance of the BfdAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.bfdaggregatedstatistics.bfdaggregatedstatistics import (
            BfdAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BfdAggregatedStatistics", None) is not None:
                return self._properties.get("BfdAggregatedStatistics")
        return BfdAggregatedStatistics(self)._select()

    @property
    def BgpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.bgpaggregatedstatistics.bgpaggregatedstatistics.BgpAggregatedStatistics): An instance of the BgpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.bgpaggregatedstatistics.bgpaggregatedstatistics import (
            BgpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BgpAggregatedStatistics", None) is not None:
                return self._properties.get("BgpAggregatedStatistics")
        return BgpAggregatedStatistics(self)._select()

    @property
    def CfmAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.cfmaggregatedstatistics.cfmaggregatedstatistics.CfmAggregatedStatistics): An instance of the CfmAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.cfmaggregatedstatistics.cfmaggregatedstatistics import (
            CfmAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CfmAggregatedStatistics", None) is not None:
                return self._properties.get("CfmAggregatedStatistics")
        return CfmAggregatedStatistics(self)._select()

    @property
    def EigrpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.eigrpaggregatedstatistics.eigrpaggregatedstatistics.EigrpAggregatedStatistics): An instance of the EigrpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.eigrpaggregatedstatistics.eigrpaggregatedstatistics import (
            EigrpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EigrpAggregatedStatistics", None) is not None:
                return self._properties.get("EigrpAggregatedStatistics")
        return EigrpAggregatedStatistics(self)._select()

    @property
    def GlobalProtocolStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.globalprotocolstatistics.globalprotocolstatistics.GlobalProtocolStatistics): An instance of the GlobalProtocolStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.globalprotocolstatistics.globalprotocolstatistics import (
            GlobalProtocolStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("GlobalProtocolStatistics", None) is not None:
                return self._properties.get("GlobalProtocolStatistics")
        return GlobalProtocolStatistics(self)._select()

    @property
    def IgmpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.igmpaggregatedstatistics.igmpaggregatedstatistics.IgmpAggregatedStatistics): An instance of the IgmpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.igmpaggregatedstatistics.igmpaggregatedstatistics import (
            IgmpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IgmpAggregatedStatistics", None) is not None:
                return self._properties.get("IgmpAggregatedStatistics")
        return IgmpAggregatedStatistics(self)._select()

    @property
    def IgmpQuerierAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.igmpquerieraggregatedstatistics.igmpquerieraggregatedstatistics.IgmpQuerierAggregatedStatistics): An instance of the IgmpQuerierAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.igmpquerieraggregatedstatistics.igmpquerieraggregatedstatistics import (
            IgmpQuerierAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("IgmpQuerierAggregatedStatistics", None)
                is not None
            ):
                return self._properties.get("IgmpQuerierAggregatedStatistics")
        return IgmpQuerierAggregatedStatistics(self)._select()

    @property
    def IsisAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.isisaggregatedstatistics.isisaggregatedstatistics.IsisAggregatedStatistics): An instance of the IsisAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.isisaggregatedstatistics.isisaggregatedstatistics import (
            IsisAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("IsisAggregatedStatistics", None) is not None:
                return self._properties.get("IsisAggregatedStatistics")
        return IsisAggregatedStatistics(self)._select()

    @property
    def LacpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.lacpaggregatedstatistics.lacpaggregatedstatistics.LacpAggregatedStatistics): An instance of the LacpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.lacpaggregatedstatistics.lacpaggregatedstatistics import (
            LacpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LacpAggregatedStatistics", None) is not None:
                return self._properties.get("LacpAggregatedStatistics")
        return LacpAggregatedStatistics(self)._select()

    @property
    def LdpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ldpaggregatedstatistics.ldpaggregatedstatistics.LdpAggregatedStatistics): An instance of the LdpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ldpaggregatedstatistics.ldpaggregatedstatistics import (
            LdpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LdpAggregatedStatistics", None) is not None:
                return self._properties.get("LdpAggregatedStatistics")
        return LdpAggregatedStatistics(self)._select()

    @property
    def LispAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.lispaggregatedstatistics.lispaggregatedstatistics.LispAggregatedStatistics): An instance of the LispAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.lispaggregatedstatistics.lispaggregatedstatistics import (
            LispAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LispAggregatedStatistics", None) is not None:
                return self._properties.get("LispAggregatedStatistics")
        return LispAggregatedStatistics(self)._select()

    @property
    def MldAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.mldaggregatedstatistics.mldaggregatedstatistics.MldAggregatedStatistics): An instance of the MldAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.mldaggregatedstatistics.mldaggregatedstatistics import (
            MldAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldAggregatedStatistics", None) is not None:
                return self._properties.get("MldAggregatedStatistics")
        return MldAggregatedStatistics(self)._select()

    @property
    def MldQuerierAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.mldquerieraggregatedstatistics.mldquerieraggregatedstatistics.MldQuerierAggregatedStatistics): An instance of the MldQuerierAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.mldquerieraggregatedstatistics.mldquerieraggregatedstatistics import (
            MldQuerierAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("MldQuerierAggregatedStatistics", None) is not None:
                return self._properties.get("MldQuerierAggregatedStatistics")
        return MldQuerierAggregatedStatistics(self)._select()

    @property
    def OamAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.oamaggregatedstatistics.oamaggregatedstatistics.OamAggregatedStatistics): An instance of the OamAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.oamaggregatedstatistics.oamaggregatedstatistics import (
            OamAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OamAggregatedStatistics", None) is not None:
                return self._properties.get("OamAggregatedStatistics")
        return OamAggregatedStatistics(self)._select()

    @property
    def OpenflowAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.openflowaggregatedstatistics.openflowaggregatedstatistics.OpenflowAggregatedStatistics): An instance of the OpenflowAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.openflowaggregatedstatistics.openflowaggregatedstatistics import (
            OpenflowAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OpenflowAggregatedStatistics", None) is not None:
                return self._properties.get("OpenflowAggregatedStatistics")
        return OpenflowAggregatedStatistics(self)._select()

    @property
    def OpenflowSwitchAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.openflowswitchaggregatedstatistics.openflowswitchaggregatedstatistics.OpenflowSwitchAggregatedStatistics): An instance of the OpenflowSwitchAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.openflowswitchaggregatedstatistics.openflowswitchaggregatedstatistics import (
            OpenflowSwitchAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("OpenflowSwitchAggregatedStatistics", None)
                is not None
            ):
                return self._properties.get("OpenflowSwitchAggregatedStatistics")
        return OpenflowSwitchAggregatedStatistics(self)._select()

    @property
    def OspfAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ospfaggregatedstatistics.ospfaggregatedstatistics.OspfAggregatedStatistics): An instance of the OspfAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ospfaggregatedstatistics.ospfaggregatedstatistics import (
            OspfAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("OspfAggregatedStatistics", None) is not None:
                return self._properties.get("OspfAggregatedStatistics")
        return OspfAggregatedStatistics(self)._select()

    @property
    def Ospfv3AggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ospfv3aggregatedstatistics.ospfv3aggregatedstatistics.Ospfv3AggregatedStatistics): An instance of the Ospfv3AggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ospfv3aggregatedstatistics.ospfv3aggregatedstatistics import (
            Ospfv3AggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Ospfv3AggregatedStatistics", None) is not None:
                return self._properties.get("Ospfv3AggregatedStatistics")
        return Ospfv3AggregatedStatistics(self)._select()

    @property
    def PimsmAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.pimsmaggregatedstatistics.pimsmaggregatedstatistics.PimsmAggregatedStatistics): An instance of the PimsmAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.pimsmaggregatedstatistics.pimsmaggregatedstatistics import (
            PimsmAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PimsmAggregatedStatistics", None) is not None:
                return self._properties.get("PimsmAggregatedStatistics")
        return PimsmAggregatedStatistics(self)._select()

    @property
    def PortStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.portstatistics.portstatistics.PortStatistics): An instance of the PortStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.portstatistics.portstatistics import (
            PortStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PortStatistics", None) is not None:
                return self._properties.get("PortStatistics")
        return PortStatistics(self)._select()

    @property
    def RipAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ripaggregatedstatistics.ripaggregatedstatistics.RipAggregatedStatistics): An instance of the RipAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ripaggregatedstatistics.ripaggregatedstatistics import (
            RipAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RipAggregatedStatistics", None) is not None:
                return self._properties.get("RipAggregatedStatistics")
        return RipAggregatedStatistics(self)._select()

    @property
    def RipngAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ripngaggregatedstatistics.ripngaggregatedstatistics.RipngAggregatedStatistics): An instance of the RipngAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.ripngaggregatedstatistics.ripngaggregatedstatistics import (
            RipngAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RipngAggregatedStatistics", None) is not None:
                return self._properties.get("RipngAggregatedStatistics")
        return RipngAggregatedStatistics(self)._select()

    @property
    def RsvpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.rsvpaggregatedstatistics.rsvpaggregatedstatistics.RsvpAggregatedStatistics): An instance of the RsvpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.rsvpaggregatedstatistics.rsvpaggregatedstatistics import (
            RsvpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("RsvpAggregatedStatistics", None) is not None:
                return self._properties.get("RsvpAggregatedStatistics")
        return RsvpAggregatedStatistics(self)._select()

    @property
    def StpAggregatedStatistics(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.stpaggregatedstatistics.stpaggregatedstatistics.StpAggregatedStatistics): An instance of the StpAggregatedStatistics class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.statistics.statfilter.stpaggregatedstatistics.stpaggregatedstatistics import (
            StpAggregatedStatistics,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StpAggregatedStatistics", None) is not None:
                return self._properties.get("StpAggregatedStatistics")
        return StpAggregatedStatistics(self)._select()

    def find(self):
        """Finds and retrieves statFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve statFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all statFilter resources from the server.

        Returns
        -------
        - self: This instance with matching statFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of statFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the statFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
