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


class Watch(Base):
    """Top level node for watch topics and notifications.
    The Watch class encapsulates a required watch resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = 'watch'
    _SDM_ATT_MAP = {
        'Topics': 'topics',
    }

    def __init__(self, parent):
        super(Watch, self).__init__(parent)

    @property
    def AttributeWatch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.attributewatch.attributewatch.AttributeWatch): An instance of the AttributeWatch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.attributewatch.attributewatch import AttributeWatch
        return AttributeWatch(self)

    @property
    def ExecWatch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.execwatch.execwatch.ExecWatch): An instance of the ExecWatch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.execwatch.execwatch import ExecWatch
        return ExecWatch(self)

    @property
    def ListWatch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.listwatch.listwatch.ListWatch): An instance of the ListWatch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.listwatch.listwatch import ListWatch
        return ListWatch(self)

    @property
    def SelectWatch(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.selectwatch.selectwatch.SelectWatch): An instance of the SelectWatch class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.watch.selectwatch.selectwatch import SelectWatch
        return SelectWatch(self)

    @property
    def Topics(self):
        """
        Returns
        -------
        - list(str): 
        """
        return self._get_attribute(self._SDM_ATT_MAP['Topics'])

    def AddAttributeWatch(self, *args, **kwargs):
        """Executes the addAttributeWatch operation on the server.

        addAttributeWatch(Arg2=href, Arg3=list, Arg4=string)object
        ----------------------------------------------------------
        - Arg2 (str(None)): 
        - Arg3 (list(str)): 
        - Arg4 (str): 
        - Returns dict(arg1:str,arg2:number): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addAttributeWatch', payload=payload, response_object=None)

    def AddExecWatch(self, *args, **kwargs):
        """Executes the addExecWatch operation on the server.

        addExecWatch(Arg2=string, Arg3=string)object
        --------------------------------------------
        - Arg2 (str): 
        - Arg3 (str): 
        - Returns dict(arg1:str,arg2:number): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addExecWatch', payload=payload, response_object=None)

    def AddListWatch(self, *args, **kwargs):
        """Executes the addListWatch operation on the server.

        addListWatch(Arg2=href, Arg3=list, Arg4=string)object
        -----------------------------------------------------
        - Arg2 (str(None)): 
        - Arg3 (list(str)): 
        - Arg4 (str): 
        - Returns dict(arg1:str,arg2:number): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addListWatch', payload=payload, response_object=None)

    def AddSelectWatch(self, *args, **kwargs):
        """Executes the addSelectWatch operation on the server.

        addSelectWatch(Selects=list, WatchTopic=string)object
        -----------------------------------------------------
        - Selects (list(dict(from:str[None | /api/v1/sessions/1/ixnetwork//.../*],properties:list[str],children:list[dict(child:str,properties:list[str],filters:list[dict(property:str,regex:str)])],inlines:list[dict(child:str,properties:list[str])]))): 
        - WatchTopic (str): 
        - Returns dict(arg1:str,arg2:number): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('addSelectWatch', payload=payload, response_object=None)

    def RemoveWatches(self, *args, **kwargs):
        """Executes the removeWatches operation on the server.

        removeWatches(WatchIds=list)
        ----------------------------
        - WatchIds (list(number)): 

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('removeWatches', payload=payload, response_object=None)
