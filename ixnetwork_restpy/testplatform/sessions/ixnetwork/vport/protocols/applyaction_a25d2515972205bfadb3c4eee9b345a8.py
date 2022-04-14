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


class ApplyAction(Base):
    """NOT DEFINED
    The ApplyAction class encapsulates a required applyAction resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "applyAction"
    _SDM_ATT_MAP = {
        "ExperimenterData": "experimenterData",
        "ExperimenterDataLength": "experimenterDataLength",
        "ExperimenterDataLengthMiss": "experimenterDataLengthMiss",
        "ExperimenterDataMiss": "experimenterDataMiss",
        "ExperimenterId": "experimenterId",
        "ExperimenterIdMiss": "experimenterIdMiss",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(ApplyAction, self).__init__(parent, list_op)

    @property
    def ApplyActionMissType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionmisstype_cb65e7e380c3e82fd0727515601c37f8.ApplyActionMissType): An instance of the ApplyActionMissType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactionmisstype_cb65e7e380c3e82fd0727515601c37f8 import (
            ApplyActionMissType,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyActionMissType", None) is not None:
                return self._properties.get("ApplyActionMissType")
        return ApplyActionMissType(self)._select()

    @property
    def ApplyActionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactiontype_c99bd67b1f4afee24406c78527adb40f.ApplyActionType): An instance of the ApplyActionType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.applyactiontype_c99bd67b1f4afee24406c78527adb40f import (
            ApplyActionType,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("ApplyActionType", None) is not None:
                return self._properties.get("ApplyActionType")
        return ApplyActionType(self)._select()

    @property
    def ExperimenterData(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterData"])

    @ExperimenterData.setter
    def ExperimenterData(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterData"], value)

    @property
    def ExperimenterDataLength(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterDataLength"])

    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterDataLength"], value)

    @property
    def ExperimenterDataLengthMiss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterDataLengthMiss"])

    @ExperimenterDataLengthMiss.setter
    def ExperimenterDataLengthMiss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterDataLengthMiss"], value)

    @property
    def ExperimenterDataMiss(self):
        # type: () -> str
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterDataMiss"])

    @ExperimenterDataMiss.setter
    def ExperimenterDataMiss(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterDataMiss"], value)

    @property
    def ExperimenterId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterId"])

    @ExperimenterId.setter
    def ExperimenterId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterId"], value)

    @property
    def ExperimenterIdMiss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterIdMiss"])

    @ExperimenterIdMiss.setter
    def ExperimenterIdMiss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterIdMiss"], value)

    def update(
        self,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterDataLengthMiss=None,
        ExperimenterDataMiss=None,
        ExperimenterId=None,
        ExperimenterIdMiss=None,
    ):
        # type: (str, int, int, str, int, int) -> ApplyAction
        """Updates applyAction resource on the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterDataLengthMiss (number): NOT DEFINED
        - ExperimenterDataMiss (str): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED
        - ExperimenterIdMiss (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterDataLengthMiss=None,
        ExperimenterDataMiss=None,
        ExperimenterId=None,
        ExperimenterIdMiss=None,
    ):
        # type: (str, int, int, str, int, int) -> ApplyAction
        """Finds and retrieves applyAction resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve applyAction resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all applyAction resources from the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterDataLengthMiss (number): NOT DEFINED
        - ExperimenterDataMiss (str): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED
        - ExperimenterIdMiss (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching applyAction resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of applyAction data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the applyAction resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
