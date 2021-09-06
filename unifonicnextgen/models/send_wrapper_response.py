# -*- coding: utf-8 -*-

"""
    unifonicnextgen

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class SendWrapperResponse(object):

    """Implementation of the 'Send Wrapper response' model.

    Sends message to one or more recipients.

    Attributes:
        error (string): The default error code
        message_id (string): A unique ID that identifies a message

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error":'Error',
        "message_id":'MessageID'
    }

    def __init__(self,
                 error=None,
                 message_id=None):
        """Constructor for the SendWrapperResponse class"""

        # Initialize members of the class
        self.error = error
        self.message_id = message_id


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
        error = dictionary.get('Error')
        message_id = dictionary.get('MessageID')

        # Return an object of this model
        return cls(error,
                   message_id)


