#!/usr/bin/env ruby
require 'ws2812'

# Init
hat = Ws2812::UnicornHAT.new

brightness = 1

hat.brightness = brightness

# Create the colour red
red = Ws2812::Color.new(0xff, 0, 0)

# Set it to the four corners of the hat
hat[0,0] = red
hat[0,7] = red
hat[7,0] = red
hat[7,7] = red

hat.show

# Enter unending loop till ^C
puts "Hit ^C to terminate"
begin
  loop do
    sleep 0.1
    puts "Setting brightness to #{brightness}"
    hat.brightness = brightness += 1
    hat.show
  end
rescue SignalException => e
  hat.clear
  puts "received Exception #{e}"
end
