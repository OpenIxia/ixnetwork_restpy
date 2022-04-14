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


class Wildcards(Base):
    """NOT DEFINED
    The Wildcards class encapsulates a required wildcards resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "wildcards"
    _SDM_ATT_MAP = {
        "ExperimenterData": "experimenterData",
        "ExperimenterDataLength": "experimenterDataLength",
        "ExperimenterField": "experimenterField",
        "ExperimenterHasMask": "experimenterHasMask",
        "ExperimenterId": "experimenterId",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Wildcards, self).__init__(parent, list_op)

    @property
    def WildcardsFields(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsfields_a9d755a9e53cafc314f8e288acc0e118.WildcardsFields): An instance of the WildcardsFields class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.wildcardsfields_a9d755a9e53cafc314f8e288acc0e118 import (
            WildcardsFields,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("WildcardsFields", None) is not None:
                return self._properties.get("WildcardsFields")
        return WildcardsFields(self)._select()

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
    def ExperimenterField(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterField"])

    @ExperimenterField.setter
    def ExperimenterField(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterField"], value)

    @property
    def ExperimenterHasMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterHasMask"])

    @ExperimenterHasMask.setter
    def ExperimenterHasMask(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterHasMask"], value)

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

    def update(
        self,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterField=None,
        ExperimenterHasMask=None,
        ExperimenterId=None,
    ):
        # type: (str, int, int, bool, int) -> Wildcards
        """Updates wildcards resource on the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterField (number): NOT DEFINED
        - ExperimenterHasMask (bool): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ExperimenterData=None,
        ExperimenterDataLength=None,
        ExperimenterField=None,
        ExperimenterHasMask=None,
        ExperimenterId=None,
    ):
        # type: (str, int, int, bool, int) -> Wildcards
        """Finds and retrieves wildcards resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve wildcards resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all wildcards resources from the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterField (number): NOT DEFINED
        - ExperimenterHasMask (bool): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching wildcards resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of wildcards data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the wildcards resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
