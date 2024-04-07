from django.db import models


class Basetable(models.Model):
    basetable_id = models.AutoField(primary_key=True)
    visibility = models.IntegerField()
    timezone = models.IntegerField()
    dt = models.IntegerField()
    name = models.CharField(max_length=100)
    cod = models.IntegerField()
    id = models.IntegerField()
    base = models.CharField(max_length=100)


class Main(models.Model):
    main_id = models.AutoField(primary_key=True)
    temp = models.CharField(max_length=100)
    temp_min = models.CharField(max_length=100)
    humidity = models.IntegerField()
    pressure = models.IntegerField()
    feels_like = models.CharField(max_length=100)
    temp_max = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Clouds(models.Model):
    clouds_id = models.AutoField(primary_key=True)
    all = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Sys(models.Model):
    sys_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    sunrise = models.IntegerField()
    id = models.IntegerField()
    type = models.CharField(max_length=100)
    sunset = models.IntegerField()
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Coord(models.Model):
    coord_id = models.AutoField(primary_key=True)
    lon = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)


class Weather(models.Model):
    weather_id = models.AutoField(primary_key=True)
    icon = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    id = models.IntegerField()
    basetable_id = models.ForeignKey(Basetable, on_delete=models.CASCADE)


class Wind(models.Model):
    wind_id = models.AutoField(primary_key=True)
    speed = models.CharField(max_length=100)
    deg = models.IntegerField()
    basetable_id = models.OneToOneField(Basetable, on_delete=models.CASCADE)