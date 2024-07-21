from PIL import Image
import os
from django.core.exceptions import ValidationError
def validateIconImageSize(image):
    if image:
        with Image.open(image) as img:
            if img.width > 70 or img.height >70:
                raise ValidationError(f'the max dimesions for the image are 70x70, size of image you uploaded: {img.size}')

def validateImageFileExtension(value):
    ext=os.path.splitext(value.name)[1]
    validExtensios=['.jpg','.png','.jpeg','.gif']
    if not ext.lower() in validExtensios:
        raise ValidationError("unsupperted extension")