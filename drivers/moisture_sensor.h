#pragma once

#include "nrf.h"
#include "gpio.h"




typedef struct {
    uint8_t id;
    uint16_t sensitivity;
    uint16_t bias;
    uint16_t adc_val;
} moisture_sensor_t;

void init(moisture_sensor_t *sensor, uint16_t id, uint16_t sens, uint16_t bias, uint16_t adc){
    sensor->id = id;
    sensor->sensitivity = sens;
    sensor->bias = bias;
    sensor->adc_val = adc;
}

uint




