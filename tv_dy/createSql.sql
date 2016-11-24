 
CREATE TABLE `fei`.`DYURL` (
  `id` INT NULL AUTO_INCREMENT,
  `tv_name` VARCHAR(200) NULL,   -- 名称
  `tv_iconUrl` VARCHAR(200) NULL, 
  `tv_state` VARCHAR(200) NULL,	 -- 更新状态:已完结，连载中
  `tv_viewcount` VARCHAR(200) NULL, -- 点击量
  `tv_type` VARCHAR(200) NULL,    -- 动漫类型
  `tv_dub` VARCHAR(200) NULL, 	-- 配音语言
  `tv_showtime` VARCHAR(200) NULL, -- 上映时间
  `tv_updatetime` VARCHAR(200) NULL,  -- 最后更新时间
  `tv_info` VARCHAR(18000) NULL,  -- 简介：HTML类型
 -- `tv_cleaninfo` VARCHAR(8000) NULL,  -- 简介：去除HTML类型
  `tv_downtype` VARCHAR(200) NULL, -- 下载类型：百度网盘/FTP/magnet
  `tv_downseries` VARCHAR(200) NULL, -- 集，每一集的标题
  `tv_downseries_url` VARCHAR(200) NULL, -- 每一集的下载地址
  PRIMARY KEY (`id`));


----------------------------------
连载中：75
已完结：2587

共计：2662



实际上:在已完结的后面几个分页，点击已经没有数据了，so,,,
连载中：75
已完结：2520

共计：2595
----------------------------------

select count(1) from fei.DBURL;
-- 18423
select count(distinct tv_name) from fei.dburl
-- 2591

SELECT count(*) FROM fei.DBURL where tv_downSeries_url != '';



