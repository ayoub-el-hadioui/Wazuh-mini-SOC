# Low-Level Design (LLD)

## Inventories & Node Roles
See `ansible/inventories/production/hosts.ini` for hosts and roles.

## Service Specs
- Stack file template: `roles/stack/templates/wazuh-stack.yml.j2`
- Resources, healthchecks (rely on upstream images), rolling updates via Swarm.

## Storage
- Volumes: `wazuh-indexer-data`, `wazuh-manager-data`, `traefik-acme`

## Network
- Overlay networks: `frontend` (ingress) and `backend` (data plane).

## CI Jobs
- **Build**: Docker image build (example tools image).
- **Scan**: Trivy; fail on Critical/High.
- **Test**: Selenium smoke; API probe.
- **Deploy**: `ansible-playbook ansible/playbooks/deploy.yml`

## Secrets & Certs
- GitHub Encrypted Secrets → Swarm secrets via Ansible.
- TLS with Traefik + ACME; automated renewals.

## Runbooks
- Bootstrap: `ansible-playbook ... deploy.yml`
- Day-2: scale services via `docker service scale` or edit stack and redeploy.
- Teardown: `ansible-playbook ... teardown.yml`.
