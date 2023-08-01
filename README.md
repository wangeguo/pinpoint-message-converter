# Pinpoint Message Converter

Pinpoint message converter, running in python.d mode, provides an HTTP service
to the outside world, receiving raw data requests or bulk JSON lists, parsing
and converting them into line protocols and returning them.

## Prerequisites

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

## Development

### 1. Build the `pinpoint_parser` module

```
cd pinpoint_parser/
pip3 setup.py develop
```

### 2. Setting up the runtime on python.d

For development purposes, the DatakitFramework is simulated in main.py. When
running in python.d mode, please import the real package and comment out the
simulated code:

a. Enable DatakitFramework imports

```
from datakit_framework import DataKitFramework
```

b. Comment out the mock DataKitFramework

```
# class DataKitFramework:
#     name = "DataKitFramework"
#     interval = 10
#
#     def run(self):
#         pass
```

### 3. Configure Environment Variables

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

**First:**, go to the `pinpoint_parser/` directory and execute the following
command to generate the .whl package:

```
cd pinpoint_parser/
pip3 wheel .
```

Then run the following command to install this extension in your production
environment:

```
pip3 install pinpoint_parser-xxx.whl
```

*Specific file names are based on the actual operating system and architecture*

**Second:** Place the code for this project in the python.d directory of Datakit
and configure the parameters for the kafka and python.d collectors.

- Subscribe to Data in Kafka https://docs.guance.com/en/integrations/kafkamq/
- Developing Custom Collector with Python
  https://docs.guance.com/en/integrations/pythond/
- python.d handler for kafka: (Gitlab):
  https://gitlab.jiagouyun.com/cloudcare-tools/datakit/-/issues/1797 or
  (Github): https://github.com/GuanceCloud/datakit/issues/21

## Notes:
Execute the `python3 -m site` command to get the path to the installed module.
