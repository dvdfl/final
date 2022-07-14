
class Actor():
    def __init__(self, body):

        self._body = body

    def get_body(self):
        """Gets the actors's body.
        
        Returns:
            An instance of Body.
        """
        return self._body