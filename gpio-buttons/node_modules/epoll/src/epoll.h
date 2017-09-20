#ifndef EPOLL_H
#define EPOLL_H

class Epoll : public Nan::ObjectWrap {
  public:
    static NAN_MODULE_INIT(Init);
#if NODE_VERSION_AT_LEAST(0, 11, 13)
    static void HandleEvent(uv_async_t* handle);
#else
    static void HandleEvent(uv_async_t* handle, int status);
#endif

  private:
    Epoll(Nan::Callback *callback);
    ~Epoll();

    static NAN_METHOD(New);
    static NAN_METHOD(Add);
    static NAN_METHOD(Modify);
    static NAN_METHOD(Remove);
    static NAN_METHOD(Close);
    static NAN_GETTER(GetClosed);

    int Add(int fd, uint32_t events);
    int Modify(int fd, uint32_t events);
    int Remove(int fd);
    int Close();
    void DispatchEvent(int err, struct epoll_event *event);

    Nan::Callback *callback_;
    std::list<int> fds_;
    bool closed_;

    static Nan::Persistent<v8::Function> constructor;
    static std::map<int, Epoll*> fd2epoll;
};

#endif

