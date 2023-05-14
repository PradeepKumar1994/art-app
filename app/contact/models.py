from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns

class CassandraTestTable(DjangoCassandraModel):

    email = columns.UUID(primary_key=True)
    first_name = columns.UUID
    last_name = columns.UUID
    message = columns.Text()
    sending_time = columns.DateTime()

    class Meta:
        app_label = 'app'
        get_pk_field = 'email'
        #partition_key_fields = 'test_id'
        #clustering_key_fields = 'test_name'
