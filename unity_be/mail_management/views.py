from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
import datetime
from .models import Partner, Mail, Mail_Partner
from .serializers import PartnerSerializer, MailSerializer
import json
# Create your views here.

class healthcheck(APIView):
    def get(self, request, format=None):
        return JsonResponse(data="Ok", safe=False)

class AddPartner(APIView):
    def post(self, request, format=None):
        name = request.data["name"]
        current_timestamp = datetime.datetime.now()
        partner = None
        try:
            partner = Partner(name= name, creation_timestamp=current_timestamp, last_update_timestamp=current_timestamp, user_update="admin")
            partner.save()
        except Exception as e:
            return JsonResponse(data="Error when add partner: %s"%(e), safe=False) 
        partnerSerializer = PartnerSerializer(partner)
        return JsonResponse(data=partnerSerializer.data, safe=False)

class AddMail(APIView):
    def post(self, request, format=None):
        name = request.data["name"]
        is_subscribe = request.data["is_subscribe"]
        is_active = request.data["is_active"]
        partner_mail = request.data["partner_mail"]
        mail_partner_active = request.data["mail_partner_active"]
        current_timestamp = datetime.datetime.now()
        
        mail = None
        try:
            mail = Mail(name = name, is_subscribe = is_subscribe, is_active= is_active, creation_timestamp = current_timestamp, last_update_timestamp = current_timestamp)
            mail.save()
        except Exception as e:
            return JsonResponse(data="Error when add mail: %s"%(e), safe=False) 
        
        current_timestamp = datetime.datetime.now()
        mail_partner = None
        try:
            mail_partner = Mail_Partner(id_mail=mail, id_partner=Partner.objects.get(id=partner_mail) , is_active = mail_partner_active, creation_timestamp=current_timestamp, last_update_timestamp=current_timestamp)
            mail_partner.save()
        except Exception as e:
            return JsonResponse(data="Error when add mail_partner: %s"%(e), safe=False) 

        mailSerializer = MailSerializer(mail)
        return JsonResponse(data=mailSerializer.data, safe=False)


class GetListMails(APIView):
    def get(self, request):
        partner_id = int(request.GET["partner_id"][0])
        sql = '''
            select m.*
                from mail_management_mail m 
                    join mail_management_mail_partner mp 
                    on m.id = mp.id_mail_id
            where mp.id_partner_id = %s 
        '''%(partner_id)

        mails = Mail.objects.raw(sql)
        mailSerializer = MailSerializer(mails, many=True)
        return JsonResponse(data=mailSerializer.data, safe=False)


class GetNumMails(APIView):
    def get(self, request):
        partner_id = int(request.GET["partner_id"][0])
        partner = Partner.objects.get(id = partner_id)
        number = Mail_Partner.objects.filter(id_partner = partner).count()
        
        return JsonResponse(data=number, safe=False)

class GetNumNewMails(APIView):
    def get(self, request):
        partner_id = int(request.GET["partner_id"][0])
        partner = Partner.objects.get(id = partner_id)
        datem = datetime.datetime.today().strftime("%Y-%m")
        datem = datetime.datetime.strptime(datem, "%Y-%m")
        number = Mail_Partner.objects.filter(last_update_timestamp__gte = datem).filter(id_partner = partner).count()
        print(datem)
        return JsonResponse(data=number, safe=False)

       