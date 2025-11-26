# 基于 Debian 官方 PostgreSQL 17 镜像
FROM postgres:17

# 设置非交互模式
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

# 确认 pg_config 路径
ENV PG_CONFIG=/usr/bin/pg_config

# 拉取 pg_jieba 并编译安装
RUN git clone https://github.com/jaiminpan/pg_jieba.git /pg_jieba \
    && cd /pg_jieba \
    && git submodule update --init --recursive \
    && mkdir build && cd build \
    && cmake .. \
        -DPostgreSQL_EXECUTABLE=$PG_CONFIG \
        -DPostgreSQL_TYPE_INCLUDE_DIR=/usr/include/postgresql/17/server \
    && make \
    && make install

# 拷贝初始化 SQL（Docker 会在第一次启动时自动执行）
COPY init.sql /docker-entrypoint-initdb.d/
