from game.terminal_service import TerminalService
from game.guesser import Word
from game.jumper import Jumper


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): The game's word.
        is_playing (boolean): Whether or not to keep playing.
        jumper (Jumper): The game's jumper.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._guesser = Word()
        self._is_playing = True
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_outputs()

    def _get_inputs(self):
        """Gets a random word

        Args:
            self (Director): An instance of Director.
        """
        new_letter = self._terminal_service.read_number("\nEnter a letter: ")
        self._jumper.guess_letter(new_letter)
        
    def _do_outputs(self):
        """Provides a hint for the jumper to use.

        Args:
            self (Director): An instance of Director.
        """
        hint = self._guesser.get_hint()
        self._terminal_service.write_text(hint)
        if self._guesser.is_found():
            self._is_playing = False