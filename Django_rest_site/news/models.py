from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    content = models.TextField(blank=True)
    upload_at = models.DateTimeField(auto_now_add=True, verbose_name='Заргружено')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title
