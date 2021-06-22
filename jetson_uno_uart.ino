/* 
 *  Date: 2021-06-22
 *  Author: Park Kuyeon
 *  Title: Jetson - Arduino UNO UART Program
 *  Description: This is the code about the UNO recieving data from the Jetson
 *              and controls the LED attatched on the UNO and sends LED status to the Jetson.
 *              
 * 
 */


int LED = 13;
char data;


void setup() {
  //Serial.begin(9600);   // if using Serial Monitor
  Serial1.begin(9600);    // using TX(1), RX(0) pin
  pinMode(LED, OUTPUT);   // LED pin mode setup
}


void loop() {
  while(Serial1.available()){
    data = (char)Serial1.read();    // Receive data from the Jetson
    if(data == '1'){
      digitalWrite(LED, HIGH);
      Serial1.print("LED ON\n");    // Send data to the Jetson
    }
    else if(data == '0'){
      digitalWrite(LED, LOW);
      Serial1.print("LED OFF\n");   // Send data to the Jetson
    }
  }
}
