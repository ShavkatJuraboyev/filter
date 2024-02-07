from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    STATUS_CHOICES = (
        ('yangi', 'Yangi'),
        ('tekshirilmoqda', 'Tekshirilmoqda'),
        ('tekshirildi', 'Tekshirildi'),
        ('rad etildi', 'Rad etildi'),
        ('ma\'lumot topilmadi', 'Ma\'lumot topilmadi'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='yangi', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"