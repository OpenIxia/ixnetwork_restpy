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


class CustomTopologySpbNodeIsidRange(Base):
    """NOT DEFINED
    The CustomTopologySpbNodeIsidRange class encapsulates a list of customTopologySpbNodeIsidRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologySpbNodeIsidRange.find() method.
    The list can be managed by using the CustomTopologySpbNodeIsidRange.add() and CustomTopologySpbNodeIsidRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologySpbNodeIsidRange'
    _SDM_ATT_MAP = {
        'CMacAddressCount': 'cMacAddressCount',
        'CMacAddressStep': 'cMacAddressStep',
        'EnableIsid': 'enableIsid',
        'InterNodeCmacAddress': 'interNodeCmacAddress',
        'InterNodeCvlan': 'interNodeCvlan',
        'InterNodeIsIdIncrement': 'interNodeIsIdIncrement',
        'InterNodeSvlan': 'interNodeSvlan',
        'Isid': 'isid',
        'RBit': 'rBit',
        'StartCmacAddress': 'startCmacAddress',
        'StartCvlan': 'startCvlan',
        'StartSvlan': 'startSvlan',
        'TBit': 'tBit',
        'TransmissionType': 'transmissionType',
        'VlanType': 'vlanType',
    }

    def __init__(self, parent):
        super(CustomTopologySpbNodeIsidRange, self).__init__(parent)

    @property
    def CMacAddressCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMacAddressCount'])
    @CMacAddressCount.setter
    def CMacAddressCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMacAddressCount'], value)

    @property
    def CMacAddressStep(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['CMacAddressStep'])
    @CMacAddressStep.setter
    def CMacAddressStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CMacAddressStep'], value)

    @property
    def EnableIsid(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIsid'])
    @EnableIsid.setter
    def EnableIsid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIsid'], value)

    @property
    def InterNodeCmacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeCmacAddress'])
    @InterNodeCmacAddress.setter
    def InterNodeCmacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeCmacAddress'], value)

    @property
    def InterNodeCvlan(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeCvlan'])
    @InterNodeCvlan.setter
    def InterNodeCvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeCvlan'], value)

    @property
    def InterNodeIsIdIncrement(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeIsIdIncrement'])
    @InterNodeIsIdIncrement.setter
    def InterNodeIsIdIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeIsIdIncrement'], value)

    @property
    def InterNodeSvlan(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeSvlan'])
    @InterNodeSvlan.setter
    def InterNodeSvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeSvlan'], value)

    @property
    def Isid(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Isid'])
    @Isid.setter
    def Isid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Isid'], value)

    @property
    def RBit(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RBit'])
    @RBit.setter
    def RBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RBit'], value)

    @property
    def StartCmacAddress(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartCmacAddress'])
    @StartCmacAddress.setter
    def StartCmacAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartCmacAddress'], value)

    @property
    def StartCvlan(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartCvlan'])
    @StartCvlan.setter
    def StartCvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartCvlan'], value)

    @property
    def StartSvlan(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSvlan'])
    @StartSvlan.setter
    def StartSvlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSvlan'], value)

    @property
    def TBit(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TBit'])
    @TBit.setter
    def TBit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TBit'], value)

    @property
    def TransmissionType(self):
        """
        Returns
        -------
        - str(unicast | multicast): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TransmissionType'])
    @TransmissionType.setter
    def TransmissionType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TransmissionType'], value)

    @property
    def VlanType(self):
        """
        Returns
        -------
        - str(singleVlan | stackedVlanQinQ): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanType'])
    @VlanType.setter
    def VlanType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanType'], value)

    def update(self, CMacAddressCount=None, CMacAddressStep=None, EnableIsid=None, InterNodeCmacAddress=None, InterNodeCvlan=None, InterNodeIsIdIncrement=None, InterNodeSvlan=None, Isid=None, RBit=None, StartCmacAddress=None, StartCvlan=None, StartSvlan=None, TBit=None, TransmissionType=None, VlanType=None):
        """Updates customTopologySpbNodeIsidRange resource on the server.

        Args
        ----
        - CMacAddressCount (number): NOT DEFINED
        - CMacAddressStep (str): NOT DEFINED
        - EnableIsid (bool): NOT DEFINED
        - InterNodeCmacAddress (str): NOT DEFINED
        - InterNodeCvlan (number): NOT DEFINED
        - InterNodeIsIdIncrement (number): NOT DEFINED
        - InterNodeSvlan (number): NOT DEFINED
        - Isid (number): NOT DEFINED
        - RBit (bool): NOT DEFINED
        - StartCmacAddress (str): NOT DEFINED
        - StartCvlan (number): NOT DEFINED
        - StartSvlan (number): NOT DEFINED
        - TBit (bool): NOT DEFINED
        - TransmissionType (str(unicast | multicast)): NOT DEFINED
        - VlanType (str(singleVlan | stackedVlanQinQ)): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CMacAddressCount=None, CMacAddressStep=None, EnableIsid=None, InterNodeCmacAddress=None, InterNodeCvlan=None, InterNodeIsIdIncrement=None, InterNodeSvlan=None, Isid=None, RBit=None, StartCmacAddress=None, StartCvlan=None, StartSvlan=None, TBit=None, TransmissionType=None, VlanType=None):
        """Adds a new customTopologySpbNodeIsidRange resource on the server and adds it to the container.

        Args
        ----
        - CMacAddressCount (number): NOT DEFINED
        - CMacAddressStep (str): NOT DEFINED
        - EnableIsid (bool): NOT DEFINED
        - InterNodeCmacAddress (str): NOT DEFINED
        - InterNodeCvlan (number): NOT DEFINED
        - InterNodeIsIdIncrement (number): NOT DEFINED
        - InterNodeSvlan (number): NOT DEFINED
        - Isid (number): NOT DEFINED
        - RBit (bool): NOT DEFINED
        - StartCmacAddress (str): NOT DEFINED
        - StartCvlan (number): NOT DEFINED
        - StartSvlan (number): NOT DEFINED
        - TBit (bool): NOT DEFINED
        - TransmissionType (str(unicast | multicast)): NOT DEFINED
        - VlanType (str(singleVlan | stackedVlanQinQ)): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologySpbNodeIsidRange resources using find and the newly added customTopologySpbNodeIsidRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologySpbNodeIsidRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CMacAddressCount=None, CMacAddressStep=None, EnableIsid=None, InterNodeCmacAddress=None, InterNodeCvlan=None, InterNodeIsIdIncrement=None, InterNodeSvlan=None, Isid=None, RBit=None, StartCmacAddress=None, StartCvlan=None, StartSvlan=None, TBit=None, TransmissionType=None, VlanType=None):
        """Finds and retrieves customTopologySpbNodeIsidRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologySpbNodeIsidRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologySpbNodeIsidRange resources from the server.

        Args
        ----
        - CMacAddressCount (number): NOT DEFINED
        - CMacAddressStep (str): NOT DEFINED
        - EnableIsid (bool): NOT DEFINED
        - InterNodeCmacAddress (str): NOT DEFINED
        - InterNodeCvlan (number): NOT DEFINED
        - InterNodeIsIdIncrement (number): NOT DEFINED
        - InterNodeSvlan (number): NOT DEFINED
        - Isid (number): NOT DEFINED
        - RBit (bool): NOT DEFINED
        - StartCmacAddress (str): NOT DEFINED
        - StartCvlan (number): NOT DEFINED
        - StartSvlan (number): NOT DEFINED
        - TBit (bool): NOT DEFINED
        - TransmissionType (str(unicast | multicast)): NOT DEFINED
        - VlanType (str(singleVlan | stackedVlanQinQ)): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologySpbNodeIsidRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologySpbNodeIsidRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologySpbNodeIsidRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
