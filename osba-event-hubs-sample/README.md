# Open Service Broker for Azure Storage Demo

Simple demo using Open Service Broker for Azure to provision and use Azure Storage. When running this sample, the following takes place:

- Azure resource group, storage account, and storage container is created.
- A Kubernetes secret is automatically created with the names and credentials for the storage account.
- A pod is started that consumes the secrets, runs the [osba-storage-demo.py](https://github.com/neilpeterson/osba-storage-sample/blob/master/osba-storage-demo.py), which writes a `hello-osba` file to the storage account.

# Run the sample

First you need a Kubernetes cluster with the Open Service Broker for Azure installed and configured. See this [documentation](https://docs.microsoft.com/en-us/azure/aks/integrate-azure) for steps on configuring OSBA in an Azure Container Service (AKS) cluster.

Once OSBA is configured, the sample can be deployed with the manifest found in this repo or with a Helm chart (detailed here).

Add the azure-samples chart repository:

```
helm repo add azure-samples https://azure-samples.github.io/helm-charts/
```

Run the chart:

```
helm install azure-samples/osba-storage-demo
```

## Artifacts

**Storage Account / File**:

If you open the Azure portal and browse to the storage account / blob, you should see that a file named `hello-osba` has been created.

![osba-storage-demo](./images/hello-osba.png)