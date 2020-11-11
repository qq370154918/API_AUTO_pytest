import requests
def upload_img(img_path,cookies,headers):
    url = 'https://q.test.dos.cheanjia.net/api/v1/upload_image'#这个url是评估的时候上传车辆图片的地址
    # url = 'https://q.test.dos.cheanjia.net/api/v1/upload_image_with_login'  # 这个url是签合同/财务放款 的时候上传图片的地址
    file = {'img': ('rename.jpg', open(img_path, 'rb'))}

    response = requests.post(url, headers=headers, cookies=cookies, files=file, verify=False)
    return (eval(response.text)["data"])

