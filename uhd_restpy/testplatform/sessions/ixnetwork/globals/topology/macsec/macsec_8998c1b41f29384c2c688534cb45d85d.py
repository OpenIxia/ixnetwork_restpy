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
import sys
from uhd_restpy.base import Base
from uhd_restpy.files import Files
if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class Macsec(Base):
    """MACsec Port Specific Data
    The Macsec class encapsulates a required macsec resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'macsec'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'KeyGenerationMode': 'keyGenerationMode',
        'MacsecValidation': 'macsecValidation',
        'Name': 'name',
        'ReplayProtection': 'replayProtection',
        'RowNames': 'rowNames',
        'RxSecTagOffset': 'rxSecTagOffset',
        'SecTagOffsetUnknown': 'secTagOffsetUnknown',
    }
    _SDM_ENUM_MAP = {
        'keyGenerationMode': ['staticKeyGenerationMode', 'dynamicKeyGenerationMode'],
    }

    def __init__(self, parent, list_op=False):
        super(Macsec, self).__init__(parent, list_op)

    @property
    def StartRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0.StartRate): An instance of the StartRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.startrate.startrate_2bc83a4fb9730935e8259bdb40af2dc0 import StartRate
        if len(self._object_properties) > 0:
            if self._properties.get('StartRate', None) is not None:
                return self._properties.get('StartRate')
        return StartRate(self)._select()

    @property
    def StopRate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04.StopRate): An instance of the StopRate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.globals.topology.ethernet.stoprate.stoprate_4ea9a1b38960d2b21012777131469a04 import StopRate
        if len(self._object_properties) > 0:
            if self._properties.get('StopRate', None) is not None:
                return self._properties.get('StopRate')
        return StopRate(self)._select()

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def KeyGenerationMode(self):
        # type: () -> str
        """
        Returns
        -------
        - str(staticKeyGenerationMode | dynamicKeyGenerationMode): Whether the encryption keys will be informed by MKA or configured statically in MACsec.
        """
        return self._get_attribute(self._SDM_ATT_MAP['KeyGenerationMode'])
    @KeyGenerationMode.setter
    def KeyGenerationMode(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['KeyGenerationMode'], value)

    @property
    def MacsecValidation(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Rx Validation behavior set at the port. Can be either Disabled, Check or Strict.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MacsecValidation']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ReplayProtection(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Replay protection behavior of the port. Based on this out of window packets will either be discarded or passed to the upper layer control plane plugins and corresponding stats will be incremented.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReplayProtection']))

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP['RowNames'])

    @property
    def RxSecTagOffset(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): This denotes the position of the SecTAG in macsec packets received from the DUT. The default offset is 12, but it may not be always 12 depending on different tunneling scenario.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RxSecTagOffset']))

    @property
    def SecTagOffsetUnknown(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): If the position of the SecTAG in MACsec packets received from the DUT is not known. By default it should be known, and only in some cases DUT may insert some outer headers due to which position of SecTAG will be moved.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecTagOffsetUnknown']))

    def update(self, KeyGenerationMode=None, Name=None):
        # type: (str, str) -> Macsec
        """Updates macsec resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - KeyGenerationMode (str(staticKeyGenerationMode | dynamicKeyGenerationMode)): Whether the encryption keys will be informed by MKA or configured statically in MACsec.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, KeyGenerationMode=None, Name=None, RowNames=None):
        # type: (int, str, str, str, List[str]) -> Macsec
        """Finds and retrieves macsec resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve macsec resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all macsec resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - KeyGenerationMode (str(staticKeyGenerationMode | dynamicKeyGenerationMode)): Whether the encryption keys will be informed by MKA or configured statically in MACsec.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching macsec resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of macsec data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the macsec resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, MacsecValidation=None, ReplayProtection=None, RxSecTagOffset=None, SecTagOffsetUnknown=None):
        """Base class infrastructure that gets a list of macsec device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - MacsecValidation (str): optional regex of macsecValidation
        - ReplayProtection (str): optional regex of replayProtection
        - RxSecTagOffset (str): optional regex of rxSecTagOffset
        - SecTagOffsetUnknown (str): optional regex of secTagOffsetUnknown

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
