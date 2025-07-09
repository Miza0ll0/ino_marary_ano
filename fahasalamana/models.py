from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

class Aretina(models.Model):
    anarana = models.CharField(max_length=200)
    famaritana = models.TextField()
    sary = models.ImageField(upload_to='sary_aretina/', blank=True, null=True)
    daty_nampidirana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.anarana

class ZavaManiry(models.Model):
    anarana = models.CharField(max_length=200)
    famaritana = models.TextField()
    sary = models.ImageField(upload_to='sary_zava_maniry/', blank=True, null=True)
    aretina_tsaboina = models.ManyToManyField(Aretina, related_name='zava_maniry_tsaboina', blank=True)
    daty_nampidirana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.anarana

class Fitsaboana(models.Model):
    zava_maniry = models.ForeignKey(ZavaManiry, on_delete=models.CASCADE, related_name='fitsaboana')
    aretina = models.ForeignKey(Aretina, on_delete=models.CASCADE, related_name='fitsaboana')
    fomba_fampiasana = models.TextField()
    daty_nampidirana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.zava_maniry.anarana} ho an'ny {self.aretina.anarana}"

class Mpitsabo(models.Model):
    mpampiasa = models.OneToOneField('Mpampiasa', on_delete=models.CASCADE, related_name='mpitsabo')
    anarana = models.CharField(max_length=100)
    sary = models.ImageField(upload_to='sary_mpitsabo/', blank=True, null=True)
    momba = models.TextField(blank=True)
    laharana = models.CharField(max_length=100, blank=True, verbose_name="Laharana fahamarinana")
    taona_asa = models.PositiveIntegerField(default=0, verbose_name="Taona niasana")

    def __str__(self):
        return self.anarana

class Mpampiasa(AbstractUser):
    anarana_feno = models.CharField(max_length=150, verbose_name="Anarana feno")
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True, verbose_name="Sary")
    no_telifonina = models.CharField(max_length=30, blank=True, verbose_name="Nomeraon-telefaona")
    is_mpitsabo = models.BooleanField(default=False, verbose_name="Mpitsabo")

    def __str__(self):
        return self.username

class Hafatra(models.Model):
    mpandefa = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='hafatra_nandefasana', on_delete=models.CASCADE)
    mpandray = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='hafatra_nakarina', on_delete=models.CASCADE)
    votoaty = models.TextField()
    daty = models.DateTimeField(auto_now_add=True)
    vakina = models.BooleanField(default=False)

    class Meta:
        ordering = ['-daty']

    def __str__(self):
        return f"Hafatra avy amin'ny {self.mpandefa} ho an'ny {self.mpandray}"
    
class Fanafody(models.Model):
    anarana = models.CharField(max_length=200)
    famaritana = models.TextField()
    vidiny = models.PositiveIntegerField()
    sary = models.ImageField(upload_to='sary_fanafody/', blank=True, null=True)
    daty_nampidirana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.anarana
    
class Sosokevitra(models.Model):
    lohateny = models.CharField(max_length=200)
    ambara = models.TextField(blank=True)
    sary = models.ImageField(upload_to='sary_sosokevitra/', blank=True, null= True)
    daty_nampidirana = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.lohateny


