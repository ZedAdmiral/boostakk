from django.db import models


class Task(models.Model):
    title = models.CharField('Ник', max_length=50)
    task = models.TextField('Коммент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='main/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'рейтинг'
        verbose_name_plural = 'рейтинг'
