Need to create cm
kubectl create cm nginx-config -n demo-app --from-file=argo_cd/docker-project/web/nginx.conf
kubectl create configmap nginx-html   --from-file=argo_cd/docker-project/web/html/   -n demo-app

How to install kubeseal for SealedSecret
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.29.0/kubeseal-0.29.0-linux-amd64.tar.gz
ll
tar -xvzf kubeseal-0.29.0-linux-amd64.tar.gz
chmod +x kubeseal
sudo mv kubeseal /usr/local/bin/
kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/latest/download/controller.yaml
kubectl create secret generic postgres-secret   --namespace demo-app   --from-literal=POSTGRES_USER=user   --from-literal=POSTGRES_PASSWORD=password   --from-literal=POSTGRES_DB=mydb   --dry-run=client -o yaml > postgres-secret.yaml
kubeseal --format yaml --namespace demo-app < postgres-secret.yaml > sealed-postgres-secret.yaml

Need to create a configmap for database migration.
kubectl create configmap db-migrate-script   --from-file=db_migrate.py   -n demo-app
