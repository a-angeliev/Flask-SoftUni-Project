from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError, NotFound
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models import RoleType
from models.users import UsersModel


class UsersManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UsersModel(**user_data)
        try:
            db.session.add(user)
            db.session.flush()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server is unavailable.")

        return user

    @staticmethod
    def login(user_data):
        user = UsersModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def create_admin(email_data):
        admin = UsersModel.query.filter_by(email=email_data["email"]).first()
        if not admin:
            raise NotFound("This user does not exist.")
        admin.role = RoleType.admin
        db.session.add(admin)
        db.session.flush()
        return 201
