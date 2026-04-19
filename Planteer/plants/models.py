from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()
    used_for = models.TextField()
    category = models.CharField(max_length=50, choices=[
        ('Fruit', 'Fruit'),
        ('Vegetable', 'Vegetable'),
        ('Herb', 'Herb'),
        ('Flower', 'Flower'),
        ('Tree', 'Tree')
    ])
    is_edible = models.BooleanField(default=False)
    image = models.ImageField(upload_to='plant_images/', default='plant_images/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)