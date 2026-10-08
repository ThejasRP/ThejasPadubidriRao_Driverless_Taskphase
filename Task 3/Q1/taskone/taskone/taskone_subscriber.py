import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne

class TaskOneSubscriber(Node):
    def __init__(self):
        super().__init__('taskone_subscriber')
        self.subscription = self.create_subscription(
            TaskOne,
            'taskone',
            self.sub_callback,
            10)
        self.subscription 
        self.i=1
    def sub_callback(self, msg):
        ls = float(msg.angvel * msg.radius)
        self.get_logger().info(f'Received {self.i}\nLongitudinal speed = {ls}')  
        self.i+=1


def main(args=None):
    rclpy.init(args=args)
    taskone_subscriber = TaskOneSubscriber()
    rclpy.spin(taskone_subscriber)
    taskone_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
