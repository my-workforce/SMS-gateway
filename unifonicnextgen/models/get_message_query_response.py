# -*- coding: utf-8 -*-

"""
    unifonicnextgen

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class GetMessageQueryResponse(object):

    """Implementation of the 'Get Message Query response' model.

    Gets details of specified message

    Attributes:
        status_05 (string): The message statues

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status_05":'STATUS05'
    }

    def __init__(self,
                 status_05=None):
        """Constructor for the GetMessageQueryResponse class"""

        # Initialize members of the class
        self.status_05 = status_05


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
        status_05 = dictionary.get('STATUS05')

        # Return an object of this model
        return cls(status_05)


