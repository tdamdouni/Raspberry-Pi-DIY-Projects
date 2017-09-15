#!/usr/bin/env ruby
require 'ws2812'
require 'color'
require 'color-generator'
require 'color_gradient'

cg  = ColorGenerator.new(saturation: 0.75, lightness: 0.4)
hat = Ws2812::UnicornHAT.new

begin
  puts 'Hit ^C to terminate...'
  hat.rotation = 90
  hat.clear false
  loop do
    start = Color::RGB.by_hex(cg.create_hex)
    stop  = Color::RGB.by_hex(cg.create_hex)
    g     = ColorGradient.new(start, stop, 7)
    (0..7).each do |x|
      (0..7).each do |y|
        c = g.gradient(x)

        hat[x, y] = Ws2812::Color.new(c.red.to_i, c.green.to_i, c.blue.to_i)
        hat.show
        sleep 0.04
      end
    end
  end
rescue SignalException => e
  $hat.clear
  puts "received Exception #{e}"
end
