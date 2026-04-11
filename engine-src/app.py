#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ASGI production app.

(There is no "development" mode; it's an API! :^)
"""

if __name__ == '__main__':
    import argparse
    import socket
    import uvicorn

    from socket import (
            inet_ntop,
            AF_INET,
            INADDR_LOOPBACK
            )
    from struct import pack

    INET_LOOPBACK = inet_ntop(AF_INET, pack("!I", INADDR_LOOPBACK))

    getopt = argparse.ArgumentParser()
    getopt.add_argument('host', nargs='?', default=INET_LOOPBACK)
    getopt.add_argument('port', nargs='?', default=8000)
    o = getopt.parse_args()

    uvicorn.run(f"dkwk.asgi:default", factory=True, host=o.host, port=o.port)
