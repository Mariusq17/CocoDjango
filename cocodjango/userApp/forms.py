from django import forms

class UpdateProfileForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    available = forms.BooleanField(required=False)  # Dacă vrei un checkbox real
    start_date = forms.DateField(disabled=True)
    position = forms.CharField(disabled=True)
    my_buddy = forms.CharField(disabled=True)

    def __init__(self, *args, **kwargs):
        initial = kwargs.pop('initial', {})
        super().__init__(*args, **kwargs)
        
        # Setăm placeholder-ul și clasa pentru email
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Enter email',
            'type': 'email',
            'class': 'form-control'
        })

        # Inițializăm câmpurile cu valorile din `initial`
        for field, value in initial.items():
            self.fields[field].initial = value