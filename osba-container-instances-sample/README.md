# Open Service Broker for Azure Container Instances Demo

Simple demo using Open Service Broker for Azure to provision an Azure Container Instance. When running this sample, the following takes place:

- Azure resource group and Azure Container Instances is created with a Public IP Address.
- A Kubernetes secret is automatically created that contains the ACI Public IP Address.
- A pod is started that consumes the secrets, runs the [osba-container-instances-demo.py](https://github.com/neilpeterson/osba-storage-sample/blob/master/osba-storage-demo.py), which validates that the ACI instances is running.

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

**Storage Account / File**:

If you open the Azure portal and browse to the storage account / blob, you should see that a file named `hello-osba` has been created.

![osba-storage-demo](./images/hello-osba.png)