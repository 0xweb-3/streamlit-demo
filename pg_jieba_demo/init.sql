-- 创建数据库
CREATE DATABASE testdb;

-- 切换到 testdb
\c testdb;

-- 安装 pg_jieba 扩展
CREATE EXTENSION IF NOT EXISTS pg_jieba;

-- 查询有关jieba的配置名
SELECT cfgname FROM pg_ts_config WHERE cfgname LIKE 'jieba%';

-- 测试分词
SELECT to_tsvector('jiebacfg', '我爱中国北京天安门') AS result;
SELECT to_tsvector('jiebaqry', '我爱中国北京天安门') AS result;
