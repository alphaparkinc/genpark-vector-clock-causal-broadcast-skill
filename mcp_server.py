import sys
import json
from client import VectorClockNode

def main():
    node = VectorClockNode(node_id=0, total_nodes=3)
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "broadcast":
            res = node.broadcast_event()
        elif method == "receive":
            status = node.receive_message(params.get("message", {}))
            res = {"status": status, "clock": node.clock}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
