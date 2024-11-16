# 🚀 KubeVirt examples

If you are new to Kubernetes, take a look at [k8s_getting_started](k8s_getting_started/README.md) and [k8s_deployment](k8s_deployment/README.md)

## Pre-requisite

- Access to a working KubeVirt cluster 🔥
- Install virtctl stable version for kubevirt:

``` bash
export VERSION=$(curl -L -s https://storage.googleapis.com/kubevirt-prow/release/kubevirt/kubevirt/stable.txt)
sudo curl -L -o /usr/local/bin/virtctl https://github.com/kubevirt/kubevirt/releases/download/${VERSION}/virtctl-${VERSION}-linux-amd64 
sudo chmod +x /usr/local/bin/virtctl
```

1. ☸️ Getting started with Kubernetes [k8s_getting_started](k8s_getting_started/README.md)
2. 🚢 Learn about Kubernetes deployment [k8s_deployment](k8s_deployment/README.md)
3. 💻 Everything about creating VMs under [vm](vm/READEME.md)
4. 🏭 Create and automate a set of similar VMs using VMPools, [vmpool](vmpool/README.md) 
5. 📚 Create a new VM by cloning, [vmclone](vmclone/README.md)
6. 💾 Snapshot and restore from a VM [snapshot_restore](snapshot_restore/README.md)
7. 🤖 Scope of automation using KubeVirt and its CRDs [automation_ideas](automation_ideas/README.md)

If you have any sugessions or improvements, open an issue here
