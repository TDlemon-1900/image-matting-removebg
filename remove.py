# Requires "requests" to be installed (see python-requests.org)
# @author by:andy meng

# 此脚本调用的是"removebg"网站提供的API，此网站每个账号每月限次50张
# 使用此脚本时要注意path的更改，以及文件夹编号的修改


import requests
import os


path = r"500_images/yqd/"   # r"Patant map/yxd/"    此处修改文件夹的路径


def matting(filename, path):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(filename, 'rb')},
        data={'size': 'auto'},
        # 此处添加API Key
        headers={'X-Api-Key': 'nw4oxGMSMRn3SkSUrpxbsLSi'},
    )
    if response.status_code == requests.codes.ok:
        with open(path, 'wb') as out:
            out.write(response.content)

    else:
        print("Error:", response.status_code, response.text)


if __name__ == '__main__':
    # 1.读取path中的文件夹，然后读取从0开始文件夹的内容,使用该脚本时注意变量path的修改
    # 2.将去背景后的图片保存到指定的文件夹下

    for i in range(49, 70):  # 此处修改文件夹的编号，作者是从0开始的，编号为29的文件夹结束
        newPath = path + str(i) + "/"
        files = os.listdir(newPath)
        fileNew = ''.join(files)
        # 获取filename参数
        filename = newPath + fileNew
        savePath = newPath + "no-bg.png"
        matting(filename, savePath)
        print("编号为" + str(i) + "的文件夹已经抠图完成")
