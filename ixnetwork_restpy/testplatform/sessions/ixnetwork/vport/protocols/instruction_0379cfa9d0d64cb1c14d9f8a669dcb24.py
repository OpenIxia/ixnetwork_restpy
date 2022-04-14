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


class Instruction(Base):
    """NOT DEFINED
    The Instruction class encapsulates a required instruction resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "instruction"
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
        super(Instruction, self).__init__(parent, list_op)

    @property
    def InstructionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontype_48ecf22c686ab3b403480ead04a36305.InstructionType): An instance of the InstructionType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontype_48ecf22c686ab3b403480ead04a36305 import (
            InstructionType,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InstructionType", None) is not None:
                return self._properties.get("InstructionType")
        return InstructionType(self)._select()

    @property
    def InstructionTypeMiss(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontypemiss_253739e9542d1a3617b510285726bcd8.InstructionTypeMiss): An instance of the InstructionTypeMiss class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.instructiontypemiss_253739e9542d1a3617b510285726bcd8 import (
            InstructionTypeMiss,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("InstructionTypeMiss", None) is not None:
                return self._properties.get("InstructionTypeMiss")
        return InstructionTypeMiss(self)._select()

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
        # type: (str, int, int, str, int, int) -> Instruction
        """Updates instruction resource on the server.

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
        # type: (str, int, int, str, int, int) -> Instruction
        """Finds and retrieves instruction resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve instruction resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all instruction resources from the server.

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
        - self: This instance with matching instruction resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of instruction data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the instruction resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
