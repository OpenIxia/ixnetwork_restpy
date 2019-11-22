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


class EgtpNbRange(Base):
    """eNodeB Range
    The EgtpNbRange class encapsulates a required egtpNbRange resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpNbRange'

    def __init__(self, parent):
        super(EgtpNbRange, self).__init__(parent)

    @property
    def Ci(self):
        """Cell Identifier

        Returns:
            str
        """
        return self._get_attribute('ci')
    @Ci.setter
    def Ci(self, value):
        self._set_attribute('ci', value)

    @property
    def Eci(self):
        """EUTRAN Cell Identifier

        Returns:
            str
        """
        return self._get_attribute('eci')
    @Eci.setter
    def Eci(self, value):
        self._set_attribute('eci', value)

    @property
    def Enabled(self):
        """Disabled ranges won't be configured nor validated.

        Returns:
            bool
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def Lac(self):
        """Location Area Code

        Returns:
            str
        """
        return self._get_attribute('lac')
    @Lac.setter
    def Lac(self, value):
        self._set_attribute('lac', value)

    @property
    def Mcc(self):
        """Mobile Country Code

        Returns:
            str
        """
        return self._get_attribute('mcc')
    @Mcc.setter
    def Mcc(self, value):
        self._set_attribute('mcc', value)

    @property
    def Mnc(self):
        """Mobile Network Code

        Returns:
            str
        """
        return self._get_attribute('mnc')
    @Mnc.setter
    def Mnc(self, value):
        self._set_attribute('mnc', value)

    @property
    def Name(self):
        """Name of range

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

    @property
    def ParentMme(self):
        """Id of parent MME range

        Returns:
            str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=mmeSecondaryRange)
        """
        return self._get_attribute('parentMme')
    @ParentMme.setter
    def ParentMme(self, value):
        self._set_attribute('parentMme', value)

    @property
    def Rac(self):
        """Routing Area Code

        Returns:
            str
        """
        return self._get_attribute('rac')
    @Rac.setter
    def Rac(self, value):
        self._set_attribute('rac', value)

    @property
    def Railac(self):
        """LAC for UEs (Hexa value)

        Returns:
            str
        """
        return self._get_attribute('railac')
    @Railac.setter
    def Railac(self, value):
        self._set_attribute('railac', value)

    @property
    def Raimcc1(self):
        """First digit of MCC location for UEs

        Returns:
            number
        """
        return self._get_attribute('raimcc1')
    @Raimcc1.setter
    def Raimcc1(self, value):
        self._set_attribute('raimcc1', value)

    @property
    def Raimcc2(self):
        """Second digit of MCC location for UEs

        Returns:
            number
        """
        return self._get_attribute('raimcc2')
    @Raimcc2.setter
    def Raimcc2(self, value):
        self._set_attribute('raimcc2', value)

    @property
    def Raimcc3(self):
        """3rd digit of MCC location for UEs

        Returns:
            number
        """
        return self._get_attribute('raimcc3')
    @Raimcc3.setter
    def Raimcc3(self, value):
        self._set_attribute('raimcc3', value)

    @property
    def Raimnc1(self):
        """first digit of MNC location for UEs

        Returns:
            number
        """
        return self._get_attribute('raimnc1')
    @Raimnc1.setter
    def Raimnc1(self, value):
        self._set_attribute('raimnc1', value)

    @property
    def Raimnc2(self):
        """Second digit of MNC location for UEs

        Returns:
            number
        """
        return self._get_attribute('raimnc2')
    @Raimnc2.setter
    def Raimnc2(self, value):
        self._set_attribute('raimnc2', value)

    @property
    def Raimnc3(self):
        """Third digit of MNC location for UEs

        Returns:
            number
        """
        return self._get_attribute('raimnc3')
    @Raimnc3.setter
    def Raimnc3(self, value):
        self._set_attribute('raimnc3', value)

    @property
    def Rairac(self):
        """RAC for UEs (Hexa value)

        Returns:
            str
        """
        return self._get_attribute('rairac')
    @Rairac.setter
    def Rairac(self, value):
        self._set_attribute('rairac', value)

    @property
    def Sac(self):
        """Service Area Code

        Returns:
            str
        """
        return self._get_attribute('sac')
    @Sac.setter
    def Sac(self, value):
        self._set_attribute('sac', value)

    @property
    def Tac(self):
        """Tracking Area Code

        Returns:
            str
        """
        return self._get_attribute('tac')
    @Tac.setter
    def Tac(self, value):
        self._set_attribute('tac', value)

    def update(self, Ci=None, Eci=None, Enabled=None, Lac=None, Mcc=None, Mnc=None, Name=None, ParentMme=None, Rac=None, Railac=None, Raimcc1=None, Raimcc2=None, Raimcc3=None, Raimnc1=None, Raimnc2=None, Raimnc3=None, Rairac=None, Sac=None, Tac=None):
        """Updates a child instance of egtpNbRange on the server.

        Args:
            Ci (str): Cell Identifier
            Eci (str): EUTRAN Cell Identifier
            Enabled (bool): Disabled ranges won't be configured nor validated.
            Lac (str): Location Area Code
            Mcc (str): Mobile Country Code
            Mnc (str): Mobile Network Code
            Name (str): Name of range
            ParentMme (str(None|/api/v1/sessions/1/ixnetwork/vport?deepchild=mmeSecondaryRange)): Id of parent MME range
            Rac (str): Routing Area Code
            Railac (str): LAC for UEs (Hexa value)
            Raimcc1 (number): First digit of MCC location for UEs
            Raimcc2 (number): Second digit of MCC location for UEs
            Raimcc3 (number): 3rd digit of MCC location for UEs
            Raimnc1 (number): first digit of MNC location for UEs
            Raimnc2 (number): Second digit of MNC location for UEs
            Raimnc3 (number): Third digit of MNC location for UEs
            Rairac (str): RAC for UEs (Hexa value)
            Sac (str): Service Area Code
            Tac (str): Tracking Area Code

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2:list, Arg3:enum)
            Args:
                args[0] is Arg2 (list(str)): List of plugin types to be added in the new custom stack
                args[1] is Arg3 (str(kAppend|kMerge|kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to disable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2:string)string
            Args:
                args[0] is Arg2 (str): Protocol class name to enable

            Returns:
                str: Status of the exec

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
