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


class ConfigVLANParams(Base):
    """Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.
    The ConfigVLANParams class encapsulates a required configVLANParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'configVLANParams'
    _SDM_ATT_MAP = {
        'CvlanID': 'cvlanID',
        'CvlanIDStep': 'cvlanIDStep',
        'CvlanPriority': 'cvlanPriority',
        'CvlanTpid': 'cvlanTpid',
        'EnableVLAN': 'enableVLAN',
        'SvlanID': 'svlanID',
        'SvlanIDStep': 'svlanIDStep',
        'SvlanPriority': 'svlanPriority',
        'SvlanTpid': 'svlanTpid',
        'VlanID': 'vlanID',
        'VlanIDStep': 'vlanIDStep',
        'VlanPriority': 'vlanPriority',
        'VlanTpid': 'vlanTpid',
        'VlanType': 'vlanType',
    }
    _SDM_ENUM_MAP = {
        'cvlanTpid': ['vlanTpId8100', 'vlanTpId88a8', 'vlanTpId9100', 'vlanTpId9200'],
        'svlanTpid': ['vlanTpId8100', 'vlanTpId88a8', 'vlanTpId9100', 'vlanTpId9200'],
        'vlanTpid': ['vlanTpId8100', 'vlanTpId88a8', 'vlanTpId9100', 'vlanTpId9200'],
        'vlanType': ['vlanStackingTypeSingleVlan', 'vlanStackingTypeStackedVlan'],
    }

    def __init__(self, parent, list_op=False):
        super(ConfigVLANParams, self).__init__(parent, list_op)

    @property
    def CvlanID(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanID'])
    @CvlanID.setter
    def CvlanID(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CvlanID'], value)

    @property
    def CvlanIDStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanIDStep'])
    @CvlanIDStep.setter
    def CvlanIDStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CvlanIDStep'], value)

    @property
    def CvlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanPriority'])
    @CvlanPriority.setter
    def CvlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['CvlanPriority'], value)

    @property
    def CvlanTpid(self):
        # type: () -> str
        """
        Returns
        -------
        - str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanTpid'])
    @CvlanTpid.setter
    def CvlanTpid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CvlanTpid'], value)

    @property
    def EnableVLAN(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVLAN'])
    @EnableVLAN.setter
    def EnableVLAN(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableVLAN'], value)

    @property
    def SvlanID(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanID'])
    @SvlanID.setter
    def SvlanID(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SvlanID'], value)

    @property
    def SvlanIDStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanIDStep'])
    @SvlanIDStep.setter
    def SvlanIDStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SvlanIDStep'], value)

    @property
    def SvlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanPriority'])
    @SvlanPriority.setter
    def SvlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SvlanPriority'], value)

    @property
    def SvlanTpid(self):
        # type: () -> str
        """
        Returns
        -------
        - str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanTpid'])
    @SvlanTpid.setter
    def SvlanTpid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SvlanTpid'], value)

    @property
    def VlanID(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanID'])
    @VlanID.setter
    def VlanID(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['VlanID'], value)

    @property
    def VlanIDStep(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIDStep'])
    @VlanIDStep.setter
    def VlanIDStep(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['VlanIDStep'], value)

    @property
    def VlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    @property
    def VlanTpid(self):
        # type: () -> str
        """
        Returns
        -------
        - str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanTpid'])
    @VlanTpid.setter
    def VlanTpid(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['VlanTpid'], value)

    @property
    def VlanType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(vlanStackingTypeSingleVlan | vlanStackingTypeStackedVlan): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanType'])
    @VlanType.setter
    def VlanType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['VlanType'], value)

    def update(self, CvlanID=None, CvlanIDStep=None, CvlanPriority=None, CvlanTpid=None, EnableVLAN=None, SvlanID=None, SvlanIDStep=None, SvlanPriority=None, SvlanTpid=None, VlanID=None, VlanIDStep=None, VlanPriority=None, VlanTpid=None, VlanType=None):
        # type: (int, int, int, str, bool, int, int, int, str, int, int, int, str, str) -> ConfigVLANParams
        """Updates configVLANParams resource on the server.

        Args
        ----
        - CvlanID (number): Import only the best routes (provided route file has this information).
        - CvlanIDStep (number): Import only the best routes (provided route file has this information).
        - CvlanPriority (number): Import only the best routes (provided route file has this information).
        - CvlanTpid (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - EnableVLAN (bool): Import only the best routes (provided route file has this information).
        - SvlanID (number): Import only the best routes (provided route file has this information).
        - SvlanIDStep (number): Import only the best routes (provided route file has this information).
        - SvlanPriority (number): Import only the best routes (provided route file has this information).
        - SvlanTpid (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - VlanID (number): Import only the best routes (provided route file has this information).
        - VlanIDStep (number): Import only the best routes (provided route file has this information).
        - VlanPriority (number): Import only the best routes (provided route file has this information).
        - VlanTpid (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - VlanType (str(vlanStackingTypeSingleVlan | vlanStackingTypeStackedVlan)): Import only the best routes (provided route file has this information).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, CvlanID=None, CvlanIDStep=None, CvlanPriority=None, CvlanTpid=None, EnableVLAN=None, SvlanID=None, SvlanIDStep=None, SvlanPriority=None, SvlanTpid=None, VlanID=None, VlanIDStep=None, VlanPriority=None, VlanTpid=None, VlanType=None):
        # type: (int, int, int, str, bool, int, int, int, str, int, int, int, str, str) -> ConfigVLANParams
        """Finds and retrieves configVLANParams resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve configVLANParams resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all configVLANParams resources from the server.

        Args
        ----
        - CvlanID (number): Import only the best routes (provided route file has this information).
        - CvlanIDStep (number): Import only the best routes (provided route file has this information).
        - CvlanPriority (number): Import only the best routes (provided route file has this information).
        - CvlanTpid (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - EnableVLAN (bool): Import only the best routes (provided route file has this information).
        - SvlanID (number): Import only the best routes (provided route file has this information).
        - SvlanIDStep (number): Import only the best routes (provided route file has this information).
        - SvlanPriority (number): Import only the best routes (provided route file has this information).
        - SvlanTpid (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - VlanID (number): Import only the best routes (provided route file has this information).
        - VlanIDStep (number): Import only the best routes (provided route file has this information).
        - VlanPriority (number): Import only the best routes (provided route file has this information).
        - VlanTpid (str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200)): Import only the best routes (provided route file has this information).
        - VlanType (str(vlanStackingTypeSingleVlan | vlanStackingTypeStackedVlan)): Import only the best routes (provided route file has this information).

        Returns
        -------
        - self: This instance with matching configVLANParams resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of configVLANParams data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the configVLANParams resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def ConfigVLAN(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the configVLAN operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        configVLAN(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('configVLAN', payload=payload, response_object=None)
