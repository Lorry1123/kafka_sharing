# Kafka 分享实验代码

## Kafka 安装与启动

- [Quickstart](http://kafka.apache.org/quickstart)

## python client

- kafka-python
- [其他可选项](https://cwiki.apache.org/confluence/display/KAFKA/Clients#Clients-Python)

## 实验 1

- 目的：尝试启动 `Producer` 和 `Consumer`，接触 `Topic`
- 方法：创建一个 topic，启动 `test1/consumer.py` 和 `test1/producer.py`，观察情况

## 实验 2

- 目的：多个消费者的 `partition` 管理
- 方法：创建一个 topic 并指定其 `partition = 2`，在 实验 1 的基础上，增加一个 consumer，并且指定两个 consumer 的 `group_id`，同时运行两个 consumer 和 producer

## 实验 3

- 目的：`offset` 管理
- 方法：创建一个 topic，在实验 1 的基础上，关闭 consumer 的自动 commit 选项（即不再自动返回 ACK），重复启动，观察启动时消费到的第一条消息 offset 信息。然后打开 comsumer 的自动 commit，再次启动，观察 offset
