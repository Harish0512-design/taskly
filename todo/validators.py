import phonenumbers
from django.core.exceptions import ValidationError


def validate_indian_phone_number(value):
    phone_number_obj = phonenumbers.parse(value, "IN")
    if not phonenumbers.is_valid_number(phone_number_obj):
        raise ValidationError("Enter a valid Indian Phone number")
