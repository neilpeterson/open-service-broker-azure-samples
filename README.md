# Open Service Broker for Azure Samples

This is a collection of samples for demoing the Open Service Broker for Azure. Each sample creates an instance of a managed Azure service, and then an application running in a Kubernetes POD that interacts with the Azure service. These samples are all simple (Hello OSBA), however include all artifacts needed for real world replication.

Each sample includes a complete Kubernetes manifest, and a ready to run Helm chart. Your Kubernetes cluster must have the Kubernetes Service catalog installed and the Azure broker installed. See [this document](https://docs.microsoft.com/en-us/azure/aks/integrate-azure) for installation instructions on Azure Container Service (AKS).

## Included Samples

- [Azure Blob Storage](https://github.com/neilpeterson/open-service-broker-azure-samples/tree/master/osba-blob-storage-sample)
- [Azure CosmosDB / MongoDB](https://github.com/neilpeterson/open-service-broker-azure-samples/tree/master/osba-cosmosdb-mongodb-sample)
- [Azure Container Instances (AC)](https://github.com/neilpeterson/open-service-broker-azure-samples/tree/master/osba-container-instances-sample)
- Azure Event Hubs - comming soon