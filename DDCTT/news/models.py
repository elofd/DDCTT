from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_summernote.fields import SummernoteTextField

from accounts.models import CustomUser


def news_images_directory_path(instanse: "News", filename: str) -> str:
    """
    Красивый путь для хранения файлов
    :param instanse: инстанс класса News
    :param filename: имя файла
    :return: путь к файлу в формате str
    """
    return f"news/news_{instanse.pk}/images/{filename}"


class News(models.Model):
    """
    Модель новости
    """
    title = models.CharField(_('title'), max_length=250)
    main_image = models.ImageField(_('main_image'), null=True, blank=True, upload_to=news_images_directory_path)
    preview = models.ImageField(_('preview'), null=True, blank=True, upload_to=news_images_directory_path)
    description = models.TextField(_('description'))
    created_date = models.DateTimeField(_('created_date'), auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Создаём preview из main_image
        :return: None
        """
        if not self.preview:
            img = Image.open(self.main_image)
            img.thumbnail((200, 200))
            buffer = BytesIO()
            img.save(buffer, format='JPEG')
            buffer.seek(0)
            self.preview = InMemoryUploadedFile(
                buffer, 'ImageField',
                f'{self.main_image.name.split(".")[0]}_preview.jpg',
                'image/jpeg',
                buffer.getbuffer().nbytes,
                None
            )
        super().save(*args, **kwargs)
