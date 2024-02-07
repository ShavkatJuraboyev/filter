from django.db import models
class Tuman(models.Model):
    tuman_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tuman_name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    tuman = models.ForeignKey(Tuman, on_delete=models.CASCADE)
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