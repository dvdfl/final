
class Label():
    """A label to be displayed."""
 
    def __init__(self, text, position, debug = False):
        """Constructs a new Label.

        Args:
            text: An instance of Text.
            position: An instance of Point.
        """
        self._text = text
        self._position = position
        
    def get_position(self):
        """Gets the label's position.

        Returns:
            An instance of Point.
        """
        return self._position
    
    def get_text(self):
        """Gets the label's text.
        
        Returns:
            An instance of Text.
        """
        return self._text    