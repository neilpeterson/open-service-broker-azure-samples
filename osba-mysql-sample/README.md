# Open Service Broker for MySQL on Azure

Simple demo using Open Service Broker for Azure to provision and use MySQL on Azure. When running this sample, the following takes place:

- Azure resource group, MySQL instance, and database are created.
- A Kubernetes secret is created with the MySQL connection information.
- A pod is started that consumes the secret, runs the [osba-mysql-demo.py](https://github.com/neilpeterson/open-service-broker-azure-samples/blob/master/osba-mysql-sample/osba-mysql-demo.py), which creates a table named `hello_osba` the OSBA created database.

# Run the sample

First you need a Kubernetes cluster with the Open Service Broker for Azure installed and configured. See this [documentation](https://docs.microsoft.com/en-us/azure/aks/integrate-azure) for steps on configuring OSBA in an Azure Container Service (AKS) cluster.

Once OSBA is configured, the sample can be deployed with the manifest found in this repo or with a Helm chart (detailed here).

Add the azure-samples chart repository:

```
helm repo add azure-samples https://azure-samples.github.io/helm-charts/
```

Run the chart:

```
helm install azure-samples/osba-mysql-demo
```

## Artifacts

**Connection information**

I have included the MySQL connection information as output of the sample application. To retrieve the connection information, first get the pod name.

```
$ kubectl get pods -l app=osba-mysql-demo

NAME                               READY     STATUS    RESTARTS   AGE
osba-mysql-demo-3565274189-kspp6   1/1       Running   0          6m
```

Pull logs from the pod.

```
$ kubectl logs osba-mysql-demo-3565274189-kspp6

MYSQL_USER: qw2fa6emoz@41108ed8-ab9b-47ec-9e5d-86dc33b96a59
MYSQL_PASSWORD: c37oSLhJ392Vssq5
MYSQL_HOST: 41108ed8-ab9b-47ec-9e5d-86dc33b96a59.mysql.database.azure.com
MYSQL_DATABASE: flypz40m5r
```

**Hello OSB table**

Use the connection information and any compatible tool and connect to the MySQL instance. You should find a database with a table named `hello_osba`. This table was created by the application running in the Kubernetes pod. Note, you may need to update the MySQL firewall in order to connect to the MySQL instance.

![osba-storage-demo](./images/hello-osba.png)