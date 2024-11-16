# Nginx Deployment and LoadBalancer Service
This guide will walk you through the process of deploying a simple Nginx web server as a Deployment and exposing it as a LoadBalancer Service in a Kubernetes cluster.

## Prerequisites
- A Kubernetes cluster up and running (you can use a local cluster like Minikube or a cloud-based cluster like GKE, EKS, or AKS)
- The kubectl command-line tool installed and configured to communicate with your cluster

## Deployment
Create a nginx-deployment.yaml file with the following content:
``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:alpine
        ports:
        - containerPort: 80
```


This configuration defines a Deployment with 3 replicas of the Nginx container.

Apply the Deployment to your cluster:
`kubectl apply -f nginx-deployment.yaml`



Verify that the Deployment was created and the Pods are running:
``` bash
kubectl get deployments
kubectl get pods
```


## Expose your application 
There are multiple methods to expose an application in Kubernetes:
1. **ClusterIP Service**: This is the default service type in Kubernetes. It exposes the application internally within the cluster, allowing other applications within the same cluster to access it. However, it is not accessible from outside the cluster.

2. **NodePort Service**: This type of service exposes the application on a static port on each worker node in the cluster. It allows external clients to access the application by sending requests to any node's IP address and the specified NodePort.

3. **LoadBalancer Service**: This service type provisions an external load balancer (if supported by the underlying cloud provider) and assigns a publicly accessible IP address to the service. External clients can access the application using this IP address.

4. **Ingress**: Ingress is a collection of rules that allow inbound connections to reach cluster services. It acts as a reverse proxy and load balancer, routing traffic to different services based on the requested hostname or URL path. Ingress controllers, like NGINX or Contour, are responsible for implementing the Ingress rules.

5. **Port Forwarding**: Kubernetes provides a `kubectl port-forward` command that allows you to forward a local port to a port on a pod or service within the cluster. This is useful for debugging or accessing an application temporarily from your local machine.

## LoadBalancer Service
Create a nginx-service.yaml file with the following content:
``` yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
```


This configuration defines a LoadBalancer Service that will forward traffic to the Nginx Pods.

Apply the Service to your cluster:
`kubectl apply -f nginx-service.yaml`


Verify that the Service was created:
`kubectl get services`



You should see the nginx-service with an external IP address 

Access the Nginx web server using the external IP address of the LoadBalancer Service.


## Check out the go microservice
There is a simple go microservice which print the podname, namespace and nodename. Do deploy it, 
``` bash
kubectl apply -f k8s_deployment/simple-app-deploy-svc.yaml
```

## Cleanup
To delete the Deployment and Service, run:
``` bash 
kubectl delete deployment nginx-deployment
kubectl delete service nginx-service
```


