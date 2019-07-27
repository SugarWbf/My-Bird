from django.db import models

# Create your models here.

class student(models.Model):
    num = models.AutoField(primary_key=True),
    name = models.CharField(null=False, max_length=30)
    name1 = models.CharField(null=False, max_length=30,default="")
    age = models.IntegerField()

    def __str__(self):
         print("name= ", self.name, "age= ", self.age)

#
    # def __str__(self):
    #     print("name= ",self.name, "age= " , self.age)
#
#
# class student1(models.Model):
#     num = models.AutoField(primary_key=True),
#     #name = models.CharField(null=False, max_length=30),
#     name = models.CharField(null=False, max_length=30)
#     age = models.IntegerField()
#
#
#     def __str__(self):
#         print("name= ",self.name, "age= " , self.age)
#
# class student2(models.Model):
#         num = models.AutoField(primary_key=True),
#         name = models.CharField(null=False, max_length=30)
#         # name = models.CharField(null=False, max_length=30)
#         age = models.IntegerField()

        # def __str__(self):
        #     print("name= ", self.name, "age= ", self.age)
