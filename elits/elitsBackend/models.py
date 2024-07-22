from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User, AbstractUser

# Create your models here.
# class User(AbstractUser):
#     class Role(models.TextChoices):
#         ADMIN = "ADMIN", "Admin"
#         STUDENT = "STUDENT", "Student"
#         TEACHER = "TEACHER", "Teacher"

#     base_role = Role.ADMIN

#     role = models.CharField(max_length=50, choices=Role.choices)

#     def save(self, *arg, **kwargs):
#         if not self.pk:
#             self.role = self.base_role
#             return super().save(*arg, **kwargs)

# class Student(User):
    # base_role = User.Role.STUDENT

    # class Meta:
    #     proxy = True

class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    datePosted = models.CharField(max_length=12)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    authorImage = models.ImageField(upload_to='newsAuthorImage')
    newsImage = models.ImageField(upload_to='newsImages')

    class Meta:
        verbose_name_plural = 'News'
        # ordering =

class Event(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    eventDate = models.CharField(max_length=12)
    category = models.CharField(max_length=255)
    eventImage = models.ImageField(upload_to='eventImages')

    class Meta:
        verbose_name_plural = 'Event'
        # ordering =

class Merchandise(models.Model):
    CATEGORY_CATEGORY = [
        ('Lanyard', 'Lanyard'),
        ('T-shirt', 'T-shirt'),
        ('Others', 'Others'),
    ]
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    name = models.CharField(max_length=255)
    originalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    discountPrice = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    category = models.CharField(max_length=255, choices=CATEGORY_CATEGORY)
    size = models.CharField(max_length=255, choices=SIZE_CHOICES, blank=True)
    merchImage = models.ImageField(upload_to='merchandiseImage')

    class Meta:
        verbose_name_plural = 'Merchandise'

class Officer(models.Model):
    name =  models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    bio = models.TextField()
    officerImage = models.ImageField(upload_to='officerImages', blank=True)

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    studentNumber = models.CharField(max_length=9, primary_key=True)
    email = models.EmailField()
    lastName = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50, blank=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.lastName}, {self.firstName} {self.middleName[0]}."

class VerificationToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student = models.OneToOneField(Students, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email



@receiver(pre_delete, sender=News)
def news_delete(sender, instance, **kwargs):
    instance.newsImage.delete(False)

@receiver(pre_delete, sender=Event)
def event_delete(sender, instance, **kwargs):
    instance.eventImage.delete(False)

@receiver(pre_delete, sender=News)
def newsAuthor_delete(sender, instance, **kwargs):
    instance.authorImage.delete(False)

@receiver(pre_delete, sender=Merchandise)
def merch_delete(sender, instance, **kwargs):
    instance.merchImage.delete(False)