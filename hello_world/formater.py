PLAIN = "plain"
PLAIN_UP = "plain_uppercase"
PLAIN_LO = "plain_lowercase"
JSON = "json"

SUPPORTED = [PLAIN, PLAIN_UP, PLAIN_LO, JSON]


def get_formatted(msg, moje_imie, format):
    result = ""
    if format == PLAIN:
        result = plain_text(msg, moje_imie)
    elif format == PLAIN_UP:
        result = plain_text_upper_case(msg, moje_imie)
    elif format == PLAIN_LO:
        result = plain_text_lower_case(msg, moje_imie)
    elif format == JSON:
        result = format_to_json(msg, moje_imie)
    return result


def format_to_json(msg, moje_imie):
    return ('{ "imie":"' + moje_imie + '", "mgs":' +
            msg + '"}')


def plain_text(msg, moje_imie):
    return moje_imie + ' ' + msg


def plain_text_upper_case(msg, moje_imie):
    return plain_text(msg.upper(), moje_imie.upper())


def plain_text_lower_case(msg, moje_imie):
    return plain_text(msg.lower(), moje_imie.lower())
