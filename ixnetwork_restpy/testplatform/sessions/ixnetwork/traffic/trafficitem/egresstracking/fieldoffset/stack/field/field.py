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


class Field(Base):
    """
    The Field class encapsulates a list of field resources that are managed by the system.
    A list of resources can be retrieved from the server using the Field.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'field'
    _SDM_ATT_MAP = {
        'Id__': '__id__',
        'ActiveFieldChoice': 'activeFieldChoice',
        'Auto': 'auto',
        'AvailableValueTypes': 'availableValueTypes',
        'CountValue': 'countValue',
        'DefaultValue': 'defaultValue',
        'DisplayName': 'displayName',
        'EnumValues': 'enumValues',
        'FieldChoice': 'fieldChoice',
        'FieldGroupName': 'fieldGroupName',
        'FieldTypeId': 'fieldTypeId',
        'FieldValue': 'fieldValue',
        'FixedBits': 'fixedBits',
        'FormattedFieldValue': 'formattedFieldValue',
        'FullMesh': 'fullMesh',
        'Length': 'length',
        'Level': 'level',
        'MaxValue': 'maxValue',
        'MinValue': 'minValue',
        'Name': 'name',
        'Offset': 'offset',
        'OffsetFromRoot': 'offsetFromRoot',
        'OnTheFlyMask': 'onTheFlyMask',
        'Optional': 'optional',
        'OptionalEnabled': 'optionalEnabled',
        'RandomMask': 'randomMask',
        'RateVaried': 'rateVaried',
        'ReadOnly': 'readOnly',
        'RequiresUdf': 'requiresUdf',
        'Seed': 'seed',
        'SingleValue': 'singleValue',
        'StartValue': 'startValue',
        'StepValue': 'stepValue',
        'SupportsAuto': 'supportsAuto',
        'SupportsNonRepeatableRandom': 'supportsNonRepeatableRandom',
        'SupportsOnTheFlyMask': 'supportsOnTheFlyMask',
        'SupportsRepeatableRandomRange': 'supportsRepeatableRandomRange',
        'TrackingEnabled': 'trackingEnabled',
        'ValueFormat': 'valueFormat',
        'ValueList': 'valueList',
        'ValueType': 'valueType',
    }

    def __init__(self, parent):
        super(Field, self).__init__(parent)

    @property
    def Id__(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Id__'])

    @property
    def ActiveFieldChoice(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveFieldChoice'])
    @ActiveFieldChoice.setter
    def ActiveFieldChoice(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ActiveFieldChoice'], value)

    @property
    def Auto(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Auto'])
    @Auto.setter
    def Auto(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Auto'], value)

    @property
    def AvailableValueTypes(self):
        """
        Returns
        -------
        - list(str[decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableValueTypes'])

    @property
    def CountValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountValue'])
    @CountValue.setter
    def CountValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CountValue'], value)

    @property
    def DefaultValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultValue'])

    @property
    def DisplayName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayName'])

    @property
    def EnumValues(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnumValues'])

    @property
    def FieldChoice(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldChoice'])

    @property
    def FieldGroupName(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldGroupName'])

    @property
    def FieldTypeId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldTypeId'])

    @property
    def FieldValue(self):
        """DEPRECATED 
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldValue'])
    @FieldValue.setter
    def FieldValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FieldValue'], value)

    @property
    def FixedBits(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedBits'])
    @FixedBits.setter
    def FixedBits(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FixedBits'], value)

    @property
    def FormattedFieldValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FormattedFieldValue'])

    @property
    def FullMesh(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FullMesh'])
    @FullMesh.setter
    def FullMesh(self, value):
        self._set_attribute(self._SDM_ATT_MAP['FullMesh'], value)

    @property
    def Length(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])

    @property
    def Level(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level'])

    @property
    def MaxValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxValue'])
    @MaxValue.setter
    def MaxValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxValue'], value)

    @property
    def MinValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinValue'])
    @MinValue.setter
    def MinValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MinValue'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])

    @property
    def OffsetFromRoot(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetFromRoot'])

    @property
    def OnTheFlyMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OnTheFlyMask'])
    @OnTheFlyMask.setter
    def OnTheFlyMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OnTheFlyMask'], value)

    @property
    def Optional(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Optional'])

    @property
    def OptionalEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptionalEnabled'])
    @OptionalEnabled.setter
    def OptionalEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['OptionalEnabled'], value)

    @property
    def RandomMask(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomMask'])
    @RandomMask.setter
    def RandomMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RandomMask'], value)

    @property
    def RateVaried(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateVaried'])

    @property
    def ReadOnly(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReadOnly'])

    @property
    def RequiresUdf(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequiresUdf'])

    @property
    def Seed(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Seed'])
    @Seed.setter
    def Seed(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Seed'], value)

    @property
    def SingleValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SingleValue'])
    @SingleValue.setter
    def SingleValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SingleValue'], value)

    @property
    def StartValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartValue'])
    @StartValue.setter
    def StartValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartValue'], value)

    @property
    def StepValue(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepValue'])
    @StepValue.setter
    def StepValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StepValue'], value)

    @property
    def SupportsAuto(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsAuto'])

    @property
    def SupportsNonRepeatableRandom(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsNonRepeatableRandom'])

    @property
    def SupportsOnTheFlyMask(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsOnTheFlyMask'])

    @property
    def SupportsRepeatableRandomRange(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsRepeatableRandomRange'])

    @property
    def TrackingEnabled(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackingEnabled'])
    @TrackingEnabled.setter
    def TrackingEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrackingEnabled'], value)

    @property
    def ValueFormat(self):
        """
        Returns
        -------
        - str(aTM | bool | debug | decimal | decimalFixed2 | decimalSigned8 | fCID | float | floatEng | hex | hex8WithColons | hex8WithSpaces | iPv4 | iPv6 | mAC | mACMAC | mACSiteId | mACVLAN | mACVLANSiteId | string | unknown | varLenHex): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueFormat'])

    @property
    def ValueList(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueList'])
    @ValueList.setter
    def ValueList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ValueList'], value)

    @property
    def ValueType(self):
        """
        Returns
        -------
        - str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueType'])
    @ValueType.setter
    def ValueType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ValueType'], value)

    def update(self, ActiveFieldChoice=None, Auto=None, CountValue=None, FieldValue=None, FixedBits=None, FullMesh=None, MaxValue=None, MinValue=None, OnTheFlyMask=None, OptionalEnabled=None, RandomMask=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, TrackingEnabled=None, ValueList=None, ValueType=None):
        """Updates field resource on the server.

        Args
        ----
        - ActiveFieldChoice (bool): 
        - Auto (bool): 
        - CountValue (str): 
        - FieldValue (str): 
        - FixedBits (str): 
        - FullMesh (bool): 
        - MaxValue (str): 
        - MinValue (str): 
        - OnTheFlyMask (str): 
        - OptionalEnabled (bool): 
        - RandomMask (str): 
        - Seed (str): 
        - SingleValue (str): 
        - StartValue (str): 
        - StepValue (str): 
        - TrackingEnabled (bool): 
        - ValueList (list(str)): 
        - ValueType (str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList)): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Id__=None, ActiveFieldChoice=None, Auto=None, AvailableValueTypes=None, CountValue=None, DefaultValue=None, DisplayName=None, EnumValues=None, FieldChoice=None, FieldGroupName=None, FieldTypeId=None, FieldValue=None, FixedBits=None, FormattedFieldValue=None, FullMesh=None, Length=None, Level=None, MaxValue=None, MinValue=None, Name=None, Offset=None, OffsetFromRoot=None, OnTheFlyMask=None, Optional=None, OptionalEnabled=None, RandomMask=None, RateVaried=None, ReadOnly=None, RequiresUdf=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, SupportsAuto=None, SupportsNonRepeatableRandom=None, SupportsOnTheFlyMask=None, SupportsRepeatableRandomRange=None, TrackingEnabled=None, ValueFormat=None, ValueList=None, ValueType=None):
        """Finds and retrieves field resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve field resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all field resources from the server.

        Args
        ----
        - Id__ (str): 
        - ActiveFieldChoice (bool): 
        - Auto (bool): 
        - AvailableValueTypes (list(str[decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList])): 
        - CountValue (str): 
        - DefaultValue (str): 
        - DisplayName (str): 
        - EnumValues (list(str)): 
        - FieldChoice (bool): 
        - FieldGroupName (str): 
        - FieldTypeId (str): 
        - FieldValue (str): 
        - FixedBits (str): 
        - FormattedFieldValue (str): 
        - FullMesh (bool): 
        - Length (number): 
        - Level (bool): 
        - MaxValue (str): 
        - MinValue (str): 
        - Name (str): 
        - Offset (number): 
        - OffsetFromRoot (number): 
        - OnTheFlyMask (str): 
        - Optional (bool): 
        - OptionalEnabled (bool): 
        - RandomMask (str): 
        - RateVaried (bool): 
        - ReadOnly (bool): 
        - RequiresUdf (bool): 
        - Seed (str): 
        - SingleValue (str): 
        - StartValue (str): 
        - StepValue (str): 
        - SupportsAuto (bool): 
        - SupportsNonRepeatableRandom (bool): 
        - SupportsOnTheFlyMask (bool): 
        - SupportsRepeatableRandomRange (bool): 
        - TrackingEnabled (bool): 
        - ValueFormat (str(aTM | bool | debug | decimal | decimalFixed2 | decimalSigned8 | fCID | float | floatEng | hex | hex8WithColons | hex8WithSpaces | iPv4 | iPv6 | mAC | mACMAC | mACSiteId | mACVLAN | mACVLANSiteId | string | unknown | varLenHex)): 
        - ValueList (list(str)): 
        - ValueType (str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList)): 

        Returns
        -------
        - self: This instance with matching field resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of field data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the field resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddLevel(self):
        """Executes the addLevel operation on the server.

        Add a level to the current field.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('addLevel', payload=payload, response_object=None)

    def RemoveLevel(self):
        """Executes the removeLevel operation on the server.

        Remove a level.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('removeLevel', payload=payload, response_object=None)
