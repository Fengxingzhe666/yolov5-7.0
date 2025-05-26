import smbus
import argparse

device_address = 0x2d  # 设备的 I2C 地址
bus = smbus.SMBus(2)  # 使用 I2C 总线 x

def send_control_message(id,degree):
    bus.write_byte_data(device_address,id,degree)
    # print("sg90 id:"+id+" rotated to"+degree+"degree")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--id',type=int)
    parser.add_argument('--degree',type=int)
    opt = parser.parse_args()
    send_control_message(**vars(opt))
