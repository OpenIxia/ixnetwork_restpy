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


class Field(Base):
    """This object contains the attributes related to stack field.
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
        - str: An alphanumeric string that defines the internal field ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Id__'])

    @property
    def ActiveFieldChoice(self):
        """
        Returns
        -------
        - bool: It is used to select a particular option out of multiple field choice options. The activeFieldChoice will be true only for the fields of the option which is active in GUI.
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
        - bool: If true, value for the particular field is considered automatically. If false, user can set values for the particular field.
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
        - str: It is used to get the count value of the field.
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
        - str: It is used to get the default value of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultValue'])

    @property
    def DisplayName(self):
        """
        Returns
        -------
        - str: It is used to get the name of the particular field as available in Packet/Qos
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayName'])

    @property
    def EnumValues(self):
        """
        Returns
        -------
        - list(str): If the field has string options, then each string is associated with a particular integer value. This attribute is used to get the mapping of integer value with the corresponding string option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnumValues'])

    @property
    def FieldChoice(self):
        """
        Returns
        -------
        - bool: It is true for all the field options active in the GUI.
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
        - str: An alphanumeric string that returns the value of the field.
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
        - str: Sets all the fields to a constant specified size.
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
        - bool: If true, Full Mesh is enabled.
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
        - number: It is used to get the length of the field in bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])

    @property
    def Level(self):
        """
        Returns
        -------
        - bool: It is used to get the level of the field in bits.
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
        - str: An alphanumeric string that returns the name of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def Offset(self):
        """
        Returns
        -------
        - number: It is used to get the position of the field in terms of number of bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])

    @property
    def OffsetFromRoot(self):
        """
        Returns
        -------
        - number: It is used to get the position of the field in terms of number of bits from the root packet.
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
        - bool: A read-only field that accepts true/false to make the field optional.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Optional'])

    @property
    def OptionalEnabled(self):
        """
        Returns
        -------
        - bool: If true, the optional field can accept values.
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
        - str: Select to use random mask bit values.
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
        - bool: It is used to get the varied rate of packet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateVaried'])

    @property
    def ReadOnly(self):
        """
        Returns
        -------
        - bool: It is used to check whether particular field is readOnly or otherwise.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReadOnly'])

    @property
    def RequiresUdf(self):
        """
        Returns
        -------
        - bool: It is used to check whether UDF is required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequiresUdf'])

    @property
    def Seed(self):
        """
        Returns
        -------
        - str: Select to use seed.
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
        - str: If valueType is to be set as singleValue, then after setting the valueType to singleValue, the singleValue is set to a particular value.
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
        - str: Specifies the initial value of increment or decrement.
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
        - str: Specifies the value by which value will keep incrementing or decrementing.
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
        - bool: Indicates whether or not this type of stack supports non-repeatable random
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
        - bool: If true, tracking is enabled on the particular field in flowTracking.
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
        - str(aTM | bool | debug | decimal | decimalFixed2 | decimalSigned8 | fCID | float | floatEng | hex | hex8WithColons | hex8WithSpaces | iPv4 | iPv6 | mAC | mACMAC | mACSiteId | mACVLAN | mACVLANSiteId | string | unknown | varLenHex): It is used to get the format of the field like whether format is mac, hex, integer, ipv4 and ipv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueFormat'])

    @property
    def ValueList(self):
        """
        Returns
        -------
        - list(str): If valueType is set as valueList, then after setting valueType to valueList a, list of values can be provided using this attribute.
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
        - str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList): It is used to select a particular value type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueType'])
    @ValueType.setter
    def ValueType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ValueType'], value)

    def update(self, ActiveFieldChoice=None, Auto=None, CountValue=None, FieldValue=None, FixedBits=None, FullMesh=None, MaxValue=None, MinValue=None, OnTheFlyMask=None, OptionalEnabled=None, RandomMask=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, TrackingEnabled=None, ValueList=None, ValueType=None):
        """Updates field resource on the server.

        Args
        ----
        - ActiveFieldChoice (bool): It is used to select a particular option out of multiple field choice options. The activeFieldChoice will be true only for the fields of the option which is active in GUI.
        - Auto (bool): If true, value for the particular field is considered automatically. If false, user can set values for the particular field.
        - CountValue (str): It is used to get the count value of the field.
        - FieldValue (str): An alphanumeric string that returns the value of the field.
        - FixedBits (str): Sets all the fields to a constant specified size.
        - FullMesh (bool): If true, Full Mesh is enabled.
        - MaxValue (str): 
        - MinValue (str): 
        - OnTheFlyMask (str): 
        - OptionalEnabled (bool): If true, the optional field can accept values.
        - RandomMask (str): Select to use random mask bit values.
        - Seed (str): Select to use seed.
        - SingleValue (str): If valueType is to be set as singleValue, then after setting the valueType to singleValue, the singleValue is set to a particular value.
        - StartValue (str): Specifies the initial value of increment or decrement.
        - StepValue (str): Specifies the value by which value will keep incrementing or decrementing.
        - TrackingEnabled (bool): If true, tracking is enabled on the particular field in flowTracking.
        - ValueList (list(str)): If valueType is set as valueList, then after setting valueType to valueList a, list of values can be provided using this attribute.
        - ValueType (str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList)): It is used to select a particular value type.

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
        - Id__ (str): An alphanumeric string that defines the internal field ID.
        - ActiveFieldChoice (bool): It is used to select a particular option out of multiple field choice options. The activeFieldChoice will be true only for the fields of the option which is active in GUI.
        - Auto (bool): If true, value for the particular field is considered automatically. If false, user can set values for the particular field.
        - AvailableValueTypes (list(str[decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList])): 
        - CountValue (str): It is used to get the count value of the field.
        - DefaultValue (str): It is used to get the default value of the field.
        - DisplayName (str): It is used to get the name of the particular field as available in Packet/Qos
        - EnumValues (list(str)): If the field has string options, then each string is associated with a particular integer value. This attribute is used to get the mapping of integer value with the corresponding string option.
        - FieldChoice (bool): It is true for all the field options active in the GUI.
        - FieldGroupName (str): 
        - FieldTypeId (str): 
        - FieldValue (str): An alphanumeric string that returns the value of the field.
        - FixedBits (str): Sets all the fields to a constant specified size.
        - FormattedFieldValue (str): 
        - FullMesh (bool): If true, Full Mesh is enabled.
        - Length (number): It is used to get the length of the field in bits.
        - Level (bool): It is used to get the level of the field in bits.
        - MaxValue (str): 
        - MinValue (str): 
        - Name (str): An alphanumeric string that returns the name of the field.
        - Offset (number): It is used to get the position of the field in terms of number of bits.
        - OffsetFromRoot (number): It is used to get the position of the field in terms of number of bits from the root packet.
        - OnTheFlyMask (str): 
        - Optional (bool): A read-only field that accepts true/false to make the field optional.
        - OptionalEnabled (bool): If true, the optional field can accept values.
        - RandomMask (str): Select to use random mask bit values.
        - RateVaried (bool): It is used to get the varied rate of packet field.
        - ReadOnly (bool): It is used to check whether particular field is readOnly or otherwise.
        - RequiresUdf (bool): It is used to check whether UDF is required.
        - Seed (str): Select to use seed.
        - SingleValue (str): If valueType is to be set as singleValue, then after setting the valueType to singleValue, the singleValue is set to a particular value.
        - StartValue (str): Specifies the initial value of increment or decrement.
        - StepValue (str): Specifies the value by which value will keep incrementing or decrementing.
        - SupportsAuto (bool): 
        - SupportsNonRepeatableRandom (bool): Indicates whether or not this type of stack supports non-repeatable random
        - SupportsOnTheFlyMask (bool): 
        - SupportsRepeatableRandomRange (bool): 
        - TrackingEnabled (bool): If true, tracking is enabled on the particular field in flowTracking.
        - ValueFormat (str(aTM | bool | debug | decimal | decimalFixed2 | decimalSigned8 | fCID | float | floatEng | hex | hex8WithColons | hex8WithSpaces | iPv4 | iPv6 | mAC | mACMAC | mACSiteId | mACVLAN | mACVLANSiteId | string | unknown | varLenHex)): It is used to get the format of the field like whether format is mac, hex, integer, ipv4 and ipv6.
        - ValueList (list(str)): If valueType is set as valueList, then after setting valueType to valueList a, list of values can be provided using this attribute.
        - ValueType (str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList)): It is used to select a particular value type.

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
