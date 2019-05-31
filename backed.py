def register(request):
	if request.method == 'GET':
		return render("register.html")
	else:
		username = request.user_input.get("username")
		password = request.user_input.get("password")
		re_password = request.user_input.get("re_password")
		name = request.user_input.get("name")
		user_info = db.select(f"select * from user_info where username='{username}'")
		if user_info:
			return restfu.params_error("用户已存在")
		else:
			 if password != re_password:
				return restfu.params_error("两次密码输入不一致")
			else:
				db.insert(f"insert into user_info values('{username}','{password}','1','{name}')")
				return restful.ok()
				


def init_buton(request):
	if request.method == 'GET':
		return restful.params_error("请求方法错误")
	else:
		username = request.user_input.get("username")
		user_info = db.select(f"select * from user_info where username={username}")
		if user_info:
			start_qd_date = 1 if(db.select(f"select start_qd_date from user_sign where username={username}")) else 0
			end_qd_date = 1 if(db.select(f"select end_qd_date from user_sign where username={username}")) else 0
			start_jb_date = 1 if(db.select(f"select start_jb_date from user_sign where username={username}")) else 0
			end_jb_date = 1 if(db.select(f"select end_jb_date from user_sign where username={username}")) else 0
			status = {
				"start_qd_date":start_qd_date,
				"end_qd_date":end_qd_date,
				"start_jb_date":start_jb_date,
				"end_jb_date":end_jb_date
			}
			return restful.ok(data=status)
		else:
			return restful.params_error("按钮状态初始化失败")


def add_workdec(request):
	if request.method == 'GET':
		return restful.params_error("请求方法错误")
	else:
		username = request.user_input.get("username")
		work_dec = request.user_input.get("work_dec")
		date = str(datetime.now())
		user_info = db.select(f"select * from user_info where username={username}")
		if user_info and username:
			sign_info = db.select(f"select * from user_sign where username={username}")
			if sign_info:
				db.update(f"update user_sign set end_qd_date={date} where username={username}")
				return restful.ok("签退成功")
			# 没有签到记录
			else:
				db.insert(f"insert into user_sign values('{date[0:10]}','{username}','','{date}','','','{work_dec}','','','','','')")
				return restful.params_error("签退成功，但检测到您未签到")
		else:
			return restful.params_error("用户不存在")

def start_overtime(request):
	if request.method == 'GET':
		return restful.params_error("请求方法错误")
	else:
		username = request.user_input.get("username")
		date = str(datetime.now())
		user_info = db.select(f"select * from user_info where username={username}")
		if user_info and username:
			db.update(f"update user_sign set start_jb_date={date} where username={username}")
			return restful.ok("加班签到成功")
		else:
			return restful.params_error("用户不存在")

def end_overtime(request):
	if request.method == 'GET':
		return restful.params_error("请求方法错误")
	else:
		username = request.user_input.get("username")
		date = str(datetime.now())
		user_info = db.select(f"select * from user_info where username={username}")
		if user_info and username:
			db.update(f"update user_sign set end_jb_date={date} where username={username}")
			return restful.ok("加班签退成功")
		else:
			return restful.params_error("用户不存在")
