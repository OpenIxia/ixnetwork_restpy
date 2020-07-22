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


class CustomTopologyNodeTopologyRange(Base):
    """NOT DEFINED
    The CustomTopologyNodeTopologyRange class encapsulates a list of customTopologyNodeTopologyRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyNodeTopologyRange.find() method.
    The list can be managed by using the CustomTopologyNodeTopologyRange.add() and CustomTopologyNodeTopologyRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyNodeTopologyRange'
    _SDM_ATT_MAP = {
        'NicknameCount': 'nicknameCount',
        'NodeNicknameIncrement': 'nodeNicknameIncrement',
        'NumberOftreesToCompute': 'numberOftreesToCompute',
        'StartNickname': 'startNickname',
    }

    def __init__(self, parent):
        super(CustomTopologyNodeTopologyRange, self).__init__(parent)

    @property
    def CustomTopologyInterestedVlanRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyinterestedvlanrange_b57874c12eda43d1719e01dcadf708c9.CustomTopologyInterestedVlanRange): An instance of the CustomTopologyInterestedVlanRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.customtopologyinterestedvlanrange_b57874c12eda43d1719e01dcadf708c9 import CustomTopologyInterestedVlanRange
        return CustomTopologyInterestedVlanRange(self)

    @property
    def NicknameCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NicknameCount'])
    @NicknameCount.setter
    def NicknameCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NicknameCount'], value)

    @property
    def NodeNicknameIncrement(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NodeNicknameIncrement'])
    @NodeNicknameIncrement.setter
    def NodeNicknameIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NodeNicknameIncrement'], value)

    @property
    def NumberOftreesToCompute(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOftreesToCompute'])
    @NumberOftreesToCompute.setter
    def NumberOftreesToCompute(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOftreesToCompute'], value)

    @property
    def StartNickname(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartNickname'])
    @StartNickname.setter
    def StartNickname(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartNickname'], value)

    def update(self, NicknameCount=None, NodeNicknameIncrement=None, NumberOftreesToCompute=None, StartNickname=None):
        """Updates customTopologyNodeTopologyRange resource on the server.

        Args
        ----
        - NicknameCount (number): NOT DEFINED
        - NodeNicknameIncrement (number): NOT DEFINED
        - NumberOftreesToCompute (number): NOT DEFINED
        - StartNickname (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, NicknameCount=None, NodeNicknameIncrement=None, NumberOftreesToCompute=None, StartNickname=None):
        """Adds a new customTopologyNodeTopologyRange resource on the server and adds it to the container.

        Args
        ----
        - NicknameCount (number): NOT DEFINED
        - NodeNicknameIncrement (number): NOT DEFINED
        - NumberOftreesToCompute (number): NOT DEFINED
        - StartNickname (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyNodeTopologyRange resources using find and the newly added customTopologyNodeTopologyRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyNodeTopologyRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, NicknameCount=None, NodeNicknameIncrement=None, NumberOftreesToCompute=None, StartNickname=None):
        """Finds and retrieves customTopologyNodeTopologyRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyNodeTopologyRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyNodeTopologyRange resources from the server.

        Args
        ----
        - NicknameCount (number): NOT DEFINED
        - NodeNicknameIncrement (number): NOT DEFINED
        - NumberOftreesToCompute (number): NOT DEFINED
        - StartNickname (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyNodeTopologyRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyNodeTopologyRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyNodeTopologyRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
