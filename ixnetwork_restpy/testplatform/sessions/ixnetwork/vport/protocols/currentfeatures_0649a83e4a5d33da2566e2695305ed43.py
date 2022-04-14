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


class CurrentFeatures(Base):
    """An object that allows to select the current features (link modes, link types, and link features) from the list that the port will support.
    The CurrentFeatures class encapsulates a required currentFeatures resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "currentFeatures"
    _SDM_ATT_MAP = {
        "HundredGbFd": "100GbFd",
        "HundredMbFd": "100MbFd",
        "HundredMbHd": "100MbHd",
        "TenGbFd": "10GbFd",
        "TenMbFd": "10MbFd",
        "TenMbHd": "10MbHd",
        "OneGbFd": "1GbFd",
        "OneGbHd": "1GbHd",
        "OneTbFd": "1TbFd",
        "FortyGbFd": "40GbFd",
        "AsymmetricPause": "asymmetricPause",
        "AutoNegotiation": "autoNegotiation",
        "CopperMedium": "copperMedium",
        "FiberMedium": "fiberMedium",
        "OtherRate": "otherRate",
        "Pause": "pause",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(CurrentFeatures, self).__init__(parent, list_op)

    @property
    def HundredGbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 100 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HundredGbFd"])

    @HundredGbFd.setter
    def HundredGbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HundredGbFd"], value)

    @property
    def HundredMbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 100 MB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HundredMbFd"])

    @HundredMbFd.setter
    def HundredMbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HundredMbFd"], value)

    @property
    def HundredMbHd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 100 MB half-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HundredMbHd"])

    @HundredMbHd.setter
    def HundredMbHd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["HundredMbHd"], value)

    @property
    def TenGbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 10 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TenGbFd"])

    @TenGbFd.setter
    def TenGbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TenGbFd"], value)

    @property
    def TenMbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 10 MB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TenMbFd"])

    @TenMbFd.setter
    def TenMbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TenMbFd"], value)

    @property
    def TenMbHd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 10 MB half-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TenMbHd"])

    @TenMbHd.setter
    def TenMbHd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["TenMbHd"], value)

    @property
    def OneGbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 1 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OneGbFd"])

    @OneGbFd.setter
    def OneGbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OneGbFd"], value)

    @property
    def OneGbHd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 1 GB half-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OneGbHd"])

    @OneGbHd.setter
    def OneGbHd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OneGbHd"], value)

    @property
    def OneTbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 1 TB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OneTbFd"])

    @OneTbFd.setter
    def OneTbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OneTbFd"], value)

    @property
    def FortyGbFd(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, 40 GB full-duplex rate support is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FortyGbFd"])

    @FortyGbFd.setter
    def FortyGbFd(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FortyGbFd"], value)

    @property
    def AsymmetricPause(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, asymmetric pause of ports feature is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AsymmetricPause"])

    @AsymmetricPause.setter
    def AsymmetricPause(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AsymmetricPause"], value)

    @property
    def AutoNegotiation(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, auto negotiation of ports is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoNegotiation"])

    @AutoNegotiation.setter
    def AutoNegotiation(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoNegotiation"], value)

    @property
    def CopperMedium(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, copper medium link type is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CopperMedium"])

    @CopperMedium.setter
    def CopperMedium(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["CopperMedium"], value)

    @property
    def FiberMedium(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, fiber medium link type is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FiberMedium"])

    @FiberMedium.setter
    def FiberMedium(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["FiberMedium"], value)

    @property
    def OtherRate(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, supports other rate, not in the list.
        """
        return self._get_attribute(self._SDM_ATT_MAP["OtherRate"])

    @OtherRate.setter
    def OtherRate(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["OtherRate"], value)

    @property
    def Pause(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, pause ports feature is available.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Pause"])

    @Pause.setter
    def Pause(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Pause"], value)

    def update(
        self,
        HundredGbFd=None,
        HundredMbFd=None,
        HundredMbHd=None,
        TenGbFd=None,
        TenMbFd=None,
        TenMbHd=None,
        OneGbFd=None,
        OneGbHd=None,
        OneTbFd=None,
        FortyGbFd=None,
        AsymmetricPause=None,
        AutoNegotiation=None,
        CopperMedium=None,
        FiberMedium=None,
        OtherRate=None,
        Pause=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> CurrentFeatures
        """Updates currentFeatures resource on the server.

        Args
        ----
        - HundredGbFd (bool): If true, 100 GB full-duplex rate support is available.
        - HundredMbFd (bool): If true, 100 MB full-duplex rate support is available.
        - HundredMbHd (bool): If true, 100 MB half-duplex rate support is available.
        - TenGbFd (bool): If true, 10 GB full-duplex rate support is available.
        - TenMbFd (bool): If true, 10 MB full-duplex rate support is available.
        - TenMbHd (bool): If true, 10 MB half-duplex rate support is available.
        - OneGbFd (bool): If true, 1 GB full-duplex rate support is available.
        - OneGbHd (bool): If true, 1 GB half-duplex rate support is available.
        - OneTbFd (bool): If true, 1 TB full-duplex rate support is available.
        - FortyGbFd (bool): If true, 40 GB full-duplex rate support is available.
        - AsymmetricPause (bool): If true, asymmetric pause of ports feature is available.
        - AutoNegotiation (bool): If true, auto negotiation of ports is available.
        - CopperMedium (bool): If true, copper medium link type is available.
        - FiberMedium (bool): If true, fiber medium link type is available.
        - OtherRate (bool): If true, supports other rate, not in the list.
        - Pause (bool): If true, pause ports feature is available.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        HundredGbFd=None,
        HundredMbFd=None,
        HundredMbHd=None,
        TenGbFd=None,
        TenMbFd=None,
        TenMbHd=None,
        OneGbFd=None,
        OneGbHd=None,
        OneTbFd=None,
        FortyGbFd=None,
        AsymmetricPause=None,
        AutoNegotiation=None,
        CopperMedium=None,
        FiberMedium=None,
        OtherRate=None,
        Pause=None,
    ):
        # type: (bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool, bool) -> CurrentFeatures
        """Finds and retrieves currentFeatures resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve currentFeatures resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all currentFeatures resources from the server.

        Args
        ----
        - HundredGbFd (bool): If true, 100 GB full-duplex rate support is available.
        - HundredMbFd (bool): If true, 100 MB full-duplex rate support is available.
        - HundredMbHd (bool): If true, 100 MB half-duplex rate support is available.
        - TenGbFd (bool): If true, 10 GB full-duplex rate support is available.
        - TenMbFd (bool): If true, 10 MB full-duplex rate support is available.
        - TenMbHd (bool): If true, 10 MB half-duplex rate support is available.
        - OneGbFd (bool): If true, 1 GB full-duplex rate support is available.
        - OneGbHd (bool): If true, 1 GB half-duplex rate support is available.
        - OneTbFd (bool): If true, 1 TB full-duplex rate support is available.
        - FortyGbFd (bool): If true, 40 GB full-duplex rate support is available.
        - AsymmetricPause (bool): If true, asymmetric pause of ports feature is available.
        - AutoNegotiation (bool): If true, auto negotiation of ports is available.
        - CopperMedium (bool): If true, copper medium link type is available.
        - FiberMedium (bool): If true, fiber medium link type is available.
        - OtherRate (bool): If true, supports other rate, not in the list.
        - Pause (bool): If true, pause ports feature is available.

        Returns
        -------
        - self: This instance with matching currentFeatures resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of currentFeatures data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the currentFeatures resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
