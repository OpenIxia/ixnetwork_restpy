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
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class FrameSize(Base):
    """This object provides different options for the Frame Size.
    The FrameSize class encapsulates a required frameSize resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'frameSize'
    _SDM_ATT_MAP = {
        'FixedSize': 'fixedSize',
        'IncrementFrom': 'incrementFrom',
        'IncrementStep': 'incrementStep',
        'IncrementTo': 'incrementTo',
        'PresetDistribution': 'presetDistribution',
        'QuadGaussian': 'quadGaussian',
        'RandomMax': 'randomMax',
        'RandomMin': 'randomMin',
        'Type': 'type',
        'WeightedPairs': 'weightedPairs',
        'WeightedRangePairs': 'weightedRangePairs',
    }
    _SDM_ENUM_MAP = {
        'presetDistribution': ['cisco', 'imix', 'ipSecImix', 'rprQuar', 'rprTri', 'tcpImix', 'tolly'],
        'type': ['auto', 'fixed', 'increment', 'presetDistribution', 'quadGaussian', 'random', 'weightedPairs'],
    }

    def __init__(self, parent, list_op=False):
        super(FrameSize, self).__init__(parent, list_op)

    @property
    def FixedSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets all frames to a constant specified size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedSize'])
    @FixedSize.setter
    def FixedSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FixedSize'], value)

    @property
    def IncrementFrom(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Start Value if the Frame Size is incremented.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementFrom'])
    @IncrementFrom.setter
    def IncrementFrom(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IncrementFrom'], value)

    @property
    def IncrementStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Step Value if the Frame Size is Increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementStep'])
    @IncrementStep.setter
    def IncrementStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IncrementStep'], value)

    @property
    def IncrementTo(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Specifies the Final Value if the Frame Size is Increment.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementTo'])
    @IncrementTo.setter
    def IncrementTo(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['IncrementTo'], value)

    @property
    def PresetDistribution(self):
        # type: () -> str
        """
        Returns
        -------
        - str(cisco | imix | ipSecImix | rprQuar | rprTri | tcpImix | tolly): If set, Frame Size is set to IMIX.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PresetDistribution'])
    @PresetDistribution.setter
    def PresetDistribution(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['PresetDistribution'], value)

    @property
    def QuadGaussian(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): This option allows to set frames to use a calculated distribution of Frame sizes. Quad Gaussian is the superposition of four Gaussian distributions. The user can specify the center (or mean), width of half maximum, and weight of each Gaussian distribution. The distribution is then normalized to a single distribution and generates the random numbers according to the normalized distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP['QuadGaussian'])
    @QuadGaussian.setter
    def QuadGaussian(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP['QuadGaussian'], value)

    @property
    def RandomMax(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomMax'])
    @RandomMax.setter
    def RandomMax(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RandomMax'], value)

    @property
    def RandomMin(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomMin'])
    @RandomMin.setter
    def RandomMin(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['RandomMin'], value)

    @property
    def Type(self):
        # type: () -> str
        """
        Returns
        -------
        - str(auto | fixed | increment | presetDistribution | quadGaussian | random | weightedPairs): Sets the type of Frame Size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def WeightedPairs(self):
        # type: () -> List[int]
        """
        Returns
        -------
        - list(number): Defines the values for the weight pairs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WeightedPairs'])
    @WeightedPairs.setter
    def WeightedPairs(self, value):
        # type: (List[int]) -> None
        self._set_attribute(self._SDM_ATT_MAP['WeightedPairs'], value)

    @property
    def WeightedRangePairs(self):
        """
        Returns
        -------
        - list(dict(arg1:number,arg2:number,arg3:number)): A list of structures that define the weighted range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['WeightedRangePairs'])
    @WeightedRangePairs.setter
    def WeightedRangePairs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['WeightedRangePairs'], value)

    def update(self, FixedSize=None, IncrementFrom=None, IncrementStep=None, IncrementTo=None, PresetDistribution=None, QuadGaussian=None, RandomMax=None, RandomMin=None, Type=None, WeightedPairs=None, WeightedRangePairs=None):
        """Updates frameSize resource on the server.

        Args
        ----
        - FixedSize (number): Sets all frames to a constant specified size.
        - IncrementFrom (number): Specifies the Start Value if the Frame Size is incremented.
        - IncrementStep (number): Specifies the Step Value if the Frame Size is Increment.
        - IncrementTo (number): Specifies the Final Value if the Frame Size is Increment.
        - PresetDistribution (str(cisco | imix | ipSecImix | rprQuar | rprTri | tcpImix | tolly)): If set, Frame Size is set to IMIX.
        - QuadGaussian (list(number)): This option allows to set frames to use a calculated distribution of Frame sizes. Quad Gaussian is the superposition of four Gaussian distributions. The user can specify the center (or mean), width of half maximum, and weight of each Gaussian distribution. The distribution is then normalized to a single distribution and generates the random numbers according to the normalized distribution.
        - RandomMax (number): Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        - RandomMin (number): Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        - Type (str(auto | fixed | increment | presetDistribution | quadGaussian | random | weightedPairs)): Sets the type of Frame Size.
        - WeightedPairs (list(number)): Defines the values for the weight pairs.
        - WeightedRangePairs (list(dict(arg1:number,arg2:number,arg3:number))): A list of structures that define the weighted range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, FixedSize=None, IncrementFrom=None, IncrementStep=None, IncrementTo=None, PresetDistribution=None, QuadGaussian=None, RandomMax=None, RandomMin=None, Type=None, WeightedPairs=None, WeightedRangePairs=None):
        """Finds and retrieves frameSize resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve frameSize resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all frameSize resources from the server.

        Args
        ----
        - FixedSize (number): Sets all frames to a constant specified size.
        - IncrementFrom (number): Specifies the Start Value if the Frame Size is incremented.
        - IncrementStep (number): Specifies the Step Value if the Frame Size is Increment.
        - IncrementTo (number): Specifies the Final Value if the Frame Size is Increment.
        - PresetDistribution (str(cisco | imix | ipSecImix | rprQuar | rprTri | tcpImix | tolly)): If set, Frame Size is set to IMIX.
        - QuadGaussian (list(number)): This option allows to set frames to use a calculated distribution of Frame sizes. Quad Gaussian is the superposition of four Gaussian distributions. The user can specify the center (or mean), width of half maximum, and weight of each Gaussian distribution. The distribution is then normalized to a single distribution and generates the random numbers according to the normalized distribution.
        - RandomMax (number): Sets frame size to maximum length in bytes. The maximum length is 65536 bytes.
        - RandomMin (number): Sets frame size to minimum length in bytes. The minimum length is 12 bytes.
        - Type (str(auto | fixed | increment | presetDistribution | quadGaussian | random | weightedPairs)): Sets the type of Frame Size.
        - WeightedPairs (list(number)): Defines the values for the weight pairs.
        - WeightedRangePairs (list(dict(arg1:number,arg2:number,arg3:number))): A list of structures that define the weighted range.

        Returns
        -------
        - self: This instance with matching frameSize resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of frameSize data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the frameSize resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
