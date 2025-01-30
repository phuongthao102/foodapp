from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


class User(AbstractUser):
   avatar = CloudinaryField('avatar', null=True)

class BaseModel(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Store(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodItem(BaseModel):
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    food_type = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class Food(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    description = RichTextField()
    image = models.ImageField(upload_to='food/%Y/%m')  # Sử dụng ImageField
    store = models.ForeignKey('Store', on_delete=models.CASCADE, related_query_name='food')
    tags = models.ManyToManyField('Tag')


    class Meta:
        unique_together = ( 'subject', 'store')  # Đảm bảo tính duy nhất của subject trong mỗi store

    def __str__(self):
        return self.subject  # Trả về subject khi gọi Food đối tượng
class Lesson(BaseModel):
    subject = models.CharField(max_length=255, null=False)
    #noi dung bai hoc
    content =  RichTextField()
    image = models.ImageField(upload_to='lesson/%Y/%m')  # Sử dụng ImageField
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    class Meta:
        unique_together = ('subject', 'food')
class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Interaction(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=False)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE, null=False)


    class Meta:
        abstract = True

class Comment(Interaction):
    content = models.CharField(max_length=255, null=False)


class Like(Interaction):
    active = models.BooleanField()

class Rating(Interaction):
    rate = models.SmallIntegerField(default=0)
