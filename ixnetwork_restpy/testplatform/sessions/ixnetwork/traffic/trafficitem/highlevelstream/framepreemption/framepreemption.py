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


class FramePreemption(Base):
    """
    The FramePreemption class encapsulates a list of framePreemption resources that are managed by the user.
    A list of resources can be retrieved from the server using the FramePreemption.find() method.
    The list can be managed by using the FramePreemption.add() and FramePreemption.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'framePreemption'
    _SDM_ATT_MAP = {
        'AutoFragmentCount': 'autoFragmentCount',
        'Enable': 'enable',
        'FragmentCount': 'fragmentCount',
        'FrameType': 'frameType',
        'LastFragment': 'lastFragment',
        'SmdType': 'smdType',
    }

    def __init__(self, parent):
        super(FramePreemption, self).__init__(parent)

    @property
    def AutoFragmentCount(self):
        """
        Returns
        -------
        - bool: Let the fragments be auto counted
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoFragmentCount'])
    @AutoFragmentCount.setter
    def AutoFragmentCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoFragmentCount'], value)

    @property
    def Enable(self):
        """
        Returns
        -------
        - bool: Enable frame preemption on the given stream. Disabled indicates an express frame
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enable'])
    @Enable.setter
    def Enable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enable'], value)

    @property
    def FragmentCount(self):
        """
        Returns
        -------
        - number: Set the fragment count (a value between 0 and 3)
        """
        return self._get_attribute(self._SDM_ATT_MAP['FragmentCount'])
    @FragmentCount.setter
    def FragmentCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FragmentCount'], value)

    @property
    def FrameType(self):
        """
        Returns
        -------
        - str(control | fragment | invalid | wholeFrame): Select the frame type
        """
        return self._get_attribute(self._SDM_ATT_MAP['FrameType'])
    @FrameType.setter
    def FrameType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FrameType'], value)

    @property
    def LastFragment(self):
        """
        Returns
        -------
        - bool: Indicates if this is the last fragment of the preemptable packet
        """
        return self._get_attribute(self._SDM_ATT_MAP['LastFragment'])
    @LastFragment.setter
    def LastFragment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LastFragment'], value)

    @property
    def SmdType(self):
        """
        Returns
        -------
        - str(autoSMDC | autoSMDS | invalidSMD | smdC0 | smdC1 | smdC2 | smdC3 | smdE | smdR | smdS0 | smdS1 | smdS2 | smdS3 | smdV): Select the SMD type
        """
        return self._get_attribute(self._SDM_ATT_MAP['SmdType'])
    @SmdType.setter
    def SmdType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SmdType'], value)

    def update(self, AutoFragmentCount=None, Enable=None, FragmentCount=None, FrameType=None, LastFragment=None, SmdType=None):
        """Updates framePreemption resource on the server.

        Args
        ----
        - AutoFragmentCount (bool): Let the fragments be auto counted
        - Enable (bool): Enable frame preemption on the given stream. Disabled indicates an express frame
        - FragmentCount (number): Set the fragment count (a value between 0 and 3)
        - FrameType (str(control | fragment | invalid | wholeFrame)): Select the frame type
        - LastFragment (bool): Indicates if this is the last fragment of the preemptable packet
        - SmdType (str(autoSMDC | autoSMDS | invalidSMD | smdC0 | smdC1 | smdC2 | smdC3 | smdE | smdR | smdS0 | smdS1 | smdS2 | smdS3 | smdV)): Select the SMD type

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoFragmentCount=None, Enable=None, FragmentCount=None, FrameType=None, LastFragment=None, SmdType=None):
        """Adds a new framePreemption resource on the server and adds it to the container.

        Args
        ----
        - AutoFragmentCount (bool): Let the fragments be auto counted
        - Enable (bool): Enable frame preemption on the given stream. Disabled indicates an express frame
        - FragmentCount (number): Set the fragment count (a value between 0 and 3)
        - FrameType (str(control | fragment | invalid | wholeFrame)): Select the frame type
        - LastFragment (bool): Indicates if this is the last fragment of the preemptable packet
        - SmdType (str(autoSMDC | autoSMDS | invalidSMD | smdC0 | smdC1 | smdC2 | smdC3 | smdE | smdR | smdS0 | smdS1 | smdS2 | smdS3 | smdV)): Select the SMD type

        Returns
        -------
        - self: This instance with all currently retrieved framePreemption resources using find and the newly added framePreemption resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained framePreemption resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AutoFragmentCount=None, Enable=None, FragmentCount=None, FrameType=None, LastFragment=None, SmdType=None):
        """Finds and retrieves framePreemption resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve framePreemption resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all framePreemption resources from the server.

        Args
        ----
        - AutoFragmentCount (bool): Let the fragments be auto counted
        - Enable (bool): Enable frame preemption on the given stream. Disabled indicates an express frame
        - FragmentCount (number): Set the fragment count (a value between 0 and 3)
        - FrameType (str(control | fragment | invalid | wholeFrame)): Select the frame type
        - LastFragment (bool): Indicates if this is the last fragment of the preemptable packet
        - SmdType (str(autoSMDC | autoSMDS | invalidSMD | smdC0 | smdC1 | smdC2 | smdC3 | smdE | smdR | smdS0 | smdS1 | smdS2 | smdS3 | smdV)): Select the SMD type

        Returns
        -------
        - self: This instance with matching framePreemption resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of framePreemption data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the framePreemption resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
