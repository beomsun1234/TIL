## zipkin.yaml 
 
  apiVersion: v1
  kind: Service
  metadata:
    name: zipkin
  spec:
    ports:
      - port: 9411
        targetPort: 9411
    selector:
      app: zipkin
    externalIPs:
      - [GCP 내부ip]
  ---
  apiVersion: apps/v1
  kind: Deployment
  metadata:
    name: zipkin
  spec:
    selector:
      matchLabels:
        app: zipkin
    strategy:
      type: Recreate
    template:
      metadata:
        labels:
          app: zipkin
      spec:
        containers:
          - image: openzipkin/zipkin
            name: zipkin
            ports:
              - containerPort: 9411 
                name: zipkin
