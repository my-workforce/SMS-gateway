# -*- coding: utf-8 -*-

"""
    unifonicnextgen

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SendScheduledmessagesResponse(object):

    """Implementation of the 'Send scheduledmessages response' model.

    Schedules one message to be sent in the future.

    Attributes:
        success (bool): The request sent successfully
        message (string): The Error message if its false, Null if its true
        error_code (string): The error code if there is any
        status (string): Accepted or Rejected

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "success":'success',
        "message":'message',
        "error_code":'errorCode',
        "status":'Status'
    }

    def __init__(self,
                 success=None,
                 message=None,
                 error_code=None,
                 status=None):
        """Constructor for the SendScheduledmessagesResponse class"""

        # Initialize members of the class
        self.success = success
        self.message = message
        self.error_code = error_code
        self.status = status


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        success = dictionary.get('success')
        message = dictionary.get('message')
        error_code = dictionary.get('errorCode')
        status = dictionary.get('Status')

        # Return an object of this model
        return cls(success,
                   message,
                   error_code,
                   status)


