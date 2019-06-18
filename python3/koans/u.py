import re
string = "pecks.xlx\n" + "orders1.xls\n"+ "apec1.xls\n"+ "na1.xls\n"+ "na2.xls\n"+ "sa1.xls"

change_this_search_string = '[nsc]a[2-9].xls'
print(re.findall(change_this_search_string, string))