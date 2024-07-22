from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class AccountActivationTokenGenereator(PasswordResetTokenGenerator):
    def _make_hash_value(self,student, timestamp) -> str:
        return (six.text_type(student.pk) + six.text_type(timestamp) + six.text_type(student.is_verified))

account_activation_token = AccountActivationTokenGenereator()