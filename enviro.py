#!/usr/bin/env python3

from time import sleep

from numpy import disp
from enviroplus import gas
import logging
import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont

#Create LCD class instance
disp = ST7735.ST7735(
    port = 0,
    cd = 1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

disp.begin()
WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0,0,0))


while True:
    readings = gas.read_all()
    logging.info(readings)
    sleep(1)
