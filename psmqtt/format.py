class Formatter:
    env = None

    @classmethod
    def get_format(cls, path):
        i = path.find("{{")
        if i > 0:
            i = path.rfind("/", 0, i)
            if i > 0:
                return [path[0:i], path[i+1:]]
        return [path, None]

    @classmethod
    def format(cls, f, value):
        env = cls.get_environment()
        return env.from_string(f).render(value if isinstance(value, dict) else {"x": value})

    @classmethod
    def get_environment(cls):
        if cls.env is None:
            from jinja2 import Environment  # pip install jinja2
            import filters
            cls.env = Environment()
            filters.register_filters(cls.env)

        return cls.env
