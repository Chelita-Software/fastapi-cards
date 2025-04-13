from passlib.context import CryptContext

from models import User
from repository.user import UserRepository


class UserGateway:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def hash_password(cls, password: str) -> str:
        """
        Hash the password using bcrypt.
        """
        return cls.pwd_context.hash(password)

    @classmethod
    def validate_role(cls, role: str) -> None:
        """
        Validate the user role.
        """
        valid_roles = ["admin", "user"]
        if role not in valid_roles:
            raise ValueError(f"Invalid role: {role}. Valid roles are: {valid_roles}")

    @classmethod
    def create(cls, email: str, name: str, password: str, role: str) -> User:
        """
        Create a new user.
        """
        hashed_password = cls.hash_password(password)
        cls.validate_role(role)
        user = UserRepository.create(email, name, hashed_password, role)
        return user
    
    @classmethod
    def verify_user_and_password(cls, email: str, password: str) -> User:
        """
        Verify the user and password.
        """
        user = UserRepository.get_by_email(email)
        if not user:
            raise Exception("User not found")
        # Verify the password
        if not cls.pwd_context.verify(password, user.password):
            raise Exception("Invalid password")
        return user
