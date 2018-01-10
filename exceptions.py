try:
	pass
#	f=open('text.txt')
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print("When code has no issue")
finally:
	print("Executes anyways")

