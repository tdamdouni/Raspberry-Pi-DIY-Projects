#!/usr/bin/env ruby
require 'ws2812'
require 'color'
require 'color-generator'
require 'color_gradient'

require_relative 'skull'

def display(array)
  $hat.clear false

  start = Color::RGB.by_hex($cg.create_hex)
  stop  = Color::RGB.by_hex($cg.create_hex)
  g     = ColorGradient.new(start, stop, 7)

  array.each_with_index do |row, x|
    c      = g.gradient(x)
    colour = Ws2812::Color.new(c.red.to_i, c.green.to_i, c.blue.to_i)

    row.each_with_index do |pixel, y|
      $hat[x, y] = colour if pixel > 0
    end
  end
  $hat.show
end

$cg  = ColorGenerator.new(saturation: 0.75, lightness: 0.4)
$hat = Ws2812::UnicornHAT.new

$hat.rotation = 90

puts "Hit ^C to terminate"

begin
  loop do
    display Skull.call
    sleep 1.5
  end
rescue SignalException => e
  $hat.clear
  puts "received Exception #{e}"
end
