import time
import os
from inspect import getframeinfo, stack
from uhd_restpy.base import Base


class Timer(object):
    def __init__(self, base):
        """Timer as a context manager

        Args
        ----
        - base (uhd_restpy.base.Base): object that inherits from uhd_restpy.base.Base
        """
        if isinstance(base, Base) is False:
            raise Exception(
                "The base object must be a valid instance of uhd_restpy.base.Base"
            )
        self._caller = getframeinfo(stack()[1][0])
        self._base = base
        self._msgs = []

    def __enter__(self):
        """Start a new timer as a context manager"""
        self._start = time.time()
        return self

    def __exit__(self, *exc_info):
        """Stop the context manager timer
        Output the message and the total time with level INFO
        """
        self._msgs.insert(
            0,
            "Timer @ {}:{}".format(
                os.path.basename(self._caller.filename),
                self._caller.lineno,
            ),
        )
        self._base.info(
            "[{:.3f}s] {}".format(
                time.time() - self._start,
                " -> ".join(self._msgs),
            )
        )

    def info(self, msg):
        if msg is not None:
            self._msgs.append(msg)
