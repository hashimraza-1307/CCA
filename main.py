# INPUTS
customer_name = input('Enter Customer Name: ')
customer_type = input('Enter Customer Type (R or C): ').upper()
previous_meter_reading = int(input('Enter Previous Month Reading: '))
current_meter_reading = int(input('Enter Current Month Reading: '))
bill_paid = input('Bill Paid After Due Date (Y or N): ').upper()

#VALIDATION 
if customer_type != 'R' and customer_type != 'C':
    print('You Can Only Type R or C')
elif previous_meter_reading < 0:
    print('Previous Reading Cant Be Negative')
elif current_meter_reading < 0:
    print('Current Reading Cant Be Negative')
elif current_meter_reading < previous_meter_reading:
    print('Current Reading Should be greater than previous reading')
else:
  units_consumed = current_meter_reading - previous_meter_reading

  # ENERGY CHARGES
  if customer_type == 'R' and units_consumed <=100:
    energy_charges = units_consumed * 10
  elif customer_type == 'R' and units_consumed <=200:
    energy_charges = (100 * 10) + (units_consumed - 100) * 15 
  elif customer_type == 'R' and units_consumed <=300:
    energy_charges = (100 * 10) + (100 * 15) + (units_consumed - 200) * 20
  else:
    energy_charges = (100 * 10) + (100 * 15) + (100 * 20) + (units_consumed - 300) * 25

  if customer_type == 'C':
    energy_charges = units_consumed * 30

  # FIXED CHARGES
  if customer_type == 'R' and units_consumed <=200:
    fixed_charges = 100
  else:
    fixed_charges = 200

  if customer_type == 'C':
    fixed_charges = 500

  # GST
  gst = (energy_charges + fixed_charges) * 18 / 100

  # LATE PAYMENT SURCHARGE
  if bill_paid == 'Y':
    late_payment_surcharge = (energy_charges + fixed_charges + gst) * 10 / 100
  else:
     late_payment_surcharge = 0

  #TOTAL BILL
  total = energy_charges + fixed_charges + gst + late_payment_surcharge

  # CONSUMPTION LEVEL
  if units_consumed <= 100:
    consumption_level = 'Low'
  elif units_consumed > 100 and units_consumed <= 300:
    consumption_level = 'Moderate'
  else: 
    consumption_level = 'High'

  # BILL PRINTING
  print(f'Customer Name : {customer_name}')
  if customer_type == 'R':
    type = 'Residential'
  else:
     type = 'Commercial'
  print(f'Customer Type : {type}')
  print(f'Units Consumed : {units_consumed}')
  print(f'Energy Charges : {energy_charges}')
  print(f'Fixed Charges : {fixed_charges}')
  print(f'GST : {gst}')
  print(f'Late Payment Surcharge : {late_payment_surcharge}')
  print(f'Total Payable : {total:.2f} Rs')
  print(f'Consumption Level : {consumption_level}')