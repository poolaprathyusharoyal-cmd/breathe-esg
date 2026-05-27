from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EmissionRecord
import csv
from io import TextIOWrapper

@api_view(['GET'])
def home(request):
    return Response({"message": "Backend working successfully"})


@api_view(['POST'])
def upload_csv(request):

    file = request.FILES['file']

    csv_file = TextIOWrapper(file.file, encoding='utf-8')
    reader = csv.DictReader(csv_file)

    for row in reader:
        EmissionRecord.objects.create(
            source=row['source'],
            category=row['category'],
            amount=float(row['amount']),
            unit=row['unit'],
            status=row['status']
        )

    return Response({"message": "CSV uploaded successfully"})

@api_view(['GET'])
def get_records(request):

    records = EmissionRecord.objects.all().values()

    return Response(records)
