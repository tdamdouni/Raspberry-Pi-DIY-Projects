# given input file, convert and fiddle

require 'optparse'
require 'json'

$options = options = {
  iterations: 1,
  output: nil,
  amount: 0.5,
  seed: 0.5,
  verbose: false
}

OptionParser.new do |opts|
  opts.banner = "Usage: ruby glitch-raw.rb [OPTIONS] input-file.jpg"

  opts.on('-i', "--iterations NUMBER", Integer, "Number of iterations to run the glitcher [1]") do |n|
    options[:iterations] = n.to_i
  end

  opts.on('-a', "--amount PERCENT", Float, "Number in range 0 - 100 representing the amount of glitch [50]") do |n|
    options[:amount] = n.to_f / 100.0
  end

  opts.on('-s', "--seed PERCENT", Float, "Number in range 0 - 100 representing a seed value for glitching [50]") do |n|
    options[:seed] = n.to_f / 100.0
  end

  opts.on('-v', '--verbose', "Verbose output") do |n|
    options[:verbose] = true
  end

  opts.on('-o', "--output FILE", String, "File to write output to") do |f|
    options[:output] = f.to_s
  end
end.parse!

input_file = ARGV.pop
if !File.exists?(input_file)
  $stderr.write "Invalid input file given, file at '#{input_file}' does not exist"
  exit 1
end

def log(*args)
  if $options[:verbose]
    puts args.map(&:to_s).join(' ')
  end
end

if options[:output].nil?
  # get a default output file name
  dir, absfile = File.split(input_file)
  ext = File.extname(absfile)
  fname = File.basename(absfile, ext)
  options[:output] = File.join(dir, "%s-glitch%s" % [fname, ext])

  log 'NO OUTPUT SPECIFIED, USING', options[:output]
end

log "OPTIONS:"
log JSON.pretty_generate(options)

# check for file argument's existence and read file
image = IO.binread(input_file)

def jpg_header_length(bytes)
  result = 417

  # read until end of header is reached
  bytes.each_with_index do |byte, i|
    if byte === 0xFF && bytes[i + 1] === 0xDA
      result = i + 2
      break
    end
  end

  return result
end

bytes = image.bytes

header_length = jpg_header_length(bytes)
max_index = bytes.size - header_length - 4

iterations = options[:iterations]

amount_percent = options[:amount]
seed_percent = options[:seed]

# ALGORITHM FROM:
# https://github.com/snorpey/glitch-canvas/blob/master/src/glitch/glitchByteArray.js
iterations.times do |n|
  min_pi = (max_index / iterations * n) | 0
  max_pi = (max_index / iterations * (n + 1)) | 0

  delta = max_pi - min_pi
  pixel_index = (min_pi + delta * seed_percent).round | 0

  if pixel_index > max_index
    pixel_index = max_index
  end

  index_in_byte_array = ~~(header_length + pixel_index)

  log "GLITCH BYTE", index_in_byte_array

  bytes[index_in_byte_array] = ~~((amount_percent * 256).round)
end

log 'WRITING', bytes.size, 'BYTES TO', options[:output]
IO.binwrite(options[:output], bytes.pack('c*'))
