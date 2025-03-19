from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_kb = 700

    if file.size > max_size_kb * 1024:
        raise ValidationError(f"Image files cannot be > than {max_size_kb}KB")
