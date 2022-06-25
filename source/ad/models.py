from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

STATUS_CHOICES = [("moderated", "Moderated"), ("published", "Published"),
                  ("rejected", "Rejected"), ("for_removal", "For removal")]


class Ad(models.Model):
    photo = models.ImageField(null=True, blank=True, verbose_name='Изображение', upload_to='uploads/images')
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    text = models.TextField(max_length=2000, blank=True, null=True, verbose_name="Описание")
    coast = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2, verbose_name='Стоимость')
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, verbose_name='Автор', related_name='ads')
    status = models.CharField(max_length=20, default='moderated',
                              choices=STATUS_CHOICES, verbose_name='Статусы')
    category = models.ForeignKey('ad.Category', on_delete=models.CASCADE,
                                 related_name='ads', verbose_name='Категории')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    publication_date = models.DateTimeField(auto_now=True, verbose_name="Дата публикации")

    def __str__(self):
        return f"{self.pk}. {self.title}: {self.author} - {self.created_at}"

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        db_table = 'ads'


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категория")

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'
