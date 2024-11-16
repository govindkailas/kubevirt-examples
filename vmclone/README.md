# Kubevirt VirtualMachine Clone CRD

The Kubevirt VirtualMachine Clone CRD allows you to create a new VirtualMachine from an existing VirtualMachine or VirtualMachineInstance. This can be useful for creating multiple identical VMs or for creating a new VM from a known good state.

## Usage

To create a new VirtualMachine clone, create a new `VirtualMachineClone` resource:

``` yaml
apiVersion: vmclone.kubevirt.io/v1alpha1
kind: VirtualMachineClone
metadata:
  name: myvm-clone
spec:
  source:
    kind: VirtualMachine
    name: myvm
  targetName: myvm-clone
```

This will create a new VirtualMachine named `myvm-clone` based on the existing `myvm` VirtualMachine.

You can also clone from a VirtualMachineInstance:

``` yaml
apiVersion: vmclone.kubevirt.io/v1alpha1
kind: VirtualMachineClone
metadata:
  name: myvm-clone
spec:
  source:
    kind: VirtualMachineInstance
    name: myvm-instance
  targetName: myvm-clone
```

## Example 
k apply -f [clone.yaml](clone.yaml)


Clone will be created with same spec as source VM but with targetName, allowing identical VMs to be created.


To check status of clone creation:
```
kubectl get vmclone 
```

The clonned VM will be in stopped state. To start it:
```
virtctl start myvm-clone
```


## Features

- Clone from VirtualMachine or VirtualMachineInstance
- Customize the clone name
- Preserve source annotations and labels (configurable)
- Preserve source volumes and volume claims (configurable)

## Limitations

- Cloning is a new feature and is still under active development
- Some advanced features like live migration may not work on cloned VMs

For more information, see the [Kubevirt documentation](https://kubevirt.io/user-guide/operations/clone_api/).
