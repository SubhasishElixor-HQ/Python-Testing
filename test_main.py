from main import get_weather

def test_get_weather():
    assert get_weather(-5) == "It's freezing! Stay warm."
    assert get_weather(-10) == "It's freezing! Stay warm."
    assert get_weather(10) == "The weather is fine. Enjoy your day!."
    assert get_weather(5) == "It's quite cold. Wear a jacket."
# check one by one what i result pass or fail 

# def test_get_weather_cold():
#     assert get_weather(5) == "It's quite cold. Wear a jacket."

# def test_get_weather_cooldown():
#     assert get_weather(15) == "It's cool. A light sweater should be fine."

# def test_get_weather_pleasant():
#     assert get_weather(25) == "The weather is pleasant. Enjoy your day!"

# def test_get_weather_hot():
#     assert get_weather(35) == "It's hot! Stay hydrated and cool."

# multiple test cases for the same function to check different temperature ranges and their corresponding messages.
def test_get_weather_all():
    assert get_weather(-5) == "It's freezing! Stay warm."
    assert get_weather(-10) == "It's freezing! Stay warm."
    assert get_weather(10) == "The weather is fine. Enjoy your day!."