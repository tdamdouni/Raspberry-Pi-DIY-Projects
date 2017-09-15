gl.setup(640, 480)

util.resource_loader{
    "lua.png",
    "shader.frag",
}

function node.render()
    gl.clear(1,1,1,1)
    shader:use{
        Effect = math.cos(sys.now()*2)*3
    }
    lua:draw(120, 40, 520, 440)
end
