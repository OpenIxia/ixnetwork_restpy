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


class WriteAction(Base):
    """NOT DEFINED
    The WriteAction class encapsulates a required writeAction resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'writeAction'
    _SDM_ATT_MAP = {
        'ExperimenterData': 'experimenterData',
        'ExperimenterDataLength': 'experimenterDataLength',
        'ExperimenterDataLengthMiss': 'experimenterDataLengthMiss',
        'ExperimenterDataMiss': 'experimenterDataMiss',
        'ExperimenterId': 'experimenterId',
        'ExperimenterIdMiss': 'experimenterIdMiss',
    }

    def __init__(self, parent):
        super(WriteAction, self).__init__(parent)

    @property
    def WriteActionMissType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionmisstype_e63eee24d23bc546c8138246edb35dfe.WriteActionMissType): An instance of the WriteActionMissType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactionmisstype_e63eee24d23bc546c8138246edb35dfe import WriteActionMissType
        return WriteActionMissType(self)._select()

    @property
    def WriteActionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactiontype_419a58f4451d612a6f8c7aafe22d0a6c.WriteActionType): An instance of the WriteActionType class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.writeactiontype_419a58f4451d612a6f8c7aafe22d0a6c import WriteActionType
        return WriteActionType(self)._select()

    @property
    def ExperimenterData(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterData'])
    @ExperimenterData.setter
    def ExperimenterData(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterData'], value)

    @property
    def ExperimenterDataLength(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'])
    @ExperimenterDataLength.setter
    def ExperimenterDataLength(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLength'], value)

    @property
    def ExperimenterDataLengthMiss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataLengthMiss'])
    @ExperimenterDataLengthMiss.setter
    def ExperimenterDataLengthMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataLengthMiss'], value)

    @property
    def ExperimenterDataMiss(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterDataMiss'])
    @ExperimenterDataMiss.setter
    def ExperimenterDataMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterDataMiss'], value)

    @property
    def ExperimenterId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterId'])
    @ExperimenterId.setter
    def ExperimenterId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterId'], value)

    @property
    def ExperimenterIdMiss(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExperimenterIdMiss'])
    @ExperimenterIdMiss.setter
    def ExperimenterIdMiss(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExperimenterIdMiss'], value)

    def update(self, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterDataLengthMiss=None, ExperimenterDataMiss=None, ExperimenterId=None, ExperimenterIdMiss=None):
        """Updates writeAction resource on the server.

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
