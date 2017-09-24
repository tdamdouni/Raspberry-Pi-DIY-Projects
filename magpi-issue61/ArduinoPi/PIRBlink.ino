/*
 * Blinks two LEDs when motion detected
 */

//variables
int led1 = 5;
int led2 = 6;
int motion = 3;
int wait = 500; //500ms = 1/2s

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(motion,INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(motion) == HIGH){
    digitalWrite(led1,HIGH);
    digitalWrite(led2,HIGH);
    delay(wait);
    digitalWrite(led1,LOW);
    digitalWrite(led2,LOW);
    delay(wait);
    }
}

