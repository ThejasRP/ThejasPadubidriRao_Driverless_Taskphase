import rclpy
from rclpy.node import Node
from rt2string_interface.srv import Ispal

class NodeThreePubSub(Node):
    def __init__(self):
        super().__init__('nodethree_pubsub')
        self.srv=self.create_service(Ispal, "ispalindrome", self.pubsub_callback)
        self.i=1
    def pubsub_callback(self, req, res):       
        res.ispals="No"
        if req.ispalb==1:
            res.ispals="Yes"   
        self.get_logger().info(f'Received and returned {self.i} containing is palindrome string to Node 2')  
        self.i+=1
        return res


def main(args=None):
    rclpy.init(args=args)
    nodethree_pubsub = NodeThreePubSub()
    rclpy.spin(nodethree_pubsub)
    nodethree_pubsub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
