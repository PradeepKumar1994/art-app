from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns

class CassandraTestTable(DjangoCassandraModel):
    test_id = columns.UUID(primary_key=True)
    test_name = columns.UUID(primary_key=True)
    class Meta:
        app_label = 'app'
        get_pk_field = 'test_id'
        #partition_key_fields = 'test_id'
        #clustering_key_fields = 'test_name'
