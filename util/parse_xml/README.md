## Quartz配置文件解析
> 用于提取和解析 **Quartz** 定时任务配置文件中的关键信息。

## 背景
> 在工作中，经常会碰到各种中大型的 **JavaEE** 项目，其中可能包含大量且杂乱的定时任务配置。有时这些配置缺乏信息维护，也没有提供手动触发的机制，书写无规范性，导致快速获取相关信息带来了挑战。因此，为了解决这一问题，可以编写脚本来自动提取和分析定时任务配置，以便快速获取相关信息。

## 运行环境

|Python版本|3.11.6|
|--|--|

### 初阶版
> 配置写法有多种，但至少保持相同的 **书写规范**，一般写法如下:

```xml
 <!-- Job One -->
<bean id="jobOneBean" class="com.test.quartz.service.jobOne"></bean>
<bean id="jobOneDetail" class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
    <property name="targetObject" ref="jobOneBean"/>
    <property name="targetMethod" value="jobOneMethod"/>
</bean>
<bean id="jobOneTrigger" class="org.springframework.scheduling.quartz.CronTriggerFactoryBean">
    <property name="jobDetail" ref="jobOneDetail"/>
    <property name="cronExpression" value="0 0/1 * * * ?"/>
</bean>
```

#### 运行结果
![parse_quartz_config_basic](/image/img/parse_quartz_config.png)
