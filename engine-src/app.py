#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ASGI production app.

(There is no "development" mode; it's an API! :^)
"""

__all__ = ['app']

import dkwk.asgi

app = dkwk.asgi.default()

if __name__ == '__main__':
    from socket import (
            inet_ntop,
            AF_INET,
            INADDR_LOOPBACK
            )
    from struct import pack

    INET_LOOPBACK = inet_ntop(AF_INET, pack("!I", INADDR_LOOPBACK))

    import argparse
    getopt = argparse.ArgumentParser()
    getopt.add_argument('host', nargs='?', default=INET_LOOPBACK)
    getopt.add_argument('port', nargs='?', default=8000)
    o = getopt.parse_args()

    import uvicorn
    uvicorn.run(app, host=o.host, port=o.port)
