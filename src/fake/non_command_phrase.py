from random import randint


class NonCommandPhrase:
    def __init__(self):
        self._non_command_phrases = [
            'This is not a command!',
            'Don\'t repeat this error again!',
            'Should you send me a valid command!',
            'No, no, no... This is not a command!',
            'Ha ha ha, try a valid command now!'
        ]

    def retrieve_random_phrase(self):
        return self._non_command_phrases[randint(
            0,
            len(self._non_command_phrases)
        )]
