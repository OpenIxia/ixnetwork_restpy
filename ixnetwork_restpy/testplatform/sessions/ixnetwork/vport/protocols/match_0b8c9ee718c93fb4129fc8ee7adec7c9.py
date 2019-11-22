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


class Match(Base):
    """NOT DEFINED
    The Match class encapsulates a required match resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'match'

    def __init__(self, parent):
        super(Match, self).__init__(parent)

    @property
    def MatchFields(self):
        """An instance of the MatchFields class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchfields_39df33112bb1cfa56367ea58e168f287.MatchFields)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.matchfields_39df33112bb1cfa56367ea58e168f287 import MatchFields
        return MatchFields(self)._select()

    @property
    def ExperimenterData(self):
        """NOT DEFINED

        Returns:
            str
        """
        return self._get_attribute('experimenterData')
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute('experimenterData', value)

    @property
    def ExperimenterDataLength(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('experimenterDataLength')
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute('experimenterDataLength', value)

    @property
    def ExperimenterField(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('experimenterField')
    @ExperimenterField.setter
    def ExperimenterField(self, value):
        self._set_attribute('experimenterField', value)

    @property
    def ExperimenterHasMask(self):
        """NOT DEFINED

        Returns:
            bool
        """
        return self._get_attribute('experimenterHasMask')
    @ExperimenterHasMask.setter
    def ExperimenterHasMask(self, value):
        self._set_attribute('experimenterHasMask', value)

    @property
    def ExperimenterId(self):
        """NOT DEFINED

        Returns:
            number
        """
        return self._get_attribute('experimenterId')
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute('experimenterId', value)

    def update(self, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterField=None, ExperimenterHasMask=None, ExperimenterId=None):
        """Updates a child instance of match on the server.

        Args:
            ExperimenterData (str): NOT DEFINED
            ExperimenterDataLength (number): NOT DEFINED
            ExperimenterField (number): NOT DEFINED
            ExperimenterHasMask (bool): NOT DEFINED
            ExperimenterId (number): NOT DEFINED

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
