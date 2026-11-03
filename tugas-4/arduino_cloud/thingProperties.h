// Konfigurasi Arduino IoT Cloud
#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>

const char DEVICE_LOGIN_NAME[]  = "YOUR_DEVICE_ID";
const char SSID[]               = "NAMA_WIFI";
const char PASS[]               = "PASSWORD_WIFI";
const char DEVICE_KEY[]         = "YOUR_SECRET_DEVICE_KEY";

void onRelaySwitchChange();

float temperature;
float humidity;
bool relaySwitch;

void initProperties() {
  ArduinoCloud.setBoardId(DEVICE_LOGIN_NAME);
  ArduinoCloud.setSecretDeviceKey(DEVICE_KEY);

  ArduinoCloud.addProperty(temperature, READ, 10 * SECONDS, NULL);
  ArduinoCloud.addProperty(humidity, READ, 10 * SECONDS, NULL);
  ArduinoCloud.addProperty(relaySwitch, READWRITE, ON_CHANGE, onRelaySwitchChange);
}

WiFiConnectionHandler ArduinoIoTPreferredConnection(SSID, PASS);
