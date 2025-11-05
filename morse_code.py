from .symbols import MORSE_SYMBOL_TO_LETTER, InvalidSymbolError


def append_morse_symbol(message: str, symbol: str) -> str:
    """
    Decodes a Morse code symbol and appends the corresponding character to the
    message.

    Args:
        message (str): current message string being built.
        symbol (str): morse code symbol to be translated
        (e.g., ".-", ".----", "......").

    Returns:
        str: The updated message with the translated symbol appended, or with
        the last character removed if the symbol is "del".

    Raises:
        InvalidSymbolError: If the symbol is not a valid Morse code character.
    """
    try:
        # if symbol in MORSE_SYMBOL_TO_LETTER:
        a = MORSE_SYMBOL_TO_LETTER[symbol]
        if a == "del":
            ret = ""
            for i in range(len(message)-1):
                ret = ret + message[i]
            return ret
        return message + a
    except:
        # else:
        raise InvalidSymbolError()


def translate_message(morse: str) -> str:
    """
    Translates a Morse code message into an English string.

    Args:
        morse (str): A series of Morse code symbols separated by "/". Each 
        symbol can represent a letter, number, or space.

    Returns:
        str: The translated English message. If any invalid symbols are 
        encountered, they are ignored. If the last potential symbol is not 
        valid, it is appended as is (i.e., as dots and dashes).
    """
    morse_list = morse.split("/")
    eng_string = ""
    for i in range(len(morse_list)-1):
        try:
            eng_string = append_morse_symbol(eng_string, morse_list[i])
        except:
            eng_string = eng_string
    eng_string = eng_string + morse_list[-1]
    return eng_string
