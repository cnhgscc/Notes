
```mysql-text
| abt_procedure | CREATE TABLE `abt_procedure` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_time` int(11) NOT NULL,
  `uid` varchar(32) NOT NULL,
  `account` varchar(32) NOT NULL,
  `department` varchar(64) NOT NULL,
  `address` varchar(128) NOT NULL,
  `zone` varchar(32) NOT NULL,
  `trajectory` text NOT NULL,
  `opsuser` varchar(32) DEFAULT NULL,
  `opsphone` varchar(11) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_abt_procedure_uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2616 DEFAULT CHARSET=utf8 |
```
```mysql-text
# 增加列
alter table abt_procedure add column end_time int(11) not null default 1551693565 comment '统计时间' after start_time;
# 删除列
alter table abt_procedure drop column end_time;

alter table abt_procedure add index xindex_t (uid, zone);
```

```
# 查询数据库运行状态
show full processlist

# my.cnf
# 日志中把查询慢的语句添加到log中
log-slow-queries=/data/mysqldata/slowquery.log
long_query_time=2

# mysql server 接收数据包的大小
[mysqld]
max_allowed_packet = 100M
```
