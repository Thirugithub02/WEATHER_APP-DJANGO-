from django.shortcuts import redirect, render
from .forms import Cityform
from .models import City
import requests
from django.contrib import messages

def home(request):
    url= "https://api.openweathermap.org/data/2.5/weather?q={},&appid=3316efd3ed9fd73e9d0c29c08f1a3daa&units=metric"
    if request.method =='POST':
        form=Cityform(request.POST)
        if form.is_valid():
            New_city=form.cleaned_data['name']
            Created_city=City.objects.filter(name=New_city).count()
            if Created_city==0:
                result=requests.get(url.format(New_city)).json()
                print(result)
                if result['cod']==200:
                    form.save()
                    messages.success(request ,"" +New_city + "  Added successfully.....!!")
                else:
                    messages.error(request ,"City does not exixts....!!")
            else:
                messages.error(request ,"ALready exixts....!!")        
                        
            
        
    form=Cityform()
    cities=City.objects.all()
    data=[]
    for city in cities:
        result=requests.get(url.format(city)).json()
        city_weather={
            'city' : city,
            'temperature' :result['main']['temp'],
            'min' :result['main']['temp_min'],
            'max' :result['main']['temp_max'],
            'description' :result['weather'][0]['description'],
            'pressure': result['main']['pressure'],
            'humidity' :result['main']['humidity'],
            'sunrise' :result['sys']['sunrise'],
            'sunset' :result['sys']['sunset'],            
            'country' :result['sys']['country'],
            'icon' :result['weather'][0]['icon'],
                
        }
        data.append(city_weather)
    context={'data':data ,'form':form}    
    return render(request,"weatherapp.html" ,context)


def delete_city(request,cname):
    City.objects.get(name=cname).delete()
    messages.success(request,""+ cname + "Removed sucessfully........!!!!!!1")
    return redirect('home')

# Create your views here.
