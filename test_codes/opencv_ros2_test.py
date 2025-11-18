#!/usr/bin/env python3
# coding=utf-8

import rclpy
from rclpy.node import Node
from cv_bridge import CvBridge
import cv2
from sensor_msgs.msg import Image

# 定义一个图片转换的类，功能为：订阅ROS图片消息并转换为OpenCV格式处理，处理完成再转换回ROS图片消息后发布
class ImageConverter(Node):
    def __init__(self):
        super().__init__('opencv_bridge')
        self.bridge = CvBridge()
        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.callback,
            10)
        self.publisher_ = self.create_publisher(Image, 'cv_bridge_image', 10)
        self.get_logger().info('cv_bridge_test node started')

    def callback(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f"Failed to convert image: {e}")
            return

        (rows, cols, channels) = cv_image.shape
        if cols > 40 and rows > 40:
            cv2.circle(cv_image, (40, 40), 40, (0, 0, 255), 2)

        try:
            self.publisher_.publish(self.bridge.cv2_to_imgmsg(cv_image, encoding='bgr8'))
        except Exception as e:
            self.get_logger().error(f"Failed to convert image back: {e}")

        cv2.circle(cv_image, (40, 40), 20, (0, 255, 0), 2)
        cv2.namedWindow("cv_image", cv2.WINDOW_NORMAL)
        cv2.imshow("cv_image", cv_image)
        cv2.waitKey(10)

def main(args=None):
    rclpy.init(args=args)
    image_converter = ImageConverter()
    rclpy.spin(image_converter)
    image_converter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
