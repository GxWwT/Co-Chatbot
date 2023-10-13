import os
import sys

import fire
import uvicorn

from api import create_service


class T:
    def server(self, *lc: str, port=8718, auth_token=""):
        sys.path.append(os.path.dirname("."))
        app = create_service(*lc, auth_token=auth_token)
        config = uvicorn.Config(app, port=port, log_level="info")
        server = uvicorn.Server(config)
        server.run()
        return


def entrypoint():
    fire.Fire(T())


if __name__ == "__main__":
    app = T()
    app.server("scenarios.app1:chain")
