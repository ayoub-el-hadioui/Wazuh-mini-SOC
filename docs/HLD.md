# High-Level Design (HLD)

## Context & Goals
Deploy a **Wazuh SIEM** with secure-by-default CI/CD, quality gates, and automated rollout to **Docker Swarm**.

- Availability: single-node minimal demo, optionally scalable to multi-node.
- Security: TLS by default, secrets via GitHub + Swarm.
- CI orchestration: build → scan → test → deploy.

## Logical Architecture
- **CI/CD**: GitHub Actions (self-hosted runner) → Ansible → Swarm.
- **Ingress**: Traefik v2 with ACME (Let's Encrypt).
- **Wazuh Stack**: Indexer (OpenSearch), Manager, Dashboard.
- **Secrets**: GH Secrets → Ansible → Swarm secrets.
- **Monitoring**: Wazuh Dashboard.

## HA strategy (optional extension)
Documented in `docs/LLD.md` as an optional path (replicas, snapshots, rolling updates).

## Data Flows
Agents → Manager/Indexer; Dashboard ↔ Manager/Indexer; CI → Ansible → Swarm.

## Security posture
- Trust boundaries between CI, control host, Swarm managers/workers.
- TLS everywhere (Traefik terminates, internal networks encrypted by Swarm overlay).
