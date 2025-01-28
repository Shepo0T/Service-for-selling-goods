import re

from pydantic import AfterValidator
from typing import Annotated

PHONE_PATTERN = re.compile(r"^\+7\d{10}$")
PASSWORD_PATTERN = re.compile(r"^(?=.*[\d])(?=.*[!@#$%^&*])[\w!@#$%^&*]{6,128}$")


def valid_phone(phone: str) -> str:
    if not re.match(PHONE_PATTERN, phone):
        raise ValueError("Номер телефона должен начинаться с '+7' ")
    return phone


def valid_password(password: str) -> str:
    if not re.match(PASSWORD_PATTERN, password):
        raise ValueError(
            "Пароль должен соответствовать следующим требованиям:"
            "не менее 8 символов"
            "только латиница"
            "минимум 1 символ верхнего регистра"
            "минимум 1 спец символ ( $%&!: )"
        )

    return password


Check_phone = Annotated[str, AfterValidator(valid_phone)]
Check_password = Annotated[str, AfterValidator(valid_password)]
