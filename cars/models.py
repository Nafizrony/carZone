from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
import uuid
# Create your models here.

class Cars(models.Model):
    state_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    year_choice = []
    for r in range(2010, (datetime.now().year+1)):
        year_choice.append((r,r))

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=100,choices=state_choice)
    city = models.CharField(max_length=120)
    color = models.CharField(max_length=120) 
    model = models.CharField(max_length=120) 
    year = models.IntegerField(('year'),choices=year_choice) 
    condition = models.CharField(max_length=120) 
    car_price = models.IntegerField()
    car_photo = models.ImageField(upload_to='car_photos/%Y/%m/%d') 
    car_photo1 = models.ImageField(upload_to='car_photos/%Y/%m/%d',blank=True) 
    car_photo2 = models.ImageField(upload_to='car_photos/%Y/%m/%d',blank=True) 
    car_photo3 = models.ImageField(upload_to='car_photos/%Y/%m/%d',blank=True)
    car_photo4 = models.ImageField(upload_to='car_photos/%Y/%m/%d',blank=True)
    description = RichTextField()
    features = models.ManyToManyField('Car_Feature',blank=True)
    body_style = models.CharField(max_length=120) 
    engine = models.CharField(max_length=120)
    transmission = models.CharField(max_length=120) 
    interior = models.CharField(max_length=120) 
    miles = models.IntegerField() 
    doors = models.CharField(choices=door_choices,max_length=10)
    passengers = models.IntegerField() 
    vin = models.CharField(max_length=120) 
    fuel_mielage = models.CharField(max_length=120) 
    fuel_type = models.CharField(max_length=70) 
    is_featured = models.BooleanField(default=False) 
    owners = models.CharField(max_length=120) 
    warrenty = models.CharField(max_length=120) 
    created = models.DateTimeField(default=datetime.now,blank=True) 
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.car_title
    
class Car_Feature(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

