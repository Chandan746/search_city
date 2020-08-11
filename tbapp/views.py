from .models import Country,Cities,Sector,SubSector
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET'])
def geo_search(request,country_name,query):
    if request.method == 'GET':
        data=[]
        countryObj = Country.objects.filter(name__icontains=country_name)
        if countryObj:
            for cObj in countryObj:
                CitiesObj = Cities.objects.filter(country=cObj).filter(city__icontains=query) 
                for i in CitiesObj:
                    vals ={"id":i.id,"country_id":cObj.id,"name":i.city,}
                    data.append(vals)
            return Response(data)
        else:
            return Response(data,status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def sec_search(request,mongo_sector_id):
    data=[]
    try:
        SectorObj = Sector.objects.get(id__iexact =mongo_sector_id)
    except Exception as e:
        return Response(f"Mongo Sector ID '{mongo_sector_id}' does not exist : {e} ",status=status.HTTP_204_NO_CONTENT)
    SubSectorObj = SubSector.objects.filter(sector=SectorObj)
    data =[]
    for i in SubSectorObj:
        vals = {"id":i.id,"sector_id":SectorObj.id,"name":i.subSectors}
        data.append(vals)
    return Response(data)

