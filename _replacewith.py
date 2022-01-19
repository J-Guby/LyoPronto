replacement = "sim = dict([(\'tool\',\'"+ str(input_values.get("Simulation type", 0)) +"\'),(\'Kv_known\',\'"+ str(input_values.get("Vial heat coefficient known", 0)) +"\'),(\'Rp_known\',\'"+ str(input_values.get("Product properties known", 0)) +"\'),(\'Variable_Pch\',\'"+ str(input_values.get("Variable chamber pressure", 0)) +"\'),(\'Variable_Tsh\',\'"+ str(input_values.get("Variable shelf temperature", 0)) +"\')]) \n"

replacement = "vial = dict([(\'Av\',"+ str(input_values.get("Vial area", 0)) +"),(\'Ap\',"+ str(input_values.get("Product Area", 0)) +"),(\'Vfill\',"+ str(input_values.get("Fill volume", 0)) +")]) \n"

replacement = "	product = dict([(\'cSolid\',"+ str(input_values.get("Fractional concentration of solute in the frozen solution", 0)) +"),(\'Tpr0\',"+ str(input_values.get("Initial product temperature for freezing", 0)) +"),(\'Tf\',"+ str(input_values.get("Freezing temperature", 0)) +"),(\'Tn\',"+ str(input_values.get("Nucleation temperature", 0)) +")]) \n"

replacement = "	product = dict([(\'cSolid\',"+ str(input_values.get("Fractional concentration of solute in the frozen solution", 0)) +"),(\'R0\',"+ str(input_values.get("R0", 0)) +"),(\'A1\',"+ str(input_values.get("A1", 0)) +"),(\'A2\',"+ str(input_values.get("A2", 0)) +")]) \n"

replacement = "	product = dict([(\'cSolid\',"+ str(input_values.get("Fractional concentration of solute in the frozen solution", 0)) +")]) \n"

replacement = "	product_temp_filename = \'./temperature.dat\' \n"

replacement = "	product[\'T_pr_crit\'] = "+ str(input_values.get("Critical product temperature", 0)) +"		# in degC \n"

replacement = "	h_freezing = "+ str(input_values.get("h_freezing", 0)) +"		#  in W/m^2/K \n"

replacement = "	ht = dict([(\'KC\',"+ str(input_values.get("KC", 0)) +"),(\'KP\',"+ str(input_values.get("KP", 0)) +"),(\'KD\',"+ str(input_values.get("KD", 0)) +")]) \n"

replacement = "	Kv_range = np.arange("+ str(input_values.get("Array of KV", 0)) +")*1e-4;	# cal/s/K/cm^2v \n"

replacement = "	t_dry_exp = "+ str(input_values.get("Primary drying time", 0)) +"	# in hr \n"

replacement = "	Pchamber = dict([(\'setpt\',["+ str(input_values.get("Chamber pressure set points", 0)) +"])]) \n"

replacement = "	Pchamber = dict([(\'setpt\',["+ str(input_values.get("Chamber pressure set points", 0)) +"]),(\'dt_setpt\',["+ str(input_values.get("Time for chamber pressure", 0)) +"]),(\'ramp_rate\',"+ str(input_values.get("Chamber pressure ramping", 0)) +")]) \n"

replacement = "	Pchamber = dict([(\'min\',"+ str(input_values.get("Chamber Minimum", 0)) +"),(\'max\',"+ str(input_values.get("Chamber Maximum", 0)) +")]) \n"

replacement = "	Tshelf = dict([(\'init\',"+ str(input_values.get("Intial shelf temperature", 0)) +"),(\'setpt\',["+ str(input_values.get("Shelf temperature set points", 0)) +"]),(\'ramp_rate\',"+ str(input_values.get("Shelf temperature ramping", 0)) +")]) \n"

replacement = "	Tshelf = dict([(\'init\',"+ str(input_values.get("Intial shelf temperature", 0)) +"),(\'setpt\',["+ str(input_values.get("Shelf temperature set points", 0)) +"]),(\'dt_setpt\',["+ str(input_values.get("Time for shelf temperature", 0)) +"]),(\'ramp_rate\',"+ str(input_values.get("Shelf temperature ramping", 0)) +")]) \n"

replacement = "	Tshelf = dict([(\'min\',"+ str(input_values.get("Shelf Minimum", 0)) +"),(\'max\',"+ str(input_values.get("Shelf Maximum", 0)) +")]) \n"

replacement = "dt = "+ str(input_values.get("Time step", 0)) +"    # hr \n"

replacement = "	eq_cap = dict([(\'a\',"+ str(input_values.get("a", 0)) +"),(\'b\',"+ str(input_values.get("b", 0)) +")]) \n"

replacement = "	nVial = "+ str(input_values.get("Number of vials", 0)) +"	# Number of vials \n"


