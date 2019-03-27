question_dict = {"default_language": "default",
"id_string": "afxkvFvEfVDeQ8qP6ujuJ6",
 "children": [{"name": "start", "type": "start"},
                {"name": "end", "type": "end"},
                {"name": "name", "bind": {"required"    : "false"},
                "label": "name", "type": "text"},
                {"name": "__version__", "bind": {"calculate": "'vX2TDy    LMzzFWuL4NdC5Ssd'"},
                "type": "calculate"},
                {"control": {"bodyless": True},
                    "children": [{"name": "in    stanceID",
                    "bind": {"readonly": "true()", "calculate": "concat('uuid:', uuid())"},
                    "type": "calculat    e"}],
                     "name": "meta", "type": "group"}],
                     "version": "vX2TDyLMzzFWuL4NdC5Ssd",
                     "type": "survey",
                     "nam    e": "afxkvFvEfVDeQ8qP6ujuJ6",
                     "sms_keyword": "afxkvFvEfVDeQ8qP6ujuJ6",
                     "title": "john"}
print "Dictionary keys".center(100,"*")
print(question_dict.keys())
print("\n")
print "Dictionary values".center(100,'*')
print(question_dict.values())
print('\n')
print "Dictionary all items".center(100,'*')
print(question_dict)
print('children name')
print ('\n \n ')
for i in range(len(question_dict['children'])):
    #print(question_dict['children'][i]['name'])
    if 'name' in question_dict['children'][i].values():
        print question_dict['children'][i]['name']
