

import pymongo
import urllib.parse
from bson import json_util 
import json 
from tbapp.models import Country,Cities,Sector,SubSector
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = """This command will fetch the data from remote server to local server (eg: 'HOST ID' 'PORT NO' 'DB NAME' 'USER NAME' 'PASSWORD') """
    def add_arguments(self, parser):
        parser.add_argument('host', type=str, help='Host ID')
        parser.add_argument('port', type=str, help='Port NO')
        parser.add_argument('db', type=str, help='DB Name')
        parser.add_argument('user', type=str, help='UserName')
        parser.add_argument('pwd', type=str, help='Password')

    def handle(self, *args, **kwargs):
        host=   kwargs['host']
        port=   kwargs['port']
        db  =   kwargs['db']
        user=   kwargs['user']
        pwd =   kwargs['pwd']
        username = urllib.parse.quote_plus(user)
        password = urllib.parse.quote_plus(pwd)
        client =  pymongo.MongoClient(f"mongodb://{username}:{password}@{host}:{port}")
        database = client[db]
        collections = database.list_collection_names()
        for i, collection_name in enumerate(collections):
            col = getattr(database,collections[i])
            collection = list(col.find())
            print(collection_name)
            success = 0
            faild = 0
            if collection_name == "geo":
                for j in collection:
                    countryobj = ""
                    try:
                        countryobj = Country.objects.create(id=str(j['_id']), className=j['_class'], name=j['countryName'],code=j['countryCode'],currency=j['countryCurrency'])
                        success += 1
                    except Exception as e:
                        faild += 1
                        print(f"Error {e}")
                    if countryobj:
                        stateobj = [
                                Cities(city = cname,
                                country= countryobj
                                )for cname in j['cities'] 
                            ]
                        cityobj = Cities.objects.bulk_create(objs=stateobj)
                    print(f"Success: {success} Faild: {faild}", end='\r', flush=True)                    
            elif collection_name =="sectors":
                for j in collection:
                    secobj=""
                    try:
                        secobj = Sector.objects.create(id=str(j['_id']), className=j['_class'], name=j['sectorName'])
                        success +=1 
                    except Exception as e:
                        faild += 1
                        print(f"Error {e}")

                    if 'subSectors' in j.keys() and secobj:
                        subseceobj = [
                            SubSector(subSectors= sname,
                            sector  = secobj
                            )for sname in j['subSectors'] 
                        ]
                        SubSector.objects.bulk_create(objs=subseceobj)
                    print(f"Success: {success} Faild: {faild}", end='\r', flush=True)            
            else:
                print(f"Uncofigured collections {collection_name}")
                break
            print(f"Success: {success} Faild: {faild}")
