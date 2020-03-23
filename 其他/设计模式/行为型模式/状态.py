class State: ...


class DisConnectState(State):
    def init(self):
        return "Bye!"

    def replay(self, msg):
        return ""


class ConnectState(State):
    def init(self):
        return "Hello!"

    def replay(self, msg: str):
        if msg.endswith("?"):
            return f"Yes, {msg[:-1]}!"
        elif msg.endswith("."):
            return f"{msg[:-1]}!"
        return f"{msg[:-1]}?"


class Box:
    state = DisConnectState()

    def chat(self, msg: str):
        if msg.lower().startswith("hello"):
            self.state = ConnectState()
            return self.state.init()
        elif msg.lower().startswith("bye"):
            self.state = DisConnectState()
            return self.state.init()
        return self.state.replay(msg)


if __name__ == '__main__':
    box = Box()
    while True:
        msg = input()
        print(box.chat(msg))
