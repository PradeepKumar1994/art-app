from models import CassandraTestTable

rows = CassandraTestTable.objects.all()
for row in rows:
    print(f'ID: {row.test_id} | NAME: {row.test_name}')