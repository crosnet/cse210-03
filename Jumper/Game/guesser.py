import random

class Word:
    """The random to be guessed by the jumper. 
    
    The responsibility of Word is to store a random word for the jumper to make a guess at it.
    
    Attributes:
        word (List[str]): The randomly chosen word (marker, book)
        letter (str): The letters of the randomly chosen word
    """

    def __init__(self):
        """Constructs a new Word.

        Args:
            self (Word): An instance of Word.
        """
        self._word = random.choice('marker', 'book')
        self._letter = [''] # start with empty string so get_hint always works
    
    def get_hint(self):
        """Gets a hint for the Jumper.

        Args:
            self (Word): An instance of Word.
        
        Returns:
            string: A hint for the Letter.
        """
        hint = "(-.-) Nap time."
        if self._word == 'marker':
            self.letter.append('m', 'a', 'r', 'k', 'e', 'r')
            if letter == self._letter:
                hint = "You guessed right"
            else: 
                hint = 'try again'
        elif self._word == 'book':
            self.letter.append('b', 'o', 'o', 'k')
            if letter == self._letter:
                hint = "You guesses right"
            else: 
                hint = 'try again'
        return hint

    def guessed_right(self):
        """Whether or not the letters has been guessed right.

        Args:
            self (Word): An instance of Word.
            
        Returns:
            boolean: True if the word was found; false if otherwise.
        """
        return letter == self._letter
        