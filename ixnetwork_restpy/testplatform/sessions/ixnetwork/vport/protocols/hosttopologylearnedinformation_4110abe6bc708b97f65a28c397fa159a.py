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
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files
from typing import List, Any, Union


class HostTopologyLearnedInformation(Base):
    """NOT DEFINED
    The HostTopologyLearnedInformation class encapsulates a required hostTopologyLearnedInformation resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'hostTopologyLearnedInformation'
    _SDM_ATT_MAP = {
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(HostTopologyLearnedInformation, self).__init__(parent, list_op)

    @property
    def SwitchHostRangeLearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfo_c3ff6e8f58c97b1b0d4885ef2523cc50.SwitchHostRangeLearnedInfo): An instance of the SwitchHostRangeLearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfo_c3ff6e8f58c97b1b0d4885ef2523cc50 import SwitchHostRangeLearnedInfo
        if self._properties.get('SwitchHostRangeLearnedInfo', None) is not None:
            return self._properties.get('SwitchHostRangeLearnedInfo')
        else:
            return SwitchHostRangeLearnedInfo(self)

    @property
    def SwitchHostRangeLearnedInfoTriggerAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfotriggerattributes_970cca4f196b63ea57bce8499441fe35.SwitchHostRangeLearnedInfoTriggerAttributes): An instance of the SwitchHostRangeLearnedInfoTriggerAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchhostrangelearnedinfotriggerattributes_970cca4f196b63ea57bce8499441fe35 import SwitchHostRangeLearnedInfoTriggerAttributes
        if self._properties.get('SwitchHostRangeLearnedInfoTriggerAttributes', None) is not None:
            return self._properties.get('SwitchHostRangeLearnedInfoTriggerAttributes')
        else:
            return SwitchHostRangeLearnedInfoTriggerAttributes(self)._select()

    def RefreshHostRangeLearnedInformation(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[bool, None]
        """Executes the refreshHostRangeLearnedInformation operation on the server.

        NOT DEFINED

        refreshHostRangeLearnedInformation(async_operation=bool)bool
        ------------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns bool: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('refreshHostRangeLearnedInformation', payload=payload, response_object=None)
