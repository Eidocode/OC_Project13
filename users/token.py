from django.contrib.auth.tokens import PasswordResetTokenGenerator


class EmailTokenGenerator(PasswordResetTokenGenerator):
    """
    Generate a token for password reset
    """
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) + str(user.is_active)
        )


token_generator = EmailTokenGenerator()
