
const int button = 2;
const int led = 8;

void setup() {
  pinMode(button, INPUT_PULLUP);
  pinMode(led, OUTPUT);
}

void loop() {
  if (digitalRead(button) == HIGH) {
    // Button released: LED ON
    digitalWrite(led, HIGH);
  }
  else {
    // Button pressed: LED OFF
    digitalWrite(led, LOW);
  }
}
