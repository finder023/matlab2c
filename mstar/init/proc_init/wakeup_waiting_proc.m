function [] = wakeup_waiting_proc(flag, reso)
    global ProcessSet;
    global WT_PNORMAL;
    
    if flag == WT_PNORMAL
       for p = ProcessSet
           if ismember(flag, p.wait_state)
               clear_wt_flag(p, flag);
           end
       end
    end
end