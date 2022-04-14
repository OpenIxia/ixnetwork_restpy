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


class Experimenter(Base):
    """NOT DEFINED
    The Experimenter class encapsulates a required experimenter resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "experimenter"
    _SDM_ATT_MAP = {
        "ExperimenterData": "experimenterData",
        "ExperimenterDataLength": "experimenterDataLength",
        "ExperimenterDataLengthMiss": "experimenterDataLengthMiss",
        "ExperimenterDataMiss": "experimenterDataMiss",
        "ExperimenterField": "experimenterField",
        "ExperimenterFieldMiss": "experimenterFieldMiss",
        "ExperimenterId": "experimenterId",
        "ExperimenterIdMiss": "experimenterIdMiss",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(Experimenter, self).__init__(parent, list_op)

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
    def ExperimenterFieldMiss(self):
        # type: () -> int
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExperimenterFieldMiss"])

    @ExperimenterFieldMiss.setter
    def ExperimenterFieldMiss(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["ExperimenterFieldMiss"], value)

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
        ExperimenterField=None,
        ExperimenterFieldMiss=None,
        ExperimenterId=None,
        ExperimenterIdMiss=None,
    ):
        # type: (str, int, int, str, int, int, int, int) -> Experimenter
        """Updates experimenter resource on the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterDataLengthMiss (number): NOT DEFINED
        - ExperimenterDataMiss (str): NOT DEFINED
        - ExperimenterField (number): NOT DEFINED
        - ExperimenterFieldMiss (number): NOT DEFINED
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
        ExperimenterField=None,
        ExperimenterFieldMiss=None,
        ExperimenterId=None,
        ExperimenterIdMiss=None,
    ):
        # type: (str, int, int, str, int, int, int, int) -> Experimenter
        """Finds and retrieves experimenter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve experimenter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all experimenter resources from the server.

        Args
        ----
        - ExperimenterData (str): NOT DEFINED
        - ExperimenterDataLength (number): NOT DEFINED
        - ExperimenterDataLengthMiss (number): NOT DEFINED
        - ExperimenterDataMiss (str): NOT DEFINED
        - ExperimenterField (number): NOT DEFINED
        - ExperimenterFieldMiss (number): NOT DEFINED
        - ExperimenterId (number): NOT DEFINED
        - ExperimenterIdMiss (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching experimenter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of experimenter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the experimenter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
