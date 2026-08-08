from django.contrib.auth.forms import AuthenticationForm


class BootstrapAuthForm(AuthenticationForm):
    """Встроенная форма входа, но с Bootstrap-классом form-control на полях."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
