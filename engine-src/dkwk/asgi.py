"""Asynchronous Server Gateway Interface.

FastAPI is an ASGI app, so we simply create it
and return it.
"""

__all__ = ['Application', 'default']

import fastapi
from . import __version__

def default():
    """Create default application."""
    return Application().to_asgi()

class Application:
    title = "DK-Wiki backend"
    description = "Default implementation"
    version = __version__

    def to_asgi(self):
        app = fastapi.FastAPI(
            title       = self.title,
            description = self.description,
            version     = self.version,
        )
        return app
