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


class AdvFecRange(Base):
    """A set of FECs to be included in the LDP router.
    The AdvFecRange class encapsulates a list of advFecRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the AdvFecRange.find() method.
    The list can be managed by using the AdvFecRange.add() and AdvFecRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'advFecRange'
    _SDM_ATT_MAP = {
        'EnablePacking': 'enablePacking',
        'EnableReplyingLspPing': 'enableReplyingLspPing',
        'Enabled': 'enabled',
        'FirstNetwork': 'firstNetwork',
        'LabelMode': 'labelMode',
        'LabelValueStart': 'labelValueStart',
        'MaskWidth': 'maskWidth',
        'NumberOfNetworks': 'numberOfNetworks',
    }

    def __init__(self, parent):
        super(AdvFecRange, self).__init__(parent)

    @property
    def EnablePacking(self):
        """
        Returns
        -------
        - bool: (For IPv4 FEC ranges and in Unsolicited Label Distribution Mode ONLY) If checked, FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnablePacking'])
    @EnablePacking.setter
    def EnablePacking(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnablePacking'], value)

    @property
    def EnableReplyingLspPing(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableReplyingLspPing'])
    @EnableReplyingLspPing.setter
    def EnableReplyingLspPing(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableReplyingLspPing'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this FEC range for use in label mapping messages. By default, the Ixia LDP emulation uses the prefix FEC type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FirstNetwork(self):
        """
        Returns
        -------
        - str: The first network address in the range (in IP address format).
        """
        return self._get_attribute(self._SDM_ATT_MAP['FirstNetwork'])
    @FirstNetwork.setter
    def FirstNetwork(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FirstNetwork'], value)

    @property
    def LabelMode(self):
        """
        Returns
        -------
        - str(none | increment): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelMode'])
    @LabelMode.setter
    def LabelMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelMode'], value)

    @property
    def LabelValueStart(self):
        """
        Returns
        -------
        - number: The first label in the range of labels.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelValueStart'])
    @LabelValueStart.setter
    def LabelValueStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelValueStart'], value)

    @property
    def MaskWidth(self):
        """
        Returns
        -------
        - number: The number of bits in the mask applied to the network address. The masked bits in the First Network address form the address prefix.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaskWidth'])
    @MaskWidth.setter
    def MaskWidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaskWidth'], value)

    @property
    def NumberOfNetworks(self):
        """
        Returns
        -------
        - number: The number of network addresses to be included in the range. The maximum number of valid possible addresses depends on the values for the first network and the network mask.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfNetworks'])
    @NumberOfNetworks.setter
    def NumberOfNetworks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfNetworks'], value)

    def update(self, EnablePacking=None, EnableReplyingLspPing=None, Enabled=None, FirstNetwork=None, LabelMode=None, LabelValueStart=None, MaskWidth=None, NumberOfNetworks=None):
        """Updates advFecRange resource on the server.

        Args
        ----
        - EnablePacking (bool): (For IPv4 FEC ranges and in Unsolicited Label Distribution Mode ONLY) If checked, FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        - EnableReplyingLspPing (bool): NOT DEFINED
        - Enabled (bool): Enables this FEC range for use in label mapping messages. By default, the Ixia LDP emulation uses the prefix FEC type.
        - FirstNetwork (str): The first network address in the range (in IP address format).
        - LabelMode (str(none | increment)): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        - LabelValueStart (number): The first label in the range of labels.
        - MaskWidth (number): The number of bits in the mask applied to the network address. The masked bits in the First Network address form the address prefix.
        - NumberOfNetworks (number): The number of network addresses to be included in the range. The maximum number of valid possible addresses depends on the values for the first network and the network mask.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnablePacking=None, EnableReplyingLspPing=None, Enabled=None, FirstNetwork=None, LabelMode=None, LabelValueStart=None, MaskWidth=None, NumberOfNetworks=None):
        """Adds a new advFecRange resource on the server and adds it to the container.

        Args
        ----
        - EnablePacking (bool): (For IPv4 FEC ranges and in Unsolicited Label Distribution Mode ONLY) If checked, FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        - EnableReplyingLspPing (bool): NOT DEFINED
        - Enabled (bool): Enables this FEC range for use in label mapping messages. By default, the Ixia LDP emulation uses the prefix FEC type.
        - FirstNetwork (str): The first network address in the range (in IP address format).
        - LabelMode (str(none | increment)): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        - LabelValueStart (number): The first label in the range of labels.
        - MaskWidth (number): The number of bits in the mask applied to the network address. The masked bits in the First Network address form the address prefix.
        - NumberOfNetworks (number): The number of network addresses to be included in the range. The maximum number of valid possible addresses depends on the values for the first network and the network mask.

        Returns
        -------
        - self: This instance with all currently retrieved advFecRange resources using find and the newly added advFecRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained advFecRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnablePacking=None, EnableReplyingLspPing=None, Enabled=None, FirstNetwork=None, LabelMode=None, LabelValueStart=None, MaskWidth=None, NumberOfNetworks=None):
        """Finds and retrieves advFecRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve advFecRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all advFecRange resources from the server.

        Args
        ----
        - EnablePacking (bool): (For IPv4 FEC ranges and in Unsolicited Label Distribution Mode ONLY) If checked, FEC ranges will be aggregated within a single LDP PDU to conserve bandwidth and processing.
        - EnableReplyingLspPing (bool): NOT DEFINED
        - Enabled (bool): Enables this FEC range for use in label mapping messages. By default, the Ixia LDP emulation uses the prefix FEC type.
        - FirstNetwork (str): The first network address in the range (in IP address format).
        - LabelMode (str(none | increment)): Indicates whether the same label or incrementing labels should be used in the VC ranges.
        - LabelValueStart (number): The first label in the range of labels.
        - MaskWidth (number): The number of bits in the mask applied to the network address. The masked bits in the First Network address form the address prefix.
        - NumberOfNetworks (number): The number of network addresses to be included in the range. The maximum number of valid possible addresses depends on the values for the first network and the network mask.

        Returns
        -------
        - self: This instance with matching advFecRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of advFecRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the advFecRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
