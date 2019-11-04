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
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_lnldhrpbmdzl2rjynhubhzbchbryxo.DcbxTlvAppQaz)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvappqaz_lnldhrpbmdzl2rjynhubhzbchbryxo import DcbxTlvAppQaz
		return DcbxTlvAppQaz(self)._select()

	@property
	def DcbxTlvBcn(self):
		"""An instance of the DcbxTlvBcn class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_3rsdlnldhrpbmdzl2rjynhubhzcy24.DcbxTlvBcn)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvbcn_3rsdlnldhrpbmdzl2rjynhubhzcy24 import DcbxTlvBcn
		return DcbxTlvBcn(self)._select()

	@property
	def DcbxTlvCustom(self):
		"""An instance of the DcbxTlvCustom class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_lnldhrpbmdzl2rjynhubhzddxn0b20.DcbxTlvCustom)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvcustom_lnldhrpbmdzl2rjynhubhzddxn0b20 import DcbxTlvCustom
		return DcbxTlvCustom(self)._select()

	@property
	def DcbxTlvEtsQaz(self):
		"""An instance of the DcbxTlvEtsQaz class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_lnldhrpbmdzl2rjynhubhzfdhnryxo.DcbxTlvEtsQaz)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvetsqaz_lnldhrpbmdzl2rjynhubhzfdhnryxo import DcbxTlvEtsQaz
		return DcbxTlvEtsQaz(self)._select()

	@property
	def DcbxTlvFcoeIeee(self):
		"""An instance of the DcbxTlvFcoeIeee class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_dhrpbmdzl2rjynhubhzgy29lswvlzq.DcbxTlvFcoeIeee)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeieee_dhrpbmdzl2rjynhubhzgy29lswvlzq import DcbxTlvFcoeIeee
		return DcbxTlvFcoeIeee(self)._select()

	@property
	def DcbxTlvFcoeIntel(self):
		"""An instance of the DcbxTlvFcoeIntel class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_hrpbmdzl2rjynhubhzgy29lsw50zww.DcbxTlvFcoeIntel)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvfcoeintel_hrpbmdzl2rjynhubhzgy29lsw50zww import DcbxTlvFcoeIntel
		return DcbxTlvFcoeIntel(self)._select()

	@property
	def DcbxTlvLogicalLink(self):
		"""An instance of the DcbxTlvLogicalLink class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_bmdzl2rjynhubhzmb2dpy2fstgluaw.DcbxTlvLogicalLink)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvlogicallink_bmdzl2rjynhubhzmb2dpy2fstgluaw import DcbxTlvLogicalLink
		return DcbxTlvLogicalLink(self)._select()

	@property
	def DcbxTlvNivIeee(self):
		"""An instance of the DcbxTlvNivIeee class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_nldhrpbmdzl2rjynhubhzoaxzjzwvl.DcbxTlvNivIeee)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivieee_nldhrpbmdzl2rjynhubhzoaxzjzwvl import DcbxTlvNivIeee
		return DcbxTlvNivIeee(self)._select()

	@property
	def DcbxTlvNivIntel(self):
		"""An instance of the DcbxTlvNivIntel class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_dhrpbmdzl2rjynhubhzoaxzjbnrlba.DcbxTlvNivIntel)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvnivintel_dhrpbmdzl2rjynhubhzoaxzjbnrlba import DcbxTlvNivIntel
		return DcbxTlvNivIntel(self)._select()

	@property
	def DcbxTlvPfcIeee(self):
		"""An instance of the DcbxTlvPfcIeee class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_nldhrpbmdzl2rjynhubhzqzmnjzwvl.DcbxTlvPfcIeee)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcieee_nldhrpbmdzl2rjynhubhzqzmnjzwvl import DcbxTlvPfcIeee
		return DcbxTlvPfcIeee(self)._select()

	@property
	def DcbxTlvPfcIntel(self):
		"""An instance of the DcbxTlvPfcIntel class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_dhrpbmdzl2rjynhubhzqzmnjbnrlba.DcbxTlvPfcIntel)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcintel_dhrpbmdzl2rjynhubhzqzmnjbnrlba import DcbxTlvPfcIntel
		return DcbxTlvPfcIntel(self)._select()

	@property
	def DcbxTlvPfcQaz(self):
		"""An instance of the DcbxTlvPfcQaz class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_lnldhrpbmdzl2rjynhubhzqzmnryxo.DcbxTlvPfcQaz)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpfcqaz_lnldhrpbmdzl2rjynhubhzqzmnryxo import DcbxTlvPfcQaz
		return DcbxTlvPfcQaz(self)._select()

	@property
	def DcbxTlvPgIeee(self):
		"""An instance of the DcbxTlvPgIeee class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_lnldhrpbmdzl2rjynhubhzqz0llzwu.DcbxTlvPgIeee)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgieee_lnldhrpbmdzl2rjynhubhzqz0llzwu import DcbxTlvPgIeee
		return DcbxTlvPgIeee(self)._select()

	@property
	def DcbxTlvPgIntel(self):
		"""An instance of the DcbxTlvPgIntel class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_nldhrpbmdzl2rjynhubhzqz0ludgvs.DcbxTlvPgIntel)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dcbxtlvpgintel_nldhrpbmdzl2rjynhubhzqz0ludgvs import DcbxTlvPgIntel
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
