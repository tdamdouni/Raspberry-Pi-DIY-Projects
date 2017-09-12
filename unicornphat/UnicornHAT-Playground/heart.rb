#!/usr/bin/env ruby
require 'ws2812'

# Init
hat = Ws2812::UnicornHAT.new

hat.rotation = 270

red = Ws2812::Color.new(0xff, 0, 0)

heart = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 0, 1, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 0],
  [0, 0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 1, 1, 0, 0, 0]
]

heart.each_with_index do |x, xi|
  x.each_with_index do |y, yi|
    hat[xi, yi] = red if y > 0
  end
end

hat.show
