```powershell
PS C:\Users\yxqz> minikube
W0422 08:58:22.670799   17916 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\yxqz\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
minikube 提供并管理针对开发工作流程优化的本地 Kubernetes 集群。

基本命令：
  start            启动本地 Kubernetes 集群
  status           获取本地 Kubernetes 集群状态
  stop             停止正在运行的本地 Kubernetes 集群
  delete           删除本地的 Kubernetes 集群
  dashboard        访问在 minikube 集群中运行的 kubernetes dashboard
  pause            暂停 Kubernetes
  unpause          恢复 Kubernetes

镜像命令
  docker-env       提供将终端的 docker-cli 指向 minikube 内部 Docker Engine 的说明。（用于直接在 minikube 内构建 docker 镜像 ）
  podman-env       配置环境以使用 minikube's Podman service
  cache            管理 images 缓存
  image            管理 images

配置和管理命令：
  addons           启用或禁用 minikube 插件
  config           修改持久配置值
  profile          获取或列出当前配置文件（集群）
  update-context   IP或端口更改的情况下更新 kubeconfig 配置文件

网络和连接命令：
  service          返回用于连接到 service 的 URL
  tunnel           连接到 LoadBalancer 服务

高级命令：
  mount            将指定的目录挂载到 minikube
  ssh              登录到 minikube 环境（用于调试）
  kubectl          运行与集群版本匹配的 kubectl 二进制文件
  node             添加，删除或者列出其他的节点
  cp               将指定的文件复制到 minikube

故障排除命令
  ssh-key          检索指定节点的 ssh 密钥路径
  ssh-host         检索指定节点的 ssh 主机密钥
  ip               检索指定节点的IP地址
  logs             返回用于调试本地 Kubernetes 集群的日志
  update-check     打印当前版本和最新版本
  version          打印 minikube 版本
  options          显示全局命令行选项列表 (应用于所有命令)。

Other Commands:
  completion       生成命令补全的 shell 脚本
  license          将依赖项的 licenses 输出到一个目录

Use "minikube <command> --help" for more information about a given command.
PS C:\Users\yxqz> minikube status
W0422 08:58:28.416439   20932 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\yxqz\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured

PS C:\Users\yxqz> minikube status
W0422 10:43:15.878243   19260 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\yxqz\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
minikube
type: Control Plane
host: Stopped
kubelet: Stopped
apiserver: Stopped
kubeconfig: Stopped

PS C:\Users\yxqz> minikube start
W0422 10:43:24.544114   10080 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\yxqz\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
😄  Microsoft Windows 11 Home 10.0.22631.3447 Build 22631.3447 上的 minikube v1.33.0
✨  根据现有的配置文件使用 docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.43 ...
🔄  Restarting existing docker container for "minikube" ...
🐳  正在 Docker 26.0.1 中准备 Kubernetes v1.30.0…
🔎  正在验证 Kubernetes 组件...
    ▪ 正在使用镜像 gcr.io/k8s-minikube/storage-provisioner:v5
🌟  启用插件： storage-provisioner, default-storageclass
🏄  完成！kubectl 现在已配置，默认使用"minikube"集群和"default"命名空间
PS C:\Users\yxqz> kubectl
kubectl controls the Kubernetes cluster manager.

 Find more information at: https://kubernetes.io/docs/reference/kubectl/

Basic Commands (Beginner):
  create          Create a resource from a file or from stdin
  expose          Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
  run             Run a particular image on the cluster
  set             Set specific features on objects

Basic Commands (Intermediate):
  explain         Get documentation for a resource
  get             Display one or many resources
  edit            Edit a resource on the server
  delete          Delete resources by file names, stdin, resources and names, or by resources and label selector

Deploy Commands:
  rollout         Manage the rollout of a resource
  scale           Set a new size for a deployment, replica set, or replication controller
  autoscale       Auto-scale a deployment, replica set, stateful set, or replication controller

Cluster Management Commands:
  certificate     Modify certificate resources
  cluster-info    Display cluster information
  top             Display resource (CPU/memory) usage
  cordon          Mark node as unschedulable
  uncordon        Mark node as schedulable
  drain           Drain node in preparation for maintenance
  taint           Update the taints on one or more nodes

Troubleshooting and Debugging Commands:
  describe        Show details of a specific resource or group of resources
  logs            Print the logs for a container in a pod
  attach          Attach to a running container
  exec            Execute a command in a container
  port-forward    Forward one or more local ports to a pod
  proxy           Run a proxy to the Kubernetes API server
  cp              Copy files and directories to and from containers
  auth            Inspect authorization
  debug           Create debugging sessions for troubleshooting workloads and nodes
  events          List events

Advanced Commands:
  diff            Diff the live version against a would-be applied version
  apply           Apply a configuration to a resource by file name or stdin
  patch           Update fields of a resource
  replace         Replace a resource by file name or stdin
  wait            Experimental: Wait for a specific condition on one or many resources
  kustomize       Build a kustomization target from a directory or URL

Settings Commands:
  label           Update the labels on a resource
  annotate        Update the annotations on a resource
  completion      Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

Subcommands provided by plugins:

Other Commands:
  api-resources   Print the supported API resources on the server
  api-versions    Print the supported API versions on the server, in the form of "group/version"
  config          Modify kubeconfig files
  plugin          Provides utilities for interacting with plugins
  version         Print the client and server version information

Usage:
  kubectl [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
PS C:\Users\yxqz> kubectl config view
apiVersion: v1
clusters:
- cluster:
    certificate-authority: C:\Users\yxqz\.minikube\ca.crt
    extensions:
    - extension:
        last-update: Mon, 22 Apr 2024 10:43:35 CST
        provider: minikube.sigs.k8s.io
        version: v1.33.0
      name: cluster_info
    server: https://127.0.0.1:9966
  name: minikube
contexts:
- context:
    cluster: minikube
    extensions:
    - extension:
        last-update: Mon, 22 Apr 2024 10:43:35 CST
        provider: minikube.sigs.k8s.io
        version: v1.33.0
      name: context_info
    namespace: default
    user: minikube
  name: minikube
current-context: minikube
kind: Config
preferences: {}
users:
- name: minikube
  user:
    client-certificate: C:\Users\yxqz\.minikube\profiles\minikube\client.crt
    client-key: C:\Users\yxqz\.minikube\profiles\minikube\client.key
PS C:\Users\yxqz> kubectl config contexts
error: unknown command "contexts"
See 'kubectl config -h' for help and examples
PS C:\Users\yxqz> kubectl config get-contexts
CURRENT   NAME       CLUSTER    AUTHINFO   NAMESPACE
*         minikube   minikube   minikube   default
PS C:\Users\yxqz> kubectl cluster-info
Kubernetes control plane is running at https://127.0.0.1:9966
CoreDNS is running at https://127.0.0.1:9966/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
PS C:\Users\yxqz> kubectl get rc nginx
Error from server (NotFound): replicationcontrollers "nginx" not found
PS C:\Users\yxqz> cd C:\Users\yxqz\Downloads\Git\dockerfiles\k8s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\service.yaml
error: error parsing .\service.yaml: error converting YAML to JSON: yaml: line 3: mapping values are not allowed in this context
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\service.yaml
error: error parsing .\service.yaml: error converting YAML to JSON: yaml: line 4: did not find expected key
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\service.yaml
error: error parsing .\service.yaml: error converting YAML to JSON: yaml: line 7: did not find expected key
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\service.yaml
error: error parsing .\service.yaml: error converting YAML to JSON: yaml: line 7: did not find expected key
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\service.yaml
service/my-service created
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   134m
my-service   ClusterIP   10.110.54.155   <none>        80/TCP    49s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl -get endpoints my-service
Error: flags cannot be placed before plugin name: -get
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get endpoints my-service
NAME         ENDPOINTS   AGE
my-service   <none>      91s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pod --show-label
error: unknown flag: --show-label
See 'kubectl get --help' for usage.
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pod show-label
Error from server (NotFound): pods "show-label" not found
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pods --show-labels
No resources found in default namespace.
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pods
No resources found in default namespace.
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get svc
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP   138m
my-service   ClusterIP   10.110.54.155   <none>        80/TCP    4m57s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> curl  10.110.54.155:80
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\nginx.yaml
pod/nginx created
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pods
NAME    READY   STATUS              RESTARTS   AGE
nginx   0/1     ContainerCreating   0          18s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl describe node
Name:               minikube
Roles:              control-plane
Labels:             beta.kubernetes.io/arch=amd64
                    beta.kubernetes.io/os=linux
                    kubernetes.io/arch=amd64
                    kubernetes.io/hostname=minikube
                    kubernetes.io/os=linux
                    minikube.k8s.io/commit=86fc9d54fca63f295d8737c8eacdbb7987e89c67
                    minikube.k8s.io/name=minikube
                    minikube.k8s.io/primary=true
                    minikube.k8s.io/updated_at=2024_04_22T08_52_40_0700
                    minikube.k8s.io/version=v1.33.0
                    node-role.kubernetes.io/control-plane=
                    node.kubernetes.io/exclude-from-external-load-balancers=
Annotations:        kubeadm.alpha.kubernetes.io/cri-socket: unix:///var/run/cri-dockerd.sock
                    node.alpha.kubernetes.io/ttl: 0
                    volumes.kubernetes.io/controller-managed-attach-detach: true
CreationTimestamp:  Mon, 22 Apr 2024 08:52:35 +0800
Taints:             <none>
Unschedulable:      false
Lease:
  HolderIdentity:  minikube
  AcquireTime:     <unset>
  RenewTime:       Mon, 22 Apr 2024 11:13:48 +0800
Conditions:
  Type             Status  LastHeartbeatTime                 LastTransitionTime                Reason                       Message
  ----             ------  -----------------                 ------------------                ------                       -------
  MemoryPressure   False   Mon, 22 Apr 2024 11:09:10 +0800   Mon, 22 Apr 2024 08:52:30 +0800   KubeletHasSufficientMemory   kubelet has sufficient memory available
  DiskPressure     False   Mon, 22 Apr 2024 11:09:10 +0800   Mon, 22 Apr 2024 08:52:30 +0800   KubeletHasNoDiskPressure     kubelet has no disk pressure
  PIDPressure      False   Mon, 22 Apr 2024 11:09:10 +0800   Mon, 22 Apr 2024 08:52:30 +0800   KubeletHasSufficientPID      kubelet has sufficient PID available
  Ready            True    Mon, 22 Apr 2024 11:09:10 +0800   Mon, 22 Apr 2024 08:52:41 +0800   KubeletReady                 kubelet is posting ready status
Addresses:
  InternalIP:  192.168.49.2
  Hostname:    minikube
Capacity:
  cpu:                12
  ephemeral-storage:  1055762868Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             8045816Ki
  pods:               110
Allocatable:
  cpu:                12
  ephemeral-storage:  1055762868Ki
  hugepages-1Gi:      0
  hugepages-2Mi:      0
  memory:             8045816Ki
  pods:               110
System Info:
  Machine ID:                 015a99dae25a4f3fbb4323958db080e0
  System UUID:                015a99dae25a4f3fbb4323958db080e0
  Boot ID:                    201f6fd7-fbcb-410a-924a-0e3b635d8f84
  Kernel Version:             5.15.146.1-microsoft-standard-WSL2
  OS Image:                   Ubuntu 22.04.4 LTS
  Operating System:           linux
  Architecture:               amd64
  Container Runtime Version:  docker://26.0.1
  Kubelet Version:            v1.30.0
  Kube-Proxy Version:         v1.30.0
PodCIDR:                      10.244.0.0/24
PodCIDRs:                     10.244.0.0/24
Non-terminated Pods:          (8 in total)
  Namespace                   Name                                CPU Requests  CPU Limits  Memory Requests  Memory Limits  Age
  ---------                   ----                                ------------  ----------  ---------------  -------------  ---
  default                     nginx                               0 (0%)        0 (0%)      0 (0%)           0 (0%)         69s
  kube-system                 coredns-7db6d8ff4d-kmfph            100m (0%)     0 (0%)      70Mi (0%)        170Mi (2%)     141m
  kube-system                 etcd-minikube                       100m (0%)     0 (0%)      100Mi (1%)       0 (0%)         141m
  kube-system                 kube-apiserver-minikube             250m (2%)     0 (0%)      0 (0%)           0 (0%)         141m
  kube-system                 kube-controller-manager-minikube    200m (1%)     0 (0%)      0 (0%)           0 (0%)         141m
  kube-system                 kube-proxy-d8tz5                    0 (0%)        0 (0%)      0 (0%)           0 (0%)         141m
  kube-system                 kube-scheduler-minikube             100m (0%)     0 (0%)      0 (0%)           0 (0%)         141m
  kube-system                 storage-provisioner                 0 (0%)        0 (0%)      0 (0%)           0 (0%)         141m
Allocated resources:
  (Total limits may be over 100 percent, i.e., overcommitted.)
  Resource           Requests    Limits
  --------           --------    ------
  cpu                750m (6%)   0 (0%)
  memory             170Mi (2%)  170Mi (2%)
  ephemeral-storage  0 (0%)      0 (0%)
  hugepages-1Gi      0 (0%)      0 (0%)
  hugepages-2Mi      0 (0%)      0 (0%)
Events:
  Type    Reason                   Age                  From             Message
  ----    ------                   ----                 ----             -------
  Normal  Starting                 141m                 kube-proxy
  Normal  Starting                 30m                  kube-proxy
  Normal  NodeHasSufficientMemory  141m (x8 over 141m)  kubelet          Node minikube status is now: NodeHasSufficientMemory
  Normal  NodeHasNoDiskPressure    141m (x8 over 141m)  kubelet          Node minikube status is now: NodeHasNoDiskPressure
  Normal  NodeHasSufficientPID     141m (x7 over 141m)  kubelet          Node minikube status is now: NodeHasSufficientPID
  Normal  NodeAllocatableEnforced  141m                 kubelet          Updated Node Allocatable limit across pods
  Normal  NodeNotReady             141m                 kubelet          Node minikube status is now: NodeNotReady
  Normal  Starting                 141m                 kubelet          Starting kubelet.
  Normal  NodeHasNoDiskPressure    141m                 kubelet          Node minikube status is now: NodeHasNoDiskPressure
  Normal  NodeHasSufficientPID     141m                 kubelet          Node minikube status is now: NodeHasSufficientPID
  Normal  NodeHasSufficientMemory  141m                 kubelet          Node minikube status is now: NodeHasSufficientMemory
  Normal  NodeAllocatableEnforced  141m                 kubelet          Updated Node Allocatable limit across pods
  Normal  NodeReady                141m                 kubelet          Node minikube status is now: NodeReady
  Normal  RegisteredNode           141m                 node-controller  Node minikube event: Registered Node minikube in Controller
  Normal  Starting                 30m                  kubelet          Starting kubelet.
  Normal  NodeHasSufficientMemory  30m (x8 over 30m)    kubelet          Node minikube status is now: NodeHasSufficientMemory
  Normal  NodeHasNoDiskPressure    30m (x8 over 30m)    kubelet          Node minikube status is now: NodeHasNoDiskPressure
  Normal  NodeHasSufficientPID     30m (x7 over 30m)    kubelet          Node minikube status is now: NodeHasSufficientPID
  Normal  NodeAllocatableEnforced  30m                  kubelet          Updated Node Allocatable limit across pods
  Normal  RegisteredNode           30m                  node-controller  Node minikube event: Registered Node minikube in Controller
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl apply -f .\nginx-deployment.yaml
deployment.apps/nginx-deployment created
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   2/3     3            2           11s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pod
NAME                               READY   STATUS    RESTARTS   AGE
nginx                              1/1     Running   0          6m31s
nginx-deployment-576c6b7b6-8vstz   1/1     Running   0          26s
nginx-deployment-576c6b7b6-gzths   1/1     Running   0          26s
nginx-deployment-576c6b7b6-qd4pp   1/1     Running   0          26s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get deployment
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-deployment   3/3     3            3           33s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl create -f .\namespace.yaml
namespace/new-namespace created
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get namespace
NAME              STATUS   AGE
default           Active   159m
kube-node-lease   Active   159m
kube-public       Active   159m
kube-system       Active   159m
new-namespace     Active   10s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl
kubectl controls the Kubernetes cluster manager.

 Find more information at: https://kubernetes.io/docs/reference/kubectl/

Basic Commands (Beginner):
  create          Create a resource from a file or from stdin
  expose          Take a replication controller, service, deployment or pod and expose it as a new Kubernetes service
  run             Run a particular image on the cluster
  set             Set specific features on objects

Basic Commands (Intermediate):
  explain         Get documentation for a resource
  get             Display one or many resources
  edit            Edit a resource on the server
  delete          Delete resources by file names, stdin, resources and names, or by resources and label selector

Deploy Commands:
  rollout         Manage the rollout of a resource
  scale           Set a new size for a deployment, replica set, or replication controller
  autoscale       Auto-scale a deployment, replica set, stateful set, or replication controller

Cluster Management Commands:
  certificate     Modify certificate resources
  cluster-info    Display cluster information
  top             Display resource (CPU/memory) usage
  cordon          Mark node as unschedulable
  uncordon        Mark node as schedulable
  drain           Drain node in preparation for maintenance
  taint           Update the taints on one or more nodes

Troubleshooting and Debugging Commands:
  describe        Show details of a specific resource or group of resources
  logs            Print the logs for a container in a pod
  attach          Attach to a running container
  exec            Execute a command in a container
  port-forward    Forward one or more local ports to a pod
  proxy           Run a proxy to the Kubernetes API server
  cp              Copy files and directories to and from containers
  auth            Inspect authorization
  debug           Create debugging sessions for troubleshooting workloads and nodes
  events          List events

Advanced Commands:
  diff            Diff the live version against a would-be applied version
  apply           Apply a configuration to a resource by file name or stdin
  patch           Update fields of a resource
  replace         Replace a resource by file name or stdin
  wait            Experimental: Wait for a specific condition on one or many resources
  kustomize       Build a kustomization target from a directory or URL

Settings Commands:
  label           Update the labels on a resource
  annotate        Update the annotations on a resource
  completion      Output shell completion code for the specified shell (bash, zsh, fish, or powershell)

Subcommands provided by plugins:

Other Commands:
  api-resources   Print the supported API resources on the server
  api-versions    Print the supported API versions on the server, in the form of "group/version"
  config          Modify kubeconfig files
  plugin          Provides utilities for interacting with plugins
  version         Print the client and server version information

Usage:
  kubectl [flags] [options]

Use "kubectl <command> --help" for more information about a given command.
Use "kubectl options" for a list of global command-line options (applies to all commands).
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl delete pods --all
pod "nginx" deleted
pod "nginx-deployment-576c6b7b6-8vstz" deleted
pod "nginx-deployment-576c6b7b6-gzths" deleted
pod "nginx-deployment-576c6b7b6-qd4pp" deleted
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl delete services --all
service "kubernetes" deleted
service "my-service" deleted
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pod
NAME                               READY   STATUS    RESTARTS   AGE
nginx-deployment-576c6b7b6-6lwfp   1/1     Running   0          45s
nginx-deployment-576c6b7b6-7zgql   1/1     Running   0          44s
nginx-deployment-576c6b7b6-r5pq9   1/1     Running   0          45s
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl delete deployment --all
deployment.apps "nginx-deployment" deleted
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> kubectl get pod
No resources found in default namespace.
PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> minickube start
minickube : 无法将“minickube”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径
正确，然后再试一次。
所在位置 行:1 字符: 1
+ minickube start
+ ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (minickube:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\yxqz\Downloads\Git\dockerfiles\k8s> minikube start
W0422 11:37:08.660188    9084 main.go:291] Unable to resolve the current Docker CLI context "default": context "default": context not found: open C:\Users\yxqz\.docker\contexts\meta\37a8eec1ce19687d132fe29051dca629d164e2c4958ba141d5f4133a33f0688f\meta.json: The system cannot find the path specified.
😄  Microsoft Windows 11 Home 10.0.22631.3447 Build 22631.3447 上的 minikube v1.33.0
✨  根据现有的配置文件使用 docker 驱动程序
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.43 ...
🤷  docker "minikube" 缺失 container，将重新创建。
🔥  Creating docker container (CPUs=2, Memory=4000MB) ...|
```

