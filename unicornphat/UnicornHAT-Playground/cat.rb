#!/usr/bin/env ruby
require 'rubygems'
require 'bundler/setup'

# require your gems as usual
require 'ws2812'

def display(array, colours)
  $hat.clear false
  array.each_with_index do |row, x|
    row.each_with_index do |value, y|
      $hat[x, y] = colours[value]
    end
  end
  $hat.show
end

# Init
$hat = Ws2812::UnicornHAT.new

$hat.rotation = 90
$hat.clear

# sourced from http://atariage.com/forums/topic/169238-free-sprites-for-the-taking/
cat = [
  [
    [0, 1, 1, 1, 0, 0, 0, 0], #1
    [1, 0, 0, 0, 0, 0, 0, 0], #0
    [0, 1, 1, 0, 0, 0, 1, 0], #2
    [0, 0, 1, 1, 1, 0, 1, 1], #3
    [0, 0, 1, 1, 1, 1, 1, 1], #4
    [0, 1, 1, 1, 1, 1, 0, 0], #5
    [1, 0, 1, 0, 1, 1, 1, 1], #6
    [0, 0, 0, 1, 0, 0, 1, 0], #7
  ].reverse,
  [
    [0, 0, 1, 1, 0, 0, 0, 0], #1
    [0, 1, 0, 0, 1, 0, 0, 0], #0
    [0, 1, 0, 0, 0, 0, 0, 0], #2
    [0, 0, 1, 1, 1, 0, 1, 0], #3
    [0, 0, 1, 1, 1, 1, 1, 1], #4
    [0, 1, 1, 1, 1, 1, 1, 1], #5
    [0, 1, 0, 1, 0, 1, 0, 0], #6
    [0, 0, 1, 0, 1, 1, 0, 0], #7
  ].reverse,
  [
    [0, 0, 0, 0, 0, 0, 0, 0], #1
    [0, 1, 1, 0, 0, 0, 0, 0], #0
    [1, 0, 0, 1, 0, 0, 1, 0], #2
    [0, 1, 1, 1, 1, 0, 1, 1], #3
    [0, 0, 1, 1, 1, 1, 1, 1], #4
    [0, 0, 1, 1, 1, 1, 1, 0], #5
    [0, 1, 1, 0, 1, 1, 0, 1], #6
    [0, 1, 0, 0, 0, 0, 0, 0], #7
  ].reverse,
  [
    [0, 0, 0, 1, 0, 0, 0, 0], #1
    [0, 1, 1, 0, 0, 0, 1, 0], #0
    [1, 0, 0, 1, 0, 0, 1, 1], #2
    [0, 1, 1, 1, 1, 1, 1, 1], #3
    [0, 0, 1, 1, 1, 1, 0, 0], #4
    [0, 1, 1, 1, 1, 1, 1, 1], #5
    [0, 1, 0, 1, 0, 1, 1, 0], #6
    [1, 0, 0, 0, 0, 0, 0, 1], #7
  ].reverse
]

colours = [
  Ws2812::Color.new(0, 0, 0),
  Ws2812::Color.new(0, 0, 255)
]

puts "Hit ^C to terminate"

begin
  cat.cycle do |frame|
    display frame, colours
    sleep 0.1
  end
rescue SignalException => e
  $hat.clear
  puts "received Exception #{e}"
end
