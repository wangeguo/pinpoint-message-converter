# syntax=docker/dockerfile:1

FROM python:3.10-slim AS builder

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl ca-certificates gcc libc6-dev

# Install Rust
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt \
    -i http://pypi.douban.com/simple/ \
    --trusted-host=pypi.douban.com/simple

# Build pinpoint parser
COPY pinpoint_parser pinpoint_parser
RUN cd pinpoint_parser && \
    python setup.py develop   && \
    cd ..


# Final stage
FROM python:3.10-slim

RUN apt-get update
RUN apt-get install -y vim

WORKDIR /app
COPY . .

COPY --from=builder /app/venv ./venv
COPY --from=builder /app/pinpoint_parser ./pinpoint_parser

ENV PATH="/app/venv/bin:$PATH"
CMD ["python", "main.py"]
