-- Created on 2019/4/29 星期一 by ADMINISTRATOR 
declare 
  -- Local variables here
  V_MAX_NUM INT := 0;
  v_last_id INT := 0;
  v_new_id  INT := 1;
  v_count INT := 0;
  
begin
  -- Test statements here
  update company_basic_info set id=rownum;
  commit;
  
  SELECT max(id)
    INTO V_MAX_NUM
    from company_basic_info
    where search_name is not null ;
          
  IF V_MAX_NUM = 0 THEN
     dbms_output.put_line('没有需要更新的数据');
     return;
  else 
    dbms_output.put_line(V_MAX_NUM);
  END IF;

  FOR v_id IN 1 .. V_MAX_NUM
  LOOP
    dbms_output.put_line(v_new_id);
    update COMPANY_11315 t set t.searched=1
      where exists
      ( select 1
          from company_basic_info t1 
          where t1.search_name is not null 
                and t.company_name=t1.search_name
                and t1.id > v_last_id
                and t1.id <= v_new_id
         )
         and t.searched=0;
     COMMIT;
     v_last_id := v_new_id;
     v_new_id := v_new_id + 100000;
     if v_new_id >= V_MAX_NUM then
       v_new_id:=V_MAX_NUM;
       v_count := v_count+1;
     end if;
     dbms_output.put_line(v_new_id);
     
     if v_count >1 then
       dbms_output.put_line(v_new_id);
       dbms_output.put_line(v_count||'次');
       return;
     end if; 
     
  END LOOP;
  
  dbms_output.put_line('数据更新完成！');
end;
