int ledPin = 13;
int inPins[] = {2, 3, 4, 5, 6, 7, 8, 9};
int value = 0;

void setup(){
  for (int i = 0; i < 8; i++){
    pinMode(inPins[i], INPUT);
    digitalWrite(inPins[i], HIGH);
  }
  Serial.begin(9600);
}

void loop(){
  for (int i = 0; i < 8; i++){
    if (digitalRead(inPins[i]) == LOW){
      Serial.print(i);
    }
  }
}
