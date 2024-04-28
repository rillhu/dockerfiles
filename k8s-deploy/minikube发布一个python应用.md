## minikube发布一个python应用

```bash
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> docker build -t rillhu/flask:v2 .
[+] Building 0.9s (9/9) FINISHED                                                                         docker:default
 => [internal] load build definition from Dockerfile                                                               0.1s
 => => transferring dockerfile: 245B                                                                               0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                      0.5s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [1/4] FROM docker.io/library/python:3.9@sha256:c0dcc146710fed0a6d62cb55b92f00bfbfc3b931fff6218f4958bab58333c3  0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 276B                                                                                  0.0s
 => CACHED [2/4] RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple                                 0.0s
 => [3/4] COPY app.py /app/                                                                                        0.0s
 => [4/4] WORKDIR /app                                                                                             0.0s
 => exporting to image                                                                                             0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:a403d812d9b9ef57483c7af7d0e1fdf99816854cd3ffceab843ca07480e6ae50                       0.0s
 => => naming to docker.io/rillhu/flask:v2                                                                         0.0s

View build details: docker-desktop://dashboard/build/default/default/c1eu8vqcwkeyc92gnyiy94inw

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> docker images
REPOSITORY        TAG       IMAGE ID       CREATED         SIZE
rillhu/flask      v2        a403d812d9b9   5 seconds ago   922MB
kicbase/stable    v0.0.43   619d67e74933   9 days ago      1.26GB
artmisdockerimg   latest    b24b6423067f   9 days ago      1.11GB
mysql             5.7       5107333e08a8   4 months ago    501MB
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> docker push rillhu/flask:v2
The push refers to repository [docker.io/rillhu/flask]
5f70bf18a086: Layer already exists
c0212fd00035: Pushed
bf89b236c89b: Layer already exists
3c33784a62f7: Layer already exists
cb6d722583a8: Layer already exists
8982e2c53abb: Layer already exists
aedcb370b058: Layer already exists
c3a0d593ed24: Layer already exists
26a504e63be4: Layer already exists
8bf42db0de72: Layer already exists
31892cc314cb: Layer already exists
11936051f93b: Layer already exists
v2: digest: sha256:03b77000c706e77b98932b542b39c2c6f58554afda603760c3aac427d3cadb8d size: 2842
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl apply -f .\flask_deployment.yaml
deployment.apps/flask-deployment created
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl get deployments
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
flask-deployment   1/1     1            1           11s
nginx-deployment   3/3     3            3           17m
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
flask-deployment-687c7d676b-2jpkn   1/1     Running   0          26s
nginx-deployment-576c6b7b6-5q9f6    1/1     Running   0          18m
nginx-deployment-576c6b7b6-j84w5    1/1     Running   0          18m
nginx-deployment-576c6b7b6-px4hz    1/1     Running   0          18m
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl describe pod flask-deployment-687c7d676b-2jpkn
Name:             flask-deployment-687c7d676b-2jpkn
Namespace:        default
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Sun, 28 Apr 2024 09:55:28 +0800
Labels:           app=flask-app
                  pod-template-hash=687c7d676b
Annotations:      <none>
Status:           Running
IP:               10.244.0.26
IPs:
  IP:           10.244.0.26
Controlled By:  ReplicaSet/flask-deployment-687c7d676b
Containers:
  flask-app:
    Container ID:   docker://ac4304f4a348279e8ea3da772400ea6015154c0c560846147a4c9fb5c41c197d
    Image:          rillhu/flask:v2
    Image ID:       docker-pullable://rillhu/flask@sha256:03b77000c706e77b98932b542b39c2c6f58554afda603760c3aac427d3cadb8d
    Port:           5000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Sun, 28 Apr 2024 09:55:36 +0800
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-4zmt4 (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True
  Initialized                 True
  Ready                       True
  ContainersReady             True
  PodScheduled                True
Volumes:
  kube-api-access-4zmt4:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age   From               Message
  ----    ------     ----  ----               -------
  Normal  Scheduled  60s   default-scheduler  Successfully assigned default/flask-deployment-687c7d676b-2jpkn to minikube
  Normal  Pulling    60s   kubelet            Pulling image "rillhu/flask:v2"
  Normal  Pulled     53s   kubelet            Successfully pulled image "rillhu/flask:v2" in 7.049s (7.049s including waiting). Image size: 922298049 bytes.
  Normal  Created    53s   kubelet            Created container flask-app
  Normal  Started    53s   kubelet            Started container flask-app
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl apply -f .\flask_service.yaml
service/flask-deployment created
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
flask-deployment-687c7d676b-2jpkn   1/1     Running   0          98s
nginx-deployment-576c6b7b6-5q9f6    1/1     Running   0          19m
nginx-deployment-576c6b7b6-j84w5    1/1     Running   0          19m
nginx-deployment-576c6b7b6-px4hz    1/1     Running   0          19m
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl get svc
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
flask-deployment   NodePort    10.111.90.85   <none>        80:30080/TCP   10s
kubernetes         ClusterIP   10.96.0.1      <none>        443/TCP        23m
nginx-deployment   NodePort    10.99.42.22    <none>        80:30643/TCP   17m
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> kubectl get services
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
flask-deployment   NodePort    10.111.90.85   <none>        80:30080/TCP   24s
kubernetes         ClusterIP   10.96.0.1      <none>        443/TCP        24m
nginx-deployment   NodePort    10.99.42.22    <none>        80:30643/TCP   17m
PS C:\Users\hongf\Downloads\Git\dockerfiles\k8s-deploy> minikube service flask-deployment --url
W0428 09:59:30.820973   16192 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\hongf\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
http://127.0.0.1:2310
❗  因为你正在使用 windows 上的 Docker 驱动程序，所以需要打开终端才能运行它。
```

