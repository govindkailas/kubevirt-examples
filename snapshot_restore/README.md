# Kubevirt Snapshot and Restore CRD

The Kubevirt Snapshot and Restore CRD provides a way to take snapshots of virtual machine disks and restore them later. This allows you to create backups of your virtual machines and recover from failures or data corruption.

## Snapshot

The `VirtualMachineSnapshot` CRD represents a snapshot of a virtual machine's disks at a specific point in time. It contains metadata about the snapshot and references to the underlying storage snapshots.

## Restore

The `VirtualMachineRestore` CRD is used to restore a virtual machine from a previously taken snapshot. It references the `VirtualMachineSnapshot` object and specifies the target virtual machine to restore the snapshot to.

## Usage

1. Create a `VirtualMachineSnapshot` object to take a snapshot of a virtual machine's disks.
    -  k apply -f [snapshot.yaml](snapshot.yaml)
2. Wait for the snapshot to complete successfully.
3. Create a `VirtualMachineRestore` object to restore the virtual machine from the snapshot.
     -  k apply -f [restore.yaml](restore.yaml)
4. Wait for the restore process to complete.

For detailed usage instructions and examples, please refer to the [KubeVirt snapshot and restore documentation](https://kubevirt.io/user-guide/operations/snapshot_restore_api/).
