from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)
    # pip install pillow command for ImageField
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        return self.user.username

# class SchoolInfo(models.Model):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     GRADUATE = 'GR'
#     YEAR_IN_SCHOOL_CHOICES = [
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#         (GRADUATE, 'Graduate'),
#     ]
#     year_in_school = models.CharField(max_length=2,choices=YEAR_IN_SCHOOL_CHOICES,default=FRESHMAN,)

#     # def is_upperclass(self):
#     #     return self.year_in_school in {self.JUNIOR, self.SENIOR}
    
#     def __str__(self):
#         return self.year_in_school in {self.JUNIOR, self.SENIOR}