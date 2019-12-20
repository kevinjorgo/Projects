import os
#https://www.youtube.com/watch?v=ve2pmm5JqmI

os.chdir('\Users\kevs_\OneDrive\Documents\Example')

print(os.getcwd())

for f in os.listdir('\Users\kevs_\OneDrive\Documents\Example'):
    os.path.splitext(f)
    file_name, file_ext = os.path.splitext(f)
    #print(file_name.split(' '))
    f_new, f_text, f_document, f_num = file_name.split('-')
    f_num = f_num.strip()[1:].zfill(2)
    #print(f_num)
    print('{}-{}-{}-{}{}'.format(f_num, f_new, f_text, f_document,file_ext))
    new_name = '{}-{}-{}-{}{}'.format(f_num, f_new, f_text, f_document,file_ext)
    os.rename(f, new_name)
