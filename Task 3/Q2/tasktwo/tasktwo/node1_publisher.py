import rclpy
from rclpy.node import Node
from rt2string_interface.msg import RT2String

class NodeOnePublisher(Node):
    def __init__(self):
        super().__init__("nodeone_publisher")
        self.publisher=self.create_publisher(RT2String, "palindrome", 10)
        self.i=1
    def pub_callback(self):
        print(f"Iteration {self.i}")
        input_string = input("Enter string: ")
        msg = RT2String()
        msg.str = input_string
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing {self.i}')       
        self.i += 1   

def main(args=None):
    rclpy.init(args=args)
    nodeone_publisher = NodeOnePublisher()
    while rclpy.ok():
        nodeone_publisher.pub_callback()
        rclpy.spin_once(nodeone_publisher, timeout_sec=0.1)
    nodeone_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
