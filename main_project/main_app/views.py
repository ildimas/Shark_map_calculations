from django.shortcuts import render
from django.http import HttpResponse
from .models import main_db, uploaded_files
import json
import requests
import folium
from folium.features import *
import geocoder
import openpyxl 


def index(request):
    print('death loop restarted')
    # #Делаем карту
    m = folium.Map(location=[55.75, 37.62],top='8%', height='90%',left='5.5%', width='90%')
    folium.TileLayer('cartodbdark_matter', name='Темная').add_to(m)
    folium.TileLayer('cartodbpositron', name='Светлая').add_to(m)
    folium.TileLayer('stamentoner', name='Контрастная').add_to(m)
    #Создание разметки москвы и geojson
    layer_main = folium.GeoJson(data=(open('D:\ЛЦТ_хакатон_основа\main_project\main_app\geoJson\moscow_geo.geojson', 'r', encoding='utf-8').read()), name='Районы с высокой стоимостью жилья')
    folium.GeoJsonTooltip(fields=['name']).add_to(layer_main)
    layer_main.add_to(m)
    folium.LayerControl().add_to(m)
    #ввод данных на карту
    entire_db = main_db.objects.all()
    for i in range(len(entire_db)):
        some_db = entire_db[i] 
        lat = some_db.coordinates_lat
        lng = some_db.coordinates_lng
        if  lat > 56 or lng > 38 or lat < 55 or lng < 37:
            continue
        
        
        if some_db.estate_type == "вторичная":
            color_html = 'orange'
        else:
            color_html = 'teal'
        # if some_db.price >= 20_000_000:
        #     color_if = 'red'
        # elif some_db.price >= 10_000_000 and some_db.price < 20_000_000:
        #     color_if = 'yellow'
        # else:
        #     color_if = 'green'
       
        # y = folium.features.CircleMarker([lat, lng], radius=40, color=color_if, fill_color = color_if).add_to(m)
        folium.Marker([lat, lng], icon=DivIcon(icon_size=(150,36), icon_anchor=(7,20), html=f'<span style="font-size: 25pt; color : {color_html}; style=display: block"> &#9660; </span>'), 
                      tooltip=f'{some_db.estate_type}', popup=f'{some_db.price, some_db.apartment_type, some_db.address ,some_db.estate_type, some_db.estate_type, f"Этаж квартиры: {some_db.flat_floor}",f"Количество комнат: {some_db.rooms_count}", f"Площадь квартиры: {some_db.main_square}"}',
                      ).add_to(m)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        file = request.FILES['file']
        wb = openpyxl.load_workbook(file)
        ws = wb.active

        list_info = []
        for i in range(2, ws.max_row + 1):
            list_info.append([
            ws['A' + str(i)].value, ws['B' + str(i)].value, ws['C' + str(i)].value, ws['D' + str(i)].value,
            ws['D' + str(i)].value, ws['E' + str(i)].value, ws['F' + str(i)].value, ws['G' + str(i)].value, 
            ws['H' + str(i)].value, ws['I' + str(i)].value, ws['J' + str(i)].value, ws['K' + str(i)].value])
            
        u_db = uploaded_files.objects
        for i in range(len(list_info)):
            new_adress = ((list_info[i])[0])[8:]
            y = geocoder.osm(new_adress)
            print(y.latlng)
            if (list_info[i])[8] == 'Да':
                (list_info[i])[8] = True
            else:
                (list_info[i])[8] = False
            u_db.create(address=new_adress, rooms_count=(list_info[i])[1], estate_type=(list_info[i])[2], building_floor=(list_info[i])[3]
                        ,apartment_type=(list_info[i])[5], flat_floor=(list_info[i])[6], main_square=(list_info[i])[7],
                        kithcen_square=15, balcony=(list_info[i])[8], subway_distance=(list_info[i])[10], decor=(list_info[i])[11],
                        coordinates_lng=(y.latlng)[1], coordinates_lat=(y.latlng)[0])
            print(list_info[i])
            
            
            
            


                
    m = m._repr_html_()
    context = {'m': m,}
    return render(request, 'base.html', context=context)


# f'Адрес:{some_db.address},Площадь квартиры: {some_db.main_square},Балкон: {some_db.balcony},Расстояние до метро: {some_db.subway_distance}'

