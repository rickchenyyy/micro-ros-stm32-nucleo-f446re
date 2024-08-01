import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
import time  # Import time module for timestamp calculation

class AK60FeedbackSubscriber(Node):

    def __init__(self, publisher):
        super().__init__('feedback_subscriber')
        self.publisher = publisher
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/AK_60_publisher',
            self.listener_callback,
            qos_profile)

    def listener_callback(self, msg):
        current_time = time.time() * 1000  # Current time in milliseconds
        if self.publisher.last_sended_time is not None:
            time_diff = current_time - self.publisher.last_sended_time
            self.get_logger().info(f'Received: {msg.data}, Time difference: {time_diff:.2f} ms')
        else:
            self.get_logger().info(f'Received: {msg.data}')


class AK60CommandPublisher(Node):

    def __init__(self):
        super().__init__('command_publisher')
        self.last_sended_time = None  # Initialize last_sended_time
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT
        self.publisher_ = self.create_publisher(Float32MultiArray, '/AK_60_subscriber', qos_profile)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0
        self.n = 0

    def timer_callback(self):
        msg = Float32MultiArray()
        msg.data = [float(i+self.n) for i in range(12)]
        self.publisher_.publish(msg)
        self.last_sended_time = time.time() * 1000  # Update last_sended_time
        self.get_logger().info(f'Publishing: {msg.data}')
        self.n = self.n+2


def main(args=None):
    rclpy.init(args=args)

    ak60_publisher = AK60CommandPublisher()
    ak60_subscriber = AK60FeedbackSubscriber(ak60_publisher)

    # Use MultiThreadedExecutor to handle both nodes concurrently
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(ak60_subscriber)
    executor.add_node(ak60_publisher)

    try:
        executor.spin()
    finally:
        ak60_subscriber.destroy_node()
        ak60_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
