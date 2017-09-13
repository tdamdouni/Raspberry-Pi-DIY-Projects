gl.setup(800, 600)

function node.render()
    gl.clear(0, 1, 0, 1) -- green

    -- render to image object and draw
    local red = resource.render_child("red")
    red:draw(640, 20, 780, 580)

    -- render an draw without creating an intermediate value
    resource.render_child("blue"):draw(50, 200, 300, 380)
end
