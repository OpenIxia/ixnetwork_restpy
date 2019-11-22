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


class PtpNegBehaveList(Base):
    """Ptp Negative Behaviour Related Configuration
    The PtpNegBehaveList class encapsulates a required ptpNegBehaveList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ptpNegBehaveList'

    def __init__(self, parent):
        super(PtpNegBehaveList, self).__init__(parent)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def MvActive(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvActive')

    @property
    def MvDelay(self):
        """Delay To Follow in this message (ns)

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvDelay')

    @property
    def MvFieldValue(self):
        """Value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvFieldValue')

    @property
    def MvFieldValue1(self):
        """Value1

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvFieldValue1')

    @property
    def MvMsgAction(self):
        """Action On The Message Type

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvMsgAction')

    @property
    def MvPtpMsgField(self):
        """PTP Msg Field

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvPtpMsgField')

    @property
    def MvPtpMsgField1(self):
        """PTP Msg Field1

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mvPtpMsgField1')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def PtpMsgType(self):
        """Displays the current PTP Msg

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ptpMsgType')

    @property
    def PtpValueDisPattern(self):
        """Pattern For Value Field

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ptpValueDisPattern')

    @property
    def PtpValueDisPattern1(self):
        """Pattern For Value Field

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('ptpValueDisPattern1')

    def update(self, Name=None):
        """Updates a child instance of ptpNegBehaveList on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def get_device_ids(self, PortNames=None, MvActive=None, MvDelay=None, MvFieldValue=None, MvFieldValue1=None, MvMsgAction=None, MvPtpMsgField=None, MvPtpMsgField1=None, PtpMsgType=None, PtpValueDisPattern=None, PtpValueDisPattern1=None):
        """Base class infrastructure that gets a list of ptpNegBehaveList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            MvActive (str): optional regex of mvActive
            MvDelay (str): optional regex of mvDelay
            MvFieldValue (str): optional regex of mvFieldValue
            MvFieldValue1 (str): optional regex of mvFieldValue1
            MvMsgAction (str): optional regex of mvMsgAction
            MvPtpMsgField (str): optional regex of mvPtpMsgField
            MvPtpMsgField1 (str): optional regex of mvPtpMsgField1
            PtpMsgType (str): optional regex of ptpMsgType
            PtpValueDisPattern (str): optional regex of ptpValueDisPattern
            PtpValueDisPattern1 (str): optional regex of ptpValueDisPattern1

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
