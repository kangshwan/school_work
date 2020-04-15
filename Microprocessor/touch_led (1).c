#include <wiringPi.h>
#include <stdio.h>

#define TOUCH_PIN 6
#define LED_PIN 7

int main(void){
        int touch, i, led_state;

        if(wiringPiSetup() == -1) return 1;
        pinMode(TOUCH_PIN, INPUT);
	    pinMode(LED_PIN,OUTPUT);

		led_state = 0;   
        while(1){
        	touch = digitalRead(TOUCH_PIN);
			if(touch){
				printf("Pressed\n");
				if(led_state == 0){
					digitalWrite(LED_PIN, HIGH);
					led_state = 1;
				}else{
					digitalWrite(LED_PIN, LOW);
					led_state = 0;
				}
			}
			delay(100);
     	}
}
