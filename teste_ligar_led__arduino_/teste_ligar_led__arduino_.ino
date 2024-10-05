int amarelo = 2;
int azul = 3;
int verde = 4;
int branco = 5;
int vermelho = 6;

int am = 0, az = 0, vd = 0, br = 0, vm = 0;

String nome = "";

void setup() {
  Serial.begin(9600);
  pinMode(amarelo, OUTPUT);
  pinMode(azul, OUTPUT);
  pinMode(verde, OUTPUT);
  pinMode(branco, OUTPUT);
  pinMode(vermelho, OUTPUT);

}

void loop() {
  if (Serial.available()){
    int codigo = Serial.read();

    if (codigo == '1'){
      if (am == 0){
          am = 1;
          analogWrite(amarelo, 90);
          Serial.println("Led Amarelo ON");
        } else{
          am = 0;
          analogWrite (amarelo, 0);
          Serial.println("Led Amarelo OFF");
        }
    } else if (codigo == '2'){
      if (az == 0){
            az = 1;
            analogWrite(azul, 50);
            Serial.println("Led Azul ON");
        } else {
            az = 0;
            analogWrite (azul, 0);
            Serial.println("Led Azul OFF");
        }
    } else if (codigo == '3'){
      if (vd == 0){
            vd = 1;
            analogWrite(verde, 50);
            Serial.println("Led Verde ON");
        } else {
            vd = 0;
            analogWrite (verde, 0);
            Serial.println("Led Verde OFF");
        }
    } else if (codigo == '4'){
       if (br == 0){
            br = 1;
            analogWrite(branco, 50);
            Serial.println("Led Branco ON");
        } else {
            br = 0;
            analogWrite (branco, 0);
            Serial.println("Led Branco OFF");
        }
    } else if (codigo == '5'){
      if (vm == 0){
            vm = 1;
            analogWrite(vermelho, 50);
            Serial.println("Led Vermelho ON");
        } else {
            vm = 0;
            analogWrite (vermelho, 0);
            Serial.println("Led Vermelho OFF");
        }
    }
  }
  delay(50);

}
