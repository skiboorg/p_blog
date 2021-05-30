from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from pytils.translit import slugify

class Tag(models.Model):
    name = models.CharField('Название тега', max_length=255, blank=True, null=True)

    def __str__(self):
        return 'Тег : %s ' % self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

class BlogPost(models.Model):
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Тег')
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    short_description = RichTextUploadingField('Краткое описание ', blank=True,null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True,editable=False)
    video_link = models.CharField('Ссылка на видео ютуб',max_length=255, blank=True, null=True)
    link_name = models.CharField('Название ссылки перехода на страницу со статьей(если '
                                 'не указана, то статья не открывается)',max_length=255, blank=True, null=True)
    image = models.ImageField('Изображение превью (600 x 375)', upload_to='blog_img/', blank=True)

    description = RichTextUploadingField('Статья', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        slug = slugify(self.name)
        self.name_slug = slug
        super(BlogPost, self).save(*args, **kwargs)


    def __str__(self):
        return 'Статья : %s ' % self.name

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"