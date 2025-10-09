Need to create cm
kubectl create cm nginx-config -n demo-app --from-file=/argo_cd/docker-project/web/nginx.conf
kubectl create configmap nginx-html   --from-file=/argo_cd/docker-project/web/html/   -n demo-app
