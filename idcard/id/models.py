from django.db import models
from django.utils.safestring import mark_safe
import requests


class Student(models.Model):
    

    COURSES = [

        ('B.A.', (
            ('BAHENG', 'B.A (Hons) English'),
            ('BAPENG', 'B.A. (Programme) compulsory English course'),
            ('BAHHIN', 'B.A (Hons) Hindi'),
            ('BAPHIN', 'B.A. (Programme) compulsory Hindi course'),
            ('BAHHIS', 'B.A. (Hons) History'),
            ('BAPHIS', 'B.A. (Programme)with History'),
            ('BAHPOL', 'B.A (Hons) Political Science'),
            ('BAPPOL', 'B.A (Prog.) with Political Science'),
            ('BAPECO', 'B.A. (Programme) with Economics'),
            ('BAPAC', 'B.A. Program Discipline and Application Course'),

        )
    ),
        ('B.Com', (
            ('BCPENG', 'B.Com (Programme) compulsory English course'),
            ('BCPHIN', 'B.Com (Programme ) compulsory Hindi course'),
            ('BCH', 'B.Com (Hons)'),
            ('BCP', 'B.Com (Prog.)'),
        )
    ),

        ('B.Sc.', (
            ('BSHCS', 'B.Sc. (Hons) Computer Science'),
            ('BSHGEO', 'B.Sc. (Hons) Geology'),
            ('BSHMIC', 'B.Sc (Hons) Microbiology'),
            ('BSHSTA', 'B.Sc. (Hon.) Statistics'),
            ('BSHMAT', 'B.Sc(Hons) Mathematics'),
        )
        
    ),
    ('BMS','Bachelor of Management Studies'),
    ('BJMC','BJMC'),

  
    ]

    
    YEARS= (
    (1, '1st Year'),
    (2, '2nd Year'),
    (3, '3rd Year'),
  )

    BLOOD_GROUPS = [
      ('A',(
          ('A+','A +ve'),
          ('A-','A -ve'),
        ),
      ),
      ('B',(
          ('B+','B +ve'),
          ('B-','B -ve'),
        ),
      ),
      ('AB',(
          ('AB+','AB +ve'),
          ('AB-','AB -ve'),
        ),
      ),
      ('O',(
          ('O+','O +ve'),
          ('O-','O -ve'),
        ),
      ),
    ]
    name = models.CharField(max_length=50)
    
    roll = models.PositiveSmallIntegerField(unique=True)
    
    course= models.CharField(max_length=50, choices = COURSES, default=1)
    year = models.IntegerField(choices = YEARS, default = 1)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    address = models.TextField()
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    date_of_admission = models.DateField() 
    blood_group = models.CharField(max_length=3, choices = BLOOD_GROUPS, default =1)
    default_image_url = 'https://pwcenter.org/sites/default/files/default_images/default_profile.png'
    image = models.URLField(max_length = 500, default = default_image_url)
    def __str__(self):
        label = self.name +' (' + str(self.roll) + ')'
        return label
    
    @property
    def barcode(self):
      barcode_url = 'http://barcodes4.me/barcode/c128a/'+ str(self.roll)+ '.png?margin=5&height=40&resolution=2'
      return barcode_url


    @property
    def qrcode(self):
      qrcode_url = 'http://barcodes4.me/barcode/qr/usercode.png?value=http://text.ujjawal.co/' + str(self.roll)

      return qrcode_url

    @property
    def pdf(self):
      pdf_url = '/generate/'+str(self.roll)
      return pdf_url


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 160px; height:160px;" />' % self.image)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image Preview'
    def image_tag_list(self):
        if self.image:
            return mark_safe('<img src="%s" style="width: 25px; height:25px;" />' % self.image)
        else:
            return 'No Image Found'
    image_tag_list.short_description = 'Image'



    



