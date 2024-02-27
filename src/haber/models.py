from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.,


class BlogModel(models.Model):
    title                   = models.CharField(max_length=500,verbose_name = "başlık", blank=True)
    category                = models.CharField(max_length=40,verbose_name = "kategori",blank=True)
    image                   = models.ImageField(null=True,verbose_name='resim')
    created_date            = models.DateField(null=True,verbose_name="oluşturulma tarihi",auto_now_add=True)
    intro                   = RichTextUploadingField(blank=True, null=True, verbose_name='içerik')
    
    def __str__(self):
        return '%s %s' % (self.title, self.id)
    
        
    class Meta:
        ordering = ['created_date']
        verbose_name = 'Haber'
        verbose_name_plural = 'Haberler'