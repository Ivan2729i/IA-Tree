from django import forms

from .models import User


class AccountProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name")

    def clean_first_name(self):
        return self.cleaned_data["first_name"].strip()

    def clean_last_name(self):
        return self.cleaned_data["last_name"].strip()


class DeleteAccountRequestForm(forms.Form):
    password = forms.CharField(
        label="Contraseña actual",
        widget=forms.PasswordInput,
        required=False,
    )

    acknowledge = forms.BooleanField(
        label="Entiendo que esta acción es irreversible.",
        required=True,
    )

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

        if user and not user.has_usable_password():
            self.fields.pop("password")

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if self.user and self.user.has_usable_password():
            if not password or not self.user.check_password(password):
                raise forms.ValidationError("La contraseña actual no es correcta.")

        return password


class DeleteAccountConfirmForm(forms.Form):
    confirmation = forms.CharField(label="Confirmación")

    def clean_confirmation(self):
        value = self.cleaned_data["confirmation"].strip()

        if value != "ELIMINAR":
            raise forms.ValidationError('Escribe exactamente "ELIMINAR" para continuar.')

        return value
