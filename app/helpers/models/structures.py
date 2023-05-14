from typing import Any, Dict, Optional
from cassandra.cqlengine.columns import (
    Ascii,
    DateTime,
    Map,
    Integer,
    List,
    UUID,
    Blob,
    Text,
    BigInt,
    Boolean
)
from pydantic import BaseModel, ValidationError, root_validator
from .base import (
    not_empty_result,
    require_columns,
    BaseModel,
    TimeStampModel,
    CommonDBValues
)


class ContactUs(TimeStampModel):
    __table_name__ = 'contact_us'

    transaction_id = UUID()
    email_address = Ascii(primary_key=True, partition_key=True, min_length=1)
    message = Text(min_length=1, max_length=300)
    first_name = Ascii(min_length=1, max_length=40)
    last_name = Ascii(min_length=1, max_length=16)
    feedback = Boolean()

    @classmethod
    @require_columns(__table_name__)
    @not_empty_result(
        "Requested data doesn't exists"
        "combination of email_address, last_name")
    def retrieve_contacted_info(cls, email_address: str, last_name: str):
        return cls._get_record_by_primary_keys(
            email_address=email_address,
            last_name=last_name,
        )

    @classmethod
    def retrieve_customer_feedback(cls, email_address: str, last_name: str, feedback: bool):
        return cls._get_record_by_partial_primary_keys(
            email_address=email_address,
            last_name=last_name,
            feedback=feedback
        )


class ImagePosts(TimeStampModel):

    __table_name__ = "painting_images"

    post_id = UUID()
    post_name = Ascii()
    painting_image = Blob()

    @staticmethod
    def retrieve_all_posts():
        pass


class VideoPosts(TimeStampModel):

    __table_name__ = "painting_videos"

    post_id = UUID()
    video_name = Ascii()
    painting_video = Blob()





