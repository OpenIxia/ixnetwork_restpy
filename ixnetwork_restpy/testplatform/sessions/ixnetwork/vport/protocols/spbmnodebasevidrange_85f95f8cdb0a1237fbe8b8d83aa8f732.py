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


class SpbmNodeBaseVidRange(Base):
    """The SPBM Node Base VLAN ID Range.
    The SpbmNodeBaseVidRange class encapsulates a list of spbmNodeBaseVidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the SpbmNodeBaseVidRange.find() method.
    The list can be managed by using the SpbmNodeBaseVidRange.add() and SpbmNodeBaseVidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "spbmNodeBaseVidRange"
    _SDM_ATT_MAP = {
        "BVlanPriority": "bVlanPriority",
        "BVlanTpId": "bVlanTpId",
        "BaseVid": "baseVid",
        "EctAlgorithm": "ectAlgorithm",
        "UseFlag": "useFlag",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(SpbmNodeBaseVidRange, self).__init__(parent, list_op)

    @property
    def SpbmNodeIsIdRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbmnodeisidrange_ce5aa3fd54769fa53d910c12b9b3cddb.SpbmNodeIsIdRange): An instance of the SpbmNodeIsIdRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.spbmnodeisidrange_ce5aa3fd54769fa53d910c12b9b3cddb import (
            SpbmNodeIsIdRange,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("SpbmNodeIsIdRange", None) is not None:
                return self._properties.get("SpbmNodeIsIdRange")
        return SpbmNodeIsIdRange(self)

    @property
    def BVlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The user priority of the Base VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlanPriority"])

    @BVlanPriority.setter
    def BVlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BVlanPriority"], value)

    @property
    def BVlanTpId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The tag priority identifier for base VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BVlanTpId"])

    @BVlanTpId.setter
    def BVlanTpId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BVlanTpId"], value)

    @property
    def BaseVid(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["BaseVid"])

    @BaseVid.setter
    def BaseVid(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["BaseVid"], value)

    @property
    def EctAlgorithm(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The SPB Equal Cost Tree (ECT) algorithm. The default algorithm is 01-80-C2-01.
        """
        return self._get_attribute(self._SDM_ATT_MAP["EctAlgorithm"])

    @EctAlgorithm.setter
    def EctAlgorithm(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["EctAlgorithm"], value)

    @property
    def UseFlag(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Set to true to activate the user flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseFlag"])

    @UseFlag.setter
    def UseFlag(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseFlag"], value)

    def update(
        self,
        BVlanPriority=None,
        BVlanTpId=None,
        BaseVid=None,
        EctAlgorithm=None,
        UseFlag=None,
    ):
        # type: (int, int, int, int, bool) -> SpbmNodeBaseVidRange
        """Updates spbmNodeBaseVidRange resource on the server.

        Args
        ----
        - BVlanPriority (number): The user priority of the Base VLAN.
        - BVlanTpId (number): The tag priority identifier for base VLAN.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - EctAlgorithm (number): The SPB Equal Cost Tree (ECT) algorithm. The default algorithm is 01-80-C2-01.
        - UseFlag (bool): Set to true to activate the user flag.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        BVlanPriority=None,
        BVlanTpId=None,
        BaseVid=None,
        EctAlgorithm=None,
        UseFlag=None,
    ):
        # type: (int, int, int, int, bool) -> SpbmNodeBaseVidRange
        """Adds a new spbmNodeBaseVidRange resource on the server and adds it to the container.

        Args
        ----
        - BVlanPriority (number): The user priority of the Base VLAN.
        - BVlanTpId (number): The tag priority identifier for base VLAN.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - EctAlgorithm (number): The SPB Equal Cost Tree (ECT) algorithm. The default algorithm is 01-80-C2-01.
        - UseFlag (bool): Set to true to activate the user flag.

        Returns
        -------
        - self: This instance with all currently retrieved spbmNodeBaseVidRange resources using find and the newly added spbmNodeBaseVidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained spbmNodeBaseVidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        BVlanPriority=None,
        BVlanTpId=None,
        BaseVid=None,
        EctAlgorithm=None,
        UseFlag=None,
    ):
        # type: (int, int, int, int, bool) -> SpbmNodeBaseVidRange
        """Finds and retrieves spbmNodeBaseVidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve spbmNodeBaseVidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all spbmNodeBaseVidRange resources from the server.

        Args
        ----
        - BVlanPriority (number): The user priority of the Base VLAN.
        - BVlanTpId (number): The tag priority identifier for base VLAN.
        - BaseVid (number): The Base VLAN ID. The default value is 1. The maximum value is 4095. The minimum value is 0.
        - EctAlgorithm (number): The SPB Equal Cost Tree (ECT) algorithm. The default algorithm is 01-80-C2-01.
        - UseFlag (bool): Set to true to activate the user flag.

        Returns
        -------
        - self: This instance with matching spbmNodeBaseVidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of spbmNodeBaseVidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the spbmNodeBaseVidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
