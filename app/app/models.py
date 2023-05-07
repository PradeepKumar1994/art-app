from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns

class CassandraTestTable(DjangoCassandraModel):
    test_id = columns.UUID(primary_key=True)
    test_name = columns.UUID(primary_key=True)
