from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self,res):
        name = res['name']
        description=res['description']
        try:
            Course.coursemanager.get(name=name)
            return {'error': 'This username already exists'}
        except:
            pass

        if len(name)==0:
            return {'error': 'no name'}
        if len(description)==0:
            return {'error': 'no description'}
        # if len(error)!=0: # if len(errors ) is not 0:
        #     return (False, errors)

        x = Course.coursemanager.create(name = name)
        Description.objects.create(description = description, course = x)
        x.save()

        return {'course':Course.coursemanager.get(name=name)}
        # User.objects.create(name=name, username=username, password=hashpw, date_hired=datehired)
        # return {'user':User.objects.get(username=username)}



class Course(models.Model):
    name = models.CharField(max_length=100)
    date_added=models.DateField(auto_now_add=True)
    coursemanager=CourseManager()

class Description(models.Model):
    description=models.CharField(max_length=1000)
    date_added=models.DateField(auto_now_add=True)
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE,
        primary_key=True,
    )
