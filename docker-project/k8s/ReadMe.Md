Need to create cm
kubectl create cm nginx-config -n demo-app --from-file=argo_cd/docker-project/web/nginx.conf
kubectl create configmap nginx-html   --from-file=argo_cd/docker-project/web/html/   -n demo-app
How to install kubeseal for SealedSecret
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.29.0/kubeseal-0.29.0-linux-amd64.tar.gz
ll
tar -xvzf kubeseal-0.29.0-linux-amd64.tar.gz
chmod +x kubeseal
sudo mv kubeseal /usr/local/bin/
