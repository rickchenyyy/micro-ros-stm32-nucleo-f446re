import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from rclpy.qos import QoSProfile, QoSReliabilityPolicy


class AK60FeedbackSubscriber(Node):

    def __init__(self):
        super().__init__('feedback_subscriber')
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/AK_60_publisher',
            self.listener_callback,
            qos_profile)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    ak60_subscriber = AK60FeedbackSubscriber()
    rclpy.spin(ak60_subscriber)
    ak60_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
