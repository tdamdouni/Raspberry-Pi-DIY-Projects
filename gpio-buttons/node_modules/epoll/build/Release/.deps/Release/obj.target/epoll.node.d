cmd_Release/obj.target/epoll.node := g++ -shared -pthread -rdynamic  -Wl,-soname=epoll.node -o Release/obj.target/epoll.node -Wl,--start-group Release/obj.target/epoll/src/epoll.o -Wl,--end-group 
