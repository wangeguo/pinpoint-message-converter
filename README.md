# Pinpoint Message Converter

Pinpoint message converter, provides an HTTP service to the outside world,
receiving raw data requests or bulk JSON lists, parsing and converting them into
line protocols and returning them.

## Quick Start

You can run `build.sh` directly to build a Docker image and then run the `docker
 run` command, or run `deploy.sh` to run on the Kubernetes platform.

 ```
 build.sh && deploy.sh
 ```

## Development

If you want to perform the build or debug development locally, you need to
install the appropriate dependencies as instructed below.

### Prerequisites

The Rust build environment needs to be pre-installed to compile the
`pinpoint_parser` module, and the project runtime dependencies.

a. Basics & Tools

```
apt-get update
apt-get install -y curl ca-certificates gcc libc6-dev
```

b. Install Rust

```
curl https://sh.rustup.rs -sSf | sh -s -- -y
export PATH="/root/.cargo/bin:${PATH}"
```

c. Configuring Python Module Build Variables

```
export PYTHONDONTWRITEBYTECODE=1
export PYTHONUNBUFFERED=1
```

d. Install dependencies for the project:

```
pip3 install -r requirements.txt \
    -i http://pypi.douban.com/simple/ \
    --trusted-host=pypi.douban.com/simple
```

### 1. Build the `pinpoint_parser` module

```
cd pinpoint_parser/
pip3 setup.py develop
```

### 2. Configure Environment Variables

```
cp .env.sample .env
```

*Please adjust its parameters according to the actual situation.*

## Testing

Unit testing and end-to-end testing for this project can be performed by
installing pytest with the following commands:

```
pip3 install pytest
```

Then, run the following command to test:

```
pytest -rP
```

## Deployment in production environments

In production environments, it will run as a standalone Kubernetes Deployment
and be exposed as a Service to provide standard HTTP services to the outside
world.

### 1. Run the build.sh script to build the Docker image

```
build.sh
```

### 2. Copy or Upload resources

Upload the exported image package and k8s-testing.yaml to the Kubernetes host
and modify the corresponding parameter values.

```
cp pinpoint-message-converter-{version}.tar /path/to/target/
cp k8s-testing.yaml /path/to/target/
```

### 3. Import image tar to container runtime

Execute the appropriate commands to import the image package to the Kubernetes
nodes. The specific commands vary depending on the container engine.

### 4. Finally, execute the following commands to deploy

```
kubectl apply -f k8s-testing.yaml
```

### 5. Configuring the Kafka Collector

- Subscribe to Data in Kafka https://docs.guance.com/en/integrations/kafkamq/
- Developing Custom Collector with Python
  https://docs.guance.com/en/integrations/pythond/
- python.d handler for kafka: (Gitlab):
  https://gitlab.jiagouyun.com/cloudcare-tools/datakit/-/issues/1797 or
  (Github): https://github.com/GuanceCloud/datakit/issues/21
