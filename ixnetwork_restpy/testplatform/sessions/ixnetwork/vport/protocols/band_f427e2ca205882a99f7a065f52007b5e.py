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


class Band(Base):
    """Bands indicate a list of rate bands. It can contain any number of bands, and each band type can be repeated when it make sense. Only a single band is used at a time. If the current rate of packets exceed the rate of multiple bands, the band with the highest configured rate is used
    The Band class encapsulates a list of band resources that are managed by the user.
    A list of resources can be retrieved from the server using the Band.find() method.
    The list can be managed by using the Band.add() and Band.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'band'
    _SDM_ATT_MAP = {
        'BurstSize': 'burstSize',
        'Description': 'description',
        'Experimenter': 'experimenter',
        'PrecedenceLevel': 'precedenceLevel',
        'Rate': 'rate',
        'Type': 'type',
    }

    def __init__(self, parent):
        super(Band, self).__init__(parent)

    @property
    def BurstSize(self):
        """
        Returns
        -------
        - number: This indicates the length of the packet or byte burst to consider for applying the meter. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BurstSize'])
    @BurstSize.setter
    def BurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BurstSize'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description of the band.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Experimenter(self):
        """
        Returns
        -------
        - number: The experimenter ID. The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Experimenter'])
    @Experimenter.setter
    def Experimenter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Experimenter'], value)

    @property
    def PrecedenceLevel(self):
        """
        Returns
        -------
        - number: This indicates the amount by which the drop precedence of the packet should be increased if the band is exceeded. The default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PrecedenceLevel'])
    @PrecedenceLevel.setter
    def PrecedenceLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PrecedenceLevel'], value)

    @property
    def Rate(self):
        """
        Returns
        -------
        - number: This indicates the rate value above which the corresponding band may apply to packets The default value is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Rate'])
    @Rate.setter
    def Rate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Rate'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - str(drop | dscpRemark | experimenter): Select the band type from the list.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    def update(self, BurstSize=None, Description=None, Experimenter=None, PrecedenceLevel=None, Rate=None, Type=None):
        """Updates band resource on the server.

        Args
        ----
        - BurstSize (number): This indicates the length of the packet or byte burst to consider for applying the meter. The default value is 1.
        - Description (str): A description of the band.
        - Experimenter (number): The experimenter ID. The default value is 1.
        - PrecedenceLevel (number): This indicates the amount by which the drop precedence of the packet should be increased if the band is exceeded. The default value is 0.
        - Rate (number): This indicates the rate value above which the corresponding band may apply to packets The default value is 1.
        - Type (str(drop | dscpRemark | experimenter)): Select the band type from the list.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BurstSize=None, Description=None, Experimenter=None, PrecedenceLevel=None, Rate=None, Type=None):
        """Adds a new band resource on the server and adds it to the container.

        Args
        ----
        - BurstSize (number): This indicates the length of the packet or byte burst to consider for applying the meter. The default value is 1.
        - Description (str): A description of the band.
        - Experimenter (number): The experimenter ID. The default value is 1.
        - PrecedenceLevel (number): This indicates the amount by which the drop precedence of the packet should be increased if the band is exceeded. The default value is 0.
        - Rate (number): This indicates the rate value above which the corresponding band may apply to packets The default value is 1.
        - Type (str(drop | dscpRemark | experimenter)): Select the band type from the list.

        Returns
        -------
        - self: This instance with all currently retrieved band resources using find and the newly added band resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained band resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BurstSize=None, Description=None, Experimenter=None, PrecedenceLevel=None, Rate=None, Type=None):
        """Finds and retrieves band resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve band resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all band resources from the server.

        Args
        ----
        - BurstSize (number): This indicates the length of the packet or byte burst to consider for applying the meter. The default value is 1.
        - Description (str): A description of the band.
        - Experimenter (number): The experimenter ID. The default value is 1.
        - PrecedenceLevel (number): This indicates the amount by which the drop precedence of the packet should be increased if the band is exceeded. The default value is 0.
        - Rate (number): This indicates the rate value above which the corresponding band may apply to packets The default value is 1.
        - Type (str(drop | dscpRemark | experimenter)): Select the band type from the list.

        Returns
        -------
        - self: This instance with matching band resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of band data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the band resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
