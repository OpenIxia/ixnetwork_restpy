# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class IxNetworkError(Exception):
    """The base error class for all IxNetwork REST API errors"""
    def __init__(self, message, status_code=None):
        self._message = message
        self._status_code = status_code

    @property
    def message(self):
        return self._message

    @property
    def status_code(self):
        return self._status_code
        
    def __str__(self):
        return self._message
    
    def __repr__(self):
        return self._message


class ConnectionError(IxNetworkError):
    """Connection attempt has failed
    """
    def __init__(self, message, status_code=None):
        super(ConnectionError, self).__init__(message, status_code)


class AsyncOperationError(IxNetworkError):
    """Operation has failed
    """
    def __init__(self, message, status_code=None):
        super(AsyncOperationError, self).__init__(message, status_code)


class UnauthorizedError(IxNetworkError):
    """Access is unauthorized

    Authorization has not been successfully completed.
    Use the IxNetwork.auth method or the IxNetwork.api_key property prior to using any other functionality.
    """
    def __init__(self, message, status_code=None):
        super(UnauthorizedError, self).__init__(message, status_code)


class AlreadyExistsError(IxNetworkError):
    """The requested resource already exists on the server"""
    def __init__(self, message, status_code=None):
        super(AlreadyExistsError, self).__init__(message, status_code)


class BadRequestError(IxNetworkError):
    """The server has determined that the request is incorrect"""
    def __init__(self, message, status_code=None):
        super(BadRequestError, self).__init__(message, status_code)


class NotFoundError(IxNetworkError):
    """The requested resource does not exist on the server"""
    def __init__(self, message, status_code=None):
        super(NotFoundError, self).__init__(message, status_code)


class ResourceInUseError(IxNetworkError):
    """Resource in use
    
    The requested resource is in use by another request made to the server.
    The request will be retried 10 times with a wait of 6 seconds in between each retry. 
    After the retry period has elapsed this error will be raised.
    """
    def __init__(self, message, status_code=None):
        super(ResourceInUseError, self).__init__(message, status_code)


class ServerError(IxNetworkError):
    """The server has encountered an uncategorized error condition"""
    def __init__(self, message, status_code=None):
        super(ServerError, self).__init__(message, status_code)
