# Open Service Broker for Azure Container Instances Demo

Simple demo using Open Service Broker for Azure to provision an Azure Container Instance. When running this sample, the following takes place:

- Azure resource group and Azure Container Instances is created with a Public IP Address.
- A Kubernetes secret is automatically created that contains the ACI Public IP Address.
- A pod is started that consumes the secrets, runs the [osba-container-instances-demo.py](https://github.com/neilpeterson/open-service-broker-azure-samples/blob/master/osba-container-instances-sample/osba-container-instances-sample.py), which validates that the ACI instances is running.

# Run the sample

First you need a Kubernetes cluster with the Open Service Broker for Azure installed and configured. See this [documentation](https://docs.microsoft.com/en-us/azure/aks/integrate-azure) for steps on configuring OSBA in an Azure Container Service (AKS) cluster.

Once OSBA is configured, the sample can be deployed with the manifest found in this repo or with a Helm chart (detailed here).

Add the azure-samples chart repository:

```
helm repo add azure-samples https://azure-samples.github.io/helm-charts/
```

Run the chart:

```
helm install azure-samples/osba-container-instances-demo
```

## Artifacts

Once the ACI instance has been created, a pod starts and sends an HTTP request to the app running in the ACI instance. The results can be seen by pulling logs on the Kubernetes pod.

First, get the pod name:

```
$ kubectl get pods

NAME                                            READY     STATUS    RESTARTS   AGE
osba-container-instances-demo-9fb6ff8ff-2xbfg   1/1       Running   0          5m
```

Pull logs from the pod:

```
$ kubectl logs osba-container-instances-demo-9fb6ff8ff-2xbfg

Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
Hello OSB ACI Container is UP..
```