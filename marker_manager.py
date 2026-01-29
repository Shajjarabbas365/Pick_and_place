from visualization_msgs.msg import Marker

class MarkerManager:
    def __init__(self, node):
        self.node = node
        self.publisher = node.create_publisher(Marker, 'visualization_marker', 10)

    def publish_cube(self, id, color, position):
        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.id = id
        marker.type = Marker.CUBE
        marker.action = Marker.ADD
        marker.pose.position.x = float(position[0])
        marker.pose.position.y = float(position[1])
        marker.pose.position.z = float(position[2])
        marker.scale.x, marker.scale.y, marker.scale.z = 0.1, 0.1, 0.1
        marker.color.a = 1.0
        marker.color.r, marker.color.g, marker.color.b = color[0], color[1], color[2]
        self.publisher.publish(marker)
