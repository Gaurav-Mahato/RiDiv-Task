# invoices/views.py
from django.http import JsonResponse
# from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .forms import InvoiceForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date

# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer

# class InvoiceDetailViewSet(viewsets.ModelViewSet):
#     queryset = InvoiceDetail.objects.all()
#     serializer_class = InvoiceDetailSerializer

@csrf_exempt
def invoice(request, pk = -1):
    if request.method == 'POST': 
        data = request.POST.dict()
        print('......................')
        print(data)
        print('......................')
        data = json.loads(request.body.decode('utf-8'))
        data['date'] = parse_date(data['date'])
        try:
            invoice = Invoice.objects.create(**data)
            return JsonResponse({"message": "Success","invoice_id": invoice.id})
        except Exception as e:
            print('Form Invalid')
            return JsonResponse({"message": str(e)})
    print("Get Request received")

    
