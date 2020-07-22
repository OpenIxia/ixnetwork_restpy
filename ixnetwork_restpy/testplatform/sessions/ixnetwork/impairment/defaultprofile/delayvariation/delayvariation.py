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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class DelayVariation(Base):
    """Randomly vary packet delay.  Can only be used on a profile with delay enabled.
    The DelayVariation class encapsulates a required delayVariation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'delayVariation'
    _SDM_ATT_MAP = {
        'Distribution': 'distribution',
        'Enabled': 'enabled',
        'ExponentialMeanArrival': 'exponentialMeanArrival',
        'GaussianStandardDeviation': 'gaussianStandardDeviation',
        'UniformSpread': 'uniformSpread',
        'Units': 'units',
    }

    def __init__(self, parent):
        super(DelayVariation, self).__init__(parent)

    @property
    def Distribution(self):
        """
        Returns
        -------
        - str(exponential | gaussian | kExponential | kGaussian | kUniform | uniform): Specify the distribution of the random variation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Distribution'])
    @Distribution.setter
    def Distribution(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Distribution'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, randomly vary the packet delay.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExponentialMeanArrival(self):
        """
        Returns
        -------
        - number: Mean arrival time for the exponential distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExponentialMeanArrival'])
    @ExponentialMeanArrival.setter
    def ExponentialMeanArrival(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExponentialMeanArrival'], value)

    @property
    def GaussianStandardDeviation(self):
        """
        Returns
        -------
        - number: Standard deviation for the Gaussian distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP['GaussianStandardDeviation'])
    @GaussianStandardDeviation.setter
    def GaussianStandardDeviation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['GaussianStandardDeviation'], value)

    @property
    def UniformSpread(self):
        """
        Returns
        -------
        - number: Spread for the uniform distribution.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UniformSpread'])
    @UniformSpread.setter
    def UniformSpread(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UniformSpread'], value)

    @property
    def Units(self):
        """
        Returns
        -------
        - str(kilometers | kKilometers | kMicroseconds | kMilliseconds | kSeconds | microseconds | milliseconds | seconds): Specify the units for the value of the spread, standard deviation, or mean arrival time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Units'])
    @Units.setter
    def Units(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Units'], value)

    def update(self, Distribution=None, Enabled=None, ExponentialMeanArrival=None, GaussianStandardDeviation=None, UniformSpread=None, Units=None):
        """Updates delayVariation resource on the server.

        Args
        ----
        - Distribution (str(exponential | gaussian | kExponential | kGaussian | kUniform | uniform)): Specify the distribution of the random variation.
        - Enabled (bool): If true, randomly vary the packet delay.
        - ExponentialMeanArrival (number): Mean arrival time for the exponential distribution.
        - GaussianStandardDeviation (number): Standard deviation for the Gaussian distribution.
        - UniformSpread (number): Spread for the uniform distribution.
        - Units (str(kilometers | kKilometers | kMicroseconds | kMilliseconds | kSeconds | microseconds | milliseconds | seconds)): Specify the units for the value of the spread, standard deviation, or mean arrival time.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
