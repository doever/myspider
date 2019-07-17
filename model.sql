-- 需求表:需求月份,需求类型；需求编号；需求状态；创建日期；前台开发者；后台开发者；需求内容
create table requirement(
require_month text,
system_type text,
require_no text,
require_status text,
create_date text,
front_engineer text,
backend_engineer text,
require_context text
)

-- 开发回执表:开发月份；需求版本；系统类型；需求编号;需求中文简称;作业名称；作业说明；开发状态；开发进度条；开发开始日期；开发完成日期
create table development(
-- 201907  V4.1  RPHM  2017021541  wkf_y_bbq_rqb   新增作业  开发中  2019-07-15  2019-07-18
develop_month text,
version text,
system_type text,
require_no text,
workflow_name text,
workflow_desc text,
progress text,
start_date text,
end_date text
)

-- 基础指标对应表
-- 正式设备密钥表
