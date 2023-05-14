from .models import CassandraTestTable
from django.views import View
from django.http import HttpResponse
from django.test import TestCase
class ContactCassandraTest(View, TestCase):
    def get(self, request):
        rows = CassandraTestTable.objects.all()
        output = []
        for row in rows:
            output.append(f'First Name: {row.first_name} | NAME: {row.last_name} | MESSAGE: {row.message}')
        return HttpResponse('\n'.join(output))