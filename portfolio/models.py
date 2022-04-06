from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.core.files import File


# Create your models here.

class ProjectCategory(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class ProjectTag(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.name

class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  image_url = models.CharField(max_length=200, blank=True, null=True)
  deployed_url = models.CharField(max_length=300, blank=True, null=True)
  github_frontend_url = models.CharField(max_length=300, blank=True, null=True)
  github_backend_url = models.CharField(max_length=300, blank=True, null=True)
  rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],blank=True, null=True)
  categories = models.ManyToManyField(ProjectCategory)
  tags = models.ManyToManyField(ProjectTag)
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('-date_added',)

  def __str__(self):
    return self.name

  def get_image(self):
    return self.image_url
