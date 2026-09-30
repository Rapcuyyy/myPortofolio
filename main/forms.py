from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput, FileInput
from django.utils.html import strip_tags

from main.models import Experience, Education

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Experience Name",
            "description": "Experience Description",
            "category": "Category",
            "thumbnail": "Certification",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Experience name",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell your experience",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "internship, research, volunteer, part-time, full-time, freelance",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/file/d/1OFZq-AKltIAK-i8o4xHScl64AchpgqKf/view?usp=sharing",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_tech_stack(self):
        return strip_tags(self.cleaned_data["tech_stack"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class EducationForm(ModelForm):
    class Meta:
        model = Education
        # Mengecualikan 'id' karena bersifat non-editable (auto-generate)
        fields = [
            "place",
            "major",
            "category",
            "year_start",
            "year_grad",
            "description",
            "logo",
            "thumbnail",
        ]

        labels = {
            "place": "Institution Name",
            "major": "Major / Field of Study",
            "category": "Category",
            "year_start": "Start Year",
            "year_grad": "Graduation Year",
            "description": "Description",
            "logo": "Institution Logo",
            "thumbnail": "Related Link / Certificate",
        }

        widgets = {
            "place": TextInput(
                attrs={
                    "placeholder": "e.g., Universitas Indonesia",
                    "maxlength": 225,
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "e.g., Computer Science",
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "elementary, junior, senior, bachelor, other",
                }
            ),
            "year_start": NumberInput(
                attrs={
                    "placeholder": "e.g., 2022",
                }
            ),
            "year_grad": NumberInput(
                attrs={
                    "placeholder": "e.g., 2026 (Leave blank if present)",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell us about your education journey",
                    "rows": 3,
                }
            ),
            "logo": FileInput(
                attrs={
                    "class": "project-search__input",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "Website where you learn",
                }
            ),
        }