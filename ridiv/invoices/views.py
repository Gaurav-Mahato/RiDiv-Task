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
        keys_to_extract = ['date','customer_name']
        filtered_dict = dict((key, data[key]) for key in keys_to_extract if key in data)

        try:
            invoice = Invoice(**filtered_dict)
            filtered_dic = {key: value for key, value in data.items() if key not in keys_to_extract}
            filtered_dic['invoice'] = invoice
            try:
                
                invoice.save()
                invoice_details = InvoiceDetail.objects.create(**filtered_dic)
                
                return JsonResponse({"message": 'Everything went good'})
            
            except Exception as e:
                return JsonResponse({"message": "Something went wrong", "error": str(e)})


        except Exception as e:
            return JsonResponse({"message": "Bad Data","error": str(e)})
        
    # Get Request
    if pk == -1:
        # All items
        invoices = Invoice.objects.all()
        json_data = serialize('json',invoices)
        if json_data is not None:
            return JsonResponse(json_data,safe=False)
        else:
            return JsonResponse({"message": "Something went wrong"})
    else:
        # Single item
        invoice = Invoice.objects.filter(id=pk).first()
        # invoice = model_to_dict(invoice,fields=['id','customer_name','date'])
        # look for invoice
        if invoice is not None:
            data = model_to_dict(invoice,fields=['id','date','customer_name'])
            lookup = InvoiceDetail.objects.filter(invoice=invoice).first()
            if lookup is not None:
                lookup = model_to_dict(lookup,fields=['description','unit_price','price','quantity'])
                data.update(lookup)
            return JsonResponse(data)
        else:
            return JsonResponse({"message": "Object not found"})
    
