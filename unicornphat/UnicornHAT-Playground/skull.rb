# sourced from http://atariage.com/forums/topic/169238-free-sprites-for-the-taking/

class Skull
  def self.call
    (forehead + eyes + nose + mouth).reverse
  end

  def self.forehead
    SkullForehead.call
  end

  def self.eyes
    SkullEyes.call
  end

  def self.nose
    SkullNose.call
  end

  def self.mouth
    SkullMouth.call
  end
end

class SkullForehead
  def self.call
    [
      [0, 0, 1, 1, 1, 1, 1, 0], #0
      [0, 1, 1, 1, 1, 1, 1, 1], #1
    ]
  end
end

class SkullEyes
  def self.call
    [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, deal_with_it].sample
  end

  def self.one
    [
      [1, 0, 1, 1, 1, 0, 1, 1], #2
      [1, 0, 0, 1, 0, 0, 1, 1], #3
    ]
  end

  def self.two
    [
      [1, 0, 1, 1, 0, 0, 1, 1], #2
      [1, 0, 0, 1, 0, 0, 1, 1], #3
    ]
  end

  def self.three
    [
      [1, 0, 0, 1, 0, 0, 1, 1], #2
      [1, 1, 0, 1, 1, 0, 1, 1], #3
    ]
  end

  def self.four
    [
      [1, 0, 0, 1, 0, 0, 1, 1], #2
      [1, 1, 1, 1, 1, 1, 1, 1], #3
    ]
  end

  def self.five
    [
      [1, 1, 0, 1, 1, 0, 1, 1], #2
      [1, 0, 0, 1, 0, 0, 1, 1], #3
    ]
  end

  def self.six
    [
      [1, 0, 0, 1, 0, 0, 1, 1], #2
      [1, 0, 0, 1, 0, 0, 1, 1], #3
    ]
  end

  def self.seven
    [
      [1, 1, 1, 1, 1, 1, 1, 1], #2
      [1, 0, 0, 1, 0, 0, 1, 1], #3
    ]
  end

  def self.eight
    [
      [1, 0, 1, 1, 0, 1, 1, 1], #2
      [1, 0, 1, 1, 0, 1, 1, 1], #3
    ]
  end

  def self.nine
    [
      [1, 1, 0, 1, 1, 0, 1, 1], #2
      [1, 1, 0, 1, 1, 0, 1, 1], #3
    ]
  end

  def self.ten
    [
      [1, 1, 0, 1, 0, 1, 1, 1], #2
      [1, 0, 1, 1, 1, 0, 1, 1], #3
    ]
  end

  def self.eleven
    [
      [1, 1, 1, 1, 0, 0, 1, 1], #2
      [1, 0, 1, 1, 0, 0, 1, 1], #3
    ]
  end

  def self.twelve
    [
      [1, 0, 0, 0, 0, 0, 1, 1], #2
      [1, 1, 0, 1, 1, 0, 1, 1], #3
    ]
  end

  def self.deal_with_it
    [
      [0, 0, 0, 0, 0, 0, 0, 0], #2
      [1, 0, 0, 1, 0, 0, 1, 1], #3
    ]
  end
end

class SkullNose
  def self.call
    [
      [0, 1, 1, 0, 1, 1, 1, 0], #4
    ]
  end
end

class SkullMouth
  def self.call
    [one, two, three, four, five, six].sample
  end

  def self.one
    [
      [0, 0, 0, 1, 1, 1, 0, 0], #5
      [0, 0, 0, 0, 0, 1, 0, 0], #6
      [0, 0, 0, 1, 1, 1, 0, 0], #7
    ]
  end

  def self.two
    [
      [0, 0, 0, 1, 1, 1, 0, 0], #5
      [0, 0, 0, 1, 1, 1, 0, 0], #6
      [0, 0, 0, 0, 0, 0, 0, 0], #7
    ]
  end

  def self.three
    [
      [0, 0, 0, 1, 1, 1, 0, 0], #5
      [0, 0, 0, 1, 0, 1, 0, 0], #6
      [0, 0, 0, 1, 1, 1, 0, 0], #7
    ]
  end

  def self.four
    [
      [0, 0, 0, 1, 1, 1, 0, 0], #5
      [0, 0, 0, 0, 1, 1, 0, 0], #6
      [0, 0, 0, 1, 1, 1, 0, 0], #7
    ]
  end

  def self.five
    [
      [0, 0, 0, 1, 1, 1, 0, 0], #5
      [0, 0, 0, 0, 0, 0, 0, 0], #6
      [0, 0, 0, 1, 1, 1, 0, 0], #7
    ]
  end

  def self.six
    [
      [0, 0, 0, 1, 1, 1, 0, 0], #5
      [0, 0, 0, 1, 0, 1, 0, 0], #6
      [0, 0, 0, 0, 0, 0, 0, 0], #7
    ]
  end
end
