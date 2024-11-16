
# Tekton

Tekton is an open-source framework for creating CI/CD systems, allowing you to build, test, and deploy across cloud providers and on-premise systems.

## Installation

To install Tekton, follow these steps:

1. Install the Tekton Pipelines:
   
   kubectl apply --filename https://storage.googleapis.com/tekton-releases/pipeline/latest/release.yaml
   

2. Install Tekton Triggers (optional):
   
   kubectl apply --filename https://storage.googleapis.com/tekton-releases/triggers/latest/release.yaml
   

3. Install the Tekton Dashboard (optional):
   
   kubectl apply --filename https://storage.googleapis.com/tekton-releases/dashboard/latest/tekton-dashboard-release.yaml
   

4. Verify the installation:
   
   kubectl get pods --namespace tekton-pipelines
   

## Getting Started

After installation, you can create Tekton resources such as Tasks, Pipelines, and PipelineRuns to define and execute your CI/CD workflows.

For more information and detailed documentation, visit the [official Tekton website](https://tekton.dev/).


## Deploying Windows Server 2022 usings Tasks and Pipelines
Sample pipelines can be found at https://github.com/kubevirt/kubevirt-tekton-tasks/tree/main/release/pipelines/windows-efi-installer 

Get the Windows 2022 download link from here, https://www.microsoft.com/en-us/evalcenter/download-windows-server-2022

`export WIN_IMAGE_DOWNLOAD_URL=https://your-download-link-here.iso`

eg: `export WIN_IMAGE_DOWNLOAD_URL='https://software-static.download.prss.microsoft.com/sg/download/888969d5-f34g-4e03-ac9d-1f9786c66749/SERVER_EVAL_x64FRE_en-us.iso'`

Apply the config map which sets the unattended EFI installer

`k apply -f vm/tekton/windows-efi-installer-configmaps.yaml`

Apply the role and rolebinding to the default service account, this would allow tekton pipeline to create the needed resources in the cluster. 

`k apply -f vm/tekton/sa-with-rb.yaml`

Create the pipeline resource which deploys Windows Server 2022 and configure the DV with the EFI installer. This DV can then be used as a Golden Image for cloning.

Read more about the pipeline and tasks here: https://github.com/kubevirt/kubevirt-tekton-tasks/tree/main/release/pipelines/windows-efi-installer

`k create -f vm/tekton/create-windows-2022-pipeline.yaml`

Now lets create the Windows Server 2022 VM by running:

`k apply -f vm/tekton/deploy-win22-from-golden.yaml`

