# YOLOv5在ARM端部署-sg90驱动舵机对准目标无人机  
本项目fork的yolov5模型开源地址：https://github.com/ultralytics/yolov5  

## 硬件参数，连接方式  
OrangePi_3b开发板，已装官方ubuntu镜像  
二维sg90舵机云台+摄像头，外加16路i2c通信驱动板  
根据开发板手册，将OrangePi_3b开发板的40pin接口中的i2c-2接口部分与驱动板的i2c相连，具体方式见手册。  

新增文件说明：  
detect_zzk.py  
与detect.py相比改动如下：将sorce固定为0，即摄像头的输入作为源，将weight固定为"runs/train/custom_model05/weights/best.pt"，这是我提前迁移训练的无人机检测器。新增了i2c通信模块，每当检测到一个无人机目标，会给舵机驱动进行i2c通信，传输需要转动的角度，一共有2个sg90舵机在2个维度上进行旋转。  
  
capture_camera_image.py
捕捉摄像头视频流并显示，在ubuntu命令行上运行：  
```
python3 capture_camera_image.py
```
会显示当前摄像头的实时画面。  
  
serial_comm-i2c.py
与sg90舵机驱动进行i2c的示例代码，指定某个舵机转动到目标角度，例如想将1号舵机转到90度，在ubuntu命令行上运行：
```
python3 serial_comm-i2c.py --id 1 --degree 90
```
