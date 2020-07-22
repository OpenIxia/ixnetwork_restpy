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


class MulticastLeafRange(Base):
    """Configures the multicast leaf range values.
    The MulticastLeafRange class encapsulates a list of multicastLeafRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the MulticastLeafRange.find() method.
    The list can be managed by using the MulticastLeafRange.add() and MulticastLeafRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'multicastLeafRange'
    _SDM_ATT_MAP = {
        'ContinuousIncrOpaqueValuesAcrossRoot': 'continuousIncrOpaqueValuesAcrossRoot',
        'Enabled': 'enabled',
        'LabelValueStart': 'labelValueStart',
        'LabelValueStep': 'labelValueStep',
        'LspCountPerRoot': 'lspCountPerRoot',
        'LspType': 'lspType',
        'RootAddrCount': 'rootAddrCount',
        'RootAddrStep': 'rootAddrStep',
        'RootAddress': 'rootAddress',
    }

    def __init__(self, parent):
        super(MulticastLeafRange, self).__init__(parent)

    @property
    def GroupTrafficRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouptrafficrange_8bb3915c49714cddd1deea69159abce3.GroupTrafficRange): An instance of the GroupTrafficRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouptrafficrange_8bb3915c49714cddd1deea69159abce3 import GroupTrafficRange
        return GroupTrafficRange(self)

    @property
    def OpaqueValueElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_0125173541665eff2bf2844a26c5299f.OpaqueValueElement): An instance of the OpaqueValueElement class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.opaquevalueelement_0125173541665eff2bf2844a26c5299f import OpaqueValueElement
        return OpaqueValueElement(self)

    @property
    def ContinuousIncrOpaqueValuesAcrossRoot(self):
        """
        Returns
        -------
        - bool: It signifies the continuous increment of opaque values across root.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ContinuousIncrOpaqueValuesAcrossRoot'])
    @ContinuousIncrOpaqueValuesAcrossRoot.setter
    def ContinuousIncrOpaqueValuesAcrossRoot(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ContinuousIncrOpaqueValuesAcrossRoot'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the protocol.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

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
    def LabelValueStep(self):
        """
        Returns
        -------
        - number: The label value increment step for more than 1 range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LabelValueStep'])
    @LabelValueStep.setter
    def LabelValueStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LabelValueStep'], value)

    @property
    def LspCountPerRoot(self):
        """
        Returns
        -------
        - number: This is to specify how many different LSPs are created per Root.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspCountPerRoot'])
    @LspCountPerRoot.setter
    def LspCountPerRoot(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LspCountPerRoot'], value)

    @property
    def LspType(self):
        """
        Returns
        -------
        - str(p2mp): The type of multicast LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LspType'])

    @property
    def RootAddrCount(self):
        """
        Returns
        -------
        - number: The root address count for this Multicast FEC range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootAddrCount'])
    @RootAddrCount.setter
    def RootAddrCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootAddrCount'], value)

    @property
    def RootAddrStep(self):
        """
        Returns
        -------
        - str: The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootAddrStep'])
    @RootAddrStep.setter
    def RootAddrStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootAddrStep'], value)

    @property
    def RootAddress(self):
        """
        Returns
        -------
        - str: The root address of the multicast LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RootAddress'])
    @RootAddress.setter
    def RootAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RootAddress'], value)

    def update(self, ContinuousIncrOpaqueValuesAcrossRoot=None, Enabled=None, LabelValueStart=None, LabelValueStep=None, LspCountPerRoot=None, RootAddrCount=None, RootAddrStep=None, RootAddress=None):
        """Updates multicastLeafRange resource on the server.

        Args
        ----
        - ContinuousIncrOpaqueValuesAcrossRoot (bool): It signifies the continuous increment of opaque values across root.
        - Enabled (bool): If true, enables the protocol.
        - LabelValueStart (number): The first label in the range of labels.
        - LabelValueStep (number): The label value increment step for more than 1 range.
        - LspCountPerRoot (number): This is to specify how many different LSPs are created per Root.
        - RootAddrCount (number): The root address count for this Multicast FEC range.
        - RootAddrStep (str): The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        - RootAddress (str): The root address of the multicast LSP.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ContinuousIncrOpaqueValuesAcrossRoot=None, Enabled=None, LabelValueStart=None, LabelValueStep=None, LspCountPerRoot=None, RootAddrCount=None, RootAddrStep=None, RootAddress=None):
        """Adds a new multicastLeafRange resource on the server and adds it to the container.

        Args
        ----
        - ContinuousIncrOpaqueValuesAcrossRoot (bool): It signifies the continuous increment of opaque values across root.
        - Enabled (bool): If true, enables the protocol.
        - LabelValueStart (number): The first label in the range of labels.
        - LabelValueStep (number): The label value increment step for more than 1 range.
        - LspCountPerRoot (number): This is to specify how many different LSPs are created per Root.
        - RootAddrCount (number): The root address count for this Multicast FEC range.
        - RootAddrStep (str): The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        - RootAddress (str): The root address of the multicast LSP.

        Returns
        -------
        - self: This instance with all currently retrieved multicastLeafRange resources using find and the newly added multicastLeafRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained multicastLeafRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ContinuousIncrOpaqueValuesAcrossRoot=None, Enabled=None, LabelValueStart=None, LabelValueStep=None, LspCountPerRoot=None, LspType=None, RootAddrCount=None, RootAddrStep=None, RootAddress=None):
        """Finds and retrieves multicastLeafRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve multicastLeafRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all multicastLeafRange resources from the server.

        Args
        ----
        - ContinuousIncrOpaqueValuesAcrossRoot (bool): It signifies the continuous increment of opaque values across root.
        - Enabled (bool): If true, enables the protocol.
        - LabelValueStart (number): The first label in the range of labels.
        - LabelValueStep (number): The label value increment step for more than 1 range.
        - LspCountPerRoot (number): This is to specify how many different LSPs are created per Root.
        - LspType (str(p2mp)): The type of multicast LSP.
        - RootAddrCount (number): The root address count for this Multicast FEC range.
        - RootAddrStep (str): The Root Address increment step. This is applicable only if Root Address Count is greater than 1.
        - RootAddress (str): The root address of the multicast LSP.

        Returns
        -------
        - self: This instance with matching multicastLeafRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of multicastLeafRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the multicastLeafRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
