# 基于官方 PostgreSQL 17 镜像
FROM postgres:17

ENV DEBIAN_FRONTEND=noninteractive

# 安装依赖
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    cmake \
    libpq-dev \
    postgresql-server-dev-17 \
    wget \
    curl \
    perl \
    && rm -rf /var/lib/apt/lists/*

# 设置 pg_config 环境变量
ENV PG_CONFIG=/usr/bin/pg_config

# -----------------------------
# 安装 pg_jieba
# -----------------------------
RUN git clone https://github.com/jaiminpan/pg_jieba.git /pg_jieba \
    && cd /pg_jieba \
    && git submodule update --init --recursive \
    && mkdir build && cd build \
    && cmake .. \
        -DPostgreSQL_EXECUTABLE=$PG_CONFIG \
        -DPostgreSQL_TYPE_INCLUDE_DIR=/usr/include/postgresql/17/server \
    && make \
    && make install

# -----------------------------
# 安装 Rust（pgvector 编译依赖）
# -----------------------------
ENV PATH="/root/.cargo/bin:$PATH"

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
    && rustc --version \
    && cargo --version

# -----------------------------
# 安装 pgvector
# -----------------------------
RUN git clone https://github.com/pgvector/pgvector.git /pgvector \
    && cd /pgvector \
    && make PG_CONFIG=/usr/bin/pg_config \
    && make PG_CONFIG=/usr/bin/pg_config install

# 删除 Rust 减少镜像体积
RUN rm -rf /root/.cargo /root/.rustup

# -----------------------------
# 拷贝初始化 SQL
# -----------------------------
COPY init.sql /docker-entrypoint-initdb.d/
