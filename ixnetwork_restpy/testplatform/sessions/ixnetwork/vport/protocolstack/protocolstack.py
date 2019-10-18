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


class ProtocolStack(Base):
	"""The ProtocolStack class encapsulates a required protocolStack node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the ProtocolStack property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	__slots__ = ()
	_SDM_NAME = 'protocolStack'

	def __init__(self, parent):
		super(ProtocolStack, self).__init__(parent)

	@property
	def AmtOptions(self):
		"""An instance of the AmtOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions.amtoptions.AmtOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.amtoptions.amtoptions import AmtOptions
		return AmtOptions(self)

	@property
	def AncpOptions(self):
		"""An instance of the AncpOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions.ancpoptions.AncpOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ancpoptions.ancpoptions import AncpOptions
		return AncpOptions(self)

	@property
	def Atm(self):
		"""An instance of the Atm class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.atm.atm.Atm)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.atm.atm import Atm
		return Atm(self)

	@property
	def DhcpHostsOptions(self):
		"""An instance of the DhcpHostsOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions.dhcphostsoptions.DhcpHostsOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcphostsoptions.dhcphostsoptions import DhcpHostsOptions
		return DhcpHostsOptions(self)

	@property
	def DhcpOptions(self):
		"""An instance of the DhcpOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions.dhcpoptions.DhcpOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpoptions.dhcpoptions import DhcpOptions
		return DhcpOptions(self)

	@property
	def Dhcpv6ClientOptions(self):
		"""An instance of the Dhcpv6ClientOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions.dhcpv6clientoptions.Dhcpv6ClientOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6clientoptions.dhcpv6clientoptions import Dhcpv6ClientOptions
		return Dhcpv6ClientOptions(self)

	@property
	def Dhcpv6PdClientOptions(self):
		"""An instance of the Dhcpv6PdClientOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions.dhcpv6pdclientoptions.Dhcpv6PdClientOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6pdclientoptions.dhcpv6pdclientoptions import Dhcpv6PdClientOptions
		return Dhcpv6PdClientOptions(self)

	@property
	def Dhcpv6ServerOptions(self):
		"""An instance of the Dhcpv6ServerOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions.dhcpv6serveroptions.Dhcpv6ServerOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dhcpv6serveroptions.dhcpv6serveroptions import Dhcpv6ServerOptions
		return Dhcpv6ServerOptions(self)

	@property
	def Dot1xOptions(self):
		"""An instance of the Dot1xOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions.dot1xoptions.Dot1xOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.dot1xoptions.dot1xoptions import Dot1xOptions
		return Dot1xOptions(self)

	@property
	def EapoUdpOptions(self):
		"""An instance of the EapoUdpOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions.eapoudpoptions.EapoUdpOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.eapoudpoptions.eapoudpoptions import EapoUdpOptions
		return EapoUdpOptions(self)

	@property
	def EgtpClientOptions(self):
		"""An instance of the EgtpClientOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions.egtpclientoptions.EgtpClientOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpclientoptions.egtpclientoptions import EgtpClientOptions
		return EgtpClientOptions(self)

	@property
	def EgtpMmeOptions(self):
		"""An instance of the EgtpMmeOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpmmeoptions.egtpmmeoptions.EgtpMmeOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpmmeoptions.egtpmmeoptions import EgtpMmeOptions
		return EgtpMmeOptions(self)

	@property
	def EgtpOptionsBase(self):
		"""An instance of the EgtpOptionsBase class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase.egtpoptionsbase.EgtpOptionsBase)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpoptionsbase.egtpoptionsbase import EgtpOptionsBase
		return EgtpOptionsBase(self)

	@property
	def EgtpS5S8PgwOptions(self):
		"""An instance of the EgtpS5S8PgwOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions.egtps5s8pgwoptions.EgtpS5S8PgwOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8pgwoptions.egtps5s8pgwoptions import EgtpS5S8PgwOptions
		return EgtpS5S8PgwOptions(self)

	@property
	def EgtpS5S8SgwOptions(self):
		"""An instance of the EgtpS5S8SgwOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions.egtps5s8sgwoptions.EgtpS5S8SgwOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtps5s8sgwoptions.egtps5s8sgwoptions import EgtpS5S8SgwOptions
		return EgtpS5S8SgwOptions(self)

	@property
	def EgtpServerOptions(self):
		"""An instance of the EgtpServerOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions.egtpserveroptions.EgtpServerOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpserveroptions.egtpserveroptions import EgtpServerOptions
		return EgtpServerOptions(self)

	@property
	def EgtpSgwOptions(self):
		"""An instance of the EgtpSgwOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions.egtpsgwoptions.EgtpSgwOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.egtpsgwoptions.egtpsgwoptions import EgtpSgwOptions
		return EgtpSgwOptions(self)

	@property
	def Ethernet(self):
		"""An instance of the Ethernet class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ethernet.Ethernet)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ethernet import Ethernet
		return Ethernet(self)

	@property
	def EthernetEndpoint(self):
		"""An instance of the EthernetEndpoint class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ethernetendpoint.EthernetEndpoint)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ethernetendpoint import EthernetEndpoint
		return EthernetEndpoint(self)

	@property
	def EthernetOptions(self):
		"""An instance of the EthernetOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ethernetoptions.EthernetOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ethernet.ethernetoptions import EthernetOptions
		return EthernetOptions(self)

	@property
	def FcClientEndpoint(self):
		"""An instance of the FcClientEndpoint class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint.fcclientendpoint.FcClientEndpoint)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientendpoint.fcclientendpoint import FcClientEndpoint
		return FcClientEndpoint(self)

	@property
	def FcClientOptions(self):
		"""An instance of the FcClientOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions.fcclientoptions.FcClientOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcclientoptions.fcclientoptions import FcClientOptions
		return FcClientOptions(self)

	@property
	def FcFportFwdEndpoint(self):
		"""An instance of the FcFportFwdEndpoint class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint.fcfportfwdendpoint.FcFportFwdEndpoint)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportfwdendpoint.fcfportfwdendpoint import FcFportFwdEndpoint
		return FcFportFwdEndpoint(self)

	@property
	def FcFportOptions(self):
		"""An instance of the FcFportOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions.fcfportoptions.FcFportOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcfportoptions.fcfportoptions import FcFportOptions
		return FcFportOptions(self)

	@property
	def FcoeClientOptions(self):
		"""An instance of the FcoeClientOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions.fcoeclientoptions.FcoeClientOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoeclientoptions.fcoeclientoptions import FcoeClientOptions
		return FcoeClientOptions(self)

	@property
	def FcoeFwdOptions(self):
		"""An instance of the FcoeFwdOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions.fcoefwdoptions.FcoeFwdOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.fcoefwdoptions.fcoefwdoptions import FcoeFwdOptions
		return FcoeFwdOptions(self)

	@property
	def IgmpOptions(self):
		"""An instance of the IgmpOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions.igmpoptions.IgmpOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.igmpoptions.igmpoptions import IgmpOptions
		return IgmpOptions(self)

	@property
	def IpRangeOptions(self):
		"""An instance of the IpRangeOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions.iprangeoptions.IpRangeOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.iprangeoptions.iprangeoptions import IpRangeOptions
		return IpRangeOptions(self)

	@property
	def L2tpOptions(self):
		"""An instance of the L2tpOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions.l2tpoptions.L2tpOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.l2tpoptions.l2tpoptions import L2tpOptions
		return L2tpOptions(self)

	@property
	def Options(self):
		"""An instance of the Options class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options.options.Options)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.options.options import Options
		return Options(self)._select()

	@property
	def PppoxOptions(self):
		"""An instance of the PppoxOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions.pppoxoptions.PppoxOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.pppoxoptions.pppoxoptions import PppoxOptions
		return PppoxOptions(self)

	@property
	def PtpOptions(self):
		"""An instance of the PtpOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions.ptpoptions.PtpOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.ptpoptions.ptpoptions import PtpOptions
		return PtpOptions(self)

	@property
	def SmDnsOptions(self):
		"""An instance of the SmDnsOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions.smdnsoptions.SmDnsOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.smdnsoptions.smdnsoptions import SmDnsOptions
		return SmDnsOptions(self)

	@property
	def StaticHostsOptions(self):
		"""An instance of the StaticHostsOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions.statichostsoptions.StaticHostsOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.statichostsoptions.statichostsoptions import StaticHostsOptions
		return StaticHostsOptions(self)

	@property
	def TwampOptions(self):
		"""An instance of the TwampOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions.twampoptions.TwampOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampoptions.twampoptions import TwampOptions
		return TwampOptions(self)

	@property
	def TwampServerOptions(self):
		"""An instance of the TwampServerOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions.twampserveroptions.TwampServerOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.twampserveroptions.twampserveroptions import TwampServerOptions
		return TwampServerOptions(self)

	@property
	def VepaOptions(self):
		"""An instance of the VepaOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions.vepaoptions.VepaOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.vepaoptions.vepaoptions import VepaOptions
		return VepaOptions(self)

	@property
	def WebAuthOptions(self):
		"""An instance of the WebAuthOptions class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions.webauthoptions.WebAuthOptions)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocolstack.webauthoptions.webauthoptions import WebAuthOptions
		return WebAuthOptions(self)

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
