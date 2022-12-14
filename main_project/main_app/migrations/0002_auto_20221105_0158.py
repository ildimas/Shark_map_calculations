# Generated by Django 4.1.2 on 2022-11-04 12:47

from django.db import migrations
from main_app import parser_russian_realty

def old_apartments_loader(apps, schema_editor):
    db = apps.get_model('main_app', 'main_db')
    print('загружаются бу квартиры')
    x = parser_russian_realty.Application()
    pars_dict = (x.parser())
    for key in pars_dict:
        main_list = pars_dict[key]
        db.objects.create(link=f'{main_list[0]}', address=f'{main_list[3]}',
            flat_floor=main_list[8], building_floor=main_list[9],
            price=main_list[2], rooms_count=main_list[5], kithcen_square=round(main_list[7]),
            main_square=round(main_list[6]), balcony=main_list[10], decor=f'{main_list[11]}', subway_distance=main_list[4], estate_type=f'{main_list[1]}', apartment_type=f'{main_list[12]}', coordinates_lat=main_list[13], coordinates_lng=main_list[14])  

def new_apartments_loader(apps, schema_editor):
    bd = apps.get_model('main_app', 'main_db')
    print('загружаются новые квартиры квартиры')
    y = parser_russian_realty.Application()
    y.url_s = 'https://www.russianrealty.ru/%D0%9F%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%B2-%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B5/'
    pars_n_dict = (y.parser())
    for key in pars_n_dict:
        main_list = pars_n_dict[key]
        bd.objects.create(link=f'{main_list[0]}', address=f'{main_list[3]}',
            flat_floor=main_list[8], building_floor=main_list[9],
            price=main_list[2], rooms_count=main_list[5], kithcen_square=round(main_list[7]),
            main_square=round(main_list[6]), balcony=main_list[10], decor=f'{main_list[11]}', subway_distance=main_list[4], estate_type=f'{main_list[1]}', apartment_type=f'{main_list[12]}', coordinates_lat=main_list[13], coordinates_lng=main_list[14])  

        
class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [migrations.RunPython(old_apartments_loader), migrations.RunPython(new_apartments_loader)]
