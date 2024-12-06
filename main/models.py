from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
class Talaba(models.Model):
    ism=models.CharField(max_length=50)
    yosh=models.PositiveSmallIntegerField()
    telefon_raqm=models.CharField(max_length=15)
    kurs=models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(4)],default=1)
    kitob_soni=models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural='Talabalar'

class Muallif(models.Model):
    ism=models.CharField(max_length=50)
    t_yil=models.DateField(blank=True, null=True)
    jinsi=models.CharField(max_length=10,choices=(('erkak','erkak'),('ayol','ayol')))
    millat=models.CharField(max_length=50,blank=True,null=True)
    tirik=models.BooleanField(default=False)
    kitob_soni=models.PositiveSmallIntegerField(blank=True,null=True)

    def __str__(self):
        return self.ism

    class Meta:
        verbose_name_plural = 'Mualliflar'

class Kitob(models.Model):
    nom=models.CharField(max_length=50)
    janr=models.CharField(max_length=50)
    sahifa=models.PositiveSmallIntegerField()
    muqova=models.CharField(max_length=50,choices=(('Qattiq','Qattiq'),('Yumshoq','Yumshoq')))
    muallif=models.ManyToManyField(Muallif)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = 'Kitoblar'
class Kutubxonachi(models.Model):
    Ish_vaqti=(
        ('08:00-13:00','08:00-13:00'),
        ('13:00-20:00','13:00-20:00'),
        ('20:00-02:00', '20:00-02:00'),
    )
    ism=models.CharField(max_length=50)
    telefon_raqam=models.CharField(max_length=50)
    ish_vaqti=models.CharField(max_length=50,choices=Ish_vaqti)
    def __str__(self):
        return self.ism


    class Meta:
        verbose_name_plural = 'Kutubxonachilar'


class Record(models.Model):
    talaba=models.ForeignKey(Talaba,on_delete=models.SET_NULL,null=True)
    kitob=models.ForeignKey(Kitob,on_delete=models.SET_NULL,null=True)
    kutubxonachi=models.ForeignKey(Kutubxonachi,on_delete=models.SET_NULL,null=True)
    olingan_san=models.DateField(auto_now_add=True)
    qaytarilgan_sana=models.DateField(blank=True,null=True)
    qaytardi=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.talaba} - {self.kitob} ({self.kutubxonachi})'

    class Meta:
        verbose_name_plural = 'Rekordlar'








