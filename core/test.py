ins_dict_repo = {'central_class_repository_demo' : ['file_item_id', 'item_desc']}

str_list  = ins_dict_repo["central_class_repository_demo"]

print(str_list)
insert_values = []
tuple_str1 = (','.join('row' + '["' + item + '"]' for item in str_list),)
print type(tuple_str1)
tuple_str2 = (','.join('row' + '["' + item + '"]' for item in str_list),)
insert_values.append(tuple_str1)
insert_values.append(tuple_str2)
print insert_values

#str_insert_append = insert_values.append((','.join('row' + '["' + item + '"]' for item in str_list)))
# str_insert_append = 'insert_values.append((' + ','.join('row["'+ item + '"]' for item in str_list) + '))'


#print(str_insert_append)