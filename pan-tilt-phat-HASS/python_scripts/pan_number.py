entity_id = 'input_number.pan_control'
number_value = int(float(hass.states.get(entity_id).state))
hass.services.call('pan_tilt_phat', 'pan', {"Pan":number_value})
