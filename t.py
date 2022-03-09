import requests as req
import json

# r = req.post("http://www.sis.nileuniversity.edu.ng/my/loginAuth.php", data={"username": "211605045", "password": "(ENTERpassword1234)", "LogIn": "LOGIN"})
# print(r.status_code)
# res = r.content.decode()
# with open('data.json', 'w') as f:
#     json.dump(res, f)
with open('data.json') as f:
    res = json.loads(json.load(f))

str_to_find = '<h4 class="card-title m-t-10">'
# str_to_find = '<h4 class=\\\"card-title m-t-10\\\">'
idx = res.find(str_to_find)+len(str_to_find)

new_sub_str = res[idx:idx+100].replace("</h4>", "")
names = new_sub_str.split()

print(names[0:3])
