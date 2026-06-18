class MissionNotFoundError(Exception):
    def __init__(self, m_id: int, *args):
        super().__init__(*args)
        self.m_id = m_id

class AgentNotFoundError(Exception):
    def __init__(self, a_id: int, *args):
        super().__init__(*args)
        self.a_id = a_id

class NotAllowedError(Exception):
    pass