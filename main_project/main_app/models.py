from django.db import models

class main_db(models.Model):
    
    estate_type = models.CharField(max_length=200, verbose_name='Тип недвижимости')
    link = models.TextField(verbose_name='Ссылка')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    flat_floor = models.IntegerField(verbose_name='Этаж квартиры')
    building_floor = models.IntegerField(verbose_name='Этажность здания')
    price = models.IntegerField(verbose_name='Цена квартиры')
    rooms_count = models.IntegerField(verbose_name='Количество комнат')
    kithcen_square = models.IntegerField(verbose_name='Площадь кухни')
    main_square = models.IntegerField(verbose_name='Площадь квартиры')
    balcony = models.BooleanField(default=False, verbose_name='Наличие балкона')
    decor = models.CharField(max_length=150, verbose_name='Тип ремонта')
    subway_distance = models.IntegerField(verbose_name='расстояние до метро')
    apartment_type = models.CharField(max_length=200, verbose_name='Тип дома')
    coordinates_lng = models.DecimalField(max_digits=30, decimal_places=20, verbose_name='Долгота')
    coordinates_lat = models.DecimalField(max_digits=30, decimal_places=20, verbose_name='Широта')

class uploaded_files(models.Model):
    estate_type = models.CharField(max_length=200, verbose_name='Сегмент')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    flat_floor = models.IntegerField(verbose_name='Этаж квартиры')
    building_floor = models.IntegerField(verbose_name='Этажность здания')
    rooms_count = models.IntegerField(verbose_name='Количество комнат')
    kithcen_square = models.IntegerField(verbose_name='Площадь кухни')
    main_square = models.IntegerField(verbose_name='Площадь квартиры')
    balcony = models.BooleanField(default=False, verbose_name='Наличие балкона')
    decor = models.CharField(max_length=150, verbose_name='Тип ремонта')
    subway_distance = models.IntegerField(verbose_name='расстояние до метро')
    apartment_type = models.CharField(max_length=200, verbose_name='Материал стен')
    coordinates_lng = models.DecimalField(max_digits=30, decimal_places=20, verbose_name='Долгота')
    coordinates_lat = models.DecimalField(max_digits=30, decimal_places=20, verbose_name='Широта')