## 使用minikube部署一个nginx

```bash
PS C:\Users\hongf> minikube start
W0428 09:29:03.738333   10492 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\hongf\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
😄  Microsoft Windows 11 Home 10.0.22631.3447 Build 22631.3447 上的 minikube v1.33.0
✨  根据现有的配置文件使用 docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.43 ...
🔄  Restarting existing docker container for "minikube" ...
🤦  StartHost failed, but will try again: driver start: start: docker start minikube: exit status 1
stdout:

stderr:
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error setting cgroup config for procHooks process: failed to write "a *:* rwm": write /sys/fs/cgroup/devices/docker/2859e0583adf7e67adbb302f8531b459d5ab3d14274e3284288560376065ab05/devices.allow: invalid argument: unknown
Error: failed to start containers: minikube

🔄  Restarting existing docker container for "minikube" ...
🐳  正在 Docker 26.0.1 中准备 Kubernetes v1.30.0…
🔎  正在验证 Kubernetes 组件...
    ▪ 正在使用镜像 gcr.io/k8s-minikube/storage-provisioner:v5
🌟  启用插件： default-storageclass, storage-provisioner
🏄  完成！kubectl 现在已配置，默认使用"minikube"集群和"default"命名空间
PS C:\Users\hongf> kubectl get pod
NAME                                READY   STATUS      RESTARTS      AGE
flask-deployment-68d66c4449-96mk6   1/1     Running     1 (66s ago)   5d9h
nginx                               0/1     Completed   3             5d17h
PS C:\Users\hongf> kubectl delete pods --all
pod "flask-deployment-68d66c4449-96mk6" deleted
pod "nginx" deleted
PS C:\Users\hongf> kubectl delete services --all
service "flask-deployment" deleted
service "kubernetes" deleted
service "my-service" deleted
PS C:\Users\hongf> kubectl delete deployment --all
deployment.apps "flask-deployment" deleted
PS C:\Users\hongf> kubecrl get pod
kubecrl : 无法将“kubecrl”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路
径正确，然后再试一次。
所在位置 行:1 字符: 1
+ kubecrl get pod
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (kubecrl:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\hongf> kubectl get pod
No resources found in default namespace.
PS C:\Users\hongf> kubectl get pods
No resources found in default namespace.
PS C:\Users\hongf> cd C:\Users\hongf\Downloads\Git\dockerfiles\k8s
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s> kubectl apply -f .\nginx-deployment.yaml
deployment.apps/nginx-deployment created
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s> kubectl get deployments
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   1/3     3            1           7s
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s> kubectl get deployments
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           26s
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s> kubectl expose deployment nginx-deployment --type=NodePort --port=80
service/nginx-deployment exposed
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s> minikube service nginx-deployment
W0428 09:40:45.272140   10496 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\hongf\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
|-----------|------------------|-------------|---------------------------|
| NAMESPACE |       NAME       | TARGET PORT |            URL            |
|-----------|------------------|-------------|---------------------------|
| default   | nginx-deployment |          80 | http://192.168.49.2:30643 |
|-----------|------------------|-------------|---------------------------|
🏃  为服务 nginx-deployment 启动隧道。
|-----------|------------------|-------------|-----------------------|
| NAMESPACE |       NAME       | TARGET PORT |          URL          |
|-----------|------------------|-------------|-----------------------|
| default   | nginx-deployment |             | http://127.0.0.1:1408 |
|-----------|------------------|-------------|-----------------------|
🎉  正通过默认浏览器打开服务 default/nginx-deployment...
❗  因为你正在使用 windows 上的 Docker 驱动程序，所以需要打开终端才能运行它。
✋  停止服务 nginx-deployment 的隧道。
```

