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
    _SDM_ENUM_MAP = {
        'valueFormat': ['aTM', 'bool', 'debug', 'decimal', 'decimalFixed2', 'decimalSigned8', 'fCID', 'float', 'floatEng', 'hex', 'hex8WithColons', 'hex8WithSpaces', 'iPv4', 'iPv6', 'mAC', 'mACMAC', 'mACSiteId', 'mACVLAN', 'mACVLANSiteId', 'string', 'unknown', 'varLenHex'],
        'valueType': ['decrement', 'increment', 'nonRepeatableRandom', 'random', 'repeatableRandomRange', 'singleValue', 'valueList'],
    }

    def __init__(self, parent, list_op=False):
        super(Field, self).__init__(parent, list_op)

    @property
    def Id__(self):
        # type: () -> str
        """
        Returns
        -------
        - str: An alphanumeric string that defines the internal field ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Id__'])

    @property
    def ActiveFieldChoice(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It is used to select a particular option out of multiple field choice options. The activeFieldChoice will be true only for the fields of the option which is active in GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ActiveFieldChoice'])
    @ActiveFieldChoice.setter
    def ActiveFieldChoice(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['ActiveFieldChoice'], value)

    @property
    def Auto(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, value for the particular field is considered automatically. If false, user can set values for the particular field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Auto'])
    @Auto.setter
    def Auto(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Auto'], value)

    @property
    def AvailableValueTypes(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList]): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['AvailableValueTypes'])

    @property
    def CountValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It is used to get the count value of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CountValue'])
    @CountValue.setter
    def CountValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['CountValue'], value)

    @property
    def DefaultValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It is used to get the default value of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DefaultValue'])

    @property
    def DisplayName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: It is used to get the name of the particular field as available in Packet/Qos
        """
        return self._get_attribute(self._SDM_ATT_MAP['DisplayName'])

    @property
    def EnumValues(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): If the field has string options, then each string is associated with a particular integer value. This attribute is used to get the mapping of integer value with the corresponding string option.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnumValues'])

    @property
    def FieldChoice(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It is true for all the field options active in the GUI.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldChoice'])

    @property
    def FieldGroupName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldGroupName'])

    @property
    def FieldTypeId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldTypeId'])

    @property
    def FieldValue(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: An alphanumeric string that returns the value of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FieldValue'])
    @FieldValue.setter
    def FieldValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FieldValue'], value)

    @property
    def FixedBits(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Sets all the fields to a constant specified size.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FixedBits'])
    @FixedBits.setter
    def FixedBits(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['FixedBits'], value)

    @property
    def FormattedFieldValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['FormattedFieldValue'])

    @property
    def FullMesh(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, Full Mesh is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FullMesh'])
    @FullMesh.setter
    def FullMesh(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['FullMesh'], value)

    @property
    def Length(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It is used to get the length of the field in bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])

    @property
    def Level(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It is used to get the level of the field in bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level'])

    @property
    def MaxValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxValue'])
    @MaxValue.setter
    def MaxValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaxValue'], value)

    @property
    def MinValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MinValue'])
    @MinValue.setter
    def MinValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['MinValue'], value)

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: An alphanumeric string that returns the name of the field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])

    @property
    def Offset(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It is used to get the position of the field in terms of number of bits.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Offset'])

    @property
    def OffsetFromRoot(self):
        # type: () -> int
        """
        Returns
        -------
        - number: It is used to get the position of the field in terms of number of bits from the root packet.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OffsetFromRoot'])

    @property
    def OnTheFlyMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['OnTheFlyMask'])
    @OnTheFlyMask.setter
    def OnTheFlyMask(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['OnTheFlyMask'], value)

    @property
    def Optional(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: A read-only field that accepts true/false to make the field optional.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Optional'])

    @property
    def OptionalEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the optional field can accept values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['OptionalEnabled'])
    @OptionalEnabled.setter
    def OptionalEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['OptionalEnabled'], value)

    @property
    def RandomMask(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Select to use random mask bit values.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RandomMask'])
    @RandomMask.setter
    def RandomMask(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RandomMask'], value)

    @property
    def RateVaried(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It is used to get the varied rate of packet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RateVaried'])

    @property
    def ReadOnly(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It is used to check whether particular field is readOnly or otherwise.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReadOnly'])

    @property
    def RequiresUdf(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: It is used to check whether UDF is required.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RequiresUdf'])

    @property
    def Seed(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Select to use seed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Seed'])
    @Seed.setter
    def Seed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Seed'], value)

    @property
    def SingleValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: If valueType is to be set as singleValue, then after setting the valueType to singleValue, the singleValue is set to a particular value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SingleValue'])
    @SingleValue.setter
    def SingleValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SingleValue'], value)

    @property
    def StartValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the initial value of increment or decrement.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartValue'])
    @StartValue.setter
    def StartValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartValue'], value)

    @property
    def StepValue(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Specifies the value by which value will keep incrementing or decrementing.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StepValue'])
    @StepValue.setter
    def StepValue(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StepValue'], value)

    @property
    def SupportsAuto(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsAuto'])

    @property
    def SupportsNonRepeatableRandom(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Indicates whether or not this type of stack supports non-repeatable random
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsNonRepeatableRandom'])

    @property
    def SupportsOnTheFlyMask(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsOnTheFlyMask'])

    @property
    def SupportsRepeatableRandomRange(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportsRepeatableRandomRange'])

    @property
    def TrackingEnabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, tracking is enabled on the particular field in flowTracking.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrackingEnabled'])
    @TrackingEnabled.setter
    def TrackingEnabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['TrackingEnabled'], value)

    @property
    def ValueFormat(self):
        # type: () -> str
        """
        Returns
        -------
        - str(aTM | bool | debug | decimal | decimalFixed2 | decimalSigned8 | fCID | float | floatEng | hex | hex8WithColons | hex8WithSpaces | iPv4 | iPv6 | mAC | mACMAC | mACSiteId | mACVLAN | mACVLANSiteId | string | unknown | varLenHex): It is used to get the format of the field like whether format is mac, hex, integer, ipv4 and ipv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueFormat'])

    @property
    def ValueList(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): If valueType is set as valueList, then after setting valueType to valueList a, list of values can be provided using this attribute.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueList'])
    @ValueList.setter
    def ValueList(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP['ValueList'], value)

    @property
    def ValueType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(decrement | increment | nonRepeatableRandom | random | repeatableRandomRange | singleValue | valueList): It is used to select a particular value type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ValueType'])
    @ValueType.setter
    def ValueType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ValueType'], value)

    def update(self, ActiveFieldChoice=None, Auto=None, CountValue=None, FieldValue=None, FixedBits=None, FullMesh=None, MaxValue=None, MinValue=None, OnTheFlyMask=None, OptionalEnabled=None, RandomMask=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, TrackingEnabled=None, ValueList=None, ValueType=None):
        # type: (bool, bool, str, str, str, bool, str, str, str, bool, str, str, str, str, str, bool, List[str], str) -> Field
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

    def add(self, ActiveFieldChoice=None, Auto=None, CountValue=None, FieldValue=None, FixedBits=None, FullMesh=None, MaxValue=None, MinValue=None, OnTheFlyMask=None, OptionalEnabled=None, RandomMask=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, TrackingEnabled=None, ValueList=None, ValueType=None):
        # type: (bool, bool, str, str, str, bool, str, str, str, bool, str, str, str, str, str, bool, List[str], str) -> Field
        """Adds a new field resource on the json, only valid with batch add utility

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

        Returns
        -------
        - self: This instance with all currently retrieved field resources using find and the newly added field resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Id__=None, ActiveFieldChoice=None, Auto=None, AvailableValueTypes=None, CountValue=None, DefaultValue=None, DisplayName=None, EnumValues=None, FieldChoice=None, FieldGroupName=None, FieldTypeId=None, FieldValue=None, FixedBits=None, FormattedFieldValue=None, FullMesh=None, Length=None, Level=None, MaxValue=None, MinValue=None, Name=None, Offset=None, OffsetFromRoot=None, OnTheFlyMask=None, Optional=None, OptionalEnabled=None, RandomMask=None, RateVaried=None, ReadOnly=None, RequiresUdf=None, Seed=None, SingleValue=None, StartValue=None, StepValue=None, SupportsAuto=None, SupportsNonRepeatableRandom=None, SupportsOnTheFlyMask=None, SupportsRepeatableRandomRange=None, TrackingEnabled=None, ValueFormat=None, ValueList=None, ValueType=None):
        # type: (str, bool, bool, List[str], str, str, str, List[str], bool, str, str, str, str, str, bool, int, bool, str, str, str, int, int, str, bool, bool, str, bool, bool, bool, str, str, str, str, bool, bool, bool, bool, bool, str, List[str], str) -> Field
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

    def AddLevel(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the addLevel operation on the server.

        Add a level to the current field.

        addLevel(async_operation=bool)string
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: The new level that has been added.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addLevel', payload=payload, response_object=None)

    def RemoveLevel(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the removeLevel operation on the server.

        Remove a level.

        removeLevel(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('removeLevel', payload=payload, response_object=None)
