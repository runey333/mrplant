#pragma once

#include "nrf.h"
#include "gpio.h"



void sensor_init(uint8_t gpio_num, gpio_direction_t dir){
    gpio_config(gpio_num, dir);


}
