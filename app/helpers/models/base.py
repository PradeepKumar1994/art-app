from datetime import datetime, timezone
from json import loads as json_loads
from typing import Any, Dict
from typing import List as PyList
from uuid import uuid1
from inspect import isclass

from cassandra.cqlengine.columns import Text, DateTime, Ascii
from cassandra.cqlengine.models import Model

from .exceptions import (
    CassandraError,
    CassandraQueryError,
    CassandraReadError,
    CassandraWriteError,
    CassandraUserError,
    RecordDoesNotExist,
    NoDataRetrieved,
    NullValuesRead,
    EmptyValuesRetrieved,
    PartitionKeyMissingException,
    PrimaryKeyMissingException
)


def not_empty_result(error_message: str = "No data retrieved"):
    """
    With the help of this function and following decorator
    we raise exceptions when empty results are retrieved
    """
    def _not_empty_results(function_):
        @wraps(function_)
        def _retrieve_results(*args, **kwargs):
            results = function_(*args, **kwargs)
            if not results:
                filter_args = [arg for arg in args if not isclass(arg)]
                raise NoDataRetrieved(
                    f"{error_message}"
                    f"{f'{filter_args}' if filter_args else ''}"
                    f"{f'{kwargs}' if kwargs else ''}"
                )
            return results
    return _not_empty_results

def require_columns(*table_name: str):
    """
    We want to make sure empty values and null values are
    not possible for required columns
    """

    def _check_empty_row_values(table_row):
        for column_name, column in table_row.columns.items():
            if not column_name in table_row._primary_keys():
                continue
            column_value = (getattr(table_row, column_name)).strip()
            if column_value is None:
                # if column_value is None
                raise NullValuesRead(
                    f"Null value was retrieved for required column: {column_name}"
                    f"at row: {table_row} on {table_name}"
                )
            elif not column_value:
                # column_value is empty string
                raise EmptyValuesRetrieved(
                    f"Empty value was retrieved for required column: {column_name}"
                    f"at row: {table_row} on {table_name}"
                )

    def _columns_required_decorator(function_):
        @wraps(function_)
        def _get_results(*args, **kwargs):
            results = function_(*args, **kwargs)
            if not results:
                pass
            elif isinstance(results, (tuple, list)):
                for result in results:
                    _check_empty_row_values(result)
            else:
                _check_empty_row_values(results)
            return results
        return _get_results
    return _columns_required_decorator


class BaseModel(Model):

    @classmethod
    def _collect_primary_keys(cls, **kwargs):
        """
        get primary keys
        """
        gathered = {}
        for key in cls._primary_keys:
            try:
                gathered[key] = kwargs[key]
            except KeyError:
                raise PrimaryKeyMissingException(f"primary key missing {key}")
        return gathered

    @classmethod
    def _get_partition_keys(cls, **kwargs):
        partition_keys = {}
        for key in cls._partition_keys:
            try:
                partition_keys[key] = kwargs[key]
            except KeyError:
                raise PartitionKeyMissingException(f"missing partition key exception {key}")
        return partition_keys

    @classmethod
    def _get_primary_keys(cls, **kwargs):
        gathered = {}
        for key in cls._primary_keys:
            try:
                gathered[key] = kwargs[key]
            except KeyError:
                raise PrimaryKeyMissingException(f"missing primary key exception {key}")
        return gathered

    @classmethod
    def _get_records_by_primary_keys(cls, **kwargs):
        """
        get rows by primary keys
        """
        try:
            pass
        except Exception as exception:
            raise CassandraReadError(
                f"Error reading data from: '{cls.__table_name__}': {exception}"
            ) from exception

    @classmethod
    def _get_records_by_partial_primary_keys(cls, **kwargs):
        """
        get rows by partial primary keys through non-primary key values
        """
        try:
            cls._collect_primary_keys(**kwargs)
            keys = cls.objects.filter(**cls._collect_primary_keys(**kwargs))
            return [k for k in keys]
        except Exception as exception:
            raise CassandraReadError(
                f"Error reading from '{cls.__table_name__}': {exception}"
            ) from exception



class TimeStampModel(BaseModel):

    create_date = DateTime(default=datetime.now(timezone.utc), clustering_order=True)
    modify_date = DateTime(default=datetime.now(timezone.utc))


class CommonDBValues:
    __keyspace__ = "artworks"






