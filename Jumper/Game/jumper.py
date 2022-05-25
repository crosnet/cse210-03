import random

class Jumper:
    """The person guessing the letters of the randomly chosen word. 
    
    The responsibility of the Jumper is to guess the letters of a randomly chosen word.
    
    Attributes:
        letter (str): The letters of the randomly chosen word
        word (List[str]): The randomly chosen word (marker, board, pen, pencil, textbook)
    """

    def __init__(self):
        """Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """
        self._word = random.choice('marker', 'board', 'pen', 'pencil', 'texbook')
        
    def get_word(self):
        """Gets the random word.
        
        Returns:
            string: The random word,
        """
        return self._word
        
    def guess_letter(self, letter):
        """Guesses a letter from the random word.

        Args:
            self (Seeker): An instance of Jumper.
            letter (str): a letter.
        """
        self._letter = letter

  