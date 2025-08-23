from django.db import models

# Create your models here.
class HeaderImg(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MainImg(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class SkillCategory(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class SkillModel(models.Model):
    category= models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProjectModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    techstack = models.CharField(max_length=700)
    link = models.URLField()

    def __str__(self):
        return self.title
class ContactModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
       return f"Message from {self.name}"