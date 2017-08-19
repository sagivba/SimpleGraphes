from datetime import datetime
from datetime import timedelta

class Regions:
    def __init__(self,in_f,time_format):
        self.in_f=in_f
        self.data=dict()
        self.valid_regions=("CENTER", "NORTH", "SOUTH", "EAST", "WEST")
        self.errors_log=[]
        self.time_format=time_format

    def parse_file(self):
        lines=self.in_f.readlines()
        lines.pop(0)

        for line_number, line in enumerate(lines, start=1):
            try:
                #Center,01/01/2016 00h15m,West,01/01/2016 01h50m
                line=line.strip("\r\n")
                (source,start_str,dest,stop_str)=line.split(',')
                source= source.upper()
                dest  = dest.upper()
                time_format=self.time_format
                t_start=datetime.strptime(start_str,time_format)
                t_end  =datetime.strptime(stop_str, time_format)
                t_delta=int((t_end-t_start).seconds)
                if source not in self.valid_regions:
                    raise ValueError(source +" not one of:"+",".join(self.valid_regions))
                if dest not in self.valid_regions:
                    raise ValueError(dest + " not one of:" + ",".join(self.valid_regions))
                if source==dest:
                    raise ValueError("source ande destenation are equal:"+source)
                if t_delta<=0:
                    raise ValueError("time is not valid delta is zero")
                if t_delta is None:
                    raise ValueError("time is not valid delta is zero")

                if (source,dest) not in self.data:
                    self.data[(source,dest)]=[]

                self.data[(source,dest)].append(t_delta)
                if len(self.data[(source,dest)])==0:
                    self.data.pop((source,dest))
                    raise ValueError("could not detect t_delta")

            except Exception as e:
                self.errors_log.append("line:{:>4} '{}'  - {}".format(line_number, line, e))


    def _chomp(strings):
        for i in range(0,len(strings)):
            strings[i]=strings[i].strip("\r\n")


    def data_as_eges(self):
       # item=((East,South),[1 ,3,5,7]) --> (East,South,average(item[2]))
        sum_t_delta=lambda lst:float(sum(lst))
        avg_t_delta=lambda lst:sum_t_delta(lst)/len(lst)
        item_to_edge_tupel=lambda itm:(itm[0][0],itm[0][1],avg_t_delta(itm[1]))
        edges=map(item_to_edge_tupel,self.data.items())
        return edges
