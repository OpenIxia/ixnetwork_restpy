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


class PtpNegBehaveList(Base):
    """Ptp Negative Behaviour Related Configuration
    The PtpNegBehaveList class encapsulates a required ptpNegBehaveList resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'ptpNegBehaveList'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'MvActive': 'mvActive',
        'MvDelay': 'mvDelay',
        'MvFieldValue': 'mvFieldValue',
        'MvFieldValue1': 'mvFieldValue1',
        'MvMsgAction': 'mvMsgAction',
        'MvPtpMsgField': 'mvPtpMsgField',
        'MvPtpMsgField1': 'mvPtpMsgField1',
        'Name': 'name',
        'PtpMsgType': 'ptpMsgType',
        'PtpValueDisPattern': 'ptpValueDisPattern',
        'PtpValueDisPattern1': 'ptpValueDisPattern1',
    }

    def __init__(self, parent):
        super(PtpNegBehaveList, self).__init__(parent)

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
    def MvActive(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvActive']))

    @property
    def MvDelay(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Delay To Follow in this message (ns)
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvDelay']))

    @property
    def MvFieldValue(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Value
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvFieldValue']))

    @property
    def MvFieldValue1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Value1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvFieldValue1']))

    @property
    def MvMsgAction(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Action On The Message Type
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvMsgAction']))

    @property
    def MvPtpMsgField(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): PTP Msg Field
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvPtpMsgField']))

    @property
    def MvPtpMsgField1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): PTP Msg Field1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MvPtpMsgField1']))

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
    def PtpMsgType(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Displays the current PTP Msg
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PtpMsgType']))

    @property
    def PtpValueDisPattern(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Pattern For Value Field
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PtpValueDisPattern']))

    @property
    def PtpValueDisPattern1(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Pattern For Value Field
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PtpValueDisPattern1']))

    def update(self, Name=None):
        """Updates ptpNegBehaveList resource on the server.

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

    def get_device_ids(self, PortNames=None, MvActive=None, MvDelay=None, MvFieldValue=None, MvFieldValue1=None, MvMsgAction=None, MvPtpMsgField=None, MvPtpMsgField1=None, PtpMsgType=None, PtpValueDisPattern=None, PtpValueDisPattern1=None):
        """Base class infrastructure that gets a list of ptpNegBehaveList device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - MvActive (str): optional regex of mvActive
        - MvDelay (str): optional regex of mvDelay
        - MvFieldValue (str): optional regex of mvFieldValue
        - MvFieldValue1 (str): optional regex of mvFieldValue1
        - MvMsgAction (str): optional regex of mvMsgAction
        - MvPtpMsgField (str): optional regex of mvPtpMsgField
        - MvPtpMsgField1 (str): optional regex of mvPtpMsgField1
        - PtpMsgType (str): optional regex of ptpMsgType
        - PtpValueDisPattern (str): optional regex of ptpValueDisPattern
        - PtpValueDisPattern1 (str): optional regex of ptpValueDisPattern1

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
