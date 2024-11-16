# Getting Started with Kubernetes

## Setting up kubectl

1. Download the latest release of `kubectl` from the official Kubernetes release page: https://kubernetes.io/docs/tasks/tools/install-kubectl/

2. Unpack the archive and move the `kubectl` binary to a directory in your `$PATH`.

## Useful Aliases

``` bash
alias k=kubectl
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kgd='kubectl get deployments'
```

## Enabling Autocompletion

To enable autocompletion for `kubectl` commands, follow the instructions for your shell:

- [Bash](https://kubernetes.io/docs/tasks/tools/install-kubectl/#enabling-shell-autocompletion)
- [Zsh](https://kubernetes.io/docs/tasks/tools/install-kubectl/#enabling-shell-autocompletion)

## Connecting to a Cluster with kubeconfig

1. Obtain the `kubeconfig` file from your cluster administrator or cloud provider.

2. Create the folder `mkdir -p $HOME/.kube` and copy your `kubeconfig` file to `config`. `cp kubeconfig $HOME/.kube/config`
*`$HOME/.kube/config` is the default location where kubernetes checks the config file*
Another approach is by setting an env

3. Set the `KUBECONFIG` environment variable:

 - `export KUBECONFIG=/path/to/kubeconfig`


4. Verify that you can connect to the cluster:

- `kubectl cluster-info`


## Checking Context and Nodes

1. Check the current context:


- `kubectl config current-context`


2. List all available contexts:


- `kubectl config get-contexts`


3. Get information about the nodes in the cluster:


- `kubectl get nodes -o wide`

