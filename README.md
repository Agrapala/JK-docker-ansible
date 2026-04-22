# Flask Essay Topics App

This project now supports running directly on your local PC and in Docker.

## Run on Local PC

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app/main.py
```

4. Open in browser:

- http://127.0.0.1:5000

## Run with Docker

```bash
docker build -t essay-app .
docker run --rm -p 5000:5000 essay-app
```

Open:

- http://localhost:5000

## Jenkins Deployment Target

The pipeline now uses Ansible only, and the playbook drives Kubernetes deployment with `kubectl`.

The Kubernetes image must be a registry URL that your cluster can pull, for example `docker.io/<your-user>/essay-app:latest`.
Set `K8S_IMAGE` in [Jenkinsfile](Jenkinsfile) to your registry URL before running the pipeline.

Pipeline order:

1. Build Docker Image
2. Deploy with Ansible

The build stage tags the image with `K8S_IMAGE` and pushes it to the registry before the playbook deploys it.

Ansible runs:

```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml -e k8s_image=docker.io/<your-user>/essay-app:latest
```

The playbook applies [k8s/deployment.yaml](k8s/deployment.yaml), applies [k8s/service.yaml](k8s/service.yaml), sets the image, and waits for rollout.

## Available Pages

- `/` -> list of essay topics
- `/essay/technology`
- `/essay/environment`
- `/essay/teamwork`
