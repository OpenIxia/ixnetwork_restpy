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
import os


class Files(object):
    """This class is used to copy an existing file to the server or create an empty file on the server.

    - If the file does not exist on the client and the local_file is True a 0 length file will be created in the default server location.
    - When a file is uploaded/created it will be written to a default file storage location on the server:
        - windows: %APPDATA%/Ixia/sdmStreamManager/common
        - linux: /root/.local/share/Ixia/sdmStreamManager/common
    - Use this class when a generated class has an method parameter with a type of (obj[Files]).
    - This class wraps access to the REST API /api/v1/sessions/<id>/ixnetwork/files functionality.

    Example
    -------
        # to copy a file use the local_file=True setting and ensure the file exists on the client
        # to create an empty file on the server ensure local_file=True and the file does not exist on the client
        file = Files('/tmp/test.ixncfg', local_file=True)

    Parameters
    ----------
        file_path: (str)
            The name of the file. 
            The name can be fully qualified or not. 
            The file does not have to exist
        local_file : (bool default[True])
            If True then the file will be uploaded to the server to the default file storage location.

    """

    def __init__(self, file_path, local_file=True):
        self._file_path = file_path
        self._file_name = os.path.basename(file_path)
        self._local_file = local_file

    @property
    def is_local_file(self):
        return self._local_file

    @property
    def file_path(self):
        return self._file_path

    @property
    def file_name(self):
        return self._file_name
