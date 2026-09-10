from client import VectorClockNode

def main():
    print("=== Testing Vector Clock Causal Broadcast ===")
    vc0 = VectorClockNode(node_id=0, total_nodes=3)
    vc1 = VectorClockNode(node_id=1, total_nodes=3)
    msg0 = vc0.broadcast_event()
    status = vc1.receive_message(msg0)
    print("Delivery status:", status)
    assert status == "DELIVERED"
    assert vc1.clock[0] == 1
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
