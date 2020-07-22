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


class EventNotificationLearnedInfo(Base):
    """
    The EventNotificationLearnedInfo class encapsulates a list of eventNotificationLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the EventNotificationLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'eventNotificationLearnedInfo'
    _SDM_ATT_MAP = {
        'LocalFrameErrorRunningTotal': 'localFrameErrorRunningTotal',
        'LocalFrameEventRunningTotal': 'localFrameEventRunningTotal',
        'LocalFramePeriodErrorRunningTotal': 'localFramePeriodErrorRunningTotal',
        'LocalFramePeriodEventRunningTotal': 'localFramePeriodEventRunningTotal',
        'LocalFrameSecSumErrorRunningTotal': 'localFrameSecSumErrorRunningTotal',
        'LocalFrameSecSumEventRunningTotal': 'localFrameSecSumEventRunningTotal',
        'LocalSymbolPeriodErrorRunningTotal': 'localSymbolPeriodErrorRunningTotal',
        'LocalSymbolPeriodEventRunningTotal': 'localSymbolPeriodEventRunningTotal',
        'RemoteFrameError': 'remoteFrameError',
        'RemoteFrameErrorRunningTotal': 'remoteFrameErrorRunningTotal',
        'RemoteFrameEventRunningTotal': 'remoteFrameEventRunningTotal',
        'RemoteFramePeriodError': 'remoteFramePeriodError',
        'RemoteFramePeriodErrorRunningTotal': 'remoteFramePeriodErrorRunningTotal',
        'RemoteFramePeriodEventRunningTotal': 'remoteFramePeriodEventRunningTotal',
        'RemoteFramePeriodThreshold': 'remoteFramePeriodThreshold',
        'RemoteFramePeriodWindow': 'remoteFramePeriodWindow',
        'RemoteFrameSecSumError': 'remoteFrameSecSumError',
        'RemoteFrameSecSumErrorRunningTotal': 'remoteFrameSecSumErrorRunningTotal',
        'RemoteFrameSecSumEventRunningTotal': 'remoteFrameSecSumEventRunningTotal',
        'RemoteFrameSecSumThreshold': 'remoteFrameSecSumThreshold',
        'RemoteFrameSecSumWindow': 'remoteFrameSecSumWindow',
        'RemoteFrameThreshold': 'remoteFrameThreshold',
        'RemoteFrameWindow': 'remoteFrameWindow',
        'RemoteSymbolPeriodErrorRunningTotal': 'remoteSymbolPeriodErrorRunningTotal',
        'RemoteSymbolPeriodErrors': 'remoteSymbolPeriodErrors',
        'RemoteSymbolPeriodEventRunningTotal': 'remoteSymbolPeriodEventRunningTotal',
        'RemoteSymbolPeriodThreshold': 'remoteSymbolPeriodThreshold',
        'RemoteSymbolPeriodWindow': 'remoteSymbolPeriodWindow',
    }

    def __init__(self, parent):
        super(EventNotificationLearnedInfo, self).__init__(parent)

    @property
    def LocalFrameErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalFrameErrorRunningTotal'])

    @property
    def LocalFrameEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalFrameEventRunningTotal'])

    @property
    def LocalFramePeriodErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalFramePeriodErrorRunningTotal'])

    @property
    def LocalFramePeriodEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalFramePeriodEventRunningTotal'])

    @property
    def LocalFrameSecSumErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalFrameSecSumErrorRunningTotal'])

    @property
    def LocalFrameSecSumEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalFrameSecSumEventRunningTotal'])

    @property
    def LocalSymbolPeriodErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalSymbolPeriodErrorRunningTotal'])

    @property
    def LocalSymbolPeriodEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalSymbolPeriodEventRunningTotal'])

    @property
    def RemoteFrameError(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameError'])

    @property
    def RemoteFrameErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameErrorRunningTotal'])

    @property
    def RemoteFrameEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameEventRunningTotal'])

    @property
    def RemoteFramePeriodError(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFramePeriodError'])

    @property
    def RemoteFramePeriodErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFramePeriodErrorRunningTotal'])

    @property
    def RemoteFramePeriodEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFramePeriodEventRunningTotal'])

    @property
    def RemoteFramePeriodThreshold(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFramePeriodThreshold'])

    @property
    def RemoteFramePeriodWindow(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFramePeriodWindow'])

    @property
    def RemoteFrameSecSumError(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameSecSumError'])

    @property
    def RemoteFrameSecSumErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameSecSumErrorRunningTotal'])

    @property
    def RemoteFrameSecSumEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameSecSumEventRunningTotal'])

    @property
    def RemoteFrameSecSumThreshold(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameSecSumThreshold'])

    @property
    def RemoteFrameSecSumWindow(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameSecSumWindow'])

    @property
    def RemoteFrameThreshold(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameThreshold'])

    @property
    def RemoteFrameWindow(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteFrameWindow'])

    @property
    def RemoteSymbolPeriodErrorRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSymbolPeriodErrorRunningTotal'])

    @property
    def RemoteSymbolPeriodErrors(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSymbolPeriodErrors'])

    @property
    def RemoteSymbolPeriodEventRunningTotal(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSymbolPeriodEventRunningTotal'])

    @property
    def RemoteSymbolPeriodThreshold(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSymbolPeriodThreshold'])

    @property
    def RemoteSymbolPeriodWindow(self):
        """
        Returns
        -------
        - number: 
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteSymbolPeriodWindow'])

    def find(self, LocalFrameErrorRunningTotal=None, LocalFrameEventRunningTotal=None, LocalFramePeriodErrorRunningTotal=None, LocalFramePeriodEventRunningTotal=None, LocalFrameSecSumErrorRunningTotal=None, LocalFrameSecSumEventRunningTotal=None, LocalSymbolPeriodErrorRunningTotal=None, LocalSymbolPeriodEventRunningTotal=None, RemoteFrameError=None, RemoteFrameErrorRunningTotal=None, RemoteFrameEventRunningTotal=None, RemoteFramePeriodError=None, RemoteFramePeriodErrorRunningTotal=None, RemoteFramePeriodEventRunningTotal=None, RemoteFramePeriodThreshold=None, RemoteFramePeriodWindow=None, RemoteFrameSecSumError=None, RemoteFrameSecSumErrorRunningTotal=None, RemoteFrameSecSumEventRunningTotal=None, RemoteFrameSecSumThreshold=None, RemoteFrameSecSumWindow=None, RemoteFrameThreshold=None, RemoteFrameWindow=None, RemoteSymbolPeriodErrorRunningTotal=None, RemoteSymbolPeriodErrors=None, RemoteSymbolPeriodEventRunningTotal=None, RemoteSymbolPeriodThreshold=None, RemoteSymbolPeriodWindow=None):
        """Finds and retrieves eventNotificationLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eventNotificationLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eventNotificationLearnedInfo resources from the server.

        Args
        ----
        - LocalFrameErrorRunningTotal (number): 
        - LocalFrameEventRunningTotal (number): 
        - LocalFramePeriodErrorRunningTotal (number): 
        - LocalFramePeriodEventRunningTotal (number): 
        - LocalFrameSecSumErrorRunningTotal (number): 
        - LocalFrameSecSumEventRunningTotal (number): 
        - LocalSymbolPeriodErrorRunningTotal (number): 
        - LocalSymbolPeriodEventRunningTotal (number): 
        - RemoteFrameError (number): 
        - RemoteFrameErrorRunningTotal (number): 
        - RemoteFrameEventRunningTotal (number): 
        - RemoteFramePeriodError (number): 
        - RemoteFramePeriodErrorRunningTotal (number): 
        - RemoteFramePeriodEventRunningTotal (number): 
        - RemoteFramePeriodThreshold (number): 
        - RemoteFramePeriodWindow (number): 
        - RemoteFrameSecSumError (number): 
        - RemoteFrameSecSumErrorRunningTotal (number): 
        - RemoteFrameSecSumEventRunningTotal (number): 
        - RemoteFrameSecSumThreshold (number): 
        - RemoteFrameSecSumWindow (number): 
        - RemoteFrameThreshold (number): 
        - RemoteFrameWindow (number): 
        - RemoteSymbolPeriodErrorRunningTotal (number): 
        - RemoteSymbolPeriodErrors (number): 
        - RemoteSymbolPeriodEventRunningTotal (number): 
        - RemoteSymbolPeriodThreshold (number): 
        - RemoteSymbolPeriodWindow (number): 

        Returns
        -------
        - self: This instance with matching eventNotificationLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eventNotificationLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eventNotificationLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
