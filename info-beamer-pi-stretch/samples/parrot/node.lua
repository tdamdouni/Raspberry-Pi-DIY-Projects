gl.setup(400, 400)

function readln()
    return coroutine.yield()
end

if not N.clients then
    N.clients = {}
end

node.event("connect", function(client)
    local handler = coroutine.wrap(echo)
    N.clients[client] = handler
    handler(function(...)
        node.client_write(client, ...)
    end)
end)

node.event("input", function(line, client)
    N.clients[client](line)
end)

node.event("disconnect", function(client)
    N.clients[client] = nil
end)

function echo(print)
    print("I will repeat everything you send me")
    while true do
        local line = readln()
        print(line)
    end
end

util.auto_loader(_G)

function node.render()
    gl.clear(1,1,1,1)
    util.draw_correct(blue_macaw, 0, 0, WIDTH, HEIGHT)
end
