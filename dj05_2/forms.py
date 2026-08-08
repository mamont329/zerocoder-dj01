from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class BootstrapUserCreationForm(UserCreationForm):
    """Стандартная форма регистрации + Bootstrap-класс form-control на полях."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class BootstrapAuthForm(AuthenticationForm):
    """Стандартная форма входа + Bootstrap-класс form-control на полях."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
