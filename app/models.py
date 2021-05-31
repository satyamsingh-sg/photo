from django.db import models
from PIL import Image
# Create your models here.
class historial(models.Model):
     description = models.TextField('Description', blank=True)
     Photo= models.FileField(upload_to='img')


     def save(self):
          super().save()  # saving image first

          img = Image.open(self.Photo.path) # Open image using self

          if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.Photo.path)


class Comment(models.Model):
     cmt=models.TextField("comment",blank=True)