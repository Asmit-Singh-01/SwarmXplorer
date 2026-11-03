use std::collections::HashMap;
use std::time::{Instant, Duration};

pub struct MeshNode {
    pub node_id: u32,
    peers: HashMap<u32, Instant>,
    timeout_duration: Duration,
}

impl MeshNode {
    /// Initializes a new decentralized P2P mesh node handler
    pub fn new(node_id: u32, timeout_secs: u64) -> Self {
        MeshNode {
            node_id,
            peers: HashMap::new(),
            timeout_duration: Duration::from_secs(timeout_secs),
        }
    }

    /// Records incoming packet / heartbeat from a neighbor node
    pub fn update_heartbeat(&mut self, peer_id: u32) {
        self.peers.insert(peer_id, Instant::now());
    }

    /// Evaluates mesh link health and returns IDs of disconnected/timed-out nodes
    pub fn check_mesh_health(&self) -> Vec<u32> {
        let now = Instant::now();
        let mut disconnected_nodes = Vec::new();

        for (&peer_id, &last_seen) in &self.peers {
            if now.duration_since(last_seen) > self.timeout_duration {
                disconnected_nodes.push(peer_id);
            }
        }

        disconnected_nodes
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::thread;

    #[test]
    fn test_mesh_heartbeat_timeout() {
        let mut node = MeshNode::new(1, 1); // 1 second timeout
        node.update_heartbeat(2);

        // Initially healthy
        assert_eq!(node.check_mesh_health().len(), 0);

        // Wait for timeout expiration
        thread::sleep(Duration::from_millis(1100));
        let disconnected = node.check_mesh_health();
        
        assert!(disconnected.contains(&2));
    }
}
