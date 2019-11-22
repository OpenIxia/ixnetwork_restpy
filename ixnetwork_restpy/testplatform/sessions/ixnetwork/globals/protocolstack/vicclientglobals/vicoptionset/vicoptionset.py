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


class VicOptionSet(Base):
    """Defines a group of TLV options.
    The VicOptionSet class encapsulates a list of vicOptionSet resources that is be managed by the user.
    A list of resources can be retrieved from the server using the VicOptionSet.find() method.
    The list can be managed by the user by using the VicOptionSet.add() and VicOptionSet.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vicOptionSet'

    def __init__(self, parent):
        super(VicOptionSet, self).__init__(parent)

    @property
    def VicOptionTlv(self):
        """An instance of the VicOptionTlv class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptiontlv.vicoptiontlv.VicOptionTlv)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.globals.protocolstack.vicclientglobals.vicoptionset.vicoptiontlv.vicoptiontlv import VicOptionTlv
        return VicOptionTlv(self)

    @property
    def Defaultp(self):
        """True to assign this option set to new ranges.

        Returns:
            bool
        """
        return self._get_attribute('defaultp')
    @Defaultp.setter
    def Defaultp(self, value):
        self._set_attribute('defaultp', value)

    @property
    def FeatureType(self):
        """The usage purpose of this TLV set.

        Returns:
            number
        """
        return self._get_attribute('featureType')
    @FeatureType.setter
    def FeatureType(self, value):
        self._set_attribute('featureType', value)

    @property
    def Name(self):
        """Option set name.

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

    def update(self, Defaultp=None, FeatureType=None, Name=None):
        """Updates a child instance of vicOptionSet on the server.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            FeatureType (number): The usage purpose of this TLV set.
            Name (str): Option set name.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, Defaultp=None, FeatureType=None, Name=None):
        """Adds a new vicOptionSet node on the server and retrieves it in this instance.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            FeatureType (number): The usage purpose of this TLV set.
            Name (str): Option set name.

        Returns:
            self: This instance with all currently retrieved vicOptionSet data using find and the newly added vicOptionSet data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the vicOptionSet data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Defaultp=None, FeatureType=None, Name=None, ObjectId=None):
        """Finds and retrieves vicOptionSet data from the server.

        All named parameters support regex and can be used to selectively retrieve vicOptionSet data from the server.
        By default the find method takes no parameters and will retrieve all vicOptionSet data from the server.

        Args:
            Defaultp (bool): True to assign this option set to new ranges.
            FeatureType (number): The usage purpose of this TLV set.
            Name (str): Option set name.
            ObjectId (str): Unique identifier for this object

        Returns:
            self: This instance with matching vicOptionSet data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of vicOptionSet data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the vicOptionSet data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
