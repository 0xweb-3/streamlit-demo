-- 切换到数据库
\c testdb;

-- 安装 pg_jieba 扩展
CREATE EXTENSION IF NOT EXISTS pg_jieba;

-- 测试 pg_jieba
SELECT to_tsvector('jiebacfg', '我爱中国北京天安门') AS result;

-- 安装 pgvector 扩展
CREATE EXTENSION IF NOT EXISTS vector;

-- 测试 pgvector
CREATE TABLE items (
    id serial PRIMARY KEY,
    embedding vector(3)
);

INSERT INTO items (embedding) VALUES ('[1,2,3]'), ('[4,5,6]');

SELECT * FROM items;
