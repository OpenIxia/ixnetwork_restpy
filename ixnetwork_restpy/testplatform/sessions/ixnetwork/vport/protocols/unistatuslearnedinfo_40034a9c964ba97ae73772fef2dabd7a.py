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


class UniStatusLearnedInfo(Base):
    """It signifies the status learned info for UNI.
    The UniStatusLearnedInfo class encapsulates a list of uniStatusLearnedInfo resources that are managed by the system.
    A list of resources can be retrieved from the server using the UniStatusLearnedInfo.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'uniStatusLearnedInfo'
    _SDM_ATT_MAP = {
        'CbsMagnitude': 'cbsMagnitude',
        'CbsMultiplier': 'cbsMultiplier',
        'Cf': 'cf',
        'CirMagnitude': 'cirMagnitude',
        'CirMultiplier': 'cirMultiplier',
        'Cm': 'cm',
        'EbsMagnitude': 'ebsMagnitude',
        'EbsMultiplier': 'ebsMultiplier',
        'EirMagnitude': 'eirMagnitude',
        'EirMultiplier': 'eirMultiplier',
        'EvcMapType': 'evcMapType',
        'PerCos': 'perCos',
        'UniId': 'uniId',
        'UniIdLength': 'uniIdLength',
        'UserPriorityBits000': 'userPriorityBits000',
        'UserPriorityBits001': 'userPriorityBits001',
        'UserPriorityBits010': 'userPriorityBits010',
        'UserPriorityBits011': 'userPriorityBits011',
        'UserPriorityBits100': 'userPriorityBits100',
        'UserPriorityBits101': 'userPriorityBits101',
        'UserPriorityBits110': 'userPriorityBits110',
        'UserPriorityBits111': 'userPriorityBits111',
    }

    def __init__(self, parent):
        super(UniStatusLearnedInfo, self).__init__(parent)

    @property
    def CbsMagnitude(self):
        """
        Returns
        -------
        - str: It signifies one octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CbsMagnitude'])

    @property
    def CbsMultiplier(self):
        """
        Returns
        -------
        - str: It signifies one octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CbsMultiplier'])

    @property
    def Cf(self):
        """
        Returns
        -------
        - str: It signifies coupling flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cf'])

    @property
    def CirMagnitude(self):
        """
        Returns
        -------
        - str: It signifies one octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CirMagnitude'])

    @property
    def CirMultiplier(self):
        """
        Returns
        -------
        - str: It signifies two octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CirMultiplier'])

    @property
    def Cm(self):
        """
        Returns
        -------
        - str: It signifies color mode flag.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cm'])

    @property
    def EbsMagnitude(self):
        """
        Returns
        -------
        - str: It signifies one octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EbsMagnitude'])

    @property
    def EbsMultiplier(self):
        """
        Returns
        -------
        - str: It signifies one octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EbsMultiplier'])

    @property
    def EirMagnitude(self):
        """
        Returns
        -------
        - str: It signifies one octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EirMagnitude'])

    @property
    def EirMultiplier(self):
        """
        Returns
        -------
        - str: It signifies two octet field.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EirMultiplier'])

    @property
    def EvcMapType(self):
        """
        Returns
        -------
        - str: It signifies the type of EVC MAP type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EvcMapType'])

    @property
    def PerCos(self):
        """
        Returns
        -------
        - str: It signifies per cos behavior of bandwidth profile.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PerCos'])

    @property
    def UniId(self):
        """
        Returns
        -------
        - str: It signifies the ID of user network interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UniId'])

    @property
    def UniIdLength(self):
        """
        Returns
        -------
        - number: It signifies the length of the UNI ID value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UniIdLength'])

    @property
    def UserPriorityBits000(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 000 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits000'])

    @property
    def UserPriorityBits001(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 001 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits001'])

    @property
    def UserPriorityBits010(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 010 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits010'])

    @property
    def UserPriorityBits011(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 011 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits011'])

    @property
    def UserPriorityBits100(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 100 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits100'])

    @property
    def UserPriorityBits101(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 101 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits101'])

    @property
    def UserPriorityBits110(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 110 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits110'])

    @property
    def UserPriorityBits111(self):
        """
        Returns
        -------
        - str: If enabled, Bandwidth Profile applies to frames with user_priority as 111 and the value is set to 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UserPriorityBits111'])

    def find(self, CbsMagnitude=None, CbsMultiplier=None, Cf=None, CirMagnitude=None, CirMultiplier=None, Cm=None, EbsMagnitude=None, EbsMultiplier=None, EirMagnitude=None, EirMultiplier=None, EvcMapType=None, PerCos=None, UniId=None, UniIdLength=None, UserPriorityBits000=None, UserPriorityBits001=None, UserPriorityBits010=None, UserPriorityBits011=None, UserPriorityBits100=None, UserPriorityBits101=None, UserPriorityBits110=None, UserPriorityBits111=None):
        """Finds and retrieves uniStatusLearnedInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve uniStatusLearnedInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all uniStatusLearnedInfo resources from the server.

        Args
        ----
        - CbsMagnitude (str): It signifies one octet field.
        - CbsMultiplier (str): It signifies one octet field.
        - Cf (str): It signifies coupling flag.
        - CirMagnitude (str): It signifies one octet field.
        - CirMultiplier (str): It signifies two octet field.
        - Cm (str): It signifies color mode flag.
        - EbsMagnitude (str): It signifies one octet field.
        - EbsMultiplier (str): It signifies one octet field.
        - EirMagnitude (str): It signifies one octet field.
        - EirMultiplier (str): It signifies two octet field.
        - EvcMapType (str): It signifies the type of EVC MAP type.
        - PerCos (str): It signifies per cos behavior of bandwidth profile.
        - UniId (str): It signifies the ID of user network interface.
        - UniIdLength (number): It signifies the length of the UNI ID value.
        - UserPriorityBits000 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 000 and the value is set to 1.
        - UserPriorityBits001 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 001 and the value is set to 1.
        - UserPriorityBits010 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 010 and the value is set to 1.
        - UserPriorityBits011 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 011 and the value is set to 1.
        - UserPriorityBits100 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 100 and the value is set to 1.
        - UserPriorityBits101 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 101 and the value is set to 1.
        - UserPriorityBits110 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 110 and the value is set to 1.
        - UserPriorityBits111 (str): If enabled, Bandwidth Profile applies to frames with user_priority as 111 and the value is set to 1.

        Returns
        -------
        - self: This instance with matching uniStatusLearnedInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of uniStatusLearnedInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the uniStatusLearnedInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
