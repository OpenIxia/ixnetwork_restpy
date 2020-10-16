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

    def __init__(self, parent):
        super(ConfigVLANParams, self).__init__(parent)

    @property
    def CvlanID(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanID'])
    @CvlanID.setter
    def CvlanID(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanID'], value)

    @property
    def CvlanIDStep(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanIDStep'])
    @CvlanIDStep.setter
    def CvlanIDStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanIDStep'], value)

    @property
    def CvlanPriority(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanPriority'])
    @CvlanPriority.setter
    def CvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanPriority'], value)

    @property
    def CvlanTpid(self):
        """
        Returns
        -------
        - str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['CvlanTpid'])
    @CvlanTpid.setter
    def CvlanTpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CvlanTpid'], value)

    @property
    def EnableVLAN(self):
        """
        Returns
        -------
        - bool: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableVLAN'])
    @EnableVLAN.setter
    def EnableVLAN(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableVLAN'], value)

    @property
    def SvlanID(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanID'])
    @SvlanID.setter
    def SvlanID(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanID'], value)

    @property
    def SvlanIDStep(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanIDStep'])
    @SvlanIDStep.setter
    def SvlanIDStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanIDStep'], value)

    @property
    def SvlanPriority(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanPriority'])
    @SvlanPriority.setter
    def SvlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanPriority'], value)

    @property
    def SvlanTpid(self):
        """
        Returns
        -------
        - str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['SvlanTpid'])
    @SvlanTpid.setter
    def SvlanTpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SvlanTpid'], value)

    @property
    def VlanID(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanID'])
    @VlanID.setter
    def VlanID(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanID'], value)

    @property
    def VlanIDStep(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIDStep'])
    @VlanIDStep.setter
    def VlanIDStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIDStep'], value)

    @property
    def VlanPriority(self):
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanPriority'])
    @VlanPriority.setter
    def VlanPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanPriority'], value)

    @property
    def VlanTpid(self):
        """
        Returns
        -------
        - str(vlanTpId8100 | vlanTpId88a8 | vlanTpId9100 | vlanTpId9200): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanTpid'])
    @VlanTpid.setter
    def VlanTpid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanTpid'], value)

    @property
    def VlanType(self):
        """
        Returns
        -------
        - str(vlanStackingTypeSingleVlan | vlanStackingTypeStackedVlan): Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanType'])
    @VlanType.setter
    def VlanType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanType'], value)

    def update(self, CvlanID=None, CvlanIDStep=None, CvlanPriority=None, CvlanTpid=None, EnableVLAN=None, SvlanID=None, SvlanIDStep=None, SvlanPriority=None, SvlanTpid=None, VlanID=None, VlanIDStep=None, VlanPriority=None, VlanTpid=None, VlanType=None):
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

    def ConfigVLAN(self):
        """Executes the configVLAN operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('configVLAN', payload=payload, response_object=None)
