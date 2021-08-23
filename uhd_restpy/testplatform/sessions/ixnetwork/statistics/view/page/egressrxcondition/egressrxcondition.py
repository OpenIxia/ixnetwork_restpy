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


class EgressRxCondition(Base):
    """Condition for egress row display in SV. (there is only one so it applies to all egress rows).
    The EgressRxCondition class encapsulates a required egressRxCondition resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egressRxCondition'
    _SDM_ATT_MAP = {
        'Operator': 'operator',
        'Values': 'values',
    }
    _SDM_ENUM_MAP = {
        'operator': ['isBetween', 'isDifferent', 'isEqual', 'isEqualOrGreater', 'isEqualOrSmaller', 'isGreater', 'isSmaller'],
    }

    def __init__(self, parent, list_op=False):
        super(EgressRxCondition, self).__init__(parent, list_op)

    @property
    def Operator(self):
        # type: () -> str
        """
        Returns
        -------
        - str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller): The logical operation to be performed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Operator'])
    @Operator.setter
    def Operator(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Operator'], value)

    @property
    def Values(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Value to be matched for the condition.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Values'])
    @Values.setter
    def Values(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP['Values'], value)

    def update(self, Operator=None, Values=None):
        # type: (str, List[int]) -> EgressRxCondition
        """Updates egressRxCondition resource on the server.

        Args
        ----
        - Operator (str(isBetween | isDifferent | isEqual | isEqualOrGreater | isEqualOrSmaller | isGreater | isSmaller)): The logical operation to be performed.
        - Values (list(number)): Value to be matched for the condition.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
