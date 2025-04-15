from pyVim import connect
from pyVmomi import vim
import ssl
import socket
import hashlib

class VCenterManager:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def connect(self):
        try:
            self.si = connect.SmartConnect(host=self.host, user=self.username, pwd=self.password, disableSslCertValidation=True)
            return True
        except Exception as e:
            print(f"Failed to connect to vCenter Server: {e}")
            return False

    def disconnect(self):
        connect.Disconnect(self.si)

    def get_vm_info(self, vm_name):
        content = self.si.RetrieveContent()
        for child in content.rootFolder.childEntity:
            if hasattr(child, 'vmFolder'):
                vm_folder = child.vmFolder
                vm_list = vm_folder.childEntity
                for v in vm_list:
                    if isinstance(v, vim.VirtualMachine) and v.name == vm_name:
                        # Get CPU and Memory info
                        cpu_count = v.config.hardware.numCPU
                        memory_gb = v.config.hardware.memoryMB / 1024  # Convert MB to GB
                        
                        # Get disk info
                        disks = []
                        for device in v.config.hardware.device:
                            if isinstance(device, vim.vm.device.VirtualDisk):
                                disk_info = {
                                    'fileName': device.backing.fileName,
                                    'capacityGB': device.capacityInKB / 1024 / 1024
                                }
                                disks.append(disk_info)
                        
                        # Get boot option (BIOS or UEFI)
                        boot_option = v.config.firmware  # Returns 'bios' or 'efi'
                        boot_option = 'UEFI' if boot_option == 'efi' else 'BIOS'  # Normalize for output
                        
                        return {
                            'uuid': v.config.uuid,
                            'cpu_count': cpu_count,
                            'memory_gb': memory_gb,
                            'disks': disks,
                            'boot_option': boot_option
                        }
        return None

class ThumbprintRetriever:
    @staticmethod
    def get_thumbprint(server_name):
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

            with socket.create_connection((server_name, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=server_name) as ssl_sock:
                    cert = ssl_sock.getpeercert(True)
                    thumbprint = hashlib.sha1(cert).hexdigest().upper()
                    formatted_thumbprint = ':'.join([thumbprint[i:i+2] for i in range(0, len(thumbprint), 2)])
                    return formatted_thumbprint
        except Exception as e:
            print(f"Failed to retrieve thumbprint: {e}")
            return None

def main():
    vcenter_host = "10.10.10.10"
    username = "administrator@vsphere.local"
    password = "my$tronGPass"
    vm_name = "Win10-VM"

    vcenter_manager = VCenterManager(vcenter_host, username, password)
    if vcenter_manager.connect():
        vm_info = vcenter_manager.get_vm_info(vm_name)
        if vm_info:
            print(f'uuid: "{vm_info["uuid"]}"')
            print(f'CPU count: {vm_info["cpu_count"]}')
            print(f'Memory: {vm_info["memory_gb"]:.2f} GB')
            print(f'Boot Option: {vm_info["boot_option"]}')
            for i, disk in enumerate(vm_info["disks"], 1):
                print(f'Disk {i}:')
                print(f'  Backing File: "{disk["fileName"]}"')
                print(f'  Capacity: {disk["capacityGB"]:.2f} GB')
        else:
            print(f"VM '{vm_name}' not found")
        vcenter_manager.disconnect()

        thumbprint = ThumbprintRetriever.get_thumbprint(vcenter_host)
        if thumbprint:
            print(f'thumbprint: "{thumbprint}"')

        print(f'url: "https://{vcenter_host}"')
        
    else:
        print("Failed to connect to vCenter Server")

if __name__ == "__main__":
    main()
