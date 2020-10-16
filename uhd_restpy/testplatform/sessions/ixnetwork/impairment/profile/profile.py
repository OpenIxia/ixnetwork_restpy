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


class Profile(Base):
    """List of impairment profiles.  For each incoming packet, apply the highest-priority profile which matches.
    The Profile class encapsulates a list of profile resources that are managed by the user.
    A list of resources can be retrieved from the server using the Profile.find() method.
    The list can be managed by using the Profile.add() and Profile.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'profile'
    _SDM_ATT_MAP = {
        'Links__': '__links__',
        'AllLinks': 'allLinks',
        'Enabled': 'enabled',
        'Name': 'name',
        'Priority': 'priority',
        'ProfileId': 'profileId',
    }

    def __init__(self, parent):
        super(Profile, self).__init__(parent)

    @property
    def AccumulateAndBurst(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.profile.accumulateandburst.accumulateandburst.AccumulateAndBurst): An instance of the AccumulateAndBurst class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.profile.accumulateandburst.accumulateandburst import AccumulateAndBurst
        return AccumulateAndBurst(self)._select()

    @property
    def BitError(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.biterror.biterror.BitError): An instance of the BitError class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.biterror.biterror import BitError
        return BitError(self)._select()

    @property
    def Checksums(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.checksums.checksums.Checksums): An instance of the Checksums class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.checksums.checksums import Checksums
        return Checksums(self)._select()

    @property
    def CustomDelayVariation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.customdelayvariation.customdelayvariation.CustomDelayVariation): An instance of the CustomDelayVariation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.customdelayvariation.customdelayvariation import CustomDelayVariation
        return CustomDelayVariation(self)._select()

    @property
    def Delay(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delay.delay.Delay): An instance of the Delay class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delay.delay import Delay
        return Delay(self)._select()

    @property
    def DelayVariation(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delayvariation.delayvariation.DelayVariation): An instance of the DelayVariation class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.delayvariation.delayvariation import DelayVariation
        return DelayVariation(self)._select()

    @property
    def Drop(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.drop.drop.Drop): An instance of the Drop class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.drop.drop import Drop
        return Drop(self)._select()

    @property
    def Duplicate(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.duplicate.duplicate.Duplicate): An instance of the Duplicate class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.duplicate.duplicate import Duplicate
        return Duplicate(self)._select()

    @property
    def FixedClassifier(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.profile.fixedclassifier.fixedclassifier.FixedClassifier): An instance of the FixedClassifier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.profile.fixedclassifier.fixedclassifier import FixedClassifier
        return FixedClassifier(self)

    @property
    def Modifier(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.modifier.modifier.Modifier): An instance of the Modifier class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.modifier.modifier import Modifier
        return Modifier(self)

    @property
    def Reorder(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.reorder.reorder.Reorder): An instance of the Reorder class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.reorder.reorder import Reorder
        return Reorder(self)._select()

    @property
    def RxRateLimit(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.rxratelimit.rxratelimit.RxRateLimit): An instance of the RxRateLimit class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.impairment.defaultprofile.rxratelimit.rxratelimit import RxRateLimit
        return RxRateLimit(self)._select()

    @property
    def Links__(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/impairment/.../link]): List of references to impairment links.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Links__'])
    @Links__.setter
    def Links__(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Links__'], value)

    @property
    def AllLinks(self):
        """
        Returns
        -------
        - bool: If true, apply the profile to all impairment links. If not, only apply the profile to packets on selected links.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AllLinks'])
    @AllLinks.setter
    def AllLinks(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AllLinks'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the profile.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The name of the profile.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - number: Profile priority. 1 is highest.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def ProfileId(self):
        """
        Returns
        -------
        - number: A unique identifier for the profile. Read-only.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProfileId'])

    def update(self, Links__=None, AllLinks=None, Enabled=None, Name=None, Priority=None):
        """Updates profile resource on the server.

        Args
        ----
        - Links__ (list(str[None | /api/v1/sessions/1/ixnetwork/impairment/.../link])): List of references to impairment links.
        - AllLinks (bool): If true, apply the profile to all impairment links. If not, only apply the profile to packets on selected links.
        - Enabled (bool): If true, enables the profile.
        - Name (str): The name of the profile.
        - Priority (number): Profile priority. 1 is highest.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Links__=None, AllLinks=None, Enabled=None, Name=None, Priority=None):
        """Adds a new profile resource on the server and adds it to the container.

        Args
        ----
        - Links__ (list(str[None | /api/v1/sessions/1/ixnetwork/impairment/.../link])): List of references to impairment links.
        - AllLinks (bool): If true, apply the profile to all impairment links. If not, only apply the profile to packets on selected links.
        - Enabled (bool): If true, enables the profile.
        - Name (str): The name of the profile.
        - Priority (number): Profile priority. 1 is highest.

        Returns
        -------
        - self: This instance with all currently retrieved profile resources using find and the newly added profile resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained profile resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Links__=None, AllLinks=None, Enabled=None, Name=None, Priority=None, ProfileId=None):
        """Finds and retrieves profile resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve profile resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all profile resources from the server.

        Args
        ----
        - Links__ (list(str[None | /api/v1/sessions/1/ixnetwork/impairment/.../link])): List of references to impairment links.
        - AllLinks (bool): If true, apply the profile to all impairment links. If not, only apply the profile to packets on selected links.
        - Enabled (bool): If true, enables the profile.
        - Name (str): The name of the profile.
        - Priority (number): Profile priority. 1 is highest.
        - ProfileId (number): A unique identifier for the profile. Read-only.

        Returns
        -------
        - self: This instance with matching profile resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of profile data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the profile resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
