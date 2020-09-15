""" Assistant class to simplify access to statistics views
"""
import json
import websocket
import threading
import ssl
import datetime
import re
import os
import time

try:
    basestring
except NameError:
    basestring = str

class WatchAssistant(object):
    def __init__(self, IxNetwork, Callback=None):
        """Establishes a connection to an IxNetwork application instance's watch notification websocket

        Args
        ----
        - IxNetwork (obj (ixnetwork_restpy.testplatform.sessions.ixnetwork.Ixnetwork)): An Ixnetwork object
        - Callback (method(ws, message)): the callback that receives notification data. 
            The message will be a json string and will need to be converted to a dict using json
            If no callback is provided then a default one will be assigned that 
            prints received messages to the console
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.ixnetwork import Ixnetwork
        assert(isinstance(IxNetwork, Ixnetwork))
        self._watch = IxNetwork.Watch
        self._topics = []
        session = IxNetwork.parent
        test_platform = session.parent
        self._headers = {
            'x-api-key': test_platform.ApiKey
        }
        self._sslopts = {
            'cert_reqs': ssl.CERT_NONE,
            'check_hostname': False
        }
        self._url = '%s://%s:%s/ixnetworkweb/ixnrest/ws/api/v1/sessions/%s/ixnetwork/sigr/v2' % (
            'ws' if test_platform.Scheme == "http" else 'wss', 
            test_platform.Hostname,
            test_platform.RestPort, 
            session.Id)
        if Callback is None:
            self._callback = self.__default_callback
        else:
            self._callback = Callback

    @staticmethod
    def __send_topics(ws):
        def send_topics(*args):
            ws = args[0]
            ws.send(json.dumps(ws.topics))
        if ws.topics is not None and len(ws.topics) > 0:
            threading.Thread(target=send_topics, args=[ws]).start()

    @staticmethod
    def __default_callback(ws, message):
        message = json.loads(message)
        if message['key'] == 'scriptWatch':
            return
        else:
            now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print('%s %s' % (now, message))

    def start(self):
        """Start receiving watch notification messages from the server.
        Add all watches before calling this method.
        """
        self._ws = websocket.WebSocketApp(self._url, header=self._headers, 
            on_open=self.__send_topics,
            on_message=self._callback)
        self._ws.topics = self._topics
        self._ws_thread = threading.Thread(target=self._ws.run_forever, 
            kwargs={'sslopt': self._sslopts})
        self._ws_thread.start()

    def stop(self):
        """Stop receiving watch notification messages from the server
        """
        self._ws.close()
        self._ws_thread.join()
 
    def AddAttributeWatch(self, AttributesToWatch, ObjectIdToWatch, Topic, MaxExecutionTime=2000, PollInterval=2000):
        """Adds an attribute watch on the API Server
        At this time all watches must be added before the start method is called. 

        Args
        ----
        - AttributesToWatch (list(str)):
        - ObjectIdToWatch (str(None)):
        - Topic (str): A unique name for the watch topic. 
            If the name is not unique an exception will be raised
        - MaxExecutionTime (number): The maximum amount of time a watch can take in milliseconds. 
            If the execution time exceeds this value the watch will be disabled.
            To bypass this check set the value to 0.
        - PollInterval (number): The interval in milliseconds the watch will be polled. 
            Minimum value is 100ms.
        """
        if Topic in self._topics:
            raise Exception("Topic %s already exists. Please select a different topic" % Topic)
        self._watch.AttributeWatch.add(AttributesToWatch=AttributesToWatch,
            MaxExecutionTime=MaxExecutionTime, 
            ObjectIdToWatch=ObjectIdToWatch, 
            PollInterval=PollInterval, 
            Topic=Topic)
        self._topics.append(Topic)
