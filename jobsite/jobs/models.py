from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255, verbose_name='Назва вакансії')
    company = models.CharField(max_length=255, verbose_name='Компанія')
    location = models.CharField(max_length=255, verbose_name='Місто')
    description = models.TextField(verbose_name='Опис')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Вакансія'
        verbose_name_plural = 'Вакансії'

    def __str__(self):
        return f"{self.title} - {self.company}"
