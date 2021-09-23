# zabbixProcessLLD
![](https://img.shields.io/badge/zabbix-4.0-green) ![](https://img.shields.io/badge/python-3.6-green)

基于zabbix低级别自动发现（low level discovery）监控系统进程，监控指定进程名称数量，当进程数量为0时报警。
python文件放入zabbix客户端/etc/zabbix/scripts/，修改processMonitory.py中monitor_key更改监控进程；user.conf放入如/etc/zabbix/zabbix_agentd.d/中，重启agent。

服务端导入xml模板，修改主机添加模板完成监控添加。

如需自行创建模板，自动发现规则键值process.discovery，过滤器{#NAME}，监控项键值process.get[{#NAME}]，触发器{linux_process_monitor_lld:process.get[{#NAME}].last()}<>1
