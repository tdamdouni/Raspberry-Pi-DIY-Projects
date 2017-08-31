entity_id = 'input_slider.pan_control'
slider_value = int(float(hass.states.get(entity_id).state))
hass.services.call('pan_tilt_phat', 'pan', {"Pan":slider_value})
