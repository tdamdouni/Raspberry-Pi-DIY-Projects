#!/usr/bin/env ruby
require 'ws2812'
require 'color'
require 'color-generator'

hat          = Ws2812::UnicornHAT.new
hat.rotation = 90

generator = ColorGenerator.new(saturation: 0.75, lightness: 0.4)

begin
  puts 'Hit ^C to terminate...'
  hat.clear false
  loop do
    (0..7).each do |x|
      (0..7).each do |y|
        hex = generator.create_hex
        c   = Color::RGB.by_hex(hex)

        hat[x, y] = Ws2812::Color.new(c.red.to_i, c.green.to_i, c.blue.to_i)
        hat.show
        sleep 0.05
      end
    end
  end
rescue SignalException => e
  $hat.clear
  puts "received Exception #{e}"
end
