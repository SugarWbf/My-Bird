#这是将文本文件导入刀数据库的脚本
import os
#这是注册环境模块
aa = os.environ.setdefault("DJANGO_SETTINGS_MODULE","Bird.settings")
import django
django.setup()
import django03.models as modelwen

def main():
    with open("olddata.txt","r+",encoding='UTF-8') as f:
        for line in f:
            titles = line.split("**")
            modelwen.wenzhang.objects.create(title=titles[0],content=titles[-1])

    f.close()

if __name__ == '__main__':
    main()
    print("Done...")



