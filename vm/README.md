# Create VMs from various sources

## Kubevirt VirtualMachine CRD

The Kubevirt VirtualMachine CRD (Custom Resource Definition) allows you to create and manage virtual machines in a Kubernetes cluster. It provides a declarative way to define the specifications of a virtual machine, including CPU, memory, disks, and networking resources.

With the VirtualMachine CRD, you can:

- Define virtual machine specifications using YAML or JSON
- Manage the lifecycle of virtual machines (create, update, delete)
- Attach disks and network interfaces to virtual machines
- Expose virtual machine services using Kubernetes Services and Ingress
- Scale virtual machines using Kubernetes ReplicaSets or Deployments

[KubeVirt VirtualMachine Documentation](https://kubevirt.io/user-guide/virtual_machines/creating_vms/)

## Injecting SSH keys and users with Cloud-init's Cloud-config
If you do not have a ssh key already, generate an ssh key using the command:
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@corp.com"
```
More details on generating ssh keys can be found here: https://www.ssh.com/academy/ssh/keygen

Now you can use the public key in a cloud-init user-data config to authorize login
Take a look at [cloud-init-secret.yaml](cloud-init-secret.yaml)
  - k apply -f [cloud-init-secret.yaml](cloud-init-secret.yaml)
[More docs here](https://kubevirt.io/user-guide/virtual_machines/startup_scripts/#injecting-ssh-keys-with-cloud-inits-cloud-config)


There are multiple ways of creating VMs from various sources, 

- PVC
    - k apply -f [demo-ubuntu-vm-from-pvc.yaml](demo-ubuntu-vm-from-pvc.yaml)
    It's possible to bring your own iso/qcow2 image and load it to a DV. Refer, [rhel9-dv.yaml](rhel9-dv.yaml)
- local Image/ISO
    - virtctl image-upload pvc cirros-0.6.3.img --size=3Gi --image-path=cirros-0.6.3-aarch64-disk.img --insecure
    - k apply -f [demo-vm-from-local-image.yaml](demo-vm-from-local-image.yaml)
- Image/ISO url 
    - k apply -f [demo-vm-from-image-url.yaml](demo-vm-from-image-url.yaml)
- S3
    - Minio, an S3-compatible object storage server can be deployed for testing
    - `helm repo add minio https://helm.min.io/` 
    - `helm install minio -f vm/minio-values.yaml minio/minio`
    - k apply -f [demo-vm-from-s3.yaml](demo-vm-from-s3.yaml)
- Registry (eg: Harbor)
    - to build the image, `docker build -f vm/ubuntu.dockerfile . -t harbor-repo.corp.com/vmimages/ubuntu:24.10` and push to registry.
    - k apply -f [harbor-creds-secret.yaml](harbor-creds-secret.yaml) ### `Secret` for harbor credentials
    - k apply -f [ca-cert-cm.yaml](ca-cert-cm.yaml) ### `ConfigMap` for harbor ca cert
    - k apply -f [demo-vm-from-harbor.yaml](demo-vm-from-harbor.yaml)
- vCenter
    - k apply -f [demo-vm-from-vcenter.yaml](demo-vm-from-vcenter.yaml)

## SSH to the vm
Add the below configuration to your ~/.ssh/config to ssh into the vm. You would also need virtctl installed.

Make sure to use private key correspoinding to id_rsa which was reffered in cloud-init secret.


``` bash
Host vmi/*
        StrictHostKeyChecking no
        IdentityFile ~/.ssh/id_rsa ## your ssh private key path 
        ProxyCommand virtctl port-forward --stdio=true %h %p
Host vm/*
        StrictHostKeyChecking no
        IdentityFile ~/.ssh/id_rsa ## your ssh private key path 
        ProxyCommand virtctl port-forward --stdio=true %h %p
```
## Access VMs
### Method 1: SSH
Use the below steps to ssh into the vm:

`ssh <username>@vm/<vm-name>`

### Method 2: LoadBalancer (similar to associate a floating ip in Openstack)
By defaults VMs created are not accessible outside of the cluster, you will have to expose the VM as a Loadbalancer
 - LoadBalancer (similar to associate a floating ip in Openstack)

        - virtctl expose vm demo-vm-from-pvc --port=22 --name=demo-vm-from-pvc-ssh --type=LoadBalancer

        - virtctl expose vm win10 --port=3389 --name=win10-rdp-svc --type=LoadBalancer ## to enable RDP for windows VM

More details here, https://kubevirt.io/user-guide/virtual_machines/accessing_virtual_machines/ 



## Access VM using VNC
- https://kubevirt.io/user-guide/user_workloads/accessing_virtual_machines/

``` bash
virtctl vnc <vm name>
```

## Live patch the VM to increase CPU/Memory, 


``` bash
kubectl patch vm demo-vm-from-image-url  --type json -p '[{"op": "replace", "path": "/spec/instancetype", "value": {"name": "u1.large", "revisionName": ""}}]'
``` 