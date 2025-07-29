from django import forms
from .models import Image

class ImageUploadForm(forms.ModelForm):
    retention_days = forms.IntegerField(
        label="Retention Days",
        min_value=1,
        max_value=30,
        required=False,
        help_text="Set retention period in days (max 30). Leave empty for unlimited (admin only).",
        widget=forms.NumberInput(attrs={
            'class': 'rounded-md bg-white text-black px-3 py-2 w-full',
            'placeholder': 'Retention days (max 30)'
        })
    )

    class Meta:
        model = Image
        fields = ['image', 'name', 'retention_days']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full',
                'placeholder': 'Image name'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'rounded-md bg-white text-black px-3 py-2 w-full'
            }),
        }
