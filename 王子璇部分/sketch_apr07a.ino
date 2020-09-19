#define AP_SSID "     。"     // wifi账号         
#define AP_PSW "guoxuemaster"  // wifi密码            
const char *host = "192.168.43.157"; //主机地址
const uint16_t port = 8266; // 端口号       
#include <ESP8266WiFi.h>  // 导入WiFi模块
#include <MLX90615.h>  // 导入MLX90615驱动程序
WiFiClient client;   // client对象
MLX90615 mlx90615(0x5B, &Wire); 
int flag = 0;
char msg = ' '; 

void setup()
{
  Serial.begin(9600); //设置波特率
  Wire.begin();
  WiFi.mode(WIFI_STA); 
  WiFi.begin(AP_SSID, AP_PSW);   //连接wifi
  Serial.print("\r\n\r\nConnecting to ");
  Serial.println(AP_SSID);
  while (WiFi.status() != WL_CONNECTED) // 可视化连接过程
  {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\r\nWiFi connected.\r\nIP addrrss:");
  Serial.println(WiFi.localIP());
  flag = client.connect(host, port); //连接服务器
  if (!flag)
  {
    Serial.println("Connection TCP server failed");
  }
}

void loop()
{
  while(flag == 0){ // 不断链接服务器
    Serial.print(".");
    flag = client.connect(host, port); 
    }
  delay(1000);
  if(client.available()>0) //判断缓存区是否有数据
  {
    msg=client.read(); //读缓存区数据
  }
  if(msg=='0')
  {
  float Object_Temp = mlx90615.getTemperature(0x27); //读目标温度
  float Ambient_Temp = mlx90615.getTemperature(0x26);//读环境温度
  Serial.print("目标温度: ");
  Serial.println(Object_Temp);
  Serial.print("环境温度: ");
  Serial.println(Ambient_Temp);
  Serial.println();
  
  //向服务器发送json格式的温度数据
  String Json_array = "{\"Temp1\":" + String(Object_Temp) + ",\"Temp2\":" + String(Ambient_Temp) + "}"; 
  client.print(Json_array);
  Serial.println("Send Json Success");
  msg=' ';
  }
  else {
    msg = ' ';
    }
}
