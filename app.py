import json

from flask import Flask

from src.controllers import *
from src.services import *

injector = Provider()

injector.register("Flask", AppFlask(__name__))
injector.register("Controller.Containers", ContainersController)
injector.register("Controller.Logs", LogsController)

app = injector.resolve("Flask")

app.run(debug = True, host = "0.0.0.0", port = int("27001"), use_reloader=False)

