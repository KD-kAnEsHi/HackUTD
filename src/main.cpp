#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>
#include <ArduinoHttpClient.h>

#define LIGHT A0
#define LED_GREEN D2
#define LED_BLUE D8
#define DHTPIN 5 //Pin D1
DHT dht(DHTPIN, DHT11);

// Constants for converting light readings to sunlight hours
const float SLOPE = 0.008973932015694326;
const float INTERCEPT = 1.1017652451321922;

//Setup Json file
//StaticJsonDocument<200> sensor_data;
JsonDocument sensor_data;

//Setup Request Delay
unsigned long lastTime = 0;
unsigned long timerDelay = 5000; //5s delay

float lightToSunlight(int lightLevel) {
    return SLOPE * lightLevel + INTERCEPT; //linear regression curve
}

//Set WIFI Credentials
const char* ssid = "AADESH-X13";
const char* pass = "3Xc0]363";
bool timeout = false;
int counter = 0;

//Set flask server
char serverAddress[] = "mongodb://localhost"; //ADD SERVER IP-ADDRESS
int port = 27017;

WiFiClient wifi;
HttpClient client = HttpClient(wifi, serverAddress, port);

void setup() {
    Serial.begin(9600);
    delay(10);

    Serial.println("Connecting to...");
    Serial.println(ssid);
    WiFi.begin(ssid, pass);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
        counter++;
        if (counter > 30) {
            timeout = true;
            break;
        }
    }
    if (!timeout) {
        Serial.println("");
        Serial.println("WiFi connected"); 
        Serial.println('\n');
        Serial.println("Connection established!");  
        Serial.print("IP address:\t");
        Serial.println(WiFi.localIP());
    }
    else {
        Serial.println("WiFi connection FAILED");
    }

    dht.begin();
    delay(2000);

    pinMode(LIGHT,INPUT);
    pinMode(LED_GREEN, OUTPUT);
    pinMode(LED_BLUE, OUTPUT);

    Serial.println("Light Level, Temperature, Humidity");
}

void loop() {
    int lightLevel = analogRead(LIGHT);
    float sunLightHours = lightToSunlight(lightLevel);
    float temp = dht.readTemperature();
    float humidity = dht.readHumidity();

    Serial.print(sunLightHours);
    Serial.print(", ");
    Serial.print(temp);
    Serial.print(" C, ");
    Serial.print(humidity);
    Serial.print(" %\n");

    if ((millis() - lastTime) > timerDelay) {
        
        //http.begin(serverName);
        //http.addHeader("Content-Type", "app/json");

        String jsonString = "";
        JsonObject object = sensor_data.to<JsonObject>();
        object["humidity"] = humidity;
        object["Light"] = sunLightHours;
        object["Temperature"] = temp;
        object["Sensor_id"] = "1";
        object["Location"] = "row 1";
        object["Enabled"] = "true";
        object["Type_sensor"] = "x";

        //serialize the object and store it
        String postData;
        serializeJson(sensor_data, postData);

        //Send data to web server
        String contentType = "app/sensor_data-from-ESP32";
        
        client.post("/app_json", contentType, postData);
        
        int statusCode = client.responseStatusCode();
        String response = client.responseBody();

        if (statusCode < 300) {
            digitalWrite(LED_BLUE, HIGH);
            delay(100);
            digitalWrite(LED_BLUE, LOW);
        }



    }

    digitalWrite(LED_GREEN, LOW);
    delay(5000);
    digitalWrite(LED_GREEN, HIGH);

}
