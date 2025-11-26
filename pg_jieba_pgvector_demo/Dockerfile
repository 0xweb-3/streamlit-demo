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
    postgresql-17-pgvector \
    wget \
    curl \
    perl \
    && rm -rf /var/lib/apt/lists/*

## 设置 pg_config 环境变量
#ENV PG_CONFIG=/usr/bin/pg_config
ENV PG_CONFIG=/usr/lib/postgresql/17/bin/pg_config
ENV PATH="/usr/lib/postgresql/17/bin:$PATH"

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
# 拷贝初始化 SQL
# -----------------------------
COPY init.sql /docker-entrypoint-initdb.d/
