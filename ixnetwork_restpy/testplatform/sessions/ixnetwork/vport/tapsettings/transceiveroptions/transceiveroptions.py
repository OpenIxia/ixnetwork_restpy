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


class TransceiverOptions(Base):
    """
    The TransceiverOptions class encapsulates a required transceiverOptions resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "transceiverOptions"
    _SDM_ATT_MAP = {
        "ConfigStatus": "configStatus",
        "Connector": "connector",
        "CurrentAppSel": "currentAppSel",
        "FormFactor": "formFactor",
        "HostSpeed": "hostSpeed",
        "MediaTech": "mediaTech",
        "MediaType": "mediaType",
        "ModuleMedia": "moduleMedia",
        "ReqAppSel": "reqAppSel",
        "TransceiverVendor": "transceiverVendor",
    }
    _SDM_ENUM_MAP = {
        "reqAppSel": [
            "moduleDefault",
            "auto",
            "appSel1",
            "appSel2",
            "appSel3",
            "appSel4",
            "appSel5",
            "appSel6",
            "appSel7",
            "appSel8",
            "appSel9",
            "appSel10",
            "appSel11",
            "appSel12",
            "appSel13",
            "appSel14",
            "appSel15",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(TransceiverOptions, self).__init__(parent, list_op)

    @property
    def AppselMatch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.transceiveroptions.appselmatch.appselmatch.AppselMatch): An instance of the AppselMatch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.transceiveroptions.appselmatch.appselmatch import (
            AppselMatch,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AppselMatch", None) is not None:
                return self._properties.get("AppselMatch")
        return AppselMatch(self)

    @property
    def AvailableApplications(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.transceiveroptions.availableapplications.availableapplications.AvailableApplications): An instance of the AvailableApplications class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.tapsettings.transceiveroptions.availableapplications.availableapplications import (
            AvailableApplications,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("AvailableApplications", None) is not None:
                return self._properties.get("AvailableApplications")
        return AvailableApplications(self)

    @property
    def ConfigStatus(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Config Status.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConfigStatus"])

    @property
    def Connector(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Connector.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Connector"])

    @property
    def CurrentAppSel(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Current AppSel value.
        """
        return self._get_attribute(self._SDM_ATT_MAP["CurrentAppSel"])

    @property
    def FormFactor(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver Form Factor.
        """
        return self._get_attribute(self._SDM_ATT_MAP["FormFactor"])

    @property
    def HostSpeed(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Host Speed.
        """
        return self._get_attribute(self._SDM_ATT_MAP["HostSpeed"])

    @property
    def MediaTech(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver Media Tech.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaTech"])

    @property
    def MediaType(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver Media Type.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MediaType"])

    @property
    def ModuleMedia(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Module Media.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ModuleMedia"])

    @property
    def ReqAppSel(self):
        # type: () -> str
        """
        Returns
        -------
        - str(moduleDefault | auto | appSel1 | appSel2 | appSel3 | appSel4 | appSel5 | appSel6 | appSel7 | appSel8 | appSel9 | appSel10 | appSel11 | appSel12 | appSel13 | appSel14 | appSel15): The appsel to be applied on transceiver.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ReqAppSel"])

    @ReqAppSel.setter
    def ReqAppSel(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["ReqAppSel"], value)

    @property
    def TransceiverVendor(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Transceiver Vendor Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP["TransceiverVendor"])

    def update(self, ReqAppSel=None):
        # type: (str) -> TransceiverOptions
        """Updates transceiverOptions resource on the server.

        Args
        ----
        - ReqAppSel (str(moduleDefault | auto | appSel1 | appSel2 | appSel3 | appSel4 | appSel5 | appSel6 | appSel7 | appSel8 | appSel9 | appSel10 | appSel11 | appSel12 | appSel13 | appSel14 | appSel15)): The appsel to be applied on transceiver.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        ConfigStatus=None,
        Connector=None,
        CurrentAppSel=None,
        FormFactor=None,
        HostSpeed=None,
        MediaTech=None,
        MediaType=None,
        ModuleMedia=None,
        ReqAppSel=None,
        TransceiverVendor=None,
    ):
        # type: (str, str, str, str, str, str, str, str, str, str) -> TransceiverOptions
        """Finds and retrieves transceiverOptions resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve transceiverOptions resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all transceiverOptions resources from the server.

        Args
        ----
        - ConfigStatus (str): Config Status.
        - Connector (str): Connector.
        - CurrentAppSel (str): Current AppSel value.
        - FormFactor (str): Transceiver Form Factor.
        - HostSpeed (str): Host Speed.
        - MediaTech (str): Transceiver Media Tech.
        - MediaType (str): Transceiver Media Type.
        - ModuleMedia (str): Module Media.
        - ReqAppSel (str(moduleDefault | auto | appSel1 | appSel2 | appSel3 | appSel4 | appSel5 | appSel6 | appSel7 | appSel8 | appSel9 | appSel10 | appSel11 | appSel12 | appSel13 | appSel14 | appSel15)): The appsel to be applied on transceiver.
        - TransceiverVendor (str): Transceiver Vendor Name.

        Returns
        -------
        - self: This instance with matching transceiverOptions resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of transceiverOptions data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the transceiverOptions resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
