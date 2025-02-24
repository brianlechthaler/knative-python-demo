# Knative Python Demo
## `reflect` Quickstart
1. Install Knative serving: https://knative.dev/docs/install/yaml-install/serving/install-serving-with-yaml
2. Clone this repository: `git clone https://github.com/brianlechthaler/knative-python-demo;cd knative-python-demo`
3. Deploy `reflect.yml` demo: `kubectl apply -f reflect.yml`
4. Copy the endpoint URL to your clipboard from this command: `kubectl get ksvc knative-python-demo--reflect` and store it in `$ENDPOINT_URL`
5. Use cURL to query the endpoint: `curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST $URL`, this should return `{"request":{"key1":"value1","key2":"value2"}}`
