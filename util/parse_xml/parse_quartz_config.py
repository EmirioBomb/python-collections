import xml.etree.ElementTree as ET
import os
import time

def parse_quartz_config(xml_file):
    """
    【常规写法】解析Quartz配置文件，按照： 触发器ID、触发器任务ID、执行类Bean ID、执行类、执行方法、CRON表达式输出
    基本思路: 
        1. 获取所有定时任务触发器
        2. 获取触发器对应的jobDetail 及 cronExpression 属性
        3. 根据jobDetail的Bean，获取执行类及执行方法

    Args:
        xml_file: 定时任务配置文件

    Raises:
        Exception: 任何异常
    """

    # 声明配置文件命名空间，find，findall必须使用此命名空间
    NS = {'beans': 'http://www.springframework.org/schema/beans'}

    tree = ET.parse(xml_file)   # 解析XML文件
    root = tree.getroot()       # 获取根节点

    # 遍历所有Bean
    beans = root.findall(".//beans:bean", NS)

    # 遍历所有触发器
    job_triggers = root.findall(".//beans:bean[@class='org.springframework.scheduling.quartz.CronTriggerFactoryBean']", NS)
    print(f"本次共扫描到: {len(job_triggers)} 个定时任务触发器")

    print("JobTrigger \t JobDetail \t TargetObject \t TargetService \t TargetMethod \t CronExpression")

    # 遍历获取触发器相关信息
    for trigger in job_triggers:
        job_trigger_id = trigger.get("id")
        # 获取cron表达式
        cron_expression = trigger.find("beans:property[@name='cronExpression']", NS).get('value')
        # 获取jobDetail
        job_detail_ref = trigger.find("beans:property[@name='jobDetail']", NS).get('ref')

        for job_detail_bean in beans:
            if job_detail_bean.get("id") == job_detail_ref:
                # 获取执行任务方法名称
                target_method = job_detail_bean.find("beans:property[@name='targetMethod']", NS).get("value")
                # 获取执行任务Bean
                target_object = job_detail_bean.find("beans:property[@name='targetObject']", NS).get("ref")

                # 写法1: 遍历
                for target_bean in beans: 
                    if target_bean.get("id") == target_object:
                        target_service = target_bean.get("class")

                # # 写法2: 利用set特性，优化可参考 parse_quartz_config_optimize(xml_file)
                # target_class_set = {target_bean.get("class") for target_bean in beans if target_bean.get("id") == target_object}
                # # 因find返回第一个匹配到的节点，顾set元素理论上只为1个
                # target_service = str(next(iter(target_class_set)))
                
        print(f"{job_trigger_id} \t {job_detail_ref} \t {target_object} \t {target_service} \t {target_method} \t {cron_expression} ")


def parse_quartz_config_optimize(xml_file):
    """
    【优化写法】解析Quartz配置文件，按照： 触发器ID、触发器任务ID、执行类Bean ID、执行类、执行方法、CRON表达式输出

    Args:
        xml_file: 定时任务配置文件

    Raises:
        Exception: 任何异常
    """
    
    # 声明配置文件命名空间，find，findall必须使用此命名空间
    NS = {'beans': 'http://www.springframework.org/schema/beans'}

    tree = ET.parse(xml_file)   # 解析XML文件
    root = tree.getroot()       # 获取根节点

    # 使用字典存储Bean
    beans = {bean.get("id"): bean for bean in root.findall(".//beans:bean", NS)}

    # 遍历所有触发器
    job_triggers = root.findall(".//beans:bean[@class='org.springframework.scheduling.quartz.CronTriggerFactoryBean']", NS)
    print(f"本次共扫描到: {len(job_triggers)} 个定时任务触发器")

    print("JobTrigger \t JobDetail \t TargetObject \t TargetService \t TargetMethod \t CronExpression")

    for trigger in job_triggers:
        job_trigger_id = trigger.get("id")
        cron_expression = trigger.find("beans:property[@name='cronExpression']", NS).get('value')
        job_detail_ref = trigger.find("beans:property[@name='jobDetail']", NS).get('ref')

        job_detail_bean = beans.get(job_detail_ref)
        if job_detail_bean is not None:
            target_method = job_detail_bean.find("beans:property[@name='targetMethod']", NS).get("value")
            target_object = job_detail_bean.find("beans:property[@name='targetObject']", NS).get("ref")

            target_bean = beans.get(target_object)
            if target_bean is not None:
                target_service = target_bean.get("class")
        
        print(f"{job_trigger_id}  {job_detail_ref}  {target_object}  {target_service}  {target_method}  {cron_expression}")


def parse_quartz_data():
    """
    【常规写法】解析Quartz配置内容，常规写法按照： 触发器ID、触发器任务ID、执行类Bean ID、执行类、执行方法、CRON表达式输出

    Raises:
        Exception: 任何异常
    """

    # 配置文件内容
    xml_data = """
        <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">

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
            
            <!-- Job Two -->
            <bean id="jobTwoBean" class="com.test.quartz.service.jobTwo"></bean>
            <bean id="jobTwoDetail" class="org.springframework.scheduling.quartz.MethodInvokingJobDetailFactoryBean">
                <property name="targetObject" ref="jobTwoBean"/>
                <property name="targetMethod" value="jobTwoMethod"/>
            </bean>
            <bean id="jobTwoTrigger" class="org.springframework.scheduling.quartz.CronTriggerFactoryBean">
                <property name="jobDetail" ref="jobTwoDetail"/>
                <property name="cronExpression" value="0 0 12 * * ?"/>
            </bean>
        </beans>
    """

    # 声明配置文件命名空间，find，findall必须使用此命名空间
    NS = {'beans': 'http://www.springframework.org/schema/beans'}

    root = ET.fromstring(xml_data)   # 解析XML内容

    # 遍历所有Bean
    beans = root.findall(".//beans:bean", NS)

    # 遍历所有触发器
    job_triggers = root.findall(".//beans:bean[@class='org.springframework.scheduling.quartz.CronTriggerFactoryBean']", NS)
    print(f"本次共扫描到: {len(job_triggers)} 个定时任务触发器")

    print("JobTrigger \t JobDetail \t TargetObject \t TargetService \t TargetMethod \t CronExpression")

    # 遍历获取触发器相关信息
    for trigger in job_triggers:
        job_trigger_id = trigger.get("id")
        # 获取cron表达式
        cron_expression = trigger.find("beans:property[@name='cronExpression']", NS).get('value')
        # 获取jobDetail
        job_detail_ref = trigger.find("beans:property[@name='jobDetail']", NS).get('ref')

        for job_detail_bean in beans:
            if job_detail_bean.get("id") == job_detail_ref:
                # 获取执行任务方法名称
                target_method = job_detail_bean.find("beans:property[@name='targetMethod']", NS).get("value")
                # 获取执行任务Bean
                target_object = job_detail_bean.find("beans:property[@name='targetObject']", NS).get("ref")

                # 写法1: 遍历
                for target_bean in beans: 
                    if target_bean.get("id") == target_object:
                        target_service = target_bean.get("class")

        print(f"{job_trigger_id} \t {job_detail_ref} \t {target_object} \t {target_service} \t {target_method} \t {cron_expression} ")


if __name__ == "__main__":
    # 获取当前脚本的绝对路径
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # 文件名
    xml_file = os.path.join(script_directory, 'sample.xml')

    # 1. 文件解析方式（常规）
    start_time = time.time()
    parse_quartz_config(xml_file)
    end_time = time.time()
    print("【常规】文件解析方式执行时间：{:.10f}".format(end_time - start_time), "秒\n")

    # 1. 文件解析试（优化）
    start_time = time.time()
    parse_quartz_config_optimize(xml_file)
    end_time = time.time()
    print("【优化】文件解析方式执行时间：{:.10f}".format(end_time - start_time), "秒\n")

    # 2. 内容解析方式（常规）
    start_time = time.time()
    parse_quartz_data()
    end_time = time.time()
    print("【常规】内容解析方式执行时间：{:.10f}".format(end_time - start_time), "秒\n")
