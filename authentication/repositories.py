from authentication.models import User


# class UserRepository:
#     @staticmethod
#     def create_user(email):
#         user, created = User.objects.get_or_create(email=email)
#
#         if created or user.is_active is False:
#             print(created, user.is_active)
