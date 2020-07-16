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


class Base64CodeOptions(Base):
    """Contains the base64 encoding code generation options
    The Base64CodeOptions class encapsulates a required base64CodeOptions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'base64CodeOptions'
    _SDM_ATT_MAP = {
        'IncludeSampleCode': 'includeSampleCode',
        'SampleObjectReferences': 'sampleObjectReferences',
    }

    def __init__(self, parent):
        super(Base64CodeOptions, self).__init__(parent)

    @property
    def IncludeSampleCode(self):
        """
        Returns
        -------
        - bool: Flag to include sample code
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeSampleCode'])
    @IncludeSampleCode.setter
    def IncludeSampleCode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeSampleCode'], value)

    @property
    def SampleObjectReferences(self):
        """
        Returns
        -------
        - list(str[None]): A list of object references used to generate sample code
        """
        return self._get_attribute(self._SDM_ATT_MAP['SampleObjectReferences'])
    @SampleObjectReferences.setter
    def SampleObjectReferences(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SampleObjectReferences'], value)

    def update(self, IncludeSampleCode=None, SampleObjectReferences=None):
        """Updates base64CodeOptions resource on the server.

        Args
        ----
        - IncludeSampleCode (bool): Flag to include sample code
        - SampleObjectReferences (list(str[None])): A list of object references used to generate sample code

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))
