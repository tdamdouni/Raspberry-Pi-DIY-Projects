entity_id = 'input_number.tilt_control'
number_value = int(float(hass.states.get(entity_id).state))
hass.services.call('pan_tilt_phat', 'tilt', {"Tilt":-1*number_value})
