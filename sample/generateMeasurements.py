
import random

# Generate measurements

def generate_json_measurements():
    return {
        'pm1_0cf1': generate_pm10cf1()
    }


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