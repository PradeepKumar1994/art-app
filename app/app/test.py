from .models import CassandraTestTable
from django.views import View
from django.http import HttpResponse
from django.test import TestCase
class BasicCassandraTest(View, TestCase):
    def get(self, request):
        rows = CassandraTestTable.objects.all()
        output = []
        for row in rows:
            output.append(f'ID: {row.test_id} | NAME: {row.test_name}')
            print(f'ID: {row.test_id} | NAME: {row.test_name}')
        return HttpResponse('\n'.join(output))