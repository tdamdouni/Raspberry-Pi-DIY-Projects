#!/usr/bin/env ruby
require 'ws2812'

# Init
hat = Ws2812::UnicornHAT.new

hat.rotation = 90
hat.clear

hair = Ws2812::Color.new(154, 98, 49)
skin = Ws2812::Color.new(246, 174, 102)
dark = Ws2812::Color.new(0, 0, 0)
back = Ws2812::Color.new(255, 255, 255)

baboon = [
  [hair, hair, hair, hair, hair, hair, back, back],
  [hair, hair, skin, skin, skin, skin, back, back],
  [hair, hair, skin, dark, skin, dark, back, back],
  [hair, hair, hair, hair, skin, skin, skin, skin],
  [hair, hair, hair, hair, skin, dark, skin, dark],
  [hair, hair, hair, hair, skin, skin, skin, skin],
  [hair, hair, hair, hair, skin, skin, dark, skin],
  [hair, hair, hair, hair, skin, skin, skin, skin],
].reverse

# ^ because the `0,0` element is the bottom left corner, we need to reverse the outer array

baboon.each_with_index do |row, x|
  row.each_with_index do |value, y|
    hat[x, y] = value
  end
end

hat.show

puts "Press return to end"
gets

hat.clear
