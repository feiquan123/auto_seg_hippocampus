from error_code import SUCCESS

def show_desc(count:int)->dict:
	return SUCCESS.with_data({
		"count":count+1
	})

if __name__ == "__main__":
	count = 1
	print(show_desc(count))