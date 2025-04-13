import jwt

from fastapi import HTTPException

from settings.base import JWT_SECRET_KEY

from .user import UserGateway


class AuthorizationGateway:
    token_expiration_time = 3600  # 1 hour
    secret_key = JWT_SECRET_KEY # Generate using 'openssl rand -hex 32'

    @classmethod
    def login(cls, username: str, password: str) -> str:
        """
        Login the user and return a JWT token.
        """
        try:
            user = UserGateway.verify_user_and_password(username, password)
        except Exception as e:
            raise HTTPException(status_code=401, detail=str(e))
        data = {
            "id": str(user.id),
            "email": user.email,
        }
        token = cls._create_token(data)
        return token

    @classmethod
    def _create_token(cls, data: dict) -> str:
        """
        Create a JWT token.
        data example:
        {
           "id": "123e4567-e89b-12d3-a456-426614174000",
           "email": "some@example.com
        }
        """
        data["exp"] = cls.token_expiration_time
        token = jwt.encode(
            data,
            cls.secret_key,
            algorithm="HS256",
        )
        return token