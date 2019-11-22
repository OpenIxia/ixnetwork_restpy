# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class EgressRxCondition(Base):
    """
    The EgressRxCondition class encapsulates a required egressRxCondition resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egressRxCondition'

    def __init__(self, parent):
        super(EgressRxCondition, self).__init__(parent)

    @property
    def Operator(self):
        """

        Returns:
            str(isBetween|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isSmaller)
        """
        return self._get_attribute('operator')
    @Operator.setter
    def Operator(self, value):
        self._set_attribute('operator', value)

    @property
    def Values(self):
        """Value to be matched for the condition.

        Returns:
            list(number)
        """
        return self._get_attribute('values')
    @Values.setter
    def Values(self, value):
        self._set_attribute('values', value)

    def update(self, Operator=None, Values=None):
        """Updates a child instance of egressRxCondition on the server.

        Args:
            Operator (str(isBetween|isDifferent|isEqual|isEqualOrGreater|isEqualOrSmaller|isGreater|isSmaller)): 
            Values (list(number)): Value to be matched for the condition.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
