# invoices/views.py
from django.http import JsonResponse
# from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
# from .serializers import InvoiceSerializer, InvoiceDetailSerializer
from .forms import InvoiceForm
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date
from django.forms.models import model_to_dict
from django.core.serializers import serialize

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
        data = json.loads(request.body.decode('utf-8'))
        data['date'] = parse_date(data['date'])
        try:
            invoice = Invoice.objects.create(**data)
            return JsonResponse({"message": "Success","invoice_id": invoice.id})
        except Exception as e:
            print('Form Invalid')
            return JsonResponse({"message": str(e)})
    # Get Request
    if pk == -1:
        # All items
        invoices = Invoice.objects.all()
        json_data = serialize('json',invoices)
        if json_data is not None:
            return JsonResponse(json_data,safe=False)
        else:
            return JsonResponse("Something went wrong")
    else:
        # Single item
        invoice = Invoice.objects.filter(id=pk).first()
        if invoice is not None:
            data = model_to_dict(invoice,fields=['id','date','customer_name'])
            return JsonResponse(data)
        else:
            return JsonResponse("Object not found")
    
