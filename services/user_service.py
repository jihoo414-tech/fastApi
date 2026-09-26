
from schemas.user import UserCreateRequest


def create_user_service(request: UserCreateRequest):
    return {
        "username": request.username,
        "age": request.age
    }