import graphene
from graphene_django.types import DjangoObjectType
from .models import exp,NYC_data
import requests
import json

class expdata(DjangoObjectType):
    class Meta:
        model=NYC_data

class Query(graphene.ObjectType):
    all_data=graphene.List(expdata)

    def resolve_all_data(self,info,**kwargs):
        a=requests.get('https://data.cityofnewyork.us/resource/8y4t-faws.json').json()
        for i in a:
            # ny=NYC_data()
            # ny.zip_code=i['zip_code']
            # ny.Address=i['street_name']+', block NO. '+i['block']+', Lot No. '+i['gross_sqft']+', Built Year '+i['year']+ ', Building class '+i['bldg_class'] + ', Owner '+i['owner']+', State NYC'
            # ny.save()
            print('zip code '+i['zip_code'])
            print('Adderess: '+i['street_name']+', block NO. '+i['block']+', Lot No. '+i['gross_sqft']+', Built Year '+i['year']+ ', Building class '+i['bldg_class'] + ', Owner '+i['owner']+', State NYC' )
        return NYC_data.objects.all()

    def resolve_name(root,info):
        return 'sagar'
    def resolve_age(root,info):
        return "25"

