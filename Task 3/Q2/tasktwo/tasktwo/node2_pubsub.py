import rclpy
from rclpy.node import Node
from rt2string_interface.srv import Ispal
from rt2string_interface.msg import RT2String

class NodeTwoPubSub(Node):
    def __init__(self):
        super().__init__('nodetwo_pubsub')
        self.srv = self.create_client(Ispal, "ispalindrome")
        while not self.srv.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Start node 3")
        self.req = Ispal.Request()
        self.n1subscription = self.create_subscription(
            RT2String,
            'palindrome',
            self.n1pubsub_callback,
            10
        )
        self.i = 1

    def n1pubsub_callback(self, msg):    
        f = 1 if msg.str == msg.str[::-1] else 0
        self.get_logger().info(f'Publishing {self.i}: Sending requested palindrome result to node 3')  
        self.req.ispalb = f
        future = self.srv.call_async(self.req)
        future.add_done_callback(self.n3_response_callback)        
        self.i += 1

    def n3_response_callback(self, future):
        try:
            resp = future.result()
            self.get_logger().info(f'Received from Node 3\nIs palindrome? : {resp.ispals}') 
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main(args=None):
    rclpy.init(args=args)
    nodetwo_pubsub = NodeTwoPubSub()
    rclpy.spin(nodetwo_pubsub)
    nodetwo_pubsub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
