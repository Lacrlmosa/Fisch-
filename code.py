import time
import board
import pwmio
import random

motor_pwm = pwmio.PWMOut(board.GP5, frequency=1000)

weighted_values = [
    {"value": 0.02, "weight": 2},
    {"value": 0.03, "weight": 2},
    {"value": 0.04, "weight": 2},
    {"value": 0.05, "weight": 2},
    {"value": 0.06, "weight": 2},
    {"value": 0.07, "weight": 2},
    {"value": 0.08, "weight": 2},
    {"value": 0.09, "weight": 2},
    {"value": 0.1, "weight": 2},
    {"value": 0.2, "weight": 2},
    {"value": 0.3, "weight": 2},
    {"value": 0.4, "weight": 2},
    {"value": 0.5, "weight": 2},
    {"value": 0.6, "weight": 2},
    {"value": 0.7, "weight": 2},
    {"value": 0.8, "weight": 2},
    {"value": 0.9, "weight": 2},
    {"value": 1, "weight": 2},
    {"value": 1.1, "weight": 2},
    {"value": 1.2, "weight": 2},
    {"value": 1.3, "weight": 2},
    {"value": 1.4, "weight": 2},
    {"value": 1.5, "weight": 2},
    {"value": 1.6, "weight": 2},
    {"value": 1.7, "weight": 2},
    {"value": 1.8, "weight": 2},
    {"value": 1.9, "weight": 2},
    {"value": 2, "weight": 2},
    {"value": 3, "weight": 1},
    {"value": 4, "weight": 1},
    {"value": 5, "weight": 1},
]

weighted_list = []
for item in weighted_values:
    weighted_list.extend([item["value"]] * item["weight"])

def choose_weighted():
    return random.choice(weighted_list)

while True:
    on_duration = random.uniform(0.02, 0.09)
    motor_pwm.duty_cycle = 65535  # Motor ein
    time.sleep(on_duration)

    off_duration = choose_weighted()  # Auswahl eines zufälligen, gewichteten Off-Wertes
    motor_pwm.duty_cycle = 0  # Motor aus
    print(f"Motor aus für {off_duration} Sekunden")  # Zum Testen des Off-Werts
    time.sleep(off_duration)
