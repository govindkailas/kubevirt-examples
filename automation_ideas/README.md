# Automation ideas!

## Scheduling of KubeVirt VMs using Cronjobs
We can use Kubernetes CronJobs to schedule VMs to run during office hours and shut them down automatically after hours. For example, shut down all the VM in the dev namespace after 6 PM and bring them back up at 8 AM the next day.

Apply the RoleBinding for the default service account to have accees to the KubeVirt CRDs:

`k apply -f kubevirt-rolebinding.yaml`

The pods initiates by the CronJobs will have access to the KubeVirt APIs and resources like virtual machines due to this RoleBinding for the default service account.


Take a look at the cronjobs if you wish to automate VM start and stop in your namespace :) 

- [startvm-cronjob.yaml](startvm-cronjob.yaml) 

- [stopvm-cronjob.yaml](stopvm-cronjob.yaml)

If you would like to immediatlely test stopping VMs, create a `Job` by running:

`k create job --from=cronjob/stop-myvm stop-vms-now` 

