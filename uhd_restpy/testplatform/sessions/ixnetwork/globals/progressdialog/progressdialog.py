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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class ProgressDialog(Base):
    """
    The ProgressDialog class encapsulates a required progressDialog resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'progressDialog'
    _SDM_ATT_MAP = {
        'ElapsedDuration': 'elapsedDuration',
        'EstimatedDuration': 'estimatedDuration',
        'IsOpen': 'isOpen',
        'Progress': 'progress',
        'RemainingDuration': 'remainingDuration',
        'TaskName': 'taskName',
        'Title': 'title',
    }

    def __init__(self, parent):
        super(ProgressDialog, self).__init__(parent)

    @property
    def ElapsedDuration(self):
        """
        Returns
        -------
        - str: Elapsed time since the start of the Progress operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ElapsedDuration'])

    @property
    def EstimatedDuration(self):
        """
        Returns
        -------
        - str: Estimated time to complete the Progress operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EstimatedDuration'])

    @property
    def IsOpen(self):
        """
        Returns
        -------
        - bool: Indicates whether any progress bar is open.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IsOpen'])

    @property
    def Progress(self):
        """
        Returns
        -------
        - number: A progress update from 0(start) to 1(end) (Not all progress bars may have a progress update).
        """
        return self._get_attribute(self._SDM_ATT_MAP['Progress'])

    @property
    def RemainingDuration(self):
        """
        Returns
        -------
        - str: Remaining time of the Progress operation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemainingDuration'])

    @property
    def TaskName(self):
        """
        Returns
        -------
        - str: Sub Task name belonging to the Progress bar.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TaskName'])

    @property
    def Title(self):
        """
        Returns
        -------
        - str: Title or Group name of the Progress bar.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Title'])
