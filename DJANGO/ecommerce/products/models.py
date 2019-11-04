from django.db import models
import os
import random
from unidecode import unidecode
from django.template.defaultfilters import slugify, safe
from django.db.models.signals import pre_save, post_save


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(filepath)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 54123)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=False, null=True, unique=True, editable=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=12.99)
    # image = models.FileField(upload_to=upload_image_path, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.title))
        new_slug = slug
        while Product.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            prod = Product.objects.get(slug=self.slug)
            if prod.title != self.title:
                self.slug = self.get_unique_slug()
        super(Product, self).save(*args, **kwargs)
        # daha save fonksiyonu işini bitirmeden biz burda override yaptık. Bu sayede modelin slug alanını set ettik.

# def product_pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = 'default-slug-with-signal'
# pre_save.connect(product_pre_save_receiver,sender=Product)
