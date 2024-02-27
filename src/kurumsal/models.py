from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=255,verbose_name="soru")
    answer = models.TextField(verbose_name="cevap")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.question
    
    
    
class Hizmetler(models.Model):
    title = models.CharField(max_length=255,verbose_name="başlık")
    decription = RichTextUploadingField(blank=True, null=True, verbose_name='içerik') 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Hizmet'
        verbose_name_plural = 'Hizmetler'

    def __str__(self):
        return self.title
    
    
   
    
class Kazanimlar(models.Model):
    title = models.CharField(max_length=255,verbose_name="başlık")
    decription = RichTextUploadingField(blank=True, null=True, verbose_name='içerik') 
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Kazanim'
        verbose_name_plural = 'Kazanimlar'

    def __str__(self):
        return self.title
