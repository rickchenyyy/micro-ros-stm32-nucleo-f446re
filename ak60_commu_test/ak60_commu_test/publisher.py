import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class AK60CommandPublisher(Node):

    def __init__(self):
        super().__init__('command_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, '/AK_60_subscriber', 10)
        timer_period = 2.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = Float32MultiArray()
        msg.data = [float(i) for i in range(12)]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    ak60_publisher = AK60CommandPublisher()
    rclpy.spin(ak60_publisher)
    ak60_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
