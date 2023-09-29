trigPin = 12
echoPin = 10
vcc = 13
gnd = 10
duration = 0
distance = 0

def setup():
    global duration, distance
    pinMode(1, OUTPUT)
    pinMode(2, OUTPUT)
    pinMode(3, OUTPUT)
    pinMode(trigPin, OUTPUT)
    pinMode(echoPin, INPUT)
    pinMode(vcc, OUTPUT)
    pinMode(gnd, OUTPUT)
    digitalWrite(vcc, HIGH)
    digitalWrite(gnd, LOW)
    Serial.begin(9600)

def loop():
    global duration, distance
    digitalWrite(trigPin, HIGH)
    delayMicroseconds(10)
    digitalWrite(trigPin, LOW)
    distance = duration * 0.034 / 2
    Serial.print("Distance:")
    Serial.println(distance)
    delay(1000)
    if distance < 50:
        digitalWrite(1, HIGH)
        delay(1000)
        digitalWrite(2, HIGH)
        delay(1000)
        digitalWrite(3, HIGH)
        delay(1000)
    else:
        digitalWrite(1, LOW)
        delay(1000)
        digitalWrite(2, LOW)
        delay(1000)
        digitalWrite(3, LOW)
        delay(1000)

setup()
while True:
    loop()