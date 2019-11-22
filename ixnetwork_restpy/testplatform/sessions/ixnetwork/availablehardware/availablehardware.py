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


class AvailableHardware(Base):
    """This is the hierachy of the available hardware.
    The AvailableHardware class encapsulates a required availableHardware resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'availableHardware'

    def __init__(self, parent):
        super(AvailableHardware, self).__init__(parent)

    @property
    def Chassis(self):
        """An instance of the Chassis class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis.Chassis)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.chassis.chassis import Chassis
        return Chassis(self)

    @property
    def VirtualChassis(self):
        """An instance of the VirtualChassis class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.virtualchassis.VirtualChassis)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.availablehardware.virtualchassis.virtualchassis import VirtualChassis
        return VirtualChassis(self)._select()

    @property
    def IsLocked(self):
        """If true, locks the Hardware Manager.

        Returns:
            bool
        """
        return self._get_attribute('isLocked')

    @property
    def IsOffChassis(self):
        """DEPRECATED If true, the Hardware Manager is Off Chassis.

        Returns:
            bool
        """
        return self._get_attribute('isOffChassis')
    @IsOffChassis.setter
    def IsOffChassis(self, value):
        self._set_attribute('isOffChassis', value)

    @property
    def OffChassisHwM(self):
        """DEPRECATED Enables the Off Chassis Hardware Manager. The Hardware Manager is an IxOS component that manages the resources on an Ixia chassis. IxNetwork communicates with a chassis through Hardware Manager. Normally, Hardware Manager runs on the chassis itself; however, it can also be installed and run on a separate PC. This configuration is known as an Off-Chassis Hardware Manager.

        Returns:
            str
        """
        return self._get_attribute('offChassisHwM')
    @OffChassisHwM.setter
    def OffChassisHwM(self, value):
        self._set_attribute('offChassisHwM', value)

    def update(self, IsOffChassis=None, OffChassisHwM=None):
        """Updates a child instance of availableHardware on the server.

        Args:
            IsOffChassis (bool): If true, the Hardware Manager is Off Chassis.
            OffChassisHwM (str): Enables the Off Chassis Hardware Manager. The Hardware Manager is an IxOS component that manages the resources on an Ixia chassis. IxNetwork communicates with a chassis through Hardware Manager. Normally, Hardware Manager runs on the chassis itself; however, it can also be installed and run on a separate PC. This configuration is known as an Off-Chassis Hardware Manager.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())
