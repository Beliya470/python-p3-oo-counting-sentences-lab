#!/usr/bin/env python3

class MyString:

    def __init__(self, value=''):
        self._value = value  # Directly set _value, the setter will validate during subsequent assignments

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        """Returns True if the string ends with a period, else returns False."""
        return self.value.endswith('.')

    def is_question(self):
        """Returns True if the string ends with a question mark, else returns False."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Returns True if the string ends with an exclamation mark, else returns False."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Returns the count of sentences in the string. Considers sentences ending with '.', '!' or '?' as valid."""
        # Replacing all sentence ending punctuations with a common one for easier splitting
        modified_str = self.value.replace('!', '.').replace('?', '.')
        
        # Split the string using '.'
        sentences = modified_str.split('.')
        
        # Filter out empty sentences or ones that are just spaces and return the count
        return len([sentence for sentence in sentences if sentence.strip() != ''])

# Testing the MyString class
string = MyString("This is a string! It has three sentences. Right?")
print(string.count_sentences())  # Expected output: 3
