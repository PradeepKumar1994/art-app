
class CassandraError(Exception):
    """
    General error for cassandra
    """
    pass


class CassandraQueryError(CassandraError):
    """
    General user data related errors for cassandra
    """
    pass


class CassandraReadError(CassandraQueryError):
    """
    General error for cassandra reads
    """
    pass


class CassandraUserError(CassandraError):
    """
    General user related errors
    """
    pass


class CassandraWriteError(CassandraQueryError):
    """
    Error for cassandra writes
    """
    pass


class RecordDoesNotExist(CassandraWriteError):
    """
    Error when a record from database doesn't exists
    """
    pass


class NoDataRetrieved(CassandraReadError):
    """
    Raise when data could not be retrieved
    """
    pass


class NullValuesRead(CassandraReadError):
    """
    Raise when null value is read from cassandra
    """
    pass


class EmptyValuesRetrieved(CassandraReadError):
    """
    Raise when empty values are read from cassandra
    """
    pass


class PartitionKeyMissingException(CassandraQueryError):
    pass


class PrimaryKeyMissingException(CassandraQueryError):
    pass

