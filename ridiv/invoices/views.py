# invoices/views.py
from django.http import JsonResponse
# from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .forms import InvoiceForm
import json
from django.views.decorators.csrf import csrf_exempt

# class InvoiceViewSet(viewsets.ModelViewSet):
#     queryset = Invoice.objects.all()
#     serializer_class = InvoiceSerializer

# class InvoiceDetailViewSet(viewsets.ModelViewSet):
#     queryset = InvoiceDetail.objects.all()
#     serializer_class = InvoiceDetailSerializer

@csrf_exempt
def invoice(request, pk = -1):
    if request.method == 'POST':
        print('Post request received')
        
        json_data = json.loads(request.body.decode('utf-8'))
        message = json_data.get('message')
        print(f"{message}")
        return JsonResponse({'message': 'Sucess'})
    print("Get Request received")

    
