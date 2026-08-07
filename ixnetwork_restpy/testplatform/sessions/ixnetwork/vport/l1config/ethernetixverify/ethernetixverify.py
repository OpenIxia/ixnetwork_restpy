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


class Ethernetixverify(Base):
    """
    The Ethernetixverify class encapsulates a required ethernetixverify resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "ethernetixverify"
    _SDM_ATT_MAP = {
        "AutoInstrumentation": "autoInstrumentation",
        "AvailableSpeeds": "availableSpeeds",
        "CanModifySpeed": "canModifySpeed",
        "CanSetMultipleSpeeds": "canSetMultipleSpeeds",
        "EnablePPM": "enablePPM",
        "Loopback": "loopback",
        "Mtu": "mtu",
        "Ppm": "ppm",
        "PromiscuousMode": "promiscuousMode",
        "SelectedSpeeds": "selectedSpeeds",
        "Speed": "speed",
    }
    _SDM_ENUM_MAP = {
        "autoInstrumentation": ["endOfFrame", "floating"],
        "speed": [
            "speed10",
            "speed100",
            "speed1000",
            "speed100g",
            "speed10g",
            "speed2000",
            "speed200g",
            "speed20g",
            "speed25g",
            "speed3000",
            "speed30g",
            "speed4000",
            "speed400g",
            "speed40g",
            "speed5000",
            "speed50g",
            "speed6000",
            "speed60g",
            "speed7000",
            "speed70g",
            "speed8000",
            "speed80g",
            "speed9000",
            "speed90g",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(Ethernetixverify, self).__init__(parent, list_op)

    @property
    def Fcoe(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetixverify.fcoe.fcoe.Fcoe): An instance of the Fcoe class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.l1config.ethernetixverify.fcoe.fcoe import (
            Fcoe,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("Fcoe", None) is not None:
                return self._properties.get("Fcoe")
        return Fcoe(self)._select()

    @property
    def AutoInstrumentation(self):
        # type: () -> str
        """
        Returns
        -------
        - str(endOfFrame | floating):
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoInstrumentation"])

    @AutoInstrumentation.setter
    def AutoInstrumentation(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoInstrumentation"], value)

    @property
    def AvailableSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed200g | speed400g | speed1000 | speed2000 | speed3000 | speed4000 | speed5000 | speed6000 | speed7000 | speed8000 | speed9000 | speed10g | speed20g | speed30g | speed40g | speed100 | speed60g | speed70g | speed80g | speed90g | speed10]): Which speeds are available for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AvailableSpeeds"])

    @property
    def CanModifySpeed(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Returns true/false depending upon if the port can change speed for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanModifySpeed"])

    @property
    def CanSetMultipleSpeeds(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Can this port selectmultiple speeds for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CanSetMultipleSpeeds"])

    @property
    def EnablePPM(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["EnablePPM"])

    @property
    def Loopback(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Loopback"])

    @Loopback.setter
    def Loopback(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Loopback"], value)

    @property
    def Mtu(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Mtu"])

    @Mtu.setter
    def Mtu(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Mtu"], value)

    @property
    def Ppm(self):
        # type: () -> int
        """
        Returns
        -------
        - number:
        """
        return self._get_attribute(self._SDM_ATT_MAP["Ppm"])

    @property
    def PromiscuousMode(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool:
        """
        return self._get_attribute(self._SDM_ATT_MAP["PromiscuousMode"])

    @PromiscuousMode.setter
    def PromiscuousMode(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["PromiscuousMode"], value)

    @property
    def SelectedSpeeds(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[speed100g | speed25g | speed50g | speed200g | speed400g | speed1000 | speed2000 | speed3000 | speed4000 | speed5000 | speed6000 | speed7000 | speed8000 | speed9000 | speed10g | speed20g | speed30g | speed40g | speed100 | speed60g | speed70g | speed80g | speed90g | speed10]): Which speeds are selected for the current media and AN settings.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SelectedSpeeds"])

    @SelectedSpeeds.setter
    def SelectedSpeeds(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["SelectedSpeeds"], value)

    @property
    def Speed(self):
        # type: () -> str
        """
        Returns
        -------
        - str(speed10 | speed100 | speed1000 | speed100g | speed10g | speed2000 | speed200g | speed20g | speed25g | speed3000 | speed30g | speed4000 | speed400g | speed40g | speed5000 | speed50g | speed6000 | speed60g | speed7000 | speed70g | speed8000 | speed80g | speed9000 | speed90g):
        """
        return self._get_attribute(self._SDM_ATT_MAP["Speed"])

    @Speed.setter
    def Speed(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Speed"], value)

    def update(
        self,
        AutoInstrumentation=None,
        Loopback=None,
        Mtu=None,
        PromiscuousMode=None,
        SelectedSpeeds=None,
        Speed=None,
    ):
        # type: (str, bool, int, bool, List[str], str) -> Ethernetixverify
        """Updates ethernetixverify resource on the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)):
        - Loopback (bool):
        - Mtu (number):
        - PromiscuousMode (bool):
        - SelectedSpeeds (list(str[speed100g | speed25g | speed50g | speed200g | speed400g | speed1000 | speed2000 | speed3000 | speed4000 | speed5000 | speed6000 | speed7000 | speed8000 | speed9000 | speed10g | speed20g | speed30g | speed40g | speed100 | speed60g | speed70g | speed80g | speed90g | speed10])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed10 | speed100 | speed1000 | speed100g | speed10g | speed2000 | speed200g | speed20g | speed25g | speed3000 | speed30g | speed4000 | speed400g | speed40g | speed5000 | speed50g | speed6000 | speed60g | speed7000 | speed70g | speed8000 | speed80g | speed9000 | speed90g)):

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        AutoInstrumentation=None,
        AvailableSpeeds=None,
        CanModifySpeed=None,
        CanSetMultipleSpeeds=None,
        EnablePPM=None,
        Loopback=None,
        Mtu=None,
        Ppm=None,
        PromiscuousMode=None,
        SelectedSpeeds=None,
        Speed=None,
    ):
        # type: (str, List[str], bool, bool, bool, bool, int, int, bool, List[str], str) -> Ethernetixverify
        """Finds and retrieves ethernetixverify resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ethernetixverify resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ethernetixverify resources from the server.

        Args
        ----
        - AutoInstrumentation (str(endOfFrame | floating)):
        - AvailableSpeeds (list(str[speed100g | speed25g | speed50g | speed200g | speed400g | speed1000 | speed2000 | speed3000 | speed4000 | speed5000 | speed6000 | speed7000 | speed8000 | speed9000 | speed10g | speed20g | speed30g | speed40g | speed100 | speed60g | speed70g | speed80g | speed90g | speed10])): Which speeds are available for the current media and AN settings.
        - CanModifySpeed (bool): Returns true/false depending upon if the port can change speed for the current media and AN settings.
        - CanSetMultipleSpeeds (bool): Can this port selectmultiple speeds for the current media and AN settings.
        - EnablePPM (bool):
        - Loopback (bool):
        - Mtu (number):
        - Ppm (number):
        - PromiscuousMode (bool):
        - SelectedSpeeds (list(str[speed100g | speed25g | speed50g | speed200g | speed400g | speed1000 | speed2000 | speed3000 | speed4000 | speed5000 | speed6000 | speed7000 | speed8000 | speed9000 | speed10g | speed20g | speed30g | speed40g | speed100 | speed60g | speed70g | speed80g | speed90g | speed10])): Which speeds are selected for the current media and AN settings.
        - Speed (str(speed10 | speed100 | speed1000 | speed100g | speed10g | speed2000 | speed200g | speed20g | speed25g | speed3000 | speed30g | speed4000 | speed400g | speed40g | speed5000 | speed50g | speed6000 | speed60g | speed7000 | speed70g | speed8000 | speed80g | speed9000 | speed90g)):

        Returns
        -------
        - self: This instance with matching ethernetixverify resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ethernetixverify data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ethernetixverify resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
