sim = dict([('tool','Primary Drying Calculator'),('Kv_known','Y'),('Rp_known','Y'),('Variable_Pch','Y'),('Variable_Tsh','Y')])
vial = dict([('Av',3.80),('Ap',3.14),('Vfill',2.0)])
	product = dict([('cSolid',0.0),('Tpr0',15.8),('Tf',-1.54),('Tn',-5.84)])
	product = dict([('cSolid',0.05),('R0',1.4),('A1',16.0),('A2',0.0)])
	product = dict([('cSolid',0.05)])
	product_temp_filename = './temperature.dat'
	product['T_pr_crit'] = -5		# in degC
	h_freezing = 38.0		#  in W/m^2/K
	ht = dict([('KC',2.75e-4),('KP',8.93e-4),('KD',0.46)])
	Kv_range = np.arange(10.6,10.8,0.01)*1e-4;	# cal/s/K/cm^2
	t_dry_exp = 12.62	# in hr
	Pchamber = dict([('setpt',[0.1,0.4,0.7,1.5])])
	Pchamber = dict([('setpt',[0.15]),('dt_setpt',[1800.0]),('ramp_rate',0.5)])
	Pchamber = dict([('min',0.05),('max',1000)])
	Tshelf = dict([('init',-5.0),('setpt',[-5,0,2,5]),('ramp_rate',1.0)])
	Tshelf = dict([('init',-35.0),('setpt',[20.0]),('dt_setpt',[1800.0]),('ramp_rate',1.0)])
	Tshelf = dict([('min',-45),('max',120)])
dt = 0.001    # hr
	eq_cap = dict([('a',-0.182),('b',0.0117e3)])
	nVial = 398	# Number of vials
filler
filler
filler
filler