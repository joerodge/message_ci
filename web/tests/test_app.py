from web.app import format_messages

def test_stuff():
    assert format_messages([
        ('hello',),
        ('hello2',),
    ]) == [
        'hello',
        'hello2',
    ]
