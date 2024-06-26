from authentication.models import User


class UserRepository:
    @staticmethod
    def get_user_by_id(id: int):
        return User.objects.get(pk=id)

    @staticmethod
    def get_user_by_email(email: str):
        return User.objects.get(email=email)
