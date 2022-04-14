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


class LearnedFilter(Base):
    """Controls the types of LSAs that are learned by this interface.
    The LearnedFilter class encapsulates a required learnedFilter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "learnedFilter"
    _SDM_ATT_MAP = {
        "AdvRouterId": "advRouterId",
        "AreaSummaryLsaCount": "areaSummaryLsaCount",
        "EnableAdvRouterId": "enableAdvRouterId",
        "EnableFilter": "enableFilter",
        "EnableLinkStateId": "enableLinkStateId",
        "ExcludeAdvRouterId": "excludeAdvRouterId",
        "ExcludeLinkStateId": "excludeLinkStateId",
        "ExternalLsaCount": "externalLsaCount",
        "ExternalSummaryLsaCount": "externalSummaryLsaCount",
        "IsComplete": "isComplete",
        "LinkStateId": "linkStateId",
        "NetworkLsaCount": "networkLsaCount",
        "NssaLsaCount": "nssaLsaCount",
        "OpaqueAreaScopeLsaCount": "opaqueAreaScopeLsaCount",
        "OpaqueAsScopeLsaCount": "opaqueAsScopeLsaCount",
        "OpaqueLocalScopeLsaCount": "opaqueLocalScopeLsaCount",
        "RouterLsaCount": "routerLsaCount",
        "ShowExternalAsLsa": "showExternalAsLsa",
        "ShowNetworkLsa": "showNetworkLsa",
        "ShowNssaLsa": "showNssaLsa",
        "ShowOpaqueAreaLsa": "showOpaqueAreaLsa",
        "ShowOpaqueDomainLsa": "showOpaqueDomainLsa",
        "ShowOpaqueLocalLsa": "showOpaqueLocalLsa",
        "ShowRouterLsa": "showRouterLsa",
        "ShowSummaryAsLsa": "showSummaryAsLsa",
        "ShowSummaryIpLsa": "showSummaryIpLsa",
        "TotalLsaCount": "totalLsaCount",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(LearnedFilter, self).__init__(parent, list_op)

    @property
    def AdvRouterId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Filter on the router ID of the router that is originating the LSA.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdvRouterId"])

    @AdvRouterId.setter
    def AdvRouterId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdvRouterId"], value)

    @property
    def AreaSummaryLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of LSAs in the Summary Area.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AreaSummaryLsaCount"])

    @property
    def EnableAdvRouterId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true filter on the advertised router ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableAdvRouterId"])

    @EnableAdvRouterId.setter
    def EnableAdvRouterId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableAdvRouterId"], value)

    @property
    def EnableFilter(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables the use of the OSPF learned filter.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableFilter"])

    @EnableFilter.setter
    def EnableFilter(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableFilter"], value)

    @property
    def EnableLinkStateId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on the Link State ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnableLinkStateId"])

    @EnableLinkStateId.setter
    def EnableLinkStateId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["EnableLinkStateId"], value)

    @property
    def ExcludeAdvRouterId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on no advertised router ID available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExcludeAdvRouterId"])

    @ExcludeAdvRouterId.setter
    def ExcludeAdvRouterId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExcludeAdvRouterId"], value)

    @property
    def ExcludeLinkStateId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on no Link State ID available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExcludeLinkStateId"])

    @ExcludeLinkStateId.setter
    def ExcludeLinkStateId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExcludeLinkStateId"], value)

    @property
    def ExternalLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of External LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExternalLsaCount"])

    @property
    def ExternalSummaryLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of External Summary LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExternalSummaryLsaCount"])

    @property
    def IsComplete(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, indicates the Filter operation has finished.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IsComplete"])

    @property
    def LinkStateId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Filter on the Link State ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP["LinkStateId"])

    @LinkStateId.setter
    def LinkStateId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["LinkStateId"], value)

    @property
    def NetworkLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of Network LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NetworkLsaCount"])

    @property
    def NssaLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of NSSA LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NssaLsaCount"])

    @property
    def OpaqueAreaScopeLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of Opaque Area LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpaqueAreaScopeLsaCount"])

    @property
    def OpaqueAsScopeLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of AS Scope LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpaqueAsScopeLsaCount"])

    @property
    def OpaqueLocalScopeLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of Local Scope LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OpaqueLocalScopeLsaCount"])

    @property
    def RouterLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the number of Router LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RouterLsaCount"])

    @property
    def ShowExternalAsLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on the LSAs from routers with External routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowExternalAsLsa"])

    @ShowExternalAsLsa.setter
    def ShowExternalAsLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowExternalAsLsa"], value)

    @property
    def ShowNetworkLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with Network routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowNetworkLsa"])

    @ShowNetworkLsa.setter
    def ShowNetworkLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowNetworkLsa"], value)

    @property
    def ShowNssaLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with NSSA routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowNssaLsa"])

    @ShowNssaLsa.setter
    def ShowNssaLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowNssaLsa"], value)

    @property
    def ShowOpaqueAreaLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with Opaque Area routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowOpaqueAreaLsa"])

    @ShowOpaqueAreaLsa.setter
    def ShowOpaqueAreaLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowOpaqueAreaLsa"], value)

    @property
    def ShowOpaqueDomainLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with Opaque Domain routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowOpaqueDomainLsa"])

    @ShowOpaqueDomainLsa.setter
    def ShowOpaqueDomainLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowOpaqueDomainLsa"], value)

    @property
    def ShowOpaqueLocalLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with Opaque Local routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowOpaqueLocalLsa"])

    @ShowOpaqueLocalLsa.setter
    def ShowOpaqueLocalLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowOpaqueLocalLsa"], value)

    @property
    def ShowRouterLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with BR or DBR routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowRouterLsa"])

    @ShowRouterLsa.setter
    def ShowRouterLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowRouterLsa"], value)

    @property
    def ShowSummaryAsLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with Summary AS routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowSummaryAsLsa"])

    @ShowSummaryAsLsa.setter
    def ShowSummaryAsLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowSummaryAsLsa"], value)

    @property
    def ShowSummaryIpLsa(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, filter on LSAs from router with Summary IP routes.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ShowSummaryIpLsa"])

    @ShowSummaryIpLsa.setter
    def ShowSummaryIpLsa(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ShowSummaryIpLsa"], value)

    @property
    def TotalLsaCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Filter on the total number of LSAs.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TotalLsaCount"])

    def update(
        self,
        AdvRouterId=None,
        EnableAdvRouterId=None,
        EnableFilter=None,
        EnableLinkStateId=None,
        ExcludeAdvRouterId=None,
        ExcludeLinkStateId=None,
        LinkStateId=None,
        ShowExternalAsLsa=None,
        ShowNetworkLsa=None,
        ShowNssaLsa=None,
        ShowOpaqueAreaLsa=None,
        ShowOpaqueDomainLsa=None,
        ShowOpaqueLocalLsa=None,
        ShowRouterLsa=None,
        ShowSummaryAsLsa=None,
        ShowSummaryIpLsa=None,
    ):
        # type: (str, bool, bool, bool, bool, bool, str, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> LearnedFilter
        """Updates learnedFilter resource on the server.

        Args
        ----
        - AdvRouterId (str): Filter on the router ID of the router that is originating the LSA.
        - EnableAdvRouterId (bool): If true filter on the advertised router ID.
        - EnableFilter (bool): Enables the use of the OSPF learned filter.
        - EnableLinkStateId (bool): If true, filter on the Link State ID.
        - ExcludeAdvRouterId (bool): If true, filter on no advertised router ID available.
        - ExcludeLinkStateId (bool): If true, filter on no Link State ID available.
        - LinkStateId (str): Filter on the Link State ID.
        - ShowExternalAsLsa (bool): If true, filter on the LSAs from routers with External routes.
        - ShowNetworkLsa (bool): If true, filter on LSAs from router with Network routes.
        - ShowNssaLsa (bool): If true, filter on LSAs from router with NSSA routes.
        - ShowOpaqueAreaLsa (bool): If true, filter on LSAs from router with Opaque Area routes.
        - ShowOpaqueDomainLsa (bool): If true, filter on LSAs from router with Opaque Domain routes.
        - ShowOpaqueLocalLsa (bool): If true, filter on LSAs from router with Opaque Local routes.
        - ShowRouterLsa (bool): If true, filter on LSAs from router with BR or DBR routes.
        - ShowSummaryAsLsa (bool): If true, filter on LSAs from router with Summary AS routes.
        - ShowSummaryIpLsa (bool): If true, filter on LSAs from router with Summary IP routes.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AdvRouterId=None,
        AreaSummaryLsaCount=None,
        EnableAdvRouterId=None,
        EnableFilter=None,
        EnableLinkStateId=None,
        ExcludeAdvRouterId=None,
        ExcludeLinkStateId=None,
        ExternalLsaCount=None,
        ExternalSummaryLsaCount=None,
        IsComplete=None,
        LinkStateId=None,
        NetworkLsaCount=None,
        NssaLsaCount=None,
        OpaqueAreaScopeLsaCount=None,
        OpaqueAsScopeLsaCount=None,
        OpaqueLocalScopeLsaCount=None,
        RouterLsaCount=None,
        ShowExternalAsLsa=None,
        ShowNetworkLsa=None,
        ShowNssaLsa=None,
        ShowOpaqueAreaLsa=None,
        ShowOpaqueDomainLsa=None,
        ShowOpaqueLocalLsa=None,
        ShowRouterLsa=None,
        ShowSummaryAsLsa=None,
        ShowSummaryIpLsa=None,
        TotalLsaCount=None,
    ):
        # type: (str, int, bool, bool, bool, bool, bool, int, int, bool, str, int, int, int, int, int, int, bool, bool, bool, bool, bool, bool, bool, bool, bool, int) -> LearnedFilter
        """Finds and retrieves learnedFilter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve learnedFilter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all learnedFilter resources from the server.

        Args
        ----
        - AdvRouterId (str): Filter on the router ID of the router that is originating the LSA.
        - AreaSummaryLsaCount (number): Filter on the number of LSAs in the Summary Area.
        - EnableAdvRouterId (bool): If true filter on the advertised router ID.
        - EnableFilter (bool): Enables the use of the OSPF learned filter.
        - EnableLinkStateId (bool): If true, filter on the Link State ID.
        - ExcludeAdvRouterId (bool): If true, filter on no advertised router ID available.
        - ExcludeLinkStateId (bool): If true, filter on no Link State ID available.
        - ExternalLsaCount (number): Filter on the number of External LSAs.
        - ExternalSummaryLsaCount (number): Filter on the number of External Summary LSAs.
        - IsComplete (bool): If true, indicates the Filter operation has finished.
        - LinkStateId (str): Filter on the Link State ID.
        - NetworkLsaCount (number): Filter on the number of Network LSAs.
        - NssaLsaCount (number): Filter on the number of NSSA LSAs.
        - OpaqueAreaScopeLsaCount (number): Filter on the number of Opaque Area LSAs.
        - OpaqueAsScopeLsaCount (number): Filter on the number of AS Scope LSAs.
        - OpaqueLocalScopeLsaCount (number): Filter on the number of Local Scope LSAs.
        - RouterLsaCount (number): Filter on the number of Router LSAs.
        - ShowExternalAsLsa (bool): If true, filter on the LSAs from routers with External routes.
        - ShowNetworkLsa (bool): If true, filter on LSAs from router with Network routes.
        - ShowNssaLsa (bool): If true, filter on LSAs from router with NSSA routes.
        - ShowOpaqueAreaLsa (bool): If true, filter on LSAs from router with Opaque Area routes.
        - ShowOpaqueDomainLsa (bool): If true, filter on LSAs from router with Opaque Domain routes.
        - ShowOpaqueLocalLsa (bool): If true, filter on LSAs from router with Opaque Local routes.
        - ShowRouterLsa (bool): If true, filter on LSAs from router with BR or DBR routes.
        - ShowSummaryAsLsa (bool): If true, filter on LSAs from router with Summary AS routes.
        - ShowSummaryIpLsa (bool): If true, filter on LSAs from router with Summary IP routes.
        - TotalLsaCount (number): Filter on the total number of LSAs.

        Returns
        -------
        - self: This instance with matching learnedFilter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of learnedFilter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the learnedFilter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
