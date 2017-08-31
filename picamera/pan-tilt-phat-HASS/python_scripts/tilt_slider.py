entity_id = 'input_slider.tilt_control'
slider_value = int(float(hass.states.get(entity_id).state))
hass.services.call('pan_tilt_phat', 'tilt', {"Tilt":-1*slider_value})
