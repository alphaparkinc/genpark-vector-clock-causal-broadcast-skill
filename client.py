class VectorClockNode:
    """
    Vector Clock Causal Broadcast protocol ensuring messages are delivered
    strictly in causal order across asynchronous agent networks.
    """
    def __init__(self, node_id, total_nodes=3):
        self.node_id = node_id
        self.total_nodes = total_nodes
        self.clock = [0] * total_nodes
        self.buffer = []
        self.delivered = []

    def broadcast_event(self):
        self.clock[self.node_id] += 1
        msg = {
            "sender": self.node_id,
            "clock": list(self.clock),
            "payload": f"Event from {self.node_id} at {self.clock[self.node_id]}"
        }
        return msg

    def receive_message(self, msg):
        sender = msg["sender"]
        msg_clk = msg["clock"]
        can_deliver = (msg_clk[sender] == self.clock[sender] + 1)
        for k in range(self.total_nodes):
            if k != sender and msg_clk[k] > self.clock[k]:
                can_deliver = False
                break

        if can_deliver:
            self.clock[sender] += 1
            self.delivered.append(msg["payload"])
            return "DELIVERED"
        else:
            self.buffer.append(msg)
            return "BUFFERED"
