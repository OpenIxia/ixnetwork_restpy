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


class LinkTlv(Base):
    """
    The LinkTlv class encapsulates a list of linkTlv resources that are managed by the system.
    A list of resources can be retrieved from the server using the LinkTlv.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'linkTlv'
    _SDM_ATT_MAP = {
        'EnableLinkId': 'enableLinkId',
        'EnableLinkMetric': 'enableLinkMetric',
        'EnableLinkResourceClass': 'enableLinkResourceClass',
        'EnableLinkType': 'enableLinkType',
        'EnableLocalIpAddress': 'enableLocalIpAddress',
        'EnableMaxBandwidth': 'enableMaxBandwidth',
        'EnableMaxResBandwidth': 'enableMaxResBandwidth',
        'EnableRemoteIpAddress': 'enableRemoteIpAddress',
        'EnableUnreservedBandwidth': 'enableUnreservedBandwidth',
        'LinkId': 'linkId',
        'LinkLocalIpAddress': 'linkLocalIpAddress',
        'LinkMetric': 'linkMetric',
        'LinkRemoteIpAddress': 'linkRemoteIpAddress',
        'LinkResourceClass': 'linkResourceClass',
        'LinkType': 'linkType',
        'LinkUnreservedBandwidth': 'linkUnreservedBandwidth',
        'MaxBandwidth': 'maxBandwidth',
        'MaxResBandwidth': 'maxResBandwidth',
        'SubTlvs': 'subTlvs',
    }

    def __init__(self, parent):
        super(LinkTlv, self).__init__(parent)

    @property
    def EnableLinkId(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkId'])
    @EnableLinkId.setter
    def EnableLinkId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkId'], value)

    @property
    def EnableLinkMetric(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkMetric'])
    @EnableLinkMetric.setter
    def EnableLinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkMetric'], value)

    @property
    def EnableLinkResourceClass(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkResourceClass'])
    @EnableLinkResourceClass.setter
    def EnableLinkResourceClass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkResourceClass'], value)

    @property
    def EnableLinkType(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLinkType'])
    @EnableLinkType.setter
    def EnableLinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLinkType'], value)

    @property
    def EnableLocalIpAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableLocalIpAddress'])
    @EnableLocalIpAddress.setter
    def EnableLocalIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableLocalIpAddress'], value)

    @property
    def EnableMaxBandwidth(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMaxBandwidth'])
    @EnableMaxBandwidth.setter
    def EnableMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMaxBandwidth'], value)

    @property
    def EnableMaxResBandwidth(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMaxResBandwidth'])
    @EnableMaxResBandwidth.setter
    def EnableMaxResBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMaxResBandwidth'], value)

    @property
    def EnableRemoteIpAddress(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRemoteIpAddress'])
    @EnableRemoteIpAddress.setter
    def EnableRemoteIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRemoteIpAddress'], value)

    @property
    def EnableUnreservedBandwidth(self):
        """
        Returns
        -------
        - bool: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableUnreservedBandwidth'])
    @EnableUnreservedBandwidth.setter
    def EnableUnreservedBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableUnreservedBandwidth'], value)

    @property
    def LinkId(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkId'])
    @LinkId.setter
    def LinkId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkId'], value)

    @property
    def LinkLocalIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkLocalIpAddress'])
    @LinkLocalIpAddress.setter
    def LinkLocalIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkLocalIpAddress'], value)

    @property
    def LinkMetric(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMetric'], value)

    @property
    def LinkRemoteIpAddress(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkRemoteIpAddress'])
    @LinkRemoteIpAddress.setter
    def LinkRemoteIpAddress(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkRemoteIpAddress'], value)

    @property
    def LinkResourceClass(self):
        """
        Returns
        -------
        - str: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkResourceClass'])
    @LinkResourceClass.setter
    def LinkResourceClass(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkResourceClass'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(pointToPoint | multiaccess): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkType'], value)

    @property
    def LinkUnreservedBandwidth(self):
        """
        Returns
        -------
        - list(number): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkUnreservedBandwidth'])
    @LinkUnreservedBandwidth.setter
    def LinkUnreservedBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkUnreservedBandwidth'], value)

    @property
    def MaxBandwidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxBandwidth'])
    @MaxBandwidth.setter
    def MaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxBandwidth'], value)

    @property
    def MaxResBandwidth(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxResBandwidth'])
    @MaxResBandwidth.setter
    def MaxResBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxResBandwidth'], value)

    @property
    def SubTlvs(self):
        """
        Returns
        -------
        - list(dict(arg1:str,arg2:number,arg3:number)): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['SubTlvs'])
    @SubTlvs.setter
    def SubTlvs(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SubTlvs'], value)

    def update(self, EnableLinkId=None, EnableLinkMetric=None, EnableLinkResourceClass=None, EnableLinkType=None, EnableLocalIpAddress=None, EnableMaxBandwidth=None, EnableMaxResBandwidth=None, EnableRemoteIpAddress=None, EnableUnreservedBandwidth=None, LinkId=None, LinkLocalIpAddress=None, LinkMetric=None, LinkRemoteIpAddress=None, LinkResourceClass=None, LinkType=None, LinkUnreservedBandwidth=None, MaxBandwidth=None, MaxResBandwidth=None, SubTlvs=None):
        """Updates linkTlv resource on the server.

        Args
        ----
        - EnableLinkId (bool): 
        - EnableLinkMetric (bool): 
        - EnableLinkResourceClass (bool): 
        - EnableLinkType (bool): 
        - EnableLocalIpAddress (bool): 
        - EnableMaxBandwidth (bool): 
        - EnableMaxResBandwidth (bool): 
        - EnableRemoteIpAddress (bool): 
        - EnableUnreservedBandwidth (bool): 
        - LinkId (str): 
        - LinkLocalIpAddress (str): 
        - LinkMetric (number): 
        - LinkRemoteIpAddress (str): 
        - LinkResourceClass (str): 
        - LinkType (str(pointToPoint | multiaccess)): 
        - LinkUnreservedBandwidth (list(number)): 
        - MaxBandwidth (number): 
        - MaxResBandwidth (number): 
        - SubTlvs (list(dict(arg1:str,arg2:number,arg3:number))): 

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, EnableLinkId=None, EnableLinkMetric=None, EnableLinkResourceClass=None, EnableLinkType=None, EnableLocalIpAddress=None, EnableMaxBandwidth=None, EnableMaxResBandwidth=None, EnableRemoteIpAddress=None, EnableUnreservedBandwidth=None, LinkId=None, LinkLocalIpAddress=None, LinkMetric=None, LinkRemoteIpAddress=None, LinkResourceClass=None, LinkType=None, LinkUnreservedBandwidth=None, MaxBandwidth=None, MaxResBandwidth=None, SubTlvs=None):
        """Finds and retrieves linkTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve linkTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all linkTlv resources from the server.

        Args
        ----
        - EnableLinkId (bool): 
        - EnableLinkMetric (bool): 
        - EnableLinkResourceClass (bool): 
        - EnableLinkType (bool): 
        - EnableLocalIpAddress (bool): 
        - EnableMaxBandwidth (bool): 
        - EnableMaxResBandwidth (bool): 
        - EnableRemoteIpAddress (bool): 
        - EnableUnreservedBandwidth (bool): 
        - LinkId (str): 
        - LinkLocalIpAddress (str): 
        - LinkMetric (number): 
        - LinkRemoteIpAddress (str): 
        - LinkResourceClass (str): 
        - LinkType (str(pointToPoint | multiaccess)): 
        - LinkUnreservedBandwidth (list(number)): 
        - MaxBandwidth (number): 
        - MaxResBandwidth (number): 
        - SubTlvs (list(dict(arg1:str,arg2:number,arg3:number))): 

        Returns
        -------
        - self: This instance with matching linkTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of linkTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the linkTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
