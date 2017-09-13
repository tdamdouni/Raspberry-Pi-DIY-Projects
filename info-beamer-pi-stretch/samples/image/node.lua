gl.setup(1024, 768)

local image = resource.load_image "beamer.png"

function node.render()
    gl.clear(1,1,1,1)
    util.draw_correct(image, 0, 0, WIDTH, HEIGHT)
end
