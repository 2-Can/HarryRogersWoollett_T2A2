from flask import Blueprint
from main import db


db_commands = Blueprint('db', __name__)


@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")