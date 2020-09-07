#include <MLX90615.h>
MLX90615 mlx90615(MLX90615_DefaultAddr, &Wire);
void setup() {
    Serial.begin(9600);
    delay(2000);
    Serial.println("Setup...");
    Wire.begin();
}

void loop() {
    Serial.print("目标温度: ");
    Serial.println(mlx90615.getTemperature(MLX90615_OBJECT_TEMPERATURE));
    Serial.print("环境温度: ");
    Serial.println(mlx90615.getTemperature(MLX90615_AMBIENT_TEMPERATURE));
    delay(1000);
}
