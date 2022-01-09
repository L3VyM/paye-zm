# function defined that takes in an argument for gross salary or amount
def Paye(basic_slry = int(input('Enter Gross Amount: '))):

	"""
	- Below are tax bands upon which the calculation is made
	for the first 4500, individual is PAYE free
	"""	
	first_band = 4500
	second_lower_band = 4500.01
	second_higher_band = 4800
	third_lower_band = 4800.01
	third_higher_band = 6900

	"""
	- Conditions below test and compare bands list above,
	- Amount processed as gross amount has caculated PAYE
	"""
	if basic_slry >= first_band:
		chargeable_income_0 = first_band
		per_0 = 0 * chargeable_income_0
		print(f"0 - {first_band} @ {per_0}")

		if basic_slry >= second_lower_band:
			chargeable_income_1 = second_higher_band - second_lower_band
			per_1 = 0.25 * chargeable_income_1
			print(f"{second_lower_band} - {second_higher_band} @ {per_1}")

			if basic_slry >= third_lower_band:
				chargeable_income_2 = third_higher_band - third_lower_band
				per_2 = 0.30 * chargeable_income_2
				print(f"{third_lower_band} - {third_higher_band} @ {per_2}")

				if basic_slry >= third_higher_band:
					chargeable_income_3 = basic_slry - chargeable_income_2 - chargeable_income_1 - first_band
					per_3 = 0.375 * chargeable_income_3
					print(f"{third_higher_band} and above @ {per_3}")
Paye()