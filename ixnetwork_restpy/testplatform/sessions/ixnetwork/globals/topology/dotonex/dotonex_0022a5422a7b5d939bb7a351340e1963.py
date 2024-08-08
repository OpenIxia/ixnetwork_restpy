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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class DotOneX(Base):
    """
    The DotOneX class encapsulates a required dotOneX resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "dotOneX"
    _SDM_ATT_MAP = {
        "AltName": "altName",
        "AuthOnNoResponse": "authOnNoResponse",
        "AuthWaitPeriod": "authWaitPeriod",
        "City": "city",
        "Company": "company",
        "Count": "count",
        "Country": "country",
        "Department": "department",
        "DescriptiveName": "descriptiveName",
        "DisableLogoff": "disableLogoff",
        "DupResponse": "dupResponse",
        "DutTestMode": "dutTestMode",
        "FragmentSize": "fragmentSize",
        "GetCACertOnly": "getCACertOnly",
        "KeySize": "keySize",
        "KeyUsage": "keyUsage",
        "MacAuthPrefix": "macAuthPrefix",
        "MaxOutstandingRequests": "maxOutstandingRequests",
        "MaxSetupRate": "maxSetupRate",
        "MaxStart": "maxStart",
        "MaxTeardownRate": "maxTeardownRate",
        "Name": "name",
        "OnlyMulticast": "onlyMulticast",
        "RowNames": "rowNames",
        "ServerURL": "serverURL",
        "StartPeriod": "startPeriod",
        "State": "state",
        "SuccessiveStart": "successiveStart",
        "UseVlanIdentify": "useVlanIdentify",
        "WaitBeforeRun": "waitBeforeRun",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(DotOneX, self).__init__(parent, list_op)

    @property
    def AltName(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Other Options - Alternative Subject Name
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AltName"]))

    @property
    def AuthOnNoResponse(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If the DUT is not responding to EAPoL Start after configured number of retries, declare the session a success
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthOnNoResponse"])
        )

    @property
    def AuthWaitPeriod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The maximum time interval, measured in seconds, that a Supplicant will wait for an Authenticator response.Maximum value is 3600
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AuthWaitPeriod"])
        )

    @property
    def City(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identification Info - City
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["City"]))

    @property
    def Company(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identification Info - Company
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Company"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def Country(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identification Info - Country
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Country"]))

    @property
    def Department(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identification Info - Department
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Department"]))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def DisableLogoff(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Do not send Logoff message when closing a session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DisableLogoff"]))

    @property
    def DupResponse(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Respond to Duplicates when enabled.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DupResponse"]))

    @property
    def DutTestMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify what is the dut port mode
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DutTestMode"]))

    @property
    def FragmentSize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The maximum size of a fragment that can be sent on the wire for TLS fragments that comprise the phase 1 conversation (tunnel establishment). Max value is 1400
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FragmentSize"]))

    @property
    def GetCACertOnly(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Use this option to get CA Certificate Only. Eg: For PEAPv0/v1 case there is no need to get User Certificate.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GetCACertOnly"]))

    @property
    def KeySize(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Key Options - Key Size
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeySize"]))

    @property
    def KeyUsage(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select key usage extensions
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["KeyUsage"]))

    @property
    def MacAuthPrefix(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When using machine authentication, a prefix is needed to differentiate between users and machines.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MacAuthPrefix"]))

    @property
    def MaxOutstandingRequests(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The maximum number of sessions that can be negotiated at one moment. Max value is 1024
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxOutstandingRequests"])
        )

    @property
    def MaxSetupRate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of interfaces to setup per second. Max rate is 1024
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxSetupRate"]))

    @property
    def MaxStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of times to send EAPOL Start frames for which no response is received before declaring that the sessions have timed out. Max value is 100
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["MaxStart"]))

    @property
    def MaxTeardownRate(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of interfaces to tear down per second. Max value is 1024
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MaxTeardownRate"])
        )

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def OnlyMulticast(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify if destination MAC address can be multicast.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OnlyMulticast"]))

    @property
    def RowNames(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str): Name of rows
        """
        return self._get_attribute(self._SDM_ATT_MAP["RowNames"])

    @property
    def ServerURL(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Certificate Server URL
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["ServerURL"]))

    @property
    def StartPeriod(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The time interval between successive EAPOL Start messages sent by a Supplicant.Maxium value is 3600
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["StartPeriod"]))

    @property
    def State(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identification Info - State
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["State"]))

    @property
    def SuccessiveStart(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of EAPOL Start messages sent when the supplicant starts the process of authentication. Max value is 100
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SuccessiveStart"])
        )

    @property
    def UseVlanIdentify(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify if VLAN is to be used to identify the supplicants
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UseVlanIdentify"])
        )

    @property
    def WaitBeforeRun(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of secs to wait before running the protocol.Maximum wait is 500
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["WaitBeforeRun"]))

    def update(self, Name=None):
        # type: (str) -> DotOneX
        """Updates dotOneX resource on the server.

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

    def find(self, Count=None, DescriptiveName=None, Name=None, RowNames=None):
        # type: (int, str, str, List[str]) -> DotOneX
        """Finds and retrieves dotOneX resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dotOneX resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dotOneX resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - RowNames (list(str)): Name of rows

        Returns
        -------
        - self: This instance with matching dotOneX resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dotOneX data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dotOneX resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(
        self,
        PortNames=None,
        AltName=None,
        AuthOnNoResponse=None,
        AuthWaitPeriod=None,
        City=None,
        Company=None,
        Country=None,
        Department=None,
        DisableLogoff=None,
        DupResponse=None,
        DutTestMode=None,
        FragmentSize=None,
        GetCACertOnly=None,
        KeySize=None,
        KeyUsage=None,
        MacAuthPrefix=None,
        MaxOutstandingRequests=None,
        MaxSetupRate=None,
        MaxStart=None,
        MaxTeardownRate=None,
        OnlyMulticast=None,
        ServerURL=None,
        StartPeriod=None,
        State=None,
        SuccessiveStart=None,
        UseVlanIdentify=None,
        WaitBeforeRun=None,
    ):
        """Base class infrastructure that gets a list of dotOneX device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - AltName (str): optional regex of altName
        - AuthOnNoResponse (str): optional regex of authOnNoResponse
        - AuthWaitPeriod (str): optional regex of authWaitPeriod
        - City (str): optional regex of city
        - Company (str): optional regex of company
        - Country (str): optional regex of country
        - Department (str): optional regex of department
        - DisableLogoff (str): optional regex of disableLogoff
        - DupResponse (str): optional regex of dupResponse
        - DutTestMode (str): optional regex of dutTestMode
        - FragmentSize (str): optional regex of fragmentSize
        - GetCACertOnly (str): optional regex of getCACertOnly
        - KeySize (str): optional regex of keySize
        - KeyUsage (str): optional regex of keyUsage
        - MacAuthPrefix (str): optional regex of macAuthPrefix
        - MaxOutstandingRequests (str): optional regex of maxOutstandingRequests
        - MaxSetupRate (str): optional regex of maxSetupRate
        - MaxStart (str): optional regex of maxStart
        - MaxTeardownRate (str): optional regex of maxTeardownRate
        - OnlyMulticast (str): optional regex of onlyMulticast
        - ServerURL (str): optional regex of serverURL
        - StartPeriod (str): optional regex of startPeriod
        - State (str): optional regex of state
        - SuccessiveStart (str): optional regex of successiveStart
        - UseVlanIdentify (str): optional regex of useVlanIdentify
        - WaitBeforeRun (str): optional regex of waitBeforeRun

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
