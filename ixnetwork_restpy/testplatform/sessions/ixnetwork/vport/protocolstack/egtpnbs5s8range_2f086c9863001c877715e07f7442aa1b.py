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


class EgtpNbS5S8Range(Base):
    """eNodeB Range
    The EgtpNbS5S8Range class encapsulates a required egtpNbS5S8Range resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'egtpNbS5S8Range'
    _SDM_ATT_MAP = {
        'ECI': 'eCI',
        'Enabled': 'enabled',
        'MCC': 'mCC',
        'MNC': 'mNC',
        'Name': 'name',
        'ObjectId': 'objectId',
        'ParentMme': 'parentMme',
        'ParentSgw': 'parentSgw',
        'RAILAC': 'rAILAC',
        'RAIMCC1': 'rAIMCC1',
        'RAIMCC2': 'rAIMCC2',
        'RAIMCC3': 'rAIMCC3',
        'RAIMNC1': 'rAIMNC1',
        'RAIMNC2': 'rAIMNC2',
        'RAIMNC3': 'rAIMNC3',
        'RAIRAC': 'rAIRAC',
        'TAC': 'tAC',
    }

    def __init__(self, parent):
        super(EgtpNbS5S8Range, self).__init__(parent)

    @property
    def ECI(self):
        """
        Returns
        -------
        - str: EUTRAN Cell Identifier
        """
        return self._get_attribute(self._SDM_ATT_MAP['ECI'])
    @ECI.setter
    def ECI(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ECI'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Disabled ranges won't be configured nor validated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def MCC(self):
        """
        Returns
        -------
        - str: Mobile Country Code
        """
        return self._get_attribute(self._SDM_ATT_MAP['MCC'])
    @MCC.setter
    def MCC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MCC'], value)

    @property
    def MNC(self):
        """
        Returns
        -------
        - str: Mobile Network Code
        """
        return self._get_attribute(self._SDM_ATT_MAP['MNC'])
    @MNC.setter
    def MNC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MNC'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of range
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute(self._SDM_ATT_MAP['ObjectId'])

    @property
    def ParentMme(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../mmeS5S8SecondaryRange): Id of parent MME range
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentMme'])
    @ParentMme.setter
    def ParentMme(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ParentMme'], value)

    @property
    def ParentSgw(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../range): Id of parent SGW range
        """
        return self._get_attribute(self._SDM_ATT_MAP['ParentSgw'])
    @ParentSgw.setter
    def ParentSgw(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ParentSgw'], value)

    @property
    def RAILAC(self):
        """
        Returns
        -------
        - str: LAC for UEs (Hexa value)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAILAC'])
    @RAILAC.setter
    def RAILAC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAILAC'], value)

    @property
    def RAIMCC1(self):
        """
        Returns
        -------
        - number: First digit of MCC location for UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIMCC1'])
    @RAIMCC1.setter
    def RAIMCC1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIMCC1'], value)

    @property
    def RAIMCC2(self):
        """
        Returns
        -------
        - number: Second digit of MCC location for UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIMCC2'])
    @RAIMCC2.setter
    def RAIMCC2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIMCC2'], value)

    @property
    def RAIMCC3(self):
        """
        Returns
        -------
        - number: 3rd digit of MCC location for UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIMCC3'])
    @RAIMCC3.setter
    def RAIMCC3(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIMCC3'], value)

    @property
    def RAIMNC1(self):
        """
        Returns
        -------
        - number: first digit of MNC location for UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIMNC1'])
    @RAIMNC1.setter
    def RAIMNC1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIMNC1'], value)

    @property
    def RAIMNC2(self):
        """
        Returns
        -------
        - number: Second digit of MNC location for UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIMNC2'])
    @RAIMNC2.setter
    def RAIMNC2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIMNC2'], value)

    @property
    def RAIMNC3(self):
        """
        Returns
        -------
        - number: Third digit of MNC location for UEs
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIMNC3'])
    @RAIMNC3.setter
    def RAIMNC3(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIMNC3'], value)

    @property
    def RAIRAC(self):
        """
        Returns
        -------
        - str: RAC for UEs (Hexa value)
        """
        return self._get_attribute(self._SDM_ATT_MAP['RAIRAC'])
    @RAIRAC.setter
    def RAIRAC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RAIRAC'], value)

    @property
    def TAC(self):
        """
        Returns
        -------
        - str: Tracking Area Code
        """
        return self._get_attribute(self._SDM_ATT_MAP['TAC'])
    @TAC.setter
    def TAC(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TAC'], value)

    def update(self, ECI=None, Enabled=None, MCC=None, MNC=None, Name=None, ParentMme=None, ParentSgw=None, RAILAC=None, RAIMCC1=None, RAIMCC2=None, RAIMCC3=None, RAIMNC1=None, RAIMNC2=None, RAIMNC3=None, RAIRAC=None, TAC=None):
        """Updates egtpNbS5S8Range resource on the server.

        Args
        ----
        - ECI (str): EUTRAN Cell Identifier
        - Enabled (bool): Disabled ranges won't be configured nor validated.
        - MCC (str): Mobile Country Code
        - MNC (str): Mobile Network Code
        - Name (str): Name of range
        - ParentMme (str(None | /api/v1/sessions/1/ixnetwork/vport/.../mmeS5S8SecondaryRange)): Id of parent MME range
        - ParentSgw (str(None | /api/v1/sessions/1/ixnetwork/vport/.../range)): Id of parent SGW range
        - RAILAC (str): LAC for UEs (Hexa value)
        - RAIMCC1 (number): First digit of MCC location for UEs
        - RAIMCC2 (number): Second digit of MCC location for UEs
        - RAIMCC3 (number): 3rd digit of MCC location for UEs
        - RAIMNC1 (number): first digit of MNC location for UEs
        - RAIMNC2 (number): Second digit of MNC location for UEs
        - RAIMNC3 (number): Third digit of MNC location for UEs
        - RAIRAC (str): RAC for UEs (Hexa value)
        - TAC (str): Tracking Area Code

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def CustomProtocolStack(self, *args, **kwargs):
        """Executes the customProtocolStack operation on the server.

        Create custom protocol stack under /vport/protocolStack

        customProtocolStack(Arg2=list, Arg3=enum)
        -----------------------------------------
        - Arg2 (list(str)): List of plugin types to be added in the new custom stack
        - Arg3 (str(kAppend | kMerge | kOverwrite)): Append, merge or overwrite existing protocol stack

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('customProtocolStack', payload=payload, response_object=None)

    def DisableProtocolStack(self, *args, **kwargs):
        """Executes the disableProtocolStack operation on the server.

        Disable a protocol under protocolStack using the class name

        disableProtocolStack(Arg2=string)string
        ---------------------------------------
        - Arg2 (str): Protocol class name to disable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('disableProtocolStack', payload=payload, response_object=None)

    def EnableProtocolStack(self, *args, **kwargs):
        """Executes the enableProtocolStack operation on the server.

        Enable a protocol under protocolStack using the class name

        enableProtocolStack(Arg2=string)string
        --------------------------------------
        - Arg2 (str): Protocol class name to enable
        - Returns str: Status of the exec

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('enableProtocolStack', payload=payload, response_object=None)
