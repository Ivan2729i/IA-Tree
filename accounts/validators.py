from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class StrongPasswordValidator:
    def validate(self, password, user=None):
        errors = []

        if not any(character.isupper() for character in password):
            errors.append(
                ValidationError(
                    _("La contraseña debe contener al menos una letra mayúscula."),
                    code="password_no_uppercase",
                )
            )

        if not any(character.isdigit() for character in password):
            errors.append(
                ValidationError(
                    _("La contraseña debe contener al menos un número."),
                    code="password_no_number",
                )
            )

        if not any(
            not character.isalnum() and not character.isspace()
            for character in password
        ):
            errors.append(
                ValidationError(
                    _("La contraseña debe contener al menos un carácter especial."),
                    code="password_no_special_character",
                )
            )

        if errors:
            raise ValidationError(errors)

    def get_help_text(self):
        return _(
            "La contraseña debe contener al menos una mayúscula, "
            "un número y un carácter especial."
        )

