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
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_3d4a798f097a174b136d18ef8549541a.DcbxTlvAppQaz): An instance of the DcbxTlvAppQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_3d4a798f097a174b136d18ef8549541a import DcbxTlvAppQaz
        return DcbxTlvAppQaz(self)._select()

    @property
    def DcbxTlvBcn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_b4f491195cdcf91505ba57ca761d09e1.DcbxTlvBcn): An instance of the DcbxTlvBcn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_b4f491195cdcf91505ba57ca761d09e1 import DcbxTlvBcn
        return DcbxTlvBcn(self)._select()

    @property
    def DcbxTlvCustom(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_a354e83f5906b2e5e4199ba4d7fbfcd3.DcbxTlvCustom): An instance of the DcbxTlvCustom class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_a354e83f5906b2e5e4199ba4d7fbfcd3 import DcbxTlvCustom
        return DcbxTlvCustom(self)._select()

    @property
    def DcbxTlvEtsQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_d1d231fe91b44972932854b3f6e7c91e.DcbxTlvEtsQaz): An instance of the DcbxTlvEtsQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_d1d231fe91b44972932854b3f6e7c91e import DcbxTlvEtsQaz
        return DcbxTlvEtsQaz(self)._select()

    @property
    def DcbxTlvFcoeIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_22cf7d24ee8c1fde139433ccee01b1c6.DcbxTlvFcoeIeee): An instance of the DcbxTlvFcoeIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_22cf7d24ee8c1fde139433ccee01b1c6 import DcbxTlvFcoeIeee
        return DcbxTlvFcoeIeee(self)._select()

    @property
    def DcbxTlvFcoeIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_1522c8da9c53f8b47430db9b879ebded.DcbxTlvFcoeIntel): An instance of the DcbxTlvFcoeIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_1522c8da9c53f8b47430db9b879ebded import DcbxTlvFcoeIntel
        return DcbxTlvFcoeIntel(self)._select()

    @property
    def DcbxTlvLogicalLink(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_1a9d7e45da17353b8e3718baef5b709b.DcbxTlvLogicalLink): An instance of the DcbxTlvLogicalLink class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_1a9d7e45da17353b8e3718baef5b709b import DcbxTlvLogicalLink
        return DcbxTlvLogicalLink(self)._select()

    @property
    def DcbxTlvNivIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_2153cc9cdfaaa73cd0f4476d6bd59275.DcbxTlvNivIeee): An instance of the DcbxTlvNivIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_2153cc9cdfaaa73cd0f4476d6bd59275 import DcbxTlvNivIeee
        return DcbxTlvNivIeee(self)._select()

    @property
    def DcbxTlvNivIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_25404974e2a200ee0bc4e340dcce5b04.DcbxTlvNivIntel): An instance of the DcbxTlvNivIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_25404974e2a200ee0bc4e340dcce5b04 import DcbxTlvNivIntel
        return DcbxTlvNivIntel(self)._select()

    @property
    def DcbxTlvPfcIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_ee89b99a93199a7cb38c0b4aab1d3902.DcbxTlvPfcIeee): An instance of the DcbxTlvPfcIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_ee89b99a93199a7cb38c0b4aab1d3902 import DcbxTlvPfcIeee
        return DcbxTlvPfcIeee(self)._select()

    @property
    def DcbxTlvPfcIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_941071691ce90d5aa115f21bc51a2606.DcbxTlvPfcIntel): An instance of the DcbxTlvPfcIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_941071691ce90d5aa115f21bc51a2606 import DcbxTlvPfcIntel
        return DcbxTlvPfcIntel(self)._select()

    @property
    def DcbxTlvPfcQaz(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_f57e160a2f234ec486a825023475960b.DcbxTlvPfcQaz): An instance of the DcbxTlvPfcQaz class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_f57e160a2f234ec486a825023475960b import DcbxTlvPfcQaz
        return DcbxTlvPfcQaz(self)._select()

    @property
    def DcbxTlvPgIeee(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_3e049735ef6016dd1f04a02602c0c738.DcbxTlvPgIeee): An instance of the DcbxTlvPgIeee class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_3e049735ef6016dd1f04a02602c0c738 import DcbxTlvPgIeee
        return DcbxTlvPgIeee(self)._select()

    @property
    def DcbxTlvPgIntel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_c7f9bf3b488201b0250f1f0d425a8df1.DcbxTlvPgIntel): An instance of the DcbxTlvPgIntel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_c7f9bf3b488201b0250f1f0d425a8df1 import DcbxTlvPgIntel
        return DcbxTlvPgIntel(self)._select()

    @property
    def ObjectId(self):
        """
        Returns
        -------
        - str: Unique identifier for this object
        """
        return self._get_attribute('objectId')

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
