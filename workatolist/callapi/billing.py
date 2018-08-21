from datetime import datetime, date, time


def billing(start_ts, end_ts):
	paid_final_hour = time(22,0,0)
	paid_start_hour = time(6,0,0)
	
	if start_ts.time() > paid_start_hour and start_ts.time() < paid_final_hour and end_ts.time() > paid_start_hour and end_ts.time() < paid_final_hour:
		print("billing 1")
		duration = datetime.combine(end_ts, end_ts.time()) - datetime.combine(start_ts, start_ts.time())
		price = 0.36 + ((duration.seconds//60) * 0.09)
		price = round(price,2)
		if duration.days >= 1:
			day_cost = 86.40 * duration.days
			price = price + day_cost
			price = round(price, 2)
			return price
		return price

	elif start_ts.time() > paid_start_hour and start_ts.time() < paid_final_hour and (end_ts.time() > paid_final_hour or end_ts.time() < paid_start_hour):
		print("billing 2")
		duration = datetime.combine(end_ts, paid_final_hour) - datetime.combine(start_ts, start_ts.time())
		price = 0.36 + ((duration.seconds//60) * 0.09)
		price = round(price,2)
		if duration.days >= 1:
			day_cost = 86.40 * duration.days
			price = price + day_cost
			price = round(price, 2)
			return price
		return price
	
	elif (start_ts.time() < paid_start_hour or start_ts.time() > paid_final_hour) and (end_ts.time() > paid_start_hour and end_ts.time() < paid_final_hour):
		print("billing 3")
		duration = datetime.combine(end_ts, end_ts.time()) - datetime.combine(start_ts, paid_start_hour)
		price = 0.36 + ((duration.seconds//60) * 0.09)
		price = round(price,2)
		if duration.days >= 1:
			day_cost = 86.40 * duration.days
			price = price + day_cost
			price = round(price, 2)
			return price
		return price


	elif (start_ts.time() > paid_final_hour or start_ts.time() < paid_start_hour) and (end_ts.time() > paid_final_hour or end_ts.time() < paid_start_hour):
		print("billing 4")
		duration = datetime.combine(end_ts, end_ts.time()) - datetime.combine(start_ts, start_ts.time())
		price = 0.36
		price = round(price,2)
		if duration.days >= 1:
			day_cost = 86.40 * duration.days
			price = price + day_cost
			price = round(price, 2)
			return price
		return price