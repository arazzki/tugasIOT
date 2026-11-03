/*
 * Tugas 2 - Internet of Things (ITH3V3)
 * Soal No 5: Program Konversi Radiks Bilangan (Biner, Heksa, Oktal)
 * Deskripsi: Membaca input nilai desimal melalui Serial Monitor (atau pengujian otomatis)
 *            dan mengonversinya ke representasi Biner, Heksadesimal, dan Oktal pada ESP32/ESP8266.
 */

void setup() {
  Serial.begin(115200);
  while (!Serial) { delay(10); }

  Serial.println("\n=======================================================");
  Serial.println("  TUGAS 2 IOT: KONVERSI NILAI RADIK BILANGAN (ESP32)");
  Serial.println("=======================================================");
  Serial.println("Ketik sebuah bilangan bulat desimal di Serial Monitor lalu tekan Enter.");
  Serial.println("Atau perhatikan demo otomatis berikut ini:\n");

  // Demo otomatis beberapa bilangan sampel
  unsigned long sampleValues[] = {42, 127, 255, 1024, 65535};
  for (int i = 0; i < 5; i++) {
    tampilkanKonversi(sampleValues[i]);
    delay(500);
  }
}

void loop() {
  if (Serial.available() > 0) {
    long inputVal = Serial.parseInt();
    // Bersihkan buffer sisa newline
    while (Serial.available() > 0) { Serial.read(); }

    if (inputVal != 0 || Serial.peek() == '0') {
      tampilkanKonversi(inputVal);
    }
  }
}

void tampilkanKonversi(unsigned long val) {
  unsigned long startMicros = micros();

  Serial.println("-------------------------------------------------------");
  Serial.printf("Nilai Desimal (Base 10) : %lu\n", val);
  
  // Format Biner (Base 2)
  Serial.print("Format Biner   (Base 2)  : 0b");
  Serial.println(val, BIN);

  // Format Heksa (Base 16)
  Serial.print("Format Hexa    (Base 16) : 0x");
  Serial.println(val, HEX);

  // Format Oktal (Base 8)
  Serial.print("Format Oktal   (Base 8)  : 0o");
  Serial.println(val, OCT);

  unsigned long execTime = micros() - startMicros;
  Serial.printf("Waktu Eksekusi Konversi  : %lu mikrosekon (µs)\n", execTime);
  Serial.println("-------------------------------------------------------\n");
}
