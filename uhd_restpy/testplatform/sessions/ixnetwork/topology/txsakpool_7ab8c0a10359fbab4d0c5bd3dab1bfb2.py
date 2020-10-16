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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class TxSakPool(Base):
    """Tx SAKs configuration.
    The TxSakPool class encapsulates a required txSakPool resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'txSakPool'
    _SDM_ATT_MAP = {
        'ActiveSak': 'activeSak',
        'AnInUse': 'anInUse',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Name': 'name',
        'TxSak128': 'txSak128',
        'TxSak256': 'txSak256',
        'TxSalt': 'txSalt',
        'TxSsci': 'txSsci',
    }

    def __init__(self, parent):
        super(TxSakPool, self).__init__(parent)

    @property
    def ActiveSak(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Points to the SAK value with which packets are currently getting encrypted.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActiveSak']))

    @property
    def AnInUse(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Shows the current AN value in use.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AnInUse']))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def TxSak128(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 128 bit value of Secure Association Key with which DUT is expected to encrypt MACsec packets.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxSak128']))

    @property
    def TxSak256(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 256 bit value of Secure Association Key with which DUT is expected to encrypt MACsec packets.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxSak256']))

    @property
    def TxSalt(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 12 bytes Salt value for XPN cipher suites.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxSalt']))

    @property
    def TxSsci(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): 4 bytes Short SCI for XPN cipher suites.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TxSsci']))

    def update(self, Name=None):
        """Updates txSakPool resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def get_device_ids(self, PortNames=None, ActiveSak=None, AnInUse=None, TxSak128=None, TxSak256=None, TxSalt=None, TxSsci=None):
        """Base class infrastructure that gets a list of txSakPool device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActiveSak (str): optional regex of activeSak
        - AnInUse (str): optional regex of anInUse
        - TxSak128 (str): optional regex of txSak128
        - TxSak256 (str): optional regex of txSak256
        - TxSalt (str): optional regex of txSalt
        - TxSsci (str): optional regex of txSsci

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
