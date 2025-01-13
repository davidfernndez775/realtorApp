from django.contrib.auth.password_validation import MinimumLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
# for phonenumber validation
from phonenumber_field.phonenumber import PhoneNumber
from phonenumbers import NumberParseException, is_valid_number, parse


class CustomMinimumLengthValidator(MinimumLengthValidator):
    def __init__(self, min_length=5):
        self.min_length = min_length

    def get_help_text(self):
        return _(
            f"Your password must contain at least {
                self.min_length} characters."
        )

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _(f"Password must be at least {
                  self.min_length} characters long."),
                code="password_too_short",
            )

# Validate a phonenumber as US phonenumber format


def validate_us_phone_number(value):
    try:
        phone_number = parse(value, "US")
        if not is_valid_number(phone_number):
            raise ValidationError("The phone number entered is not valid.")
    except NumberParseException:
        raise ValidationError("The phone number entered is not valid.")
