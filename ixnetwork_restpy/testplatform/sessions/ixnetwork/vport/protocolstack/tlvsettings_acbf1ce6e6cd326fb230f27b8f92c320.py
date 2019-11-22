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


class TlvSettings(Base):
    """DCBX TLV settings
    The TlvSettings class encapsulates a required tlvSettings resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'tlvSettings'

    def __init__(self, parent):
        super(TlvSettings, self).__init__(parent)

    @property
    def DcbxTlvAppQaz(self):
        """An instance of the DcbxTlvAppQaz class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_dcd8c49733dfdd238372ab418c35293f.DcbxTlvAppQaz)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_dcd8c49733dfdd238372ab418c35293f import DcbxTlvAppQaz
        return DcbxTlvAppQaz(self)._select()

    @property
    def DcbxTlvBcn(self):
        """An instance of the DcbxTlvBcn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_2ec7b9df0ea6afd3964d822d1125ddd4.DcbxTlvBcn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_2ec7b9df0ea6afd3964d822d1125ddd4 import DcbxTlvBcn
        return DcbxTlvBcn(self)._select()

    @property
    def DcbxTlvCustom(self):
        """An instance of the DcbxTlvCustom class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_7ca03e41e7c06f81101aa5a8701cb828.DcbxTlvCustom)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_7ca03e41e7c06f81101aa5a8701cb828 import DcbxTlvCustom
        return DcbxTlvCustom(self)._select()

    @property
    def DcbxTlvEtsQaz(self):
        """An instance of the DcbxTlvEtsQaz class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_42cd6197478471b60f3270c47c9d8b86.DcbxTlvEtsQaz)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_42cd6197478471b60f3270c47c9d8b86 import DcbxTlvEtsQaz
        return DcbxTlvEtsQaz(self)._select()

    @property
    def DcbxTlvFcoeIeee(self):
        """An instance of the DcbxTlvFcoeIeee class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_1083208c3c386768819a7e6dc8c2934e.DcbxTlvFcoeIeee)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_1083208c3c386768819a7e6dc8c2934e import DcbxTlvFcoeIeee
        return DcbxTlvFcoeIeee(self)._select()

    @property
    def DcbxTlvFcoeIntel(self):
        """An instance of the DcbxTlvFcoeIntel class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_22b1f9a2fe8e603dc2f8389e163f7e79.DcbxTlvFcoeIntel)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_22b1f9a2fe8e603dc2f8389e163f7e79 import DcbxTlvFcoeIntel
        return DcbxTlvFcoeIntel(self)._select()

    @property
    def DcbxTlvLogicalLink(self):
        """An instance of the DcbxTlvLogicalLink class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_535a56f4266d3fe5245c8bd20c96eaef.DcbxTlvLogicalLink)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_535a56f4266d3fe5245c8bd20c96eaef import DcbxTlvLogicalLink
        return DcbxTlvLogicalLink(self)._select()

    @property
    def DcbxTlvNivIeee(self):
        """An instance of the DcbxTlvNivIeee class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_a39ad1f8b1cb0f529443de035b111e3c.DcbxTlvNivIeee)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_a39ad1f8b1cb0f529443de035b111e3c import DcbxTlvNivIeee
        return DcbxTlvNivIeee(self)._select()

    @property
    def DcbxTlvNivIntel(self):
        """An instance of the DcbxTlvNivIntel class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_07cc119365f82740d51463ee26ad55fe.DcbxTlvNivIntel)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_07cc119365f82740d51463ee26ad55fe import DcbxTlvNivIntel
        return DcbxTlvNivIntel(self)._select()

    @property
    def DcbxTlvPfcIeee(self):
        """An instance of the DcbxTlvPfcIeee class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_678e4364e1fe44baf1419314193226c0.DcbxTlvPfcIeee)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_678e4364e1fe44baf1419314193226c0 import DcbxTlvPfcIeee
        return DcbxTlvPfcIeee(self)._select()

    @property
    def DcbxTlvPfcIntel(self):
        """An instance of the DcbxTlvPfcIntel class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_195cd597e8e9170d72360bcd9752c375.DcbxTlvPfcIntel)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_195cd597e8e9170d72360bcd9752c375 import DcbxTlvPfcIntel
        return DcbxTlvPfcIntel(self)._select()

    @property
    def DcbxTlvPfcQaz(self):
        """An instance of the DcbxTlvPfcQaz class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_2d5059114410112880beef33e3c19459.DcbxTlvPfcQaz)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_2d5059114410112880beef33e3c19459 import DcbxTlvPfcQaz
        return DcbxTlvPfcQaz(self)._select()

    @property
    def DcbxTlvPgIeee(self):
        """An instance of the DcbxTlvPgIeee class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_50604a082d57558238447c424ff95a07.DcbxTlvPgIeee)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_50604a082d57558238447c424ff95a07 import DcbxTlvPgIeee
        return DcbxTlvPgIeee(self)._select()

    @property
    def DcbxTlvPgIntel(self):
        """An instance of the DcbxTlvPgIntel class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_19c05a3e963f93962597eb890f366fe9.DcbxTlvPgIntel)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_19c05a3e963f93962597eb890f366fe9 import DcbxTlvPgIntel
        return DcbxTlvPgIntel(self)._select()

    @property
    def ObjectId(self):
        """Unique identifier for this object

        Returns:
            str
        """
        return self._get_attribute('objectId')

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
