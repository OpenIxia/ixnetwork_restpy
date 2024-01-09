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


class ConfigMDLevelsParams(Base):
    """Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.
    The ConfigMDLevelsParams class encapsulates a required configMDLevelsParams resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "configMDLevelsParams"
    _SDM_ATT_MAP = {
        "MdLevel1": "mdLevel1",
        "MdLevel2": "mdLevel2",
        "MdLevel3": "mdLevel3",
        "MdLevel4": "mdLevel4",
        "MdLevel5": "mdLevel5",
        "MdLevel6": "mdLevel6",
        "MdLevel7": "mdLevel7",
        "MdLevel8": "mdLevel8",
        "MdName1": "mdName1",
        "MdName2": "mdName2",
        "MdName3": "mdName3",
        "MdName4": "mdName4",
        "MdName5": "mdName5",
        "MdName6": "mdName6",
        "MdName7": "mdName7",
        "MdName8": "mdName8",
        "MdNameFormat1": "mdNameFormat1",
        "MdNameFormat2": "mdNameFormat2",
        "MdNameFormat3": "mdNameFormat3",
        "MdNameFormat4": "mdNameFormat4",
        "MdNameFormat5": "mdNameFormat5",
        "MdNameFormat6": "mdNameFormat6",
        "MdNameFormat7": "mdNameFormat7",
        "MdNameFormat8": "mdNameFormat8",
        "NumMDLevels": "numMDLevels",
    }
    _SDM_ENUM_MAP = {
        "mdNameFormat1": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat2": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat3": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat4": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat5": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat6": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat7": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
        "mdNameFormat8": [
            "mdNameFormatNoMaintenanceDomainName",
            "mdNameFormatDomainNameBasedStr",
            "mdNameFormatMacPlusTwoOctetInt",
            "mdNameFormatCharacterStr",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(ConfigMDLevelsParams, self).__init__(parent, list_op)

    @property
    def MdLevel1(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel1"])

    @MdLevel1.setter
    def MdLevel1(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel1"], value)

    @property
    def MdLevel2(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel2"])

    @MdLevel2.setter
    def MdLevel2(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel2"], value)

    @property
    def MdLevel3(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel3"])

    @MdLevel3.setter
    def MdLevel3(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel3"], value)

    @property
    def MdLevel4(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel4"])

    @MdLevel4.setter
    def MdLevel4(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel4"], value)

    @property
    def MdLevel5(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel5"])

    @MdLevel5.setter
    def MdLevel5(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel5"], value)

    @property
    def MdLevel6(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel6"])

    @MdLevel6.setter
    def MdLevel6(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel6"], value)

    @property
    def MdLevel7(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel7"])

    @MdLevel7.setter
    def MdLevel7(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel7"], value)

    @property
    def MdLevel8(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdLevel8"])

    @MdLevel8.setter
    def MdLevel8(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdLevel8"], value)

    @property
    def MdName1(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName1"])

    @MdName1.setter
    def MdName1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName1"], value)

    @property
    def MdName2(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName2"])

    @MdName2.setter
    def MdName2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName2"], value)

    @property
    def MdName3(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName3"])

    @MdName3.setter
    def MdName3(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName3"], value)

    @property
    def MdName4(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName4"])

    @MdName4.setter
    def MdName4(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName4"], value)

    @property
    def MdName5(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName5"])

    @MdName5.setter
    def MdName5(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName5"], value)

    @property
    def MdName6(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName6"])

    @MdName6.setter
    def MdName6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName6"], value)

    @property
    def MdName7(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName7"])

    @MdName7.setter
    def MdName7(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName7"], value)

    @property
    def MdName8(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Network Address Step Value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdName8"])

    @MdName8.setter
    def MdName8(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdName8"], value)

    @property
    def MdNameFormat1(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat1"])

    @MdNameFormat1.setter
    def MdNameFormat1(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat1"], value)

    @property
    def MdNameFormat2(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat2"])

    @MdNameFormat2.setter
    def MdNameFormat2(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat2"], value)

    @property
    def MdNameFormat3(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat3"])

    @MdNameFormat3.setter
    def MdNameFormat3(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat3"], value)

    @property
    def MdNameFormat4(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat4"])

    @MdNameFormat4.setter
    def MdNameFormat4(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat4"], value)

    @property
    def MdNameFormat5(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat5"])

    @MdNameFormat5.setter
    def MdNameFormat5(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat5"], value)

    @property
    def MdNameFormat6(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat6"])

    @MdNameFormat6.setter
    def MdNameFormat6(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat6"], value)

    @property
    def MdNameFormat7(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat7"])

    @MdNameFormat7.setter
    def MdNameFormat7(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat7"], value)

    @property
    def MdNameFormat8(self):
        # type: () -> str
        """
        Returns
        -------
        - str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr): Text
        """
        return self._get_attribute(self._SDM_ATT_MAP["MdNameFormat8"])

    @MdNameFormat8.setter
    def MdNameFormat8(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MdNameFormat8"], value)

    @property
    def NumMDLevels(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Import only the best routes (provided route file has this information).
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumMDLevels"])

    @NumMDLevels.setter
    def NumMDLevels(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumMDLevels"], value)

    def update(
        self,
        MdLevel1=None,
        MdLevel2=None,
        MdLevel3=None,
        MdLevel4=None,
        MdLevel5=None,
        MdLevel6=None,
        MdLevel7=None,
        MdLevel8=None,
        MdName1=None,
        MdName2=None,
        MdName3=None,
        MdName4=None,
        MdName5=None,
        MdName6=None,
        MdName7=None,
        MdName8=None,
        MdNameFormat1=None,
        MdNameFormat2=None,
        MdNameFormat3=None,
        MdNameFormat4=None,
        MdNameFormat5=None,
        MdNameFormat6=None,
        MdNameFormat7=None,
        MdNameFormat8=None,
        NumMDLevels=None,
    ):
        # type: (int, int, int, int, int, int, int, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, int) -> ConfigMDLevelsParams
        """Updates configMDLevelsParams resource on the server.

        Args
        ----
        - MdLevel1 (number): Text
        - MdLevel2 (number): Text
        - MdLevel3 (number): Text
        - MdLevel4 (number): Text
        - MdLevel5 (number): Text
        - MdLevel6 (number): Text
        - MdLevel7 (number): Text
        - MdLevel8 (number): Text
        - MdName1 (str): Network Address Step Value.
        - MdName2 (str): Network Address Step Value.
        - MdName3 (str): Network Address Step Value.
        - MdName4 (str): Network Address Step Value.
        - MdName5 (str): Network Address Step Value.
        - MdName6 (str): Network Address Step Value.
        - MdName7 (str): Network Address Step Value.
        - MdName8 (str): Network Address Step Value.
        - MdNameFormat1 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat2 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat3 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat4 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat5 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat6 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat7 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat8 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - NumMDLevels (number): Import only the best routes (provided route file has this information).

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        MdLevel1=None,
        MdLevel2=None,
        MdLevel3=None,
        MdLevel4=None,
        MdLevel5=None,
        MdLevel6=None,
        MdLevel7=None,
        MdLevel8=None,
        MdName1=None,
        MdName2=None,
        MdName3=None,
        MdName4=None,
        MdName5=None,
        MdName6=None,
        MdName7=None,
        MdName8=None,
        MdNameFormat1=None,
        MdNameFormat2=None,
        MdNameFormat3=None,
        MdNameFormat4=None,
        MdNameFormat5=None,
        MdNameFormat6=None,
        MdNameFormat7=None,
        MdNameFormat8=None,
        NumMDLevels=None,
    ):
        # type: (int, int, int, int, int, int, int, int, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, int) -> ConfigMDLevelsParams
        """Finds and retrieves configMDLevelsParams resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve configMDLevelsParams resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all configMDLevelsParams resources from the server.

        Args
        ----
        - MdLevel1 (number): Text
        - MdLevel2 (number): Text
        - MdLevel3 (number): Text
        - MdLevel4 (number): Text
        - MdLevel5 (number): Text
        - MdLevel6 (number): Text
        - MdLevel7 (number): Text
        - MdLevel8 (number): Text
        - MdName1 (str): Network Address Step Value.
        - MdName2 (str): Network Address Step Value.
        - MdName3 (str): Network Address Step Value.
        - MdName4 (str): Network Address Step Value.
        - MdName5 (str): Network Address Step Value.
        - MdName6 (str): Network Address Step Value.
        - MdName7 (str): Network Address Step Value.
        - MdName8 (str): Network Address Step Value.
        - MdNameFormat1 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat2 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat3 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat4 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat5 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat6 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat7 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - MdNameFormat8 (str(mdNameFormatNoMaintenanceDomainName | mdNameFormatDomainNameBasedStr | mdNameFormatMacPlusTwoOctetInt | mdNameFormatCharacterStr)): Text
        - NumMDLevels (number): Import only the best routes (provided route file has this information).

        Returns
        -------
        - self: This instance with matching configMDLevelsParams resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of configMDLevelsParams data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the configMDLevelsParams resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def ConfigMDLevels(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the configMDLevels operation on the server.

        Import IPv6 routes from standard route file. Supported format - Cisco IOS, Juniper JUNOS, Classis Ixia (.csv) and standard CSV.

        configMDLevels(async_operation=bool)
        ------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("configMDLevels", payload=payload, response_object=None)
