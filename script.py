# This is a collection of half ready manual functions to move a spider around.
from collections import namedtuple
from gpiozero import LED
from time import sleep

# while b.wait_for_press():
#   random.choice(l).toggle()
#   print 'Hello, Slava!'
#   _ = b.wait_for_release()

breadboard_port_mapping = {
    'p0': 17,
    'p1': 18,
    'p2': 27,
    'p3': 22,
    'p4': 23,
    'p5': 24,
    'p6': 25,
    'p7': 4,
    'ce1': 7,
    'ce0': 8,
    'sclk': 11,
    'miso': 9,
    'mosi': 10,
    'rxd': 15,
    'txd': 14,
    'scl': 3,
    'sda': 2
}

T_BB_PORTS = namedtuple('BB_PORTS', breadboard_port_mapping.keys())
BB_PORTS = T_BB_PORTS(**breadboard_port_mapping)

class Spider(object):
    def __init__(self, left_leg_pin, right_leg_pin, legs_power_pin, attack_pin):
        self.left_leg = LED(left_leg_pin, initial_value=1)
        self.right_leg = LED(right_leg_pin, initial_value=1)
        self.legs_power = LED(legs_power_pin, initial_value=1)
        self.attack_trigger = LED(attack_pin, initial_value=1)
    def attack(self):
        self.attack_trigger.off()
    def stop_attack(self):
        self.attack_trigger.on()
    def forward(self, duration=None):
        self.legs_power.on()
        self.left_leg.on()
        self.right_leg.on()
        self.legs_power.off()
        if duration:
           sleep(duration)
           self.stop()
    def backward(self, duration=None):
        self.legs_power.on()
        self.left_leg.off()
        self.right_leg.off()
        self.legs_power.off()
        if duration:
           sleep(duration)
           self.stop()
    def rotate_left(self, duration=None):
        self.legs_power.on()
        self.left_leg.off()
        self.right_leg.on()
        self.legs_power.off()
        if duration:
           sleep(duration)
           self.stop()
    def rotate_right(self, duration=None):
        self.legs_power.on()
        self.left_leg.on()
        self.right_leg.off()
        self.legs_power.off()
        if duration:
           sleep(duration)
           self.stop()
    def stop(self):
        self.legs_power.on()
    def reset(self):
        self.legs_power.on()
        self.left_leg.on()
        self.right_leg.on()
        self.attack_trigger.on()

s = Spider(BB_PORTS.p0, BB_PORTS.p1, BB_PORTS.p2, BB_PORTS.p3)
