# VirtualMachinePool

VirtualMachinePool is a resource introduced in KubeVirt that allows you to create and manage pools of virtual machines. It provides a convenient way to scale and manage a group of similar virtual machines as a single entity.

## Features

- **Automatic Scaling**: VirtualMachinePool can automatically scale the number of virtual machines based on defined policies and resource usage.
- **Resource Management**: You can specify resource requests and limits for the virtual machines in the pool, ensuring efficient resource utilization.
- **High Availability**: VirtualMachinePool supports configuring high availability policies to ensure virtual machines are distributed across different nodes for better fault tolerance.
- **Template-based Provisioning**: Virtual machines in the pool are created from a common template, allowing for consistent configuration and easy management.
- **[Antiaffinity](https://kubevirt.io/user-guide/operations/node_assignment/#affinity-and-anti-affinity)** rule to schedule on different nodes 

## Usage

1. To create a VirtualMachinePool, 
    - k apply -f [vmpool-nginx.yaml](vmpool-nginx.yaml)
2. Expose as loadbalancer service 
    - k apply -f [vmpool-svc.yaml](vmpool-svc.yaml)
3. Scale replicas 
    - k scale vmpool vmpool-nginx --replicas 5

it's also possible to use the HPA to autoscale the number of replicas based on CPU utilization:

`kubectl autoscale vmpool vm-pool-cirros --min=3 --max=10 --cpu-percent=50`

For more advanced configuration options and examples, refer to the [KubeVirt documentation](https://kubevirt.io/user-guide/user_workloads/pool/)

## Startup Scripts 
KubeVirt supports the ability to assign a startup script to a VirtualMachineInstance instance which is executed automatically when the VM initializes.
Take a look at [cloud-init-with-nginx-secret.yaml](cloud-init-with-nginx-secret.yaml) , we are configuring installation of nginx and customizing welcome page

[More details here](https://kubevirt.io/user-guide/virtual_machines/startup_scripts/) 