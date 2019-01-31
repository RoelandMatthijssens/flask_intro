from flask import Flask

app = Flask('someapp')

import flask_intro.db

app.cli.add_command(db.init_db_command)

import flask_intro.products.routes
import flask_intro.lists.routes
