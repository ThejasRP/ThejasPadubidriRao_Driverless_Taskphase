import rclpy
from rclpy.node import Node
from taskone_interfaces.msg import TaskOne  

class TaskOnePublisher(Node):
    def __init__(self):
        super().__init__('taskone_publisher')
        self.taskonepub = self.create_publisher(TaskOne, 'taskone', 10)
        self.i = 1
    def pub_taskone(self):
        msg = TaskOne()                                         
        print(f"Iteration {self.i}")
        msg.angvel = float(input("Enter angular velocity: "))
        msg.radius = float(input("Enter radius: "))                                           
        self.taskonepub.publish(msg)
        self.get_logger().info(f'Published {self.i}')       
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    taskone_publisher = TaskOnePublisher()
    while rclpy.ok():
        taskone_publisher.pub_taskone()
    taskone_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
