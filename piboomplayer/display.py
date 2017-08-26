from papirus import Papirus
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

WHITE = 1
BLACK = 0
SIZE = 16

class Driver():
        papirus = Papirus()
        line_position=0

        def write_lines(self, lines, fontsize):
                # initially set all white background
                image = Image.new('1', self.papirus.size, WHITE)
                # prepare for drawing
                draw = ImageDraw.Draw(image)
                self.line_position = 0
                for line in lines:
                        self.line_position += 1
                        self.write_text(draw, line, fontsize)

                self.papirus.display(image)
                self.papirus.update()

        def write_text(self, draw, text, size):
                font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', size)
                # Calculate the max number of char to fit on line
                line_size = (self.papirus.width / (size*0.65))
                current_line = 0
                text_lines = [""]
                # Compute each line
                for word in text.split():
                        # If there is space on line add the word to it
                        if (len(text_lines[current_line]) + len(word)) < line_size:
                                text_lines[current_line] += " " + word
                        else:
                                # No space left on line so move to next one
                                text_lines.append("")
                                current_line += 1
                                text_lines[current_line] += " " + word
                current_line = self.line_position - 1
                for l in text_lines:
                        current_line += 1
                        draw.text( (0, ((size*current_line)-size)) , l, font=font, fill=BLACK)
                self.line_position += (current_line - 1)


