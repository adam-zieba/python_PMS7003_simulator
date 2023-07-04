
import random
import json

# Generate measurements

def generate_json_measurements():
    json_format = {
        'pm1_0cf1': generate_pm10cf1(),
        'pm2_5cf1': generate_pm2_5cf1(),
        'pm10cf1': generate_pm10cf1(),
        'pm1_0': generate_pm1_0cf1(),
        'pm2_5': generate_pm2_5(),
        'pm10': generate_pm10(),
        'n0_3': generate_n0_3(),
        'n0_5': generate_n5_0(),
        'n1_0': generate_n1_0(),
        'n2_5': generate_n2_5(),
        'n5_0': generate_n5_0(),
        'n10': generate_n10()
    }
    return json.dumps(json_format)


def generate_pm1_0cf1():
    return random.randrange(1, 100)

def generate_pm2_5cf1():
    return random.randrange(1, 100)

def generate_pm10cf1():
    return random.randrange(1, 100)

def generate_pm1_0():
    return random.randrange(1, 100)

def generate_pm2_5():
    return random.randrange(1, 100)

def generate_pm10():
    return random.randrange(1, 100)

def generate_n0_3():
    return random.randrange(1000, 2000)

def generate_n0_5():
    return random.randrange(100, 500)

def generate_n1_0():
    return random.randrange(1, 100)

def generate_n2_5():
    return random.randrange(1, 100)

def generate_n5_0():
    return random.randrange(1, 100)

def generate_n10():
    return random.randrange(1, 10)