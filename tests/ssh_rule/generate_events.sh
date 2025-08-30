#!/usr/bin/env bash
# Generate sample sshd logs and run ossec-logtest inside the Wazuh manager container.

set -euo pipefail

MANAGER_CONTAINER="${MANAGER_CONTAINER:-$(docker ps --format '{{.Names}}' | grep -m1 wazuh-manager)}"

if [[ -z "${MANAGER_CONTAINER}" ]]; then
  echo "Wazuh manager container not found. Set MANAGER_CONTAINER or ensure the stack is running."
  exit 1
fi

cat > /tmp/ssh_events.log <<'EOF'
Jan 14 12:30:12 server sshd[1830]: Failed password for invalid user test1 from 203.0.113.5 port 50234 ssh2
Jan 14 12:30:14 server sshd[1830]: Failed password for invalid user test1 from 203.0.113.5 port 50234 ssh2
Jan 14 12:30:20 server sshd[1830]: Accepted password for backupuser from 203.0.113.5 port 50234 ssh2
EOF

echo "Running ossec-logtest ..."
docker exec -i "$MANAGER_CONTAINER" /var/ossec/bin/ossec-logtest < /tmp/ssh_events.log | tee tests/ssh_rule/logtest-output.txt
echo "Done. Check tests/ssh_rule/logtest-output.txt"
