from web.app import format_messages

def test_format_messages():
    format_messages([
        ('hello',),
        ('hello2',),
    ]
    ) == [
        'hello',
        'hello2',
    ]
