#pragma once

#include "nrf.h"
#include "stdbool.h"
#include <stdint.h>

#define GPIO_first ((GPIO1*) 0x50000500)
#define GPIO_second ((GPIO2*) 0x50000700)

typedef enum {
    INPUT = 0,
    OUTPUT,
} gpio_direction_t;

// Inputs: 
//  gpio_num - gpio number 0-31
//  dir - gpio direction (INPUT, OUTPUT)
void gpio_config(uint8_t gpio_num, gpio_direction_t dir);

// Inputs: 
//  gpio_num - gpio number 0-31
void gpio_set(uint8_t gpio_num);

// Inputs: 
//  gpio_num - gpio number 0-31
void gpio_clear(uint8_t gpio_num);

// Inputs: 
//  gpio_num - gpio number 0-31
// Returns:
//  current state of the specified gpio pin
bool gpio_read(uint8_t gpio_num);

typedef struct {
  uint32_t P0;
  uint32_t OUT;
  uint32_t OUTSET;
  uint32_t OUTCLR;
  uint32_t IN;
  uint32_t DIR;
  uint32_t DIRSET;
  uint32_t DIRCLR;
  uint32_t LATCH;
  uint32_t DETECTMODE;
} GPIO1; 

typedef struct{
  uint32_t PIN_0;
  uint32_t PIN_1;
  uint32_t PIN_2;
  uint32_t PIN_3;
  uint32_t PIN_4;
  uint32_t PIN_5;
  uint32_t PIN_6;
  uint32_t PIN_7; 
  uint32_t PIN_8;
  uint32_t PIN_9;
  uint32_t PIN_10;
  uint32_t PIN_11;
  uint32_t PIN_12;
  uint32_t PIN_13;
  uint32_t PIN_14;
  uint32_t PIN_15;
  uint32_t PIN_16;
  uint32_t PIN_17;
  uint32_t PIN_18;
  uint32_t PIN_19;
  uint32_t PIN_20;
  uint32_t PIN_21;
  uint32_t PIN_22;
  uint32_t PIN_23;
  uint32_t PIN_24;
  uint32_t PIN_25;
  uint32_t PIN_26;
  uint32_t PIN_27;
  uint32_t PIN_28;
  uint32_t PIN_29;
  uint32_t PIN_30;
  uint32_t PIN_31;
} GPIO2;